import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import Output, Input

app = dash.Dash(__name__)

app.layout = html.Div(

                fac.AntdCol(
                    fac.AntdAffix(
                        fuc.FefferyDiv(
                            [
                                fac.AntdRow(
                                    fac.AntdText('Agents', style={'border-bottom': '1px solid black', 'width': '100%'}),
                                ),
                                fac.AntdText('Select or create an agent workflow'),
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fac.AntdText('Default Agent')
                                        ),
                                        fac.AntdCol(
                                            [
                                                fac.AntdButton('Settings', type='link', block=True, id='btn'),
                                                fac.AntdModal('测试内容', id='modal', title='对话框示例')
                                            ]
                                        )
                                    ], align='middle', justify='space-between',
                                ),
                                fac.AntdSelect(
                                    options=[
                                        {
                                            'label': f'选项{i}',
                                            'value': f'选项{i}'
                                        } for i in range(1, 6)
                                    ], style={'width': 200}
                                ),
                                fac.AntdRow(
                                    [
                                        fac.AntdText('Skills'),
                                        fac.AntdDivider(),
                                        fac.AntdText('Skills are python functions that agents can use to solve tasks.'),

                                    ]
                                )

                            ],
                            scrollbar='simple',
                            style={
                                'width': 300,
                                'height': 'calc(100vh - 64px)',
                                'overflowY': 'auto'
                            }
                        ),
                        offsetTop=64, style={'padding': '20px'}  # 扣除页首所占高度
                    ),
                    flex='none'
                ),
)


if __name__ == '__main__':
    app.run(debug=True)
