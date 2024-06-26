# -*- coding: utf-8 -*-
"""ML-project 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sFFRClZykNJCbBySArtj2hiSoYHx9ffZ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("/content/fashion_products.csv")
test_data=pd.read_csv("/content/fashion_products.csv")

cat_col=[]
for col in data.columns:
    if(data[col].dtypes=='object'):
        cat_col.append(col)

num_col=[]
for col in data.columns:
    if(data[col].dtypes!='object'):
        num_col.append(col)

data.set_index('Product ID',inplace=True)

data.drop(columns=['User ID'],inplace=True)

#Removing columns that are not required further in num_col
num_col.remove('Product ID')
num_col.remove('User ID')

#Encoding Categorical Columns
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
cat_class=[]
for col in cat_col:
    data[col]=encoder.fit_transform(data[col])
    cat_class.append(encoder.classes_)

#Standardization of numerical columns
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
for col in num_col:
    data[col]=scaler.fit_transform(np.array(data[col]).reshape(len(data[col]),1))

data.head()

data.info()

#Model Creation for recommedation system
from sklearn.metrics.pairwise import cosine_similarity
similar=cosine_similarity(data)

def recommend(product_id):
    index=product_id-1
    item=sorted(list(enumerate(similar[index])),key=lambda x:x[1],reverse=True)[1:6]
    id=[]
    for i in item:
        id.append(i[0])
    return test_data.iloc[id]

#Input
#product_id=int(input("Enter Product ID"))
product_id=11
result=recommend(product_id)

#Input Data
test_data.iloc[product_id-1]

#Output
result







