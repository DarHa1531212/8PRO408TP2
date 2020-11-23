import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import pickle

class FloatingWindow:

    def fenetreFlottante(tailleFenetre, saut, df):
        tempDf = pd.DataFrame(columns=['Date', 'Value'])
        outputDf = pd.DataFrame(
            columns=['Date', 'MovingAverage', 'Variance', 'StandardDeviation', 'Kurtosis', 'Skewness', 'Slope',
                     'StdError', 'ZScore'])

        for j in range(0, int(len(df.index)), saut):
            for i in range(j, j + tailleFenetre):
                if (i + 1 < int(len(df.index))):
                    tempRow = {'Date': df['Date'].iloc[i], 'Value': df['PercentOfBaseline'].iloc[i]}
                    tempDf = tempDf.append(tempRow, ignore_index=True)

            slope, intercept, r_value, p_value, std_err = stats.linregress(tempDf.index, tempDf['Value'])

            if outputDf['MovingAverage'].std() != 0:
                zscore = (tempDf['Value'].mean() - outputDf['MovingAverage'].mean()) / outputDf['MovingAverage'].std()
            else:
                zscore = None
            newRow = {'Date': df['Date'].iloc[j], 'MovingAverage': tempDf['Value'].mean(),
                      'Variance': tempDf['Value'].var(), 'StandardDeviation': tempDf['Value'].std(),
                      'Kurtosis': tempDf['Value'].kurtosis(), 'Skewness': tempDf['Value'].skew(), 'Slope': slope,
                      'StdError': tempDf['Value'].sem(), 'ZScore': zscore}
            outputDf = outputDf.append(newRow, ignore_index=True)
            tempDf = tempDf.drop(tempDf.index, inplace=True)
            tempDf = pd.DataFrame(columns=['Date', 'Value'])

        outputDf = outputDf.set_index('Date')
        return (outputDf)
