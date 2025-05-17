import os
import csv
# # Code to read a csv fille
# path=input("enter the path of csv file to read:")
# path=os.path.abspath(path)
# with open(path,"r") as rf:
#     csv_reader=csv.reader(rf)
#     k=0
#     for line in csv_reader:
#         print(line)


# Code to write in csv file
path=input("enter the path of csv file on which content to be written:")
path=os.path.abspath(path)
with open(path,"w",newline='') as wf:
    csv_writer=csv.writer(wf)
    headrow=input("Enter the headrow to written in file seperating them by commas:").split(",")
    csv_writer.writerow(headrow)
    k=int(input("enter the no.of row tp be added:"))
    for i in range(k):
        lis=[]
        for j in headrow:
            o=input("Enter the ",j,":")
            lis.append(o)
        csv_writer.writerow(lis)