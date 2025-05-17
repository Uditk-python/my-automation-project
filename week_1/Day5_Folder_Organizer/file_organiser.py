import os
import shutil
#save all type of extensions in a folder named all_files
l=[]
for dirpath,dirnames,filenames in os.walk(r"C:\first in coding"):
    for filename in filenames:
        _,ext=os.path.splitext(filename)
        if ext and ext not in l:
            l.append(ext)
# making folders for each extension inside the l 
for ext in l:
    os.makedirs(os.path.join(r"C:\first in coding",ext[1:]+"_files"),exist_ok=True)
#saving each file for a given extension in as respective folder
for dirpath,dirnames,filenames in os.walk(r"C:\first in coding"):
    for filename in filenames:
        _,ext=os.path.splitext(filename)
        shutil.move(os.path.join(dirpath,filename),os.path.join(r"C:\first in coding",ext[1:]+"_files",filename))
