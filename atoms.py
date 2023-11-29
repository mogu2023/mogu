from dash import html
import dash

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(__name__,
                external_scripts=external_script)
app.scripts.config.serve_locally = True


def GroupView(children, title, className = ""):
    return html.Div(
                html.Div(
                    [
                        html.Div(title,
                                className='absolute  -top-5   bg-primary p-2 inline-block'),
                        html.Div(children,
                                className='mt-2')
                    ] ,className='mt-4 p-2 rounded border relative'
                    ),
                className='rounded mt-4  border-secondary'
            )


def ControlRowView(title, description, value, control, className):
    html.Div(
        [
            html.Div(
                [
                    html.Span(title, className="text-primary inline-block"),
                    html.Span(value, className="text-xs ml-1 text-accent -mt-2 inline-block")
                ]
            ),
            html.Div(description, className='text-secondary text-xs'),
            control,
            html.Div(className='border-b border-dashed mt-2 mx-2')
        ],
        className=className
    )