# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:07:54 2020

@author: Dhiman
"""

"""
##############################################################################
                    Importing Necessary Libraries
##############################################################################
"""

import pandas as pd                     #to work with data frame
import os                               #to change working directory
import numpy as np                      #to work with data frame
import matplotlib.pyplot as plt         #for visualisation 
import seaborn as sns                   #for visualisation 
from sklearn.model_selection import train_test_split
#                                       #to divide the data into train and test samples
from sklearn.linear_model import LogisticRegression
#                                       #to create a distinct classification model as logistic regression model
"""
******************************************************************************
                           import the data
******************************************************************************
"""
os.chdir('E:\python\data set')          #specify the path of file
data=pd.read_excel('India-Car-Database.xls',sheet_name='Database',na_values=['N/A ','N/A'])
#                                       import the data removing N/A as NaN
data2=data.copy()
data2.info()

"""
*******************************************************************************
                              Data cleaning
*******************************************************************************
"""
data2.rename({'Unnamed: 0':'a'}, axis='columns', inplace=True)
data2.drop(columns='a', inplace=True)
#data2.dropna(subset=['Price production cars(Lakhs)'],inplace=True)


data2['Ground clearance (mm)'].value_counts()                                 #check the frequency in each column
data2['Kerb weight (kg)'].value_counts() 
data2['Bootspace (litres)'].value_counts()
data2['Ground clearance (mm)'].fillna(data2['Ground clearance (mm)'].mean(), inplace=True)
data2['Kerb weight (kg)'].fillna(data2['Kerb weight (kg)'].mean(), inplace=True)
data2['Bootspace (litres)'].fillna(data2['Bootspace (litres)'].mean(), inplace=True)


'''
1. We are developing the classification model so we need to creat a categorical column.
2. We can divide the price into three categories ie: low, midium, expencive
'''

#creating a new column for cetegorising the price if the car
data2.insert(36,'Price range','')

for j in range(0,len(data2['Price production cars(Lakhs)']),1):
    print(j)
    if(data2['Price production cars(Lakhs)'][j]<=3.5):
        data2['Price range'][j]=0
    elif(data2['Price production cars(Lakhs)'][j]>=7):
        data2['Price range'][j]=1
    else:
        data2['Price range'][j]=2
    


#to fill the number of rows we have to check the relation between number of seats and seating rows
#corr_data2=data2.corr()

plt.scatter(data2['Seating capacity'],data2['No of seating rows'],c='red')
plt.xlabel('seating capacity')
plt.ylabel('no. of seating rows')
plt.show()

for i in range(0,len(data2['Seating capacity']),1):
    if (data2['Seating capacity'][i]<=5):
        data2['No of seating rows'][i]=2
    else:
        data2['No of seating rows'][i]=3
    i=i+1




data2.dropna(axis=0,inplace= True)

#finding the total number of missing values
#dealing with missing data
missing=data2.isnull().sum()#one way saving athe data in data frame
print(data2.isnull().sum())#second way directly printing the data