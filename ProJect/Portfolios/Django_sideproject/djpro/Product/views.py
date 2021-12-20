from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Product
from django.views.decorators.csrf import csrf_exempt,csrf_protect


def ShoppingView(request):
    productname=''
    startprice=''
    endprice=''

    if request.GET:
        productname = request.GET.get('productName','')
        startprice = request.GET.get('startp','')
        endprice = request.GET.get('endp','')
        sort = request.GET.get('sort','price')

        if len(productname)>0 and len(startprice)>0 and len(endprice)>0:
            data = Product.objects.filter(name__icontains=productname, price__gte=startprice, price__lte=endprice).order_by(sort)
        elif len(productname)==0 and len(startprice)>0 and len(endprice)>0:
            data = Product.objects.filter(price__gte=startprice, price__lte=endprice).order_by(sort)
        else:
            data = Product.objects.filter(name__icontains=productname).order_by(sort)
    else:
        data = Product.objects.all().order_by('price')

    #先抓好資料再分頁
    if request.method == 'POST':
        print(request.POST)
        pass



    paginator=Paginator(data,5)
    page=request.GET.get('page')  #顯示url指定頁面
    try:
        data=paginator.page(page)
    except PageNotAnInteger:      # 如果換頁錯誤
        data=paginator.page(1)   #跳回第一頁
    except EmptyPage:             # 如果是空白頁面
        data=paginator.page(paginator.num_pages)  # 跳到最後一頁

    context = {
        'outPut':data,
        'productName':productname,
        'startp':startprice,
        'endp':endprice
    }


    return  render(request, 'product-shop.html', context = context)
    