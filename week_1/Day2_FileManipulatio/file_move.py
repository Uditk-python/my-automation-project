#code to move a file
import os
import shutil
source_path=input("enter the source path of the file to be moved")
destinaion=input("enter the final path of the file to be moved")
if os.path.isdir(destinaion):
    if os.path.exists(source_path):
        shutil.move(source_path,destinaion)
    else:
        print("path is invalid")
else:
    print("Warning:the file to be moved will be overwritten")