import dash
from dash import html
from sidebar import SideBarView

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(__name__,
                external_scripts=external_script)
app.scripts.config.serve_locally = True

app.layout = html.Div(
    SideBarView()
)

app.run(debug=True)