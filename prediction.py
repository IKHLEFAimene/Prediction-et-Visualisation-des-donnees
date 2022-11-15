import numpy as np
import collections as cl
import os
import matplotlib.pyplot as plt
#import pmdarima as pm
#from pmdarima import auto_arima, ARIMA
import pandas as pd
from  sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")
#import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing
#lire les donnés sur python la ligne ci-dessous#
data = pd.read_csv('C:\\Users\\SCD UM\\Desktop\\AD\\consommation-annuelle-residentielle-par-adresse.csv',sep = ';',index_col='Année',parse_dates=True)
C=data["Consommation annuelle totale de l'adresse (MWh)"]
#A=data['Année']
#nbl=data.shape[0]

#data["Consommation annuelle totale de l'adresse (MWh)"].describe()
#data["Consommation annuelle moyenne par logement de l'adresse (MWh)"].plot(figsize=(10,5))

plt.figure(figsize=(12,5))
plt.plot(data["Consommation annuelle moyenne par logement de l'adresse (MWh)"])

plt.plot(data.index,data["Consommation annuelle totale de l'adresse (MWh)"])
#plt.show()


#data=data[['PNuméro de voie','Code INSEE de la commune','Nombre de logements',"Consommation annuelle totale de l'adresse (MWh)","Consommation annuelle moyenne par logement de l'adresse (MWh)",'Tri des adresses']].astype(float)

data=data[["Consommation annuelle totale de l'adresse (MWh)","Consommation annuelle moyenne par logement de l'adresse (MWh)",'Nombre de logements','Code INSEE de la commune','Tri des adresses']]
y=data["Consommation annuelle totale de l'adresse (MWh)"]
X=data.drop("Consommation annuelle totale de l'adresse (MWh)",axis=1)
model=LinearRegression()
model.fit(X,y)
#print(model.score(X,y))
data['Year']=data.index.year
#data["Consommation annuelle totale de l'adresse (MWh)"].plot(linewidth=5,figsize=(12,5))
#plt.show()
nbl=1603548
train=data[:]
#print(len(train))
test=data.iloc[-96:]
#print(test)

#plt.show()
#seasonal_decompose(data, model='additive', freq=2)

#fg=auto_arima(data["Consommation annuelle totale de l'adresse (MWh)"],trace=True,suppress_warnings=True)

#fg.summary()


#p=adfuller(train["Consommation annuelle totale de l'adresse (MWh)"],maxlag=None,regression='c',autolag='AIC',store=False, regresults=False)

#model=ARIMA(train["Consommation annuelle totale de l'adresse (MWh)"],select =(1,0,96))
#model=model.fit()
#model.summary()
#start=len(train)
#end=start+96
#pred=model.predict(start=start,end=end,type='levels')
#print(pred)
print(data)