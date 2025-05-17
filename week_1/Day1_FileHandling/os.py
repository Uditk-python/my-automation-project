#script to list all the files in a folder and also checking if folder exist 
import os
file_path=input("enter the file path")
if os.path.exists(file_path):
    print(os.listdir(file_path))
else:
    print("file does not exist")
