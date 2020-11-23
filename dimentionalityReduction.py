import os
import pickle
from sklearn import impute
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import ExtraTreesClassifier


########################################################################################################################
#                                                    USER PARAMETERS                                                   #
########################################################################################################################

# Define the path name of your .pickle file (dataset)
path_name = "precentageOfBaseline.pkl"

# Define the number of attribute to select
attribute_number_to_select = 4

########################################################################################################################
#                                                   LOAD THE DATASET                                                   #
########################################################################################################################

# Load the dataset (you can modify the variables to be load. In this case, we have x an array of the features extracted
# for each instance and y a list of labels)
with open(path_name, 'rb') as file:
  df = pickle.load(file)
  df = df.dropna()
  y = df.drop(['Variance', 'StandardDeviation', 'Kurtosis', 'Skewness', 'Slope', 'StdError', 'ZScore'], axis=1)
  x = df.drop('MovingAverage', axis=1)
  y['Traffic'] = y['MovingAverage'].apply(lambda y : 'true' if y > 32 else 'false')
  y = y.drop(['MovingAverage'], axis=1)

  '''imp = impute.SimpleImputer(missing_values=0, strategy='median')
  array = x.values
  imp.fit(array)
  x = imp.transform(array)'''





########################################################################################################################
#                                    REDUCE THE DIMENSIONALITY BY SELECTING FEATURES                                   #
########################################################################################################################

# Define the classifier
classifier_model = ExtraTreesClassifier(n_estimators=50)

# Train the classifier model to classify correctly the instances into the correct classes  .ravel()
classifier_model = classifier_model.fit(x, np.array(y['Traffic']))

# Get the score of importances for each attribute
importance_scores = classifier_model.feature_importances_
print(importance_scores)


# Maintenant c'est a votre tour de coder le reste.
# Le reste doit extraire de x les N meilleurs attributs et afficher un rapport des attributs selectionnes par ordre
# croissant d'importances. Puis a la fin, vous sauvegarderez le nouveau dataset.
data = {'Property': ['Variance', 'StandardDeviation', 'Kurtosis', 'Skewness', 'Slope', 'StdError', 'ZScore'], 'Value': importance_scores}
df = pd.DataFrame(data )
df = df.set_index(['Property'])
df = df.nlargest(attribute_number_to_select,'Value')


df.plot(kind = 'bar')
plt.show()

print (df)

