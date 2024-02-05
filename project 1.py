# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:10:41 2024

@author: Pamela
"""
import pandas
file = pandas.read_csv("movie_dataset.csv")
print(file)

print(file.info())
print(file.describe())

import pandas
data = {'Genre':['Action','Adventure','Horror','Animation','Comedy','Biography','Drama','Crime','Mystery','Stupid']}
df = pandas.DataFrame(data)
print(df)

file = pandas.read_csv("movie_dataset.csv", skiprows=19)
print(file)
print(df['Revenue (Millions)'])
print(min('Revenue (Millions)'))

import pandas
df = pandas.read_csv("movie_dataset.csv")
df.loc[11, 'Metascore'] = '2014'
df.to_csv("movie_dataset.csv" , index=False)
print(df)

import pandas
df = pandas.read_csv("movie_dataset.csv")
df = df.loc[(df['Year']>=2015)&(df['Year']<2018)]
print(df)