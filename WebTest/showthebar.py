import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import json


app = dash.Dash()
server = app.server

def get_show_bar():
    sctx = []
    scty1 = []
    with open('IPres.json','r',encoding='utf-8') as file:
        data = json.load(file)
    for k,v in data[1].items():
        sctx.append(k)
        scty1.append(v)
    # sctx = [
    #     'Taipei',"China"
    #     # '2019/1/11', '2019/1/12', '2019/1/13', '2019/1/14', '2019/1/15',
    #     # '2019/1/16', '2019/1/17', '2019/1/18', '2019/1/19', '2019/1/20',
    # ]
    # scty1 = [
    #     5,6
    # ]

    trace1 = go.Bar(
        x=sctx,
        y=scty1,
        name='食物类',
        hoverlabel={
            'bgcolor': '#000000',
            'bordercolor': '#000000', #浮标外框颜色
            'font': {
                'family': ['Arial', 'Balto', 'Courier New', 'Droid Sans', 'Droid Serif', 'Droid Sans Mono', 'Gravitas One', 'Old Standard TT', 'Open Sans', 'Overpass'],
                'size': 20,
                'color': '#FFFFFF'
            },
            'align': 'left', #设置对齐方式，默认‘auto’，还可以是‘left’、‘right’
            'namelength': 2, #显示浮标中‘name’属性的字符串长度
        },
        marker={
            # 'line': { #设置线的样式
            # 'width': 4, #线的宽度
            # 'color': '#FFFFFF', #先的颜色
            # },
            'color': scty1,
            'colorbar': {
                'thicknessmode': 'pixels',
                'thickness': 12,
                'lenmode': 'fraction',
                'len': 0.8,
                'x': -0.08,
                'xanchor': 'center',
                'y': 0, #标尺的y位置
                'yanchor': 'bottom',
                'tickformat': '.2s',
                'title': { 
                    'text': '人數',
                    'font': {
                        'size': 16,
                        'color': '#000000',
                    },
                    'side': 'top',
                },
            },
        },
    )
    layout = go.Layout(
        title='全球IP位置',
        barmode='group', #可以分为 ‘stack’(叠加）、‘group’（分组）、‘overlay’（重叠）、‘relative’（相关）， 默认是‘group’
        barnorm='', #设置柱形图纵轴或横轴数据的表示形式，可以是fraction（分数），percent（百分数）
        yaxis={
            # 'hoverformat': '.2%',
            # 'showline': True,
            # 'showgrid': True,
            # 'side': 'right',
        }
    )
    return go.Figure(
        data=[trace1],
        layout=layout
    )


app.layout = html.Div([
    dcc.Graph(
        id='show_graph',
        figure=get_show_bar()
    ),
    html.Div(
        id = 'show_click_content',
        style={
            'margin-top': 20,
            'text-align': 'center',
            'font-size': 30
        }
    )
], style={'margin': 100})

@app.callback(
    Output('show_click_content', 'children'),
    [
        Input('show_graph', 'clickData'), #监听点击事件，会将每个点的信息带出来
    ]
)
def show_click_content(clickdata):
    if clickdata == None:
        return ''
    return str(clickdata)

if __name__ == '__main__':
    app.run_server(debug=True)