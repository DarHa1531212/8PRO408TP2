import math

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

from timeline import Timelines

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('covid_impact_on_airport_traffic.csv')


# Timelines.DisplayChile(df, 14)


def fenetreFlottante(tailleFenetre, saut, df):
    tempDf = pd.DataFrame(columns=['Date', 'Value'])
    outputDf = pd.DataFrame(columns=['Date', 'MovingAverage', 'Variance', 'StandardDeviation', 'Kurtosis', 'Skewness', 'Slope', 'StdError'])

    for j in range(0, int(len(df.index)), saut):
        for i in range(j, j + tailleFenetre):
            if (i + 1 < int(len(df.index))):
                tempRow = {'Date': df['Date'].iloc[i], 'Value': df['PercentOfBaseline'].iloc[i]}
                tempDf = tempDf.append(tempRow, ignore_index=True)

        slope, intercept, r_value, p_value, std_err = stats.linregress(tempDf.index, tempDf['Value'])
        newRow = {'Date': df['Date'].iloc[j], 'MovingAverage': tempDf['Value'].mean(),
                  'Variance': tempDf['Value'].var(), 'StandardDeviation': tempDf['Value'].std(),
                  'Kurtosis': tempDf['Value'].kurtosis(), 'Skewness': tempDf['Value'].skew(), 'Slope':slope, 'StdError':tempDf['Value'].sem()}
        outputDf = outputDf.append(newRow, ignore_index=True)
        tempDf = tempDf.drop(tempDf.index, inplace=True)
        tempDf = pd.DataFrame(columns=['Date', 'Value'])

    outputDf = outputDf.set_index('Date')
    print(outputDf)
    return (outputDf)


# df_test['Btime'].iloc[0]

df = df[df['Country'] == 'Chile']
df = df.sort_values(by='Date')
df.index = pd.DatetimeIndex(df['Date'])
# df = df.set_index('Date')
df = df.reindex(pd.date_range('2020-03-16', '2020-10-16'), fill_value=None)
df = df.fillna(method='bfill')
df = df.reset_index()
# print( df)
newDf = fenetreFlottante(7, 4, df)



'''df = pd.DataFrame(list, columns=['date', 'value'])
df.date =pd.to_datetime(df.date)
df['date_ordinal'] = pd.to_datetime(df['date']).map(dt.datetime.toordinal)
slope, intercept, r_value, p_value, std_err = stats.linregress(df['date_ordinal'], df['value'])
##'''