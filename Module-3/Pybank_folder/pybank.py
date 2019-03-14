#Selecting the csv file to use Python on. I do not know how to make this Git and what not.  
import pandas as pd
import os
import csv
df = pd.read_csv("02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
#Print the total number of months included in the dataset by pringing rows
numline = len(df)
print ("Total Months:"+ ' ' +str(numline))
#To get net profit sum second column 
Total = df['Profit/Losses'].sum()
print ("Total:"+ ''+ str(Total))
#Shifted values to get average change
df['shifted_column'] = df['Profit/Losses'].shift(1)
#difference between profit/losses and last line of new column 
df['difference'] = df['Profit/Losses'] - df['shifted_column']
#mean, gratest value, least value 
average = df['difference'].mean()
maximum = df['difference'].max()
minimum = df['difference'].min()
print("Average:"+ ''+ str(average))
print("Greatest Increase in Profits:"+ ''+ str(maximum))
print("Greatest Decrease in Profits:"+ str(minimum))
