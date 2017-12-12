#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:41:13 2017

@author: alterith
"""
# =============================================================================
# apriori algorithm rules
# =============================================================================

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

data:pd.DataFrame = pd.read_csv('Final data/TransformedData_V9_Binary(Enrolled).csv', sep = ',')
data2:pd.DataFrame = pd.read_csv('Final data/TransformedData_V9_Binary(Enrolled).csv', sep = ',')
# =============================================================================
# remove repeated Students
# =============================================================================
data.sort_values(by=['Matric_Attempts'], inplace = True)
data.drop_duplicates(subset=['Student_Number'], keep = 'last', inplace = True)

# =============================================================================
# remove unwanted columns
# =============================================================================
cols = list(data.columns.values) #Make a list of all of the columns in the df
cols.pop(cols.index('Student_Number')) #Remove b from list
#cols.pop(cols.index('Average')) #Remove x from list
cols.pop(cols.index('APS')) #Remove x from list
cols.pop(cols.index('Quintile')) #Remove x from list
cols.pop(cols.index('Matric_Attempts')) #Remove x from list
data = data[cols] #Create new dataframe with columns in the order you want
#data = data.loc[data.Average == 1]
data = data[data['Average'] >= 50]
data.Average = 1
# =============================================================================
#  use apriori algorithm
# =============================================================================

frequent_itemsets = apriori(data, min_support = 0.1, use_colnames = True)

# =============================================================================
#  define rules
# =============================================================================
rules = association_rules(frequent_itemsets, metric="lift", min_threshold = 0.5)
rules.sort_values('confidence', inplace = True)

# =============================================================================
# export rules as csv
# =============================================================================

rules.to_csv('Final data/Rules1.csv', sep=',')