import pandas as pd
import numpy as np
file_name= "Lab_Exam_1_Raw_Data.xlsx"
df=pd.read_excel(file_name, sheet_name="Raw_Data")
print("First five rows:")
print(df.head())
#display dimension
print("\nDimensions:", df.shape)
# Data cleaning 
df=df.drop_duplicates(subset="Student_ID", keep="first")
#Remove extra spaces from columns 
text_cols=["Name", "Department"]
for col in text_cols: 
    df[col]=df[col].astype(str).str.strip()
#Standardized departmnt to tilte case
df["Department"]=df["Department"].str.title()
#replace absent in assignment with 0
df["Assignment"]=df["Assignment"].replace("Absent", 0)
#convert columns to numeric 
for col in ["Quiz", "Assignment", "Attendance"]:
    df[col]=pd.to_numeric(df[col], errors="coerce")
#treat invalid ranges as missing
df.loc[(df["Quiz"]<0) | (df["Quiz"]>20), "Quiz"]=np.nan
df.loc[(df["Assignment"]<0) | (df["Assignment"]>20), "Assignment"]=np.nan
df.loc[(df["Attendance"]<0) | (df["Attendance"]>100), "Attendance"]=np.nan
#fill missing values 
df["Quiz"]=df["Quiz"].fillna(df["Quiz"].median())
df["Assignment"]=df["Assignment"].fillna(df["Assignment"].median())
df["Attendance"]=df["Attendance"].fillna(df["Attendance"].mean())
#Create new columns using numpy 
#total score
df["Total_Score"]=df["Quiz"]+df["Assignment"]
#percentage
df["Percentage"]=np.round((df["Total_Score"] /40) *100,2)
#Result using np.where
df["Result"]=np.where(
    (df["Percentage"] >=50) & (df["Attendance"]>=75),
    "Pass",
    "Fail"
)
#sort and reset index
df=df.sort_values(by="Percentage", ascending=False).reset_index(drop=True)
print("\nCleaned Data:")
print(df.head())
# export cleaned data
output_file= "Cleaned_Student_Data.xlsx"
df.to_excel(output_file, sheet_name="Cleaned_Data", index=False)
print(f"\nCleaned file saved as: {output_file}")
df.to_excel("Cleaned_Student_Data.xlsx", sheet_name="Cleaned Data", index=False)

print("File exported successfully!")