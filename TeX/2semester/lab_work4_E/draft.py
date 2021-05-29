import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('1.csv')
df2 = pd.read_csv('2.csv')
df3 = pd.read_csv('3.csv')
df4 = pd.read_csv('4.csv')

a1 = np.array([])
for i in range(len(df1['X']) - 1):
    a1 = np.append(a1, round(df1['X'][i+1]-df1['X'][i],2))
    
a2 = np.array([])
for i in range(len(df2['X']) - 1):
    a2 = np.append(a2, round(df2['X'][i+1]-df2['X'][i],2))

a3 = np.array([])
for i in range(len(df3['X']) - 1):
    a3 = np.append(a3, round(df3['X'][i+1]-df3['X'][i],2))

a4 = np.array([])
for i in range(len(df4['X']) - 1):
    a4 = np.append(a4, round(df4['X'][i+1]-df4['X'][i],2))
    
