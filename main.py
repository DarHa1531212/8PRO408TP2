import math

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import pickle

from timeline import Timelines
from FloatingWindows import FloatingWindow

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('covid_impact_on_airport_traffic.csv')




#Filtering the wanted airport, ordering the data and filling the missing values
df = df[df['Country'] == 'Chile']
df = df.sort_values(by='Date')
df.index = pd.DatetimeIndex(df['Date'])
df = df.reindex(pd.date_range('2020-03-16', '2020-10-16'), fill_value=None)
df = df.fillna(method='bfill')
df = df.reset_index()



newDf = FloatingWindow.fenetreFlottante(7, 7, df)
newDf.to_pickle('precentageOfBaseline.pkl')

# Timelines.DisplayChile(df, 14)



