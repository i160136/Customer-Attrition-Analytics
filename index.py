import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import App, build_graph
from homepage import Homepage
from model import *
from prediction import Prediction
from report import Report

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
M=model()
M.load()
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = True),
    html.Div(id = 'page-content')
])

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
        Sample['Gender'].replace(['Male','Female'],[0,1],inplace=True)
        Sample['Partner'].replace(['Yes','No'],[1,0],inplace=True)
        Sample['Dependents'].replace(['Yes','No'],[1,0],inplace=True)
        Sample['PhoneService'].replace(['Yes','No'],[1,0],inplace=True)
        Sample['MultipleLines'].replace(['No phone service','No', 'Yes'],[0,0,1],inplace=True)
        Sample['InternetService'].replace(['No','DSL','Fiber optic'],[0,1,2],inplace=True)
        Sample['OnlineSecurity'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['OnlineBackup'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['DeviceProtection'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['TechSupport'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['StreamingTV'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['StreamingMovies'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
        Sample['Contract'].replace(['Month-to-month', 'One year', 'Two year'],[0,1,2],inplace=True)
        Sample['PaperlessBilling'].replace(['Yes','No'],[1,0],inplace=True)
        Sample['PaymentMethod'].replace(['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'],[0,1,2,3],inplace=True)
        for i in features:
            Sample[i]=pd.to_numeric(Sample[i])
        print(Sample.head())
        Pres=M.predict(Sample)
        if(Pres==1):
            return 'Customer is going to Churn.'
        return 'No Churn'



if __name__ == '__main__':
    app.run_server(debug=True)


