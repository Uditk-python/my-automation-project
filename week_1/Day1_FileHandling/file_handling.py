#code to read a txt file name 'hello.txt'
# with open(r"C:\Python Automation\Day1_FileHandling\notes.txt",'r') as rf:
#     content=rf.readlines()
#     for lines in content:
#         print(lines,end='')
# code to write in a file 
with open (r"C:\Python Automation\Day4_CSV_Excel\W&RA_csv_file.py",'w') as wf:
    content=input("enter the content to be added in the file")
    wf.write(content)
# code to append in a file
# with open(r"C:\Python Automation\Day1_FileHandling\notes.txt",'a') as wf:
#     content=input("enter the content to be added in the file")
#     wf.write(content)
