import pandas as pd
data = input("Enter the data")
df = pd.DataFrame(data)
print(df)
df.to_excel(r"C:\Python Automation\Day4_CSV_Excel\hello.xlsx", index=False)  # Saves DataFrame as Excel file