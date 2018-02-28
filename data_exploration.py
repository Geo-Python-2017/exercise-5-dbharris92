# -*- coding: utf-8 -*-
"""
Exercise 5 Exploring NOAA data

Part 1 of this script prints mean Farenheit temperature, SD of maximum, and number of unique stations

Part 2 of this script converts selected F temps to C

Part 3 of this script divides datas into subsets and saves them to file
 
db harris 2.28.18 
"""

### import pandas
import pandas as pd

### import NOAA data and declare NAN values
dF = pd.read_csv('NOAAdat.csv', na_values=['*', '**', '***', '****', '*****', '******'])

### print rows, column names, and datatypes
print(dF.columns)
print(dF.index)
print(dF.dtypes)

### print mean teamp in Fahrenheit
print('The mean F temp is', dF['TEMP'].mean())

### print SD of maximum temp
print('The std dev of maximum temp is', dF['MAX'].std())

### print unique number of unique stations
print('There are', dF['USAF'].nunique(), 'unique stations.')

### Problem 2 ###

### select USAF, YR--MODAHRMN, TEMP, MAX, MIN columns
selected = dF[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

### selected is a view/copy of dF, remove with following
selected.is_copy = None

### alt option for above view/copy issue
### new_df = old_df[list_of_columns].copy()

### alt option 2 (prevents possible chained indexing)
### new_df = old_df.loc[:, list_of_column_names]

### remove NoData from column temp
selected.dropna(subset=['TEMP'])

### convert temps to C in new column Celsius
selected['Celsius'] = (selected['TEMP']- 32) / 1.8

### round Celsius values to zero decimals and convert to integer
selected['Celsius'] = selected['Celsius'].round(0)

### Problem 3 ###

### select all rows from selected DF where USAF code is 299980
kumpula = selected.ix[selected['USAF'] == 29980]

### select rows where USAF is 28450
rovaniemi = selected.ix[selected['USAF'] == 28450]

### save these dataframes to csv
output1 = 'Kumpula_temps_May_Aug_2017.csv'
output2 = 'Rovaniemi_temps_May_Aug_2017.csv'

kumpula.to_csv(output1, sep= ',', float_format='%.2f')
rovaniemi.to_csv(output2, sep = ',', float_format='%.2f')

### Problem 4 ###

