import dash_bootstrap_components as dbc


def Navbar():
     navbar = dbc.NavbarSimple(
            children=[
              dbc.NavItem(dbc.NavLink("Home",href="/dash-board")),
            	dbc.NavItem(dbc.NavLink("Predict", href="/prediction")),
            	dbc.NavItem(dbc.NavLink("Report", href="/report")),
              dbc.NavItem(dbc.NavLink("Log Out", href="/"))
    ],
    brand="Customer Attrition Analytics",
    brand_href="/dash-board",
    color="white",
    dark=False,
)
     return navbar
