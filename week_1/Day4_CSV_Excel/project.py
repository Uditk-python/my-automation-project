import csv 
import os
import pandas as pd
pah=input("enter the path of csv file whose excel to be made:")
hell=input("enter the path of excel file :")
if os.path.exists(pah):
    udit=pd.read_csv(pah)
    udit.to_excel(hell,index=False)
choice=int(input("enter 1 if want to add in content:"))
if choice == 1:
    content=int(input("Enter the content to be added "))
print(udit)