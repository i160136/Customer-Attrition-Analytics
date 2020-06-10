import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pyodbc
import plotly
import plotly.graph_objs as go
from model import *
from navbar import Navbar




M=model()
conn = pyodbc.connect('Driver={SQL Server};'
                  'Server=EXCV;'
                  'Database=Churn;'
                  'Trusted_Connection=yes;')
a='select * from dbo.Customer'
data=pd.read_sql(a,conn)
nav = Navbar()
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

colors = {
    'background': '#202A3B',
    'text': '#8091AB'
}

cursor = conn.cursor()
cursor.execute('SELECT count(*) FROM dbo.Customer')

for row in cursor:
    count=row[0]

cursor = conn.cursor()
cursor.execute("select count(*) from Customer WHERE Churn = 'Yes'")

for row in cursor:
    ChCases=row[0]

NonCases=count-ChCases


trace1 = go.Pie(
                labels = ['Churn','Non-Churn'],
                values= [ChCases,NonCases],
                name='OperatorShare'
                )
data = [trace1]
layout = go.Layout(
                   title='',
                   )
fig = go.Figure(data=data, layout=layout)
fig.update_layout({
    'title':'Overall Distribution',
    'plot_bgcolor': '#202A3B',
    'paper_bgcolor': '#202A3B',
    'font': dict(size=14,color="#FFFFFF")
    })
pie=dcc.Graph(id='pie_plot',
              figure=fig
              )


trace2 = go.Pie(
                labels = [FI[0][0], FI[1][0], FI[2][0],FI[3][0],FI[4][0],FI[5][0], FI[6][0], FI[7][0],FI[8][0],FI[9][0],FI[10][0], FI[11][0], FI[12][0],FI[13][0],FI[14][0],FI[15][0], FI[16][0], FI[17][0],FI[18][0]],
                values= [FI[0][1], FI[1][1], FI[2][1],FI[3][1],FI[4][1],FI[5][1], FI[6][1], FI[7][1],FI[8][1],FI[9][1],FI[10][1], FI[11][1], FI[12][1],FI[13][1],FI[14][1],FI[15][1], FI[16][1], FI[17][1],FI[18][1]],
                name='OperatorShare'
                )
data2 = [trace2]
layout1 = go.Layout(
                   title='',
                   )
fig1 = go.Figure(data=data2, layout=layout1)
fig1.update_layout({
    'title':'Feature Contribution',
    'plot_bgcolor': '#202A3B',
    'paper_bgcolor': '#202A3B',
    'font': dict(size=14,color="#FFFFFF")
    })
pie1=dcc.Graph(id='pie_plot',
              figure=fig1
              )

graphRow0 = dbc.Row([dbc.Col(children=[pie1], md=6), dbc.Col(children=[pie], md=6)],style={'height':'600px'})

def Report():
    layout = html.Div(style={'backgroundColor':'#202A3B'}, children=[nav,html.H3("Total Cases:     "+str(count),style={'color':'#FFFFFF','margin-top':'30px','margin-left':'20px'}),
        graphRow0
])
    return layout



