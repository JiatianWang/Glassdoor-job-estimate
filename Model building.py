import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('EDA.csv')


# choose relevant columns

df.columns 
df_model = df[['ave_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','age','python_yn','spark','seniority','desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)
# train test split
from sklearn.model_selection import train_test_split

x = df_dum.drop('ave_salary',axis = 1)
y = df_dum['ave_salary'].values

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# multiple linear regression
# lasso regression
# random forest
# tune models GridsearchCV
# test ensembles