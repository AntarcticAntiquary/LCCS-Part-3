# Cleaning Data
# ALT2
# by Daniel, Kacper & Anthony
# 07-04-2025

import pandas as p

df=p.read_csv('covid_worldwide.csv')

print(df)

df=df.drop_duplicates()

replacements={'©':'e','§':'c','Ã':'',',':''} # Reunion, Curacao

for symbol, replacement in replacements.items():
    df['Country']=df['Country'].str.replace(symbol,replacement)
    
df['Country']=df['Country'].str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)
df['Total Deaths']=df['Total Deaths'].str.replace(',', '', regex=True)
df['Total Cases']=df['Total Cases'].str.replace(',', '', regex=True)
df['Population']=df['Population'].str.replace(',', '', regex=True)
    
#df.to_csv('output2.csv',index=False)

streamlinedDF=df[['Serial Number','Country','Total Cases','Total Deaths','Population']]

usefulDF=streamlinedDF.dropna()
print(usefulDF)

Caselist = usefulDF['Total Cases']
Deathlist = usefulDF['Total Deaths']
Poplist = usefulDF['Population']
Countries = usefulDF['Country']

CountryList=[] # Create a list of the countries' names
for i in Countries:
    CountryList.append(i)
FloatCase = [] # Convert all the case numbers to floats
for i in Caselist:
    FloatCase.append(float(i))
FloatDeath = [] # Convert all the death numbers to floats
for i in Deathlist:
    FloatDeath.append(float(i))
FloatPop = [] # Convert all the population numbers to floats
for i in Poplist:
    FloatPop.append(float(i))
TotalCase = 0 # Find the total amount of cases
for i in FloatCase:
    TotalCase = TotalCase + i
TotalDeath = 0 # Find the total amount of deaths
for i in FloatDeath: 
    TotalDeath = TotalDeath + i
world = float(TotalCase//TotalDeath) # Calculate the rate for the whole world
Ratiolist = []
for i in range(0, 221): # Create a list of each country's ratio of cases to deaths
    Ratiolist.append(round(FloatCase[i]/FloatDeath[i], 2))
TotalRatios = 0
for num in Ratiolist:
    TotalRatios += num
Mean = round((TotalRatios/len(Ratiolist)), 2) # Calculate mean of the ratios
Ratiolist.sort()
Median = Ratiolist[len(Ratiolist)//2] # 222 is the length of the list
for country in CountryList:
    if country=='Ireland':
        i=CountryList.index(country)
        irish=round((FloatCase[i]/FloatDeath[i]),2)
print("The world's rate is:", world)  # Print mean and median
print("Our median is:", Median)
print("Our mean is:",Mean)
print("Ireland's ratio is:",irish)


# Graphing

import numpy as np
import matplotlib.pyplot as pyplot # Import necessary libraries
for y in range(0, 221):
    pyplot.scatter(FloatDeath[y], FloatCase[y], s=(FloatPop[y])/300000, alpha=0.5) # Plot all the points - Cases at y, Deaths at x
    pyplot.annotate(CountryList[y], (FloatDeath[y], FloatCase[y]), va='center', ha='center', fontsize=6) # Annotate with country names
pyplot.xlabel('Deaths')
pyplot.ylabel('Cases') # Label axes
pyplot.show() # Display graph