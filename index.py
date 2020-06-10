import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import App, build_graph
from homepage import Homepage
from model import *
from prediction import Prediction
import dash_table
from report import Report
import plotly.graph_objs as go
import base64
import datetime
import io
import pyodbc
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
conn = pyodbc.connect('Driver={SQL Server};'
                  'Server=EXCV;'
                  'Database=Churn;'
                  'Trusted_Connection=yes;')
a='select * from dbo.Customer'
data=pd.read_sql(a,conn)
M=model()
#print(data.head())
M.load()
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = True),
    html.Div(id = 'page-content')
])







def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    if 'csv' in filename:
            # Assume that the user uploaded a CSV file
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
    elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    else:
        #print(e)
        return html.Div([
            html.H5('File is not compatible.',style={'color':'white','margin-left':'30px'})
        ])

#ENCODING DATAFRAME FEATURES
    df=M.encoding(df)
    pr=df.drop(columns=[df.columns[0]],axis=1)
    for i in pr.columns:
            pr[i]=pd.to_numeric(pr[i])

#PREDICTION OF BATCH AND DISTRIBUTION
    PredRes=M.predict(pr)
    CHCases=0
    NCHcases=0
    for i in PredRes:
        if i==1:
            CHCases+=1
        else:
            NCHcases+=1

#PIE CHARTVISUALIZATION OF DISTRIBUTION
    trace1=go.Pie(labels=['Churn','Non-Churn'], values=[CHCases,NCHcases], name='Git')
    data=[trace1]
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
    df['Churn']=PredRes
    df['Churn'].replace([0,1],['No','yes'],inplace=True)
    columns=['customerID','MonthlyCharges','Churn']


#PRESENTING RESULTS IN A DATA TABLE
    FirstCol=dbc.Col(id='BatchPred',children=[
        html.Div([
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in columns],
            style_as_list_view=True,
            style_cell={'padding': '5px', 'backgroundColor': '#202A3B','color':'white',},
            style_data={'width': '100px',
        'maxWidth': '100px',
        'minWidth': '100px'},
            style_header={
            'backgroundColor': '#202A3B',
            'color':'white',
            'fontWeight': 'bold'
            },
            style_cell_conditional=[
                {
                'if': {'column_id': c},
                'textAlign': 'left'
                } for c in ['Date', 'Region']
                ],
            css=[{'selector': '.row', 'rule': 'margin-left: 50px'}]
        )
    ])],md=6)

    SecondCol=dbc.Col(id='CD',children=[pie],md=6)
    FirstRow=dbc.Row(children=[FirstCol,SecondCol])
    return FirstRow



@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
        if pathname == '/dash-board':
                return App()
        elif pathname == '/prediction':
                return Prediction()
        elif pathname == '/report':
                return Report()
        else:
                return Homepage()

@app.callback(
    Output('output', 'children'),        
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph

@app.callback(
    [Output("email-input", "valid"), Output("email-input", "invalid")],
    [Input("email-input", "value")],
)
def check_email(text):
    if text:
        is_gmail = text.endswith("@nu.edu.pk")
        return is_gmail, not is_gmail
    return False, False

@app.callback(
    [Output(component_id='fedbk',component_property='children'),Output('url', 'pathname')],
    [Input('Log-button','n_clicks')],[State('email-input','value'),State('pass-input','value')]
    )
def valid_check(n_clicks,input1,input2):
    if n_clicks>0:
        if input1=='Hasan@nu.edu.pk':
            if input2=='fast':
                return 'Successful Login','/dash-board'
            else:
                return 'Incorrect password','/'
        else:
            return 'Incorrect username or password','/'


@app.callback(
    Output('result', 'children'),
    [Input('Predict-button', 'n_clicks')],
    state=[State('Gender', 'value'),
     State('Partner', 'value'),
     State('Dependents', 'value'),
     State('PhoneService', 'value'),
     State('MultipleLines', 'value'),
     State('InternetService', 'value'),
     State('OnlineSecurity', 'value'),
     State('OnlineBackup', 'value'),
     State('DeviceProtection', 'value'),
     State('TechSupport', 'value'),
     State('StreamingTV', 'value'),
     State('StreamingMovies', 'value'),
     State('Contract', 'value'),
     State('PaperlessBilling', 'value'),
     State('PaymentMethod', 'value'),
     State('Tenure', 'value'),
     State('TotalCharges', 'value'),
     State('MonthlyCharges', 'value'),
     ])
def compute(n_clicks, Gender, Partner, Dependents,PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
    TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,Tenure,TotalCharges,MonthlyCharges):
    if n_clicks is None:
        return ''
    elif(TotalCharges is None or MonthlyCharges is None or Tenure is None):
        return 'Invalid Input!'
    else:
        features=['Gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
        sdf=[[Gender,0, Partner, Dependents,int(Tenure),PhoneService,MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,
        TechSupport,StreamingTV,StreamingMovies,Contract,PaperlessBilling,PaymentMethod,float(MonthlyCharges),float(TotalCharges)]]
        Sample=pd.DataFrame(sdf,columns=features)
        Sample=M.encoding(Sample)
        for i in features:
            Sample[i]=pd.to_numeric(Sample[i])
        print(Sample.head())
        Pres=M.predict(Sample)
        if(Pres[0]==1):
            return 'Customer is predicted to Churn.'
        return 'Customer is predicted to be Non-churn.'

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')],
              [State('upload-data', 'filename'),
               State('upload-data', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

@app.callback(
    [Output('ModBod', "children"),Output('close','style')] , [Input('train_model', 'n_clicks'),Input("modal", "is_open")]
)
def on_button_click(n,is_open):
    if (is_open==True):
        if n is None :
            return "The model is being trained",{'display':'None'}
        else:
            print("Clicked")
            a='select * from dbo.Customer'
            data=pd.read_sql(a,conn)
            M.fit(data)
            print("Training Complete")
            return "Model trained Successfully",{'display':'inline'}
    else:
        return "The model is being trained",{'display':'None'}


@app.callback(
    Output("modal", "is_open"),
    [Input("train_model", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open





if __name__ == '__main__':
    app.run_server(debug=True)


