# Cleaning Data
# ALT2
# by Daniel and Anthony
# 07-04-2025

import pandas as p
import numpy as np
#import matplotlib as m

df=p.read_csv('covid_worldwide.csv')

print(df)

df=df.drop_duplicates()

replacements={'©':'e','§':'c','Ã':''} # Reunion, Curacao

for symbol, replacement in replacements.items():
    df['Country']=df['Country'].str.replace(symbol,replacement)
    
df['Country']=df['Country'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
    
#df.to_csv('output2.csv',index=False)

streamlinedDF=df[['Total Cases','Total Deaths']]

print(streamlinedDF)

usefulDF=streamlinedDF.dropna()
print(usefulDF)

cList=df['Total Cases'].tolist()
caseList=[]
for i in cList:
    caseList.append(float(i))

dList=df['Total Deaths'].tolist()

def remove_non_alphanumeric(input_string):
    return ''.join(char for char in input_string if char.isalnum())

# Example usage
input_string = "Hello, World! 123"
cleaned_string = remove_non_alphanumeric(input_string)
print(cleaned_string)  # Output: HelloWorld123


goodCase = []
for i in caseList:
    goodCase.append(int(i))
print(goodCase)

RatioList=[]
for i in range(0,221):
    RatioList.append(caseList[i]/deathsList[i])

def findMean(l):
    total=0
    for e in l: # e for element
        total+=e # total the list
    mean=round((total/len(l)),2) # divide total by number of elements
    return mean


# Graphing
# 
# import numpy as n
# import matplotlib
# from matplotlib import pyplot as plot
# 
# plot.plot(usefulDF['Total Cases'],usefulDF['Total Deaths'],'ro')
# plot.show()

