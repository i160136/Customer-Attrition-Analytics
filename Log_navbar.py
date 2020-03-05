import dash_bootstrap_components as dbc
import dash_html_components as html

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
        ),html.Br(),
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
        dbc.Button("Log In",id="Log-button", color="primary"),
    ],
    inline=True,
    style={'margin-left':'480px'}
)

def Log_Navbar():
     navbar = dbc.Navbar(
           children=[ html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("Customer Attrition Analytics", className="ml-2",style={'margin-left':'15px'})),
                ],
                align="center",
                no_gutters=True,
            ),
            href="/",
        ),html.Br(),form
              
    ],
    color="white",
    dark=False,
)
     return navbar
