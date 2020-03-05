import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar



nav = Navbar()


colors = {
    'background': '#202A3B',
    'text': '#8091AB'
}

#######################  GENDER    ######################################

vals=['Male','Female']

options = [{'label':x, 'value': x} for x in vals]

ddGender = html.Div(dcc.Dropdown(
    id = 'Gender',
    options = options,
    value = 'Male'
),style={'margin-top':'20px','margin-left': '85px','width':'25%','display':'inline-block'})


##################################     Partner   #####################################

vals=['Yes','No']

options = [{'label':x, 'value': x} for x in vals]

ddPartner = html.Div(dcc.Dropdown(
    id = 'Partner',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '85px','width':'25%','display':'inline-block'})


######################################################################################  

##################################     Dependents   #####################################

vals=['Yes','No']

options = [{'label':x, 'value': x} for x in vals]

ddDependents = html.Div(dcc.Dropdown(
    id = 'Dependents',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '60px','width':'25%','display':'inline-block'})

######################################################################################

##################################     PhoneService   #####################################

vals=['Yes','No']

options = [{'label':x, 'value': x} for x in vals]

ddPhoneService = html.Div(dcc.Dropdown(
    id = 'PhoneService',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '35px','width':'25%','display':'inline-block'})

######################################################################################

##################################     MultipleLines   #####################################

vals=['No Phone Service','No','Yes']

options = [{'label':x, 'value': x} for x in vals]

ddMultiplelines = html.Div(dcc.Dropdown(
    id = 'MultipleLines',
    options = options,
    value = 'No'
),style={'margin-top':'20px','margin-left': '50px','width':'25%','display':'inline-block'})

######################################################################################

##################################     InternetService   #####################################

vals=['DSL','No','Fiber optic']

options = [{'label':x, 'value': x} for x in vals]

ddInternetService = html.Div(dcc.Dropdown(
    id = 'InternetService',
    options = options,
    value = 'DSL'
),style={'margin-top':'20px','margin-left': '25px','width':'25%','display':'inline-block'})

######################################################################################

##################################   Online Security  #####################################

vals=['Yes','No','No Internet Service']

options = [{'label':x, 'value': x} for x in vals]

