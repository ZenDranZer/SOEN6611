# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:21:52 2020

@author: venka
"""

import pandas as pd

""" Import the .cv file as a dataframe using pandas data"""
df = pd.read_csv('C:\\Users\\venka\\OneDrive\\Desktop\\Mutationscores\\Config-pit-reports\\202003290107\\mutations.csv', names = ['Class', 'Package', 'temp1', 'temp2','temp3','Coverage_val','temp4'])

"""These are the columns that are not req so we can ignore them"""
df.drop(['temp1', 'temp2', 'temp3', 'temp4'], axis = 1, inplace = True)

""" Here we try caluclate and group the classes together and sum all there mutation score 
    for the respective classes we sum the repetions of KILLED, NO_COVRAGE, SURVIVED, TIMED_OUT respectively
    by counting how many times they are repeated in the class
"""
df['Package'] = df['Package'].map(lambda x: str(x)[:x.rfind('.')])

df['Package'] = df['Package'].map(lambda x:  x if (x.find('$')+1 == 0) else  x[:x.find('$')+1])
""" Here we just add ".java" to class names"""
df['CLASS'] =  df['Class'].astype(str) + '.java'


df = df.groupby(['Class','Package','Coverage_val']).size().unstack(fill_value=0)

"""Total number off the mutants by summing KILLED + NO_COVRAGE + SURVIVED + TIMED_OUT """
df['Total_Mutant'] = df.sum(axis = 1)

df['Mutation_Score'] =  (df['KILLED'] / df['Total_Mutant'])*100

"""To print the mutation score for the respective val"""
print('Mutation Score  '+str((df.KILLED.sum()/df.Total_Mutant.sum())*100))
df.to_csv('C:\\Users\\venka\\OneDrive\\Desktop\\data.csv')
