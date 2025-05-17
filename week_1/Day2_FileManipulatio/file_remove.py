# Remove a file or folder 
import os
import shutil
path=input("Enter the path of file to  be delleted")
if os.path.exists(path):
    if os.path.isfile(path):
        os.remove(path)
    else:
        if os.listdir(path):
            print("warning the folder is not empty want to delte whole")
            h=int(input("enter 1) for yes remove and 2) for dont remove"))
            if h==1:
                shutil.rmtree(path)
        else:
            os.rmdir(path)
else:
    print("error the path provided is wrong") 