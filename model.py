import pandas as pd
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score
import numpy as np
from imblearn.over_sampling import SMOTE
from collections import Counter
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.ensemble import VotingClassifier
from collections import Counter 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle


class model:
	def __init__(self):
		self.clf4 = RandomForestClassifier(bootstrap=True, class_weight='balanced',
                       criterion='gini', max_depth=20, max_features='log2',
                       max_leaf_nodes=None, min_impurity_decrease=0.0,
                       min_impurity_split=None, min_samples_leaf=1,
                       min_samples_split=5, min_weight_fraction_leaf=0.0,
                       n_estimators=500, n_jobs=-1, oob_score=True,
                       random_state=0, verbose=0, warm_start=False)
		self.clf2 = LogisticRegression()
		self.clf3 =  XGBClassifier(colsample_bytree= 0.6043861515534555, learning_rate= 0.017456463325448757, max_depth= 3, min_child_weight= 4, n_estimators= 832, subsample= 0.8040649088253156)
		self.clf1=MLPClassifier(max_iter=100,activation= 'relu', alpha= 0.0001, hidden_layer_sizes= (100,), learning_rate= 'constant', solver= 'adam')
		self.eclf1 = VotingClassifier(estimators=[('NN',self.clf1),('lr',self.clf2) ,('xgb', self.clf3),('rf',self.clf4)], voting='soft')

	def clean_data(self,data):
		data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors = 'coerce')
		data.loc[data['TotalCharges'].isna()==True]

		data[data['TotalCharges'].isna()==True] = 0
		data['OnlineBackup'].unique()

		data['Gender'].replace(['Male','Female'],[0,1],inplace=True)
		data['Partner'].replace(['Yes','No'],[1,0],inplace=True)
		data['Dependents'].replace(['Yes','No'],[1,0],inplace=True)
		data['PhoneService'].replace(['Yes','No'],[1,0],inplace=True)
		data['MultipleLines'].replace(['No phone service','No', 'Yes'],[0,0,1],inplace=True)
		data['InternetService'].replace(['No','DSL','Fiber optic'],[0,1,2],inplace=True)
		data['OnlineSecurity'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['OnlineBackup'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['DeviceProtection'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['TechSupport'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['StreamingTV'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['StreamingMovies'].replace(['No','Yes','No internet service'],[0,1,0],inplace=True)
		data['Contract'].replace(['Month-to-month', 'One year', 'Two year'],[0,1,2],inplace=True)
		data['PaperlessBilling'].replace(['Yes','No'],[1,0],inplace=True)
		data['PaymentMethod'].replace(['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'],[0,1,2,3],inplace=True)
		data['Churn'].replace(['Yes','No'],[1,0],inplace=True)

		data.pop('C_ID')

		X = data.drop('Churn', 1)
		y = data['Churn']

		X_t, X_test, y_t, y_test = train_test_split(X,y,test_size = 0.20, random_state = 40)
		#print('Original dataset shape %s' % Counter(y_t))
		sm = SMOTE(random_state=42)
		X_train, y_train = sm.fit_resample(X_t, y_t)
		#print('Resampled dataset shape %s' % Counter(y_train))
		X_train=pd.DataFrame(X_train,columns=X.columns)
		return X_train,y_train,X_test,y_test

	def fit(self,data):
		#x_train,y_train,x_test,y_test=self.clean_data(data)
		#self.clf3.fit(x_train,y_train)
		#self.eclf1.fit(x_train,y_train)
		filename = 'finalized_model.sav'
		#pickle.dump(self.eclf1, open(filename, 'wb'))
		self.eclf1 = pickle.load(open(filename, 'rb'))
		filename = 'model.sav'
		#pickle.dump(self.clf3, open(filename, 'wb'))
		self.clf3 = pickle.load(open(filename, 'rb'))
		return

	def load(self):
		filename = 'finalized_model.sav'
		#pickle.dump(self.eclf1, open(filename, 'wb'))
		self.eclf1 = pickle.load(open(filename, 'rb'))
		filename = 'model.sav'
		#pickle.dump(self.clf3, open(filename, 'wb'))
		self.clf3 = pickle.load(open(filename, 'rb'))
		return

	def featureImportance(self):
		fscore=self.clf3.get_booster().get_fscore()
		k=Counter(fscore) 
		top=k.most_common(20) 
		return top


	def predict(self, Pvar):
		result=self.eclf1.predict(Pvar)
		return result[0]


'''if  __name__=="__main__":

	M=model()
	conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EXCV;'
                      'Database=Churn;'
                      'Trusted_Connection=yes;')
	a='select * from dbo.Customer'
	data=pd.read_sql(a,conn)
	M.fit(data)
	print (M.featureImportance())'''




