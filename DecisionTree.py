#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:07:31 2017

@author: alterith
"""

# =============================================================================
# imports
# =============================================================================
import pandas as pd
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data:pd.DataFrame = pd.read_csv('Final data/TransformedData_V9_Binary(Passed).csv', sep = ',')
dataTemplate:pd.DataFrame = pd.read_csv('Final data/TransformedData_V9_template.csv', sep = ',')
dataTest:pd.DataFrame = pd.read_csv('Final data/TestingData_V1.csv', sep = ',')

#drop unneeded columns
dataTemplate.drop('Student_Number', axis = 1, inplace = True)
dataTest.drop('Student_Number', axis = 1, inplace = True)


# =============================================================================
# remove repeated Students
# =============================================================================
data.sort_values(by=['Matric_Attempts'], inplace = True)
data.drop_duplicates(subset=['Student_Number'], keep = 'last', inplace = True)

# =============================================================================
# remove unneeded column
# =============================================================================
feature_cols = data.columns.values.tolist()
feature_cols.remove('Student_Number')

# =============================================================================
# convert labels to classifications
# =============================================================================

def change(x):
    if (x>49):
        return 1
    else:
        return 0
data['Average'] = data['Average'].map(lambda x:change(x))

# =============================================================================
# split data
# =============================================================================

x = data[feature_cols[0:len(feature_cols)-1]]
y = data[feature_cols[len(feature_cols)-1]]
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state = 1)


# =============================================================================
# initialize tree using gini
# =============================================================================
clf = tree.DecisionTreeClassifier(criterion = "gini", random_state =10, max_depth = 10, min_samples_leaf = 100)


# =============================================================================
# fit data
# =============================================================================
clf = clf.fit(x_train, y_train)

# =============================================================================
# predict values
# =============================================================================
y_pred = clf.predict(x_test)


# =============================================================================
# calculate score
# =============================================================================
score = accuracy_score(y_test, y_pred)*100
# =============================================================================
# graph tree
# =============================================================================
export_graphviz(clf, out_file = 'graph.dot', feature_names = x.columns)

