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
import random


data:pd.DataFrame = pd.read_csv('Final data/Rules1.csv', sep = ',')
data:pd.DataFrame = pd.read_csv('Final data/Rules1.csv', sep = ',')
data2:pd.DataFrame = pd.read_csv('HumanitiesData.csv', sep = ',')
data3:pd.DataFrame = pd.read_csv('CoursePoints.csv', sep = ',')
matric_subjects = data2.Test_Segment_Name.unique().tolist()
varsity_courses = data2.Unit_Code.unique().tolist()
data = data[data['support']>=0.125]
# =============================================================================
# format data
# =============================================================================
data['antecedants'] = data['antecedants'].str.replace(r"^frozenset\(\{", "")
data['antecedants'] = data['antecedants'].str.replace(r"\}\)", "")
data['consequents'] = data['consequents'].str.replace(r"^frozenset\(\{", "")
data['consequents'] = data['consequents'].str.replace(r"\}\)", "")

data['antecedants'] = data['antecedants'].str.replace("'", "")
data['consequents'] = data['consequents'].str.replace("'", "")
# =============================================================================
# delete irrelevant data
# =============================================================================

data.drop('Unnamed: 0' ,axis = 1, inplace = True)
data = data[data['consequents'] == 'Average']
data = data[(data.antecedants.str.contains('|'.join(matric_subjects)))]
data = data[(data.antecedants.str.contains('|'.join(varsity_courses)))]

# =============================================================================
# make 2 lists and concat them as 2d list 
# =============================================================================
rules = pd.DataFrame(data['antecedants']).antecedants.apply(lambda x: x.split(', ')).tolist()

matric_rules = []
course_rules = []
for i in range(0, len(rules)):
    matric_rules.append([x for x in rules[i] if not any(x1.isdigit() for x1 in x)])
    course_rules.append([x for x in rules[i] if x not in matric_rules[i]])
# =============================================================================
# final list of valid rules
# =============================================================================
final_rules = list(zip(matric_rules, course_rules))

# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # # testing methodology
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
matric_test = random.sample(matric_subjects, 7)

reccommended_subjects = []
for i in range(0, len(final_rules)):
    if(set(final_rules[i][0]).issubset(set(matric_test))):
        reccommended_subjects = list(set(reccommended_subjects) | set(final_rules[i][1])) 

pathways:pd.DataFrame = pd.read_csv('Final data/BAGeneral.csv', sep=',')
pathways = pathways.fillna(0)
pathways = pathways.values.tolist()

j = 0
for i in range(0, len(pathways)):
    pathways[i] = [x for x in pathways[i] if not isinstance(x, int)]
    if(set(pathways[i]).issubset(reccommended_subjects)):
        j = j+1

    
    
    


