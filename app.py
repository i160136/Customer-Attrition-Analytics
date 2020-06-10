### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px
## Navbar
from navbar import Navbar
from copy import deepcopy
from model import *
import pyodbc





nav = Navbar()

M=model()
conn = pyodbc.connect('Driver={SQL Server};'
                  'Server=EXCV;'
                  'Database=Churn;'
                  'Trusted_Connection=yes;')
a='select * from dbo.Customer'
data=pd.read_sql(a,conn)

data2=deepcopy(data)
data2['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors = 'coerce')
data2.loc[data['TotalCharges'].isna()==True]


data.pop('TotalCharges')
data.pop('MonthlyCharges')
data.pop('tenure')
data.pop('Churn')
data.pop('SeniorCitizen')
data.pop('C_ID')
features=[]
for col in data.columns:
    features.append(col)
M.load()
FI=M.featureImportance()





def create_card(title, content):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.Br(),
                html.Br(),
                html.H2(content, className="card-subtitle"),
                html.Br(),
                html.Br(),
                ]
        ),
        color="info", inverse=True
    )
    return(card)

cursor=conn.cursor()
a='select count(*) from Customer'
b="select count(*) from Customer WHERE Churn = 'Yes'"
cursor.execute(a)
for i in cursor:
    cases=i

TCases=cases[0]
card3 = create_card("Total Cases", TCases)
cursor.execute(b)
for i in cursor:
    cases=i
CRate=cases[0]*100
CRate=CRate/TCases
card2 = create_card("Churn Cases", cases[0])
card1 = create_card("Churn Rate", "{0:.3f}".format(CRate)+str(' %'))



bar = dcc.Graph(
        id = "3",
        figure ={
                  "data": [
                  {
                        'y':[FI[0][1], FI[1][1], FI[2][1],FI[3][1],FI[4][1]],
                          'x':[FI[0][0], FI[1][0], FI[2][0],FI[3][0],FI[4][0]],
                          'name':'SF Zoo',
                          #'orientation':'h',
                          'type':'bar',
                          'marker' :dict(color=['#05C7F2','#D90416','#D9CB04','#05C716','#D904F2']),
                  }],
                "layout": {
                      "title" : dict(text ="Top Churn Factors",
                                     font =dict(
                                     size=20,
                                     color = 'white')),
                      "xaxis" : dict(tickfont=dict(
                          color='white')),
                      "yaxis" : dict(tickfont=dict(
                          color='white')),
                      "paper_bgcolor":"#202A3B",
                      "plot_bgcolor":"#202A3B",
                      "width": "2000",
                      #"grid": {"rows": 0, "columns": 0},
                      "annotations": [
                          {
                              "font": {
                                  "size": 20
                              },
                              "showarrow": False,
                              "text": "",
                              "x": 0.2,
                              "y": 0.2
                          }
                      ],
                      "showlegend": False
                  }
              }
	)

#b=html.Canvas(id='yes',height=256,width=350,style={'background-image':'url("assets/dial.png")',
#    'background-repeat': 'no-repeat',
#  'background-size': '85% 75%'})


modal = html.Div(
    [
        dbc.Modal(
            [
                dbc.ModalHeader("Status"),
                dbc.ModalBody("The Model is being Trained",id='ModBod'),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close",color='primary', className="ml-auto",style={'display':'None'})
                ),
            ],
            id="modal",backdrop="static",keyboard=False
        ),
    ]
)



b=dbc.Button('Train Model', id='train_model',size='lg',color='primary', style={'margin-left': '10%','margin-top':'20%','height':'20%','width':'80%'})
x=html.Div(id="hidden",style={'display':'None'})
graphRow0 = dbc.Row([dbc.Col(id='card1', children=[card3,modal,x,b], md=3), dbc.Col(id='card2', children=[card2,html.Br(),card1], md=3),dbc.Col(bar,md=6)])






##########################################################################################

header = html.H3(
    'Select the name of an Illinois city to see its population!'
)

options = [{'label':x, 'value': x} for x in features]

dropdown = html.Div(dcc.Dropdown(
    id = 'pop_dropdown',
    options = options,
    value = 'Partner'
),style={'width':'49%','display':'inline-block'})

output = html.Div(id = 'output',
                children = [],
                )

def App():
    layout = html.Div([
        nav,html.Br(),graphRow0, html.Br(),dropdown, output], style={'backgroundColor':'#17202E'})
    return layout

def build_graph(city):
    Categories=data[city].unique()
    ChurnD=[]
    NonChurnD=[]
    for j in Categories:
      print (type(j))
      qry="Select count(*) from Customer where "+city+"='"+j+"' and Churn='Yes'"
      cursor.execute(qry)
      for i in cursor:
        ChurnD.append(i)
      qry="Select count(*) from Customer where "+city+"='"+j+"' and Churn='No'"
      cursor.execute(qry)
      for i in cursor:
        NonChurnD.append(i)

    trace1 = go.Bar(
      x=Categories,
      y=[k[0] for k in NonChurnD],
      name='Non-Churn'
    )
    trace2 = go.Bar(
      x=Categories,
      y=[k[0] for k in ChurnD],
      name='Churn'
    )
    fig=go.Figure(data=[trace1, trace2],
                               layout=go.Layout(title=city+' Distribution',paper_bgcolor='#202A3B',plot_bgcolor='#202A3B',font=dict(size=14,color="#FFFFFF")))
    stack=dcc.Graph(id='bar_plot',
              figure=fig
              )

    fig1 = px.scatter(data2, x="MonthlyCharges", y="tenure", color="Churn",hover_data=['Contract','TotalCharges'])
    fig1.update_layout({
    'title':'Churn Distribution',
    'plot_bgcolor': '#202A3B',
    'paper_bgcolor': '#202A3B',
    'font': dict(size=14,color="#FFFFFF")
    })
    scatter=dcc.Graph(
        id='example-graph-2',
        figure=fig1
    )

    
    graphRow1 = dbc.Row([dbc.Col(stack, md=6),dbc.Col(scatter,md=6)])
    return graphRow1

