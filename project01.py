# -*- coding: utf-8 -*-
#Pregnant women1 with COVID-19, United States, January 22, 2020 - October 25, 2021
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

#import csv file
df  = pd.read_csv("cases_of_covid19_among_pregnant_women_by_week_of_diagnosis_download.csv")
df1 = pd.read_csv("pregnancy_data_download.csv")
df2 = pd.read_csv("Covid-Vaccine-among-prengnant.csv")
#graph1 ********
dateDiag = df.iloc[2:92,0]
numCase  = df.iloc[2:92,1]

fig,axes = plt.subplots(1,1)

plt.bar(dateDiag, numCase)
plt.xticks(rotation=45)
axes.xaxis.set_major_locator(MaxNLocator(23)) 
plt.xlabel('week of Diagnosis')
plt.ylabel('Number of cases')
plt.title('Cases of COVID-19 among Pregnant Women by Week of Diagnosis*')
plt.savefig('by Week of Diagnosis.png', dpi=300, bbox_inches='tight')
plt.show()
#*****************************************
age        = df1.iloc[5:14,0]
numAgeCase = df1.iloc[5:14,1]

plt.bar(age, numAgeCase)
plt.xticks(rotation=45)
plt.xlabel('Age Group')
plt.ylabel('Number of Cases')
plt.title('Pregnant women with COVID-19 by age, United States')
plt.savefig('Pregnant women by age.png', dpi=300, bbox_inches='tight')
plt.show()
#***************************************
Race    = df1.iloc[16:21,0]
numRace = df1.iloc[16:21,1]

plt.bar(Race, numRace)
plt.xticks(rotation=45)
plt.xlabel('Race / Ethnicity')
plt.ylabel('Number of Cases')
plt.title('Pregnant women with COVID-19 by race/ethnicity, United States')
plt.savefig('By raceEthnicity', dpi=300, bbox_inches='tight')
plt.show()
#**************************************
Hospital = df1.iloc[30:33,0]
numHos   = df1.iloc[30:33,1]

plt.bar(Hospital, numHos)
plt.xlabel('Hospitalization Status')
plt.ylabel('Number of Cases')
plt.title('Pregnant women with COVID-19 by Hospitalization Status, United States')
plt.savefig('Hospitalization Status.png', dpi=300, bbox_inches='tight')
plt.show()
#***************************Vaccine in prengnancy 14 Dec 2020 - 30 Oct 2021
prior = [[0]]*34
priorAndDuring = [[0]]*34
During = [[0]]*34
dateVaccine = [[0]]*34
CDCVaccineData1 = df2.iloc[0:102]
n = 0
a = 0
b = 0
for i in range(0,102,3):
    prior[n]       = (CDCVaccineData1.iloc[i,4])
    dateVaccine[n] = CDCVaccineData1.iloc[i,0]
    n = n+1
for i in range(1,102,3):
    priorAndDuring[a] = CDCVaccineData1.iloc[i,4]
    a = a+1
for i in range(2,102,3):
    During[b] = CDCVaccineData1.iloc[i,4]
    b = b+1
    
prior1 = np.array(prior)
priorAndDuring1 = np.array(priorAndDuring)
During1 = np.array(During)

plt.bar(dateVaccine, prior1)
plt.bar(dateVaccine, priorAndDuring1, bottom = prior1)
plt.bar(dateVaccine, During1, bottom = prior1 + priorAndDuring1)
plt.xticks(rotation=45, fontsize = 7)
plt.xlabel('Date')
plt.ylabel('Vaccination Coverage(%)')
plt.title('Percent of Pregnant People Aged 18-49 Years \n Fully Vaccinated Covid-19,United States')
plt.legend(['Prior to Pregnancy','Prior to and During Pregnancy','During Pregnancy'])
plt.savefig('FullyVaccinatedCovid-19.png', dpi=300, bbox_inches='tight')
plt.show()
#************************************





