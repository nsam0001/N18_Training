# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 19:45:45 2018

@author: neil
"""


# imports

import pandas as pd

# read data

dir_work = 'D:\\Development\\N18_Training\\N18_Training\\Python 1\\'

df_employees = pd.read_csv(dir_work + 'employees.csv')
df_sales = pd.read_csv(dir_work + 'garage_sales.csv')

# add column - sales amount

df_sales['Sales_Amount'] = df_sales.apply (lambda row: row['Quantity'] * row['Price'],axis=1)

# remove column

