import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from Log_navbar import Log_Navbar
nav = Log_Navbar()


form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Email", className="mr-2"),
                dbc.Input(id="email-input",type="email", placeholder="Enter email"),
                dbc.FormFeedback(
                    valid=False,
                ),
            ],
            className="mr-3",
        ),html.Br(),html.Br(),
        dbc.FormGroup(
            [
                dbc.Label("Password", className="mr-2"),
                dbc.Input(id="pass-input",type="password", placeholder="Enter password"),
                dbc.FormFeedback(
                    valid=False,
                ),
            ],
            className="mr-3",
        ),html.Br(),html.Br(),
        dbc.Button("Submit",id="Log-button", color="primary"),
    ],
    inline=True
)

card = dbc.Card(
        dbc.CardBody(
            [
                html.H4('Log In', className="card-title"),
                html.Br(),
                html.Br(),
                form,
                html.Br(),
                html.Br(),
                ]
        ),
        color="info", inverse=True
    )
graphRow=dbc.Row([dbc.Col(md=6),dbc.Col(children=[card],md=6)])


def Homepage():
    layout = html.Div(children=[
    nav,html.H5(id='fedbk'),html.Canvas(id='yes',height=1080,width=1920,style={'background-image':'url("assets/2.jpg")',
    'background-repeat': 'no-repeat',
	'background-size': '85% 75%'}),html.Div(id='my-div')
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()


