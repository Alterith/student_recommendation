#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:09:08 2017

@author: alterith
"""

import pandas as pd


data:pd.DataFrame = pd.read_csv('Vac Work InformationHumanitiesMatric.csv')
# =============================================================================
# clean data and standardise
# =============================================================================
data = data.rename(columns=lambda x: x.replace(' ', '_'))
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Afrikaans First.*$", "Afrikaans First Additional Language")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Adv.*Math.*$", "AP Maths")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Afrikaans Second.*$", "Afrikaans Second Additional Language")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Advanced Programme Afrikaans.*$", "AP Afrikaans")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Advanced Programme English.*$", "AP English")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"Lang.*$", "Language")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"Add.*$", "Additional Language")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"Tech.*$", "Technology")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"Exam.*$", "Examination")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"Prac.*$", "Practical")
data.drop_duplicates(subset=['Test_Segment_Name', 'Student_Number', 'Calendar_Instance_Year'], keep = 'first', inplace = True)
data['Student_Number'] = data['Student_Number'].map(lambda x: str(x))

# =============================================================================
# =============================================================================
# # Delete unrelated courses and merge groupings
# =============================================================================
# =============================================================================
data = data[data['Test_Segment_Name'] != 'Life Orientation']
data = data[data['Test_Segment_Name'] != 'AP English']
data = data[data['Test_Segment_Name'] != 'AP Afrikaans']
data = data[data['Test_Segment_Name'] != 'Mathematics Paper 3']
data = data[data['Test_Segment_Name'] != 'Mathematical Literacy']

data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*English.*$", "English")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Afrikaans.*$", "Afrikaans")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*IsiZulu.*$", "IsiZulu")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Sepedi.*$", "Sepedi")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Setswana.*$", "Setswana")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Sesotho.*$", "Sesotho")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*IsiXhosa.*$", "IsiXhosa")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*French.*$", "French")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Xitsonga.*$", "Xitsonga")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Hebrew.*$", "Hebrew")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*SiSwati.*$", "SiSwati")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Tshivenda.*$", "Tshivenda")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*German.*$", "German")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Greek.*$", "Greek")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Arabic.*$", "Arabic")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*IsiNdebele.*$", "IsiNdebele")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Portuguese.*$", "Portuguese")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Italian.*$", "Italian")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Latin.*$", "Latin")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Spanish.*$", "Spanish")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Chinese.*$", "Chinese")
data['Test_Segment_Name'] = data['Test_Segment_Name'].str.replace(r"^.*Gujarati.*$", "Gujarati")
# =============================================================================
# Gather info for understanding
# =============================================================================
matric_subjects = data.groupby('Test_Segment_Name').size().to_frame()
data.sort_values(by = ['Student_Number','Test_Segment_Name', 'Calendar_Instance_Year'], inplace = True)

dataTest = data[data['Calendar_Instance_Year'] == 2017]

# =============================================================================
# import the second set of data
# =============================================================================
data2:pd.DataFrame = pd.read_csv('Vac Work InformationHumanities.csv')
# =============================================================================
# standardise the header names
# =============================================================================
data2 = data2.rename(columns=lambda x: x.replace(' ', '_'))
# =============================================================================
# # =============================================================================
# # delete education and laws for bageneral formatting
# # =============================================================================
# data2 = data2[~data2.Unit_Code.str.contains(r'^.*EDUC.*$')]
# data2 = data2[~data2.Unit_Code.str.contains(r'^.*LAWS.*$')]
# =============================================================================
# =============================================================================
# join the 2 tables
# =============================================================================
d = pd.merge(data, data2, on='Student_Number', how='inner')
# =============================================================================
# import data3
# =============================================================================
data3:pd.DataFrame = pd.read_csv('Vac Work InformationHumanitiesTerm.csv')
# =============================================================================
# standardise the header names
# =============================================================================
data3 = data3.rename(columns=lambda x: x.replace(' ', '_'))
# =============================================================================
# use on bachelor of arts
# =============================================================================
data3 = data3[data3['Program_Title'] == 'Bachelor Of Arts']
# =============================================================================
# join the 2 tables
# =============================================================================
finalDataFrame = pd.merge(d, data3, on='Student_Number', how='inner')
# =============================================================================
# drop unneeded columns
# =============================================================================
finalDataFrame.drop(['Faculty_Name_x', 'School_Name', 'Year_Of_Study_x', 'Calendar_Instance_Year_x', 'Admission_Test_Type', 'Registration_Status_x', 'New_To_University_x', 'Calendar_Instance_Year_y', 'Registration_Status_y', 'Progress_Outcome_Type_Description', 'Progress_Outcome_Type', 'Year_Of_Study_y', 'Program_Code', 'Program_Title', 'Calendar_Instance_Year', 'Faculty_Name_y', 'New_To_University_y', 'Unit_Attempt_Status', 'Achieved_Credit_Points_SUM', 'Unit_Level', 'Faculty_Name'], axis = 1, inplace = True)
unit_codes = finalDataFrame.groupby('Unit_Code').size().to_frame()

# =============================================================================
# =============================================================================
# =============================================================================
# # # data exclusion
# =============================================================================
# =============================================================================
# =============================================================================
varsity_quantile = unit_codes[0].quantile(0.85)
matric_quantile = matric_subjects[0].quantile(0.70)

unit_codes.columns = ['Intake']
unit_codes['Unit_Code'] = unit_codes.index

matric_subjects.columns = ['Taken']
matric_subjects['Test_Segment_Name'] = matric_subjects.index

# =============================================================================
# merge dataframes to exclude unwanted data
# =============================================================================


finalDataFrame2 = pd.merge(finalDataFrame, matric_subjects, on='Test_Segment_Name', how='inner')
finalDataFrame2 = finalDataFrame2[finalDataFrame2.Taken >= matric_quantile]

finalDataFrame3 = pd.merge(finalDataFrame2, unit_codes, on='Unit_Code', how='inner')
finalDataFrame3 = finalDataFrame3[finalDataFrame3.Intake >= varsity_quantile]

FinalMatricSubjects = finalDataFrame3.Test_Segment_Name.unique().tolist()

dataTest = dataTest[dataTest['Test_Segment_Name'].isin(FinalMatricSubjects)]

# =============================================================================
# get course points
# =============================================================================
FinalVarsitySubjects = pd.DataFrame(finalDataFrame3.Unit_Code.unique())
FinalVarsitySubjects.columns = ['Unit_Code']

CoursePoints = pd.merge(FinalVarsitySubjects,finalDataFrame3[['Unit_Code','Enroled_Credit_Points_SUM']],on='Unit_Code', how='left')
CoursePoints.drop_duplicates('Unit_Code', keep = 'first', inplace = True)
CoursePoints.columns = ['Unit_Code', 'Points']

finalDataFrame3.drop(['Taken', 'Intake', 'Enroled_Credit_Points_SUM'], axis = 1, inplace = True)

finalDataFrame3.to_csv('HumanitiesData.csv', sep=',')
CoursePoints.to_csv('CoursePoints.csv', sep=',')

dataTest.to_csv('TestData.csv', sep=',')


studentTotal = finalDataFrame3.Student_Number.unique().tolist()
