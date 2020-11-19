import math

import pandas as pd
from timeline import Timelines

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

df = pd.read_csv('covid_impact_on_airport_traffic.csv')


# Timelines.DisplayChile(df, 14)


def fenetreFlottante(tailleFenetre, saut, df):
    valueSum = 0
    outOfBoundsValues = 0

    for j in range(0, int(int(df.size)), saut):
        for i in range(j, j + tailleFenetre):
            if (i > int(df.size + 1)):
                outOfBoundsValues += 1
            else:
                valueSum += df['PercentOfBaseline'].iloc[i]
                print('j: ' + str(j) + ',  I: ' + str(i) + ', df value: ' + str(df['PercentOfBaseline'].iloc[i]))

        print('valueSum: ' + str(valueSum))
        print('out of bounds: ' + str(outOfBoundsValues))
        print(valueSum / (tailleFenetre - outOfBoundsValues))
        valueSum = 0
        outOfBoundsValues = 0


# df_test['Btime'].iloc[0]

df = df[df['Country'] == 'Chile']
df = df.sort_values(by='Date')
df.index = pd.DatetimeIndex(df['Date'])
# df = df.set_index('Date')
df = df.reindex(pd.date_range('2020-03-16', '2020-10-16'), fill_value=None)
df = df.fillna(method='bfill')
df = df.reset_index()
print(df)

fenetreFlottante(7, 4, df)
