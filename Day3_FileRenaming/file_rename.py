# Renaming a file and folder 
import os
old_path=input("enter the old path of the file")
new_name=input("Enter the new name without extension")
l=os.path.splitext(old_path)
os.rename(old_path,os.path.join(os.path.dirname(old_path),new_name+l[1]))