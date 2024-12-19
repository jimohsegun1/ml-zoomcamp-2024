import pandas as pd
import numpy as np
import seaborn as sns

from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

import pickle

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

data = './Data/heart.csv'
df = pd.read_csv(data)

df_copy = df.copy()
df_copy = df_copy.sample(frac=1)

df_full_train, df_test = train_test_split(df_copy, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

y_full_train = (df_full_train.output).values
y_train = (df_train.output).values
y_val = (df_val.output).values
y_test = (df_test.output).values

del df_full_train['output']
del df_train['output']
del df_val['output']
del df_test['output']

categorical = ['sex', 'cp', 'restecg', 'exng', 'slp', 'thall']
numerical = ['age', 'trtbps', 'thalachh', 'oldpeak', 'caa']

dv = DictVectorizer(sparse=True)

full_train_dict = df_full_train[categorical + numerical].to_dict(orient='records')
X_full_train = dv.fit_transform(full_train_dict)

final_model = LogisticRegression(solver='liblinear', random_state=1)
final_model.fit(X_full_train, y_full_train)

test_dict = df_test[categorical + numerical].to_dict(orient='records')
X_test = dv.transform(test_dict)

y_pred = final_model.predict_proba(X_test)[:, 1]


# Performance of final_model:

score = y_pred >= 0.50
acc_final_model = round(accuracy_score(y_test, score), 5)
print("acc:  ",acc_final_model)
# Output: 0.85246

roc_final_model = round(roc_auc_score(y_test, y_pred), 5)
print("roc:  ",roc_final_model)
# Output: 0.89231

with open('Model/heart-model.bin', 'wb') as f_out:
    pickle.dump((dv, final_model), f_out)

