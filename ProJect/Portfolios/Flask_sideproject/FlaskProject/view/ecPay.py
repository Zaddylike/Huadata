# -*- coding: utf-8 -*-
from flask import (
    Blueprint,request,
    session,render_template,
    make_response,redirect
    )
from flask.helpers import url_for
from flask_restful import Api,Resource

from ..model.user import User
from ..model.db_shopcart import shopCart
from .. import call_back

import collections,os,hashlib,time
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from urllib.parse import quote_plus
import importlib.util


#-----------------------------------------------------------------------
#參數區
filename = os.path.dirname(os.path.realpath(__file__))
spec = importlib.util.spec_from_file_location(
    "ecpay_payment_sdk", filename + "/sdk/ecpay_payment_sdk.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


payment= Blueprint("ecPay",__name__)
api=Api(payment)
#-----------------------------------------------------------------------


class Params:
    def __init__(self):
        web_type = 'test'
        if web_type == 'offical':
            # 正式環境
            self.params = {
                'MerchantID': '隱藏',
                'HashKey': '隱藏',
                'HashIV': '隱藏',
                'action_url':
                'https://payment.ecpay.com.tw/Cashier/AioCheckOut/V5'
            }
        else:
            # 測試環境
            self.params = {
                'MerchantID':
                '2000132',
                'HashKey':
                '5294y06JbISpM5x9',
                'HashIV':
                'v77hoKGq4kWxNNIS',
                'action_url':
                'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5'
            }
    @classmethod
    def get_params(cls):
        return cls().params

    # 驗證綠界傳送的 check_mac_value 值是否正確
    @classmethod
    def get_mac_value(cls, get_request_form):

        params = dict(get_request_form)
        if params.get('CheckMacValue'):
            params.pop('CheckMacValue')

        ordered_params = collections.OrderedDict(
            sorted(params.items(), key=lambda k: k[0].lower()))

        HahKy = cls().params['HashKey']
        HashIV = cls().params['HashIV']

        encoding_lst = []
        encoding_lst.append('HashKey=%s&' % HahKy)
        encoding_lst.append(''.join([
            '{}={}&'.format(key, value)
            for key, value in ordered_params.items()
        ]))
        encoding_lst.append('HashIV=%s' % HashIV)

        safe_characters = '-_.!*()'

        encoding_str = ''.join(encoding_lst)
        encoding_str = quote_plus(str(encoding_str),
                                safe=safe_characters).lower()

        check_mac_value = ''
        check_mac_value = hashlib.sha256(
            encoding_str.encode('utf-8')).hexdigest().upper()

        return check_mac_value

class Payment(Resource):
    def get(self):
        if call_back():
            curUser=User.get_user(session.get('user'))
            curUsercar=shopCart.query.filter_by(uid=curUser.id).all()

            return make_response(render_template(
                'payment.html',
                outPut=curUsercar,
                productName= 'iphone',
                price= '13999',
                user=session.get("user"),
                )
                )
        return redirect(url_for("auth.loginPoint"))
    def post(self):
        # 從 session 中取得 uid
        uid = session.get('id')
        host_name = request.host_url
        print(host_name)

        # 取得 POST 的收件人資訊
        trade_name = request.form['name']
        trade_phone = request.form['phone']
        county = request.form['county']
        district = request.form['district']
        zipcode = request.form['zipcode']
        address = request.form['address']

        # 利用 uid 查詢資料庫，購物車商品 & 價錢
        # carts = sql.AddToCar.query.filter_by(uid=uid, state='Y')
        total_product_price = 0
        total_product_name = ''
        curUser=User.get_user(session.get('user'))
        curUsercar=shopCart.query.filter_by(uid=curUser.id).all()
        for c in curUsercar:
            price = c.product.price
            quan = c.productamount
            product_name = c.product.name
            total_product_price += int(price) * int(quan)
            total_product_name += product_name + '#'
            
        # 建立交易編號 tid
        date = time.time()
        tid = str(date) + 'Uid' + str(uid)
        status = '未刷卡'

        # 新增 Transaction 訂單資料
        # T = sql.Transaction(uid, tid, trade_name, trade_phone, address,
        #                     total_product_price, status, county, district, zipcode)
        # db.session.add(T)
        # db.session.commit()

        params = Params.get_params()

        # 設定傳送給綠界參數
        order_params = {
            'MerchantTradeNo': datetime.now().strftime("NO%Y%m%d%H%M%S"),
            'StoreID': '',
            'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
            'PaymentType': 'aio',
            'TotalAmount': total_product_price,
            'TradeDesc': 'ToolsFactory',
            'ItemName': total_product_name,
            'ReturnURL': host_name + 'payment/receive_result',
            'ChoosePayment': 'Credit',
            'ClientBackURL': host_name + 'payment/trad_result',
            'Remark': '交易備註',
            'ChooseSubPayment': '',
            'OrderResultURL': host_name + 'payment/trad_result',
            'NeedExtraPaidInfo': 'Y',
            'DeviceSource': '',
            'IgnorePayment': '',
            'PlatformID': '',
            'InvoiceMark': 'N',
            'CustomField1': str(tid),
            'CustomField2': '',
            'CustomField3': '',
            'CustomField4': '',
            'EncryptType': 1,
        }

        extend_params_1 = {
            'BindingCard': 0,
            'MerchantMemberID': '',
        }

        extend_params_2 = {
            'Redeem': 'N',
            'UnionPay': 0,
        }

        inv_params = {
            # 'RelateNumber': 'Tea0001', # 特店自訂編號
            # 'CustomerID': 'TEA_0000001', # 客戶編號
            # 'CustomerIdentifier': '53348111', # 統一編號
            # 'CustomerName': '客戶名稱',
            # 'CustomerAddr': '客戶地址',
            # 'CustomerPhone': '0912345678', # 客戶手機號碼
            # 'CustomerEmail': 'abc@ecpay.com.tw',
            # 'ClearanceMark': '2', # 通關方式
            # 'TaxType': '1', # 課稅類別
            # 'CarruerType': '', # 載具類別
            # 'CarruerNum': '', # 載具編號
            # 'Donation': '1', # 捐贈註記
            # 'LoveCode': '168001', # 捐贈碼
            # 'Print': '1',
            # 'InvoiceItemName': '測試商品1|測試商品2',
            # 'InvoiceItemCount': '2|3',
            # 'InvoiceItemWord': '個|包',
            # 'InvoiceItemPrice': '35|10',
            # 'InvoiceItemTaxType': '1|1',
            # 'InvoiceRemark': '測試商品1的說明|測試商品2的說明',
            # 'DelayDay': '0', # 延遲天數
            # 'InvType': '07', # 字軌類別
        }

        ecpay_payment_sdk = module.ECPayPaymentSdk(
            MerchantID=params['MerchantID'],
            HashKey=params['HashKey'],
            HashIV=params['HashIV'])

        # 合併延伸參數
        order_params.update(extend_params_1)
        order_params.update(extend_params_2)

        # 合併發票參數
        order_params.update(inv_params)

        try:
            # 產生綠界訂單所需參數
            final_order_params = ecpay_payment_sdk.create_order(order_params)

            # 產生 html 的 form 格式
            action_url = params['action_url']
            htmll = ecpay_payment_sdk.gen_html_post_form(
                action_url,
                final_order_params)
            return make_response(htmll)
            
        except Exception as error:
            print('An exception happened: ' + str(error))

api.add_resource(Payment,'/to_ecpay',endpoint='ecp')

'''
stagetest1234
test1234
53538851
'''
