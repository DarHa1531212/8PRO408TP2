import pandas as pd
import math
import matplotlib.pyplot as plt

class Timelines:


    def displayCanada(df):
        MobileAverage1 = pd.DataFrame()
        MobileAverage2 = pd.DataFrame()

        df = df[df['Country'] == 'Canada']
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.pivot(index='Date', columns='AirportName', values='PercentOfBaseline')
        df = df.apply(lambda x: x.fillna(x.mean()))



        for i in range (0, int(math.ceil(len(df.columns)/2))):
            MobileAverage1[df.columns[i]] = df.iloc[:,i].rolling(window=14).mean()
            MobileAverage2[df.columns[int(math.floor(len(df.columns)/2))+ i]] = df.iloc[:,int(math.floor(len(df.columns)/2))+ i].rolling(window=14).mean()

        #x='Date', y='PercentOfBaseline', kind='line'


        del MobileAverage2['Montreal Mirabel']

        fig, axes = plt.subplots(nrows=1, ncols=2, )


        ax1 = MobileAverage1.plot(ax= axes[0])
        ax1.set_ylim(30, 100)

        ax2 = MobileAverage2.plot(ax= axes[1])
        ax2.set_ylim(30, 100)


        plt.show()


    def DisplayChile(df, windowValue):
        MobileAverage1 = pd.DataFrame()

        df = df[df['Country'] == 'Chile']
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.pivot(index='Date', columns='AirportName', values='PercentOfBaseline')
        df = df.apply(lambda x: x.fillna(x.mean()))

        for i in range(0, len(df.columns)):
            MobileAverage1[df.columns[i]] = df.iloc[:, i].rolling(window=windowValue).mean()

        ax1 = MobileAverage1.plot()


        plt.show()


#Australia

    def DisplayAustralia (df, windowValue):
        MobileAverage1 = pd.DataFrame()

        df = df[df['Country'] == 'Australia']
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.pivot(index='Date', columns='AirportName', values='PercentOfBaseline')
        df = df.apply(lambda x: x.fillna(x.mean()))

        for i in range(0, len(df.columns)):
            MobileAverage1[df.columns[i]] = df.iloc[:, i].rolling(window=windowValue).mean()

        ax1 = MobileAverage1.plot()

        plt.show()

    def displayUSA(df, windowValue):
        MobileAverage1 = pd.DataFrame()
        MobileAverage2 = pd.DataFrame()

        df = df[df['Country'] == 'United States of America (the)']
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.pivot(index='Date', columns='AirportName', values='PercentOfBaseline')
        df = df.apply(lambda x: x.fillna(x.mean()))

        for i in range(0, int(math.ceil(len(df.columns) / 2))):
            MobileAverage1[df.columns[i]] = df.iloc[:, i].rolling(window=windowValue).mean()
            MobileAverage2[df.columns[int(math.floor(len(df.columns) / 2)) + i]] = df.iloc[:, int(
                math.floor(len(df.columns) / 2)) + i].rolling(window=14).mean()

        # x='Date', y='PercentOfBaseline', kind='line'

        del MobileAverage2['John F. Kennedy International']

        fig, axes = plt.subplots(nrows=1, ncols=2, )

        ax1 = MobileAverage1.plot(ax=axes[0])
        ax1.set_ylim(20, 100)

        ax2 = MobileAverage2.plot(ax=axes[1])
        ax2.set_ylim(20, 100)

        plt.show()
