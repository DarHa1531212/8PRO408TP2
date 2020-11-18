import math

import pandas as pd
from timeline import Timelines

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

df= pd.read_csv('covid_impact_on_airport_traffic.csv')


Timelines.DisplayChile(df, 14)
print('end')