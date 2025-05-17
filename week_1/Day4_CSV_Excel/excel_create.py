import pandas as pd
data = input("Enter the data")
df = pd.DataFrame(eval(data))
print(df)
df.to_excel(r"C:\Python Automation\week_1\Day4_CSV_Excel\hello.xlsx", index=False)  # Saves DataFrame as Excel file  