from agents import AgentsView
from dash import html

def SideBarView():
    return html.Div(
        [
            html.Div(
                [
                    AgentsView()
                ],
                className='flex-1'
            )
        ],
        className='transition overflow-hidden duration-300  flex flex-col    h-full p-2'
    )

