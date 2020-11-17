import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#tout faire en moyenne mobile, les variations sont trop dures et rendent un graph avec plusieures lignes illisibles
#moyenne mobile des jours de la semaine et moyenne mobile des jours de fin de semaine
# prendre la moyenne de tous les aéroports d'un pays et utiliser cette valeur pour faire une moyenne nationnale
#faire un graphique de moyenne de pays / comparaison internationnale
#diagrame à barre par jour
#calculer le 'drop' de semaine vs fin de semaine
#changer les taux de chevauchements dans les moyennes mobiles
df= pd.read_csv('covid_impact_on_airport_traffic.csv')

df = df[df['Country'] == 'Canada']
print(df)
df['Date'] = pd.to_datetime(df['Date'])
df = df.pivot(index='Date', columns='AirportName', values='PercentOfBaseline')
print(df)
#x ='Date', y='PercentOfBaseline', kind = 'line'
df.plot()
plt.show()


print('end')