import math

import pandas as pd
import matplotlib.pyplot as plt

from timeline import Timelines

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('covid_impact_on_airport_traffic.csv')
print(df)

# Timelines.DisplayChile(df, 14)


def fenetreFlottante(tailleFenetre, saut, df):
    outputDf = pd.DataFrame(columns=['Date', 'MovingAverage'])
    valueSum = 0
    outOfBoundsValues = 0

    for j in range(0, int(len(df.index)), saut):
        for i in range(j, j + tailleFenetre):
            if (i +1 > int(len(df.index))):
                outOfBoundsValues += 1
            else:
                valueSum += df['PercentOfBaseline'].iloc[i]
                print('j: ' + str(j) + ',  I: ' + str(i) + ', df value: ' + str(df['PercentOfBaseline'].iloc[i]))

        print('valueSum: ' + str(valueSum))
        print('out of bounds: ' + str(outOfBoundsValues))
        print(valueSum / (tailleFenetre - outOfBoundsValues))
        newRow = { 'Date':df['Date'].iloc[j] , 'MovingAverage':valueSum / (tailleFenetre - outOfBoundsValues)  }
        outputDf = outputDf.append(newRow , ignore_index=True)
        valueSum = 0
        outOfBoundsValues = 0
    outputDf= outputDf.set_index('Date')

    return (outputDf)

# df_test['Btime'].iloc[0]

df = df[df['Country'] == 'Chile']
df = df.sort_values(by='Date')
df.index = pd.DatetimeIndex(df['Date'])
# df = df.set_index('Date')
df = df.reindex(pd.date_range('2020-03-16', '2020-10-16'), fill_value=None)
df = df.fillna(method='bfill')
df = df.reset_index()
#print( df)
newDf = fenetreFlottante(7, 4, df)

newDf.plot()
plt.show()