ddOnlineSecurity = html.Div(dcc.Dropdown(
    id = 'OnlineSecurity',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '37px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Onlinebackup   #####################################

vals=['Yes','No','No Internet Service']

options = [{'label':x, 'value': x} for x in vals]

ddOnlineBackup = html.Div(dcc.Dropdown(
    id = 'OnlineBackup',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '31px','width':'25%','display':'inline-block'})

######################################################################################

##################################    Device Protection  #####################################

vals=['Yes','No','No Internet Service','No Device']

options = [{'label':x, 'value': x} for x in vals]

ddDeviceProtection = html.Div(dcc.Dropdown(
    id = 'DeviceProtection',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '10px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Tech Support   #####################################

vals=['Yes','No']

options = [{'label':x, 'value': x} for x in vals]

ddTechSupport = html.Div(dcc.Dropdown(
    id = 'TechSupport',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '45px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Streaming TV   #####################################

vals=['Yes','No','No Internet Service']

options = [{'label':x, 'value': x} for x in vals]

ddStreamingTV = html.Div(dcc.Dropdown(
    id = 'StreamingTV',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '47px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Streaming Movies   #####################################

vals=['Yes','No','No Internet Service']

options = [{'label':x, 'value': x} for x in vals]

ddStreamingMovies = html.Div(dcc.Dropdown(
    id = 'StreamingMovies',
    options = options,
    value = 'No'
),style={'margin-top':'20px','margin-left': '10px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Contract   #####################################

vals=['Month-to-month','One year','Two year']

options = [{'label':x, 'value': x} for x in vals]

ddContract = html.Div(dcc.Dropdown(
    id = 'Contract',
    options = options,
    value = 'Month-to-month'
),style={'margin-top':'20px','margin-left': '73px','width':'25%','display':'inline-block'})

######################################################################################

##################################     Paperless Billing   #####################################

vals=['Yes','No']

options = [{'label':x, 'value': x} for x in vals]

ddPaperlessBilling = html.Div(dcc.Dropdown(
    id = 'PaperlessBilling',
    options = options,
    value = 'Yes'
),style={'margin-top':'20px','margin-left': '37px','width':'25%','display':'inline-block'})

######################################################################################

##################################     PaymentMethod   #####################################

vals=['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)']

options = [{'label':x, 'value': x} for x in vals]

ddPaymentMethod = html.Div(dcc.Dropdown(
    id = 'PaymentMethod',
    options = options,
    value = 'Mailed check'
),style={'margin-top':'20px','margin-left': '25px','width':'25%','display':'inline-block'})

######################################################################################

FirstCol=dbc.Col(id='ft10',
    children=[html.Label('Gender: ', style={
            'textAlign': 'center',
            'margin-left': '30px',
            'display':'inline-block',
            'vertical-align':'middle',
            'color': colors['text']
    }),
    ddGender,
    html.Br(),
    html.Br(),
    html.Label('InternetService: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddInternetService,
    html.Br(),
    html.Br(),
    html.Label('Device Protection: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddDeviceProtection,
    html.Br(),
    html.Br(),
    html.Label('Partner: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddPartner,
    html.Br(),
    html.Br(),
    html.Label('Streaming Movies: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddStreamingMovies,
    html.Br(),
    html.Br(),
    html.Label('Phone Service: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddPhoneService,
    html.Br(),
    html.Br(),
    html.Label('Contract: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddContract,
    html.Br(),
    html.Br(),
    html.Label('Online Backup: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddOnlineBackup,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Tenure: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    dcc.Input(
    id='Tenure',
    placeholder = '0',
    type='number',
    value ='0',
    min='0',
    style={'margin-left':'85px',
            'width':'25%'}
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Button("Predict",id="Predict-button", color="primary",style={'margin-left':'540px',
                                                                    'width':'25%'}),
    html.Br(),
    html.Br(),
    html.H4("CUSTOMER",id="result",style={'margin-left':'540px',
        'color':'#FFFFFF'})
    ],md=6#Child  dead
)

SecondCol=dbc.Col(id='ft10-2',
    children=[html.Label('PaperlessBilling: ', style={
            'textAlign': 'center',
            'margin-left': '30px',
            'display':'inline-block',
            'vertical-align':'middle',
            'color': colors['text']
    }),
    ddPaperlessBilling,
    html.Br(),
    html.Br(),
    html.Label('Dependents: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddDependents,
    html.Br(),
    html.Br(),
    html.Label('Payment Method: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddPaymentMethod,
    html.Br(),
    html.Br(),
    html.Label('Online Security: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddOnlineSecurity,
    html.Br(),
    html.Br(),
    html.Label('MultipleLines: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddMultiplelines,
    html.Br(),
    html.Br(),
    html.Label('Streaming TV: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddStreamingTV,
    html.Br(),
    html.Br(),
    html.Label('Tech Support: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    ddTechSupport,
    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Total Charges: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    dcc.Input(
    id='TotalCharges',
    placeholder = '0.00',
    type='number',
    value ='0.0',
    min='0',
    style={'width':'25%',
    'margin-left':'40px'}
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Label('Monthly Charges: ', style={
            'textAlign': 'left',
            'margin-left': '30px',
            'color': colors['text']
    }),
    dcc.Input(
    id='MonthlyCharges',
    placeholder = '0.00',
    type='number',
    value ='0.0',
    min='0',
    style={'width':'25%',
    'margin-left':'18px'}
    )
    ],md=6#Child  dead
)

rowft=dbc.Row(children=[FirstCol,SecondCol],style={'height':'1080px'})












def Prediction():
    layout = html.Div( style={'backgroundColor': colors['background'], 'textAlign': 'left'}, children=[nav,
    rowft,
])
    return layout



