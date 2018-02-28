# -*- coding: utf-8 -*-
"""
Exercise 5, Problem 1

Exploring NOAA data

This script prints mean Farenheit temperature, SD of maximum, and number of unique stations


db harris 2.28.18 
"""

###import pandas
import pandas as pd

###import NOAA data and declare NAN values
dF = pd.read_csv('NOAAdat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

###print rows, column names, and datatypes
print(dF.columns)
print(dF.index)
print(dF.dtypes)

###print mean teamp in Fahrenheit
print('The mean F temp is', dF['TEMP'].mean())

###print SD of maximum temp
print('The std dev of maximum temp is', dF['MAX'].std())

###print unique number of unique stations
print('There are', dF['USAF'].nunique(), 'unique stations.')