
import numpy as np
import collections as cl
import os
import matplotlib.pyplot as plt
import math
#import pmdarima as pm
from pmdarima import auto_arima, ARIMA
import pandas as pd
from  sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")
#import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
#from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api  as sm 
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv('C:\\Users\\SCD UM\\Desktop\\AD\\eco2mix-national-tr.csv',sep = ';')
df=df.dropna()
#df['Date - Heure']=pd.to_datetime(df['Date - Heure'])
#print(df['Date - Heure'])
df['Date']=pd.to_datetime(df['Date'])
df=df[['Consommation (MW)','Date']]
df.plot(x='Date',y='Consommation (MW)',figsize=(12,6))
plt.show()
df.set_index('Date', inplace=True) #indexing la variable date#
df.resample('M').plot(x='Date',y='Consommation (MW)',figsize=(12,6)) #Couleur par mois#
df.resample('D').mean().plot()
df.resample('M').mean().plot()
plt.show()

analysis=df[['Consommation (MW)']]
df['moyenne_mobile_Consommation']=df['Consommation (MW)'].rolling(window=5).mean()
df.resample('D').mean().plot() #compare la courbe de la ^moyenne mobile et celle du dat#
df.resample('D').mean().plot()
plt.show()


taille=df.shape[0]
A=np.zeros(l)
for i in range(0,5):
    A[i]=2
for i in range(5,l):
    A[i]=df['moyenne_mobile_Consommation'][i] /df['Consommation (MW)'][i]
print(min(A)) #minimum de ce rapport égale à 0.72 Donc la méthode des moyennes mobiles est une bonne prévision pour ce modéle #

taille=df.shape[0]
m=np.zeros(2*taille)
moy_mob=np.zeros(2*taille)
for i in range (0,taille):
    m[i]=df['Consommation (MW)'][i]
    moy_mob[i]=df['moyenne_mobile_Consommation'][i]


def Prevision(k):
    taille=8855
    l=taille-k
    for i in range (0,l):
        z=m[taille+i]
        m[taille+i]=moy_mob[taille+i-1]
        moy_mob[taille+i-1]=z
    return (moy_mob[taille+l-1])
p=Prevision(taille+3000)
print(p) 
        
P=np.zeros(96)
for i in range (0,96):
    P[i]=Prevision(taille+480+i)
   
fic=open("fichier1.csv","w")
fic.write("Heure,Prediction\n")
for i in range(1,96):
    
    fic.write(str(i)+","+str(P[i])+"\n")
    print("\n")
fic.close
df1 = pd.read_csv('C:\\Users\\SCD UM\\Desktop\\fichier1.csv',sep = ',')
df1.set_index('Heure', inplace=True) 
print(df1)


plot_acf(analysis,lags=20)
plot_pacf(analysis , lags=40)
plt.show()


