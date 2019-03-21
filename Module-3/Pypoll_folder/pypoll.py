import pandas as pd
import numpy as np
import os
import csv
df = pd.read_csv("02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")
numvotes=len(df)

print('Total Votes:' + ' ' + str(numvotes))
candi=df["Candidate"].value_counts()
Table=candi/((numvotes))
Percentage=(Table)
print(Percentage)