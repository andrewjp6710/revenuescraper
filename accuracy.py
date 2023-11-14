import pandas as pd
import os


fileName = input("ACCURACY CHECK: Please input name of Excel File (including '.xlsx'). Please ensure the code and the excel file are located in the same directory/folder: ")

base_dir = os.getcwd()
excelFinalPath = os.path.join(base_dir, fileName)
data = pd.read_excel(excelFinalPath)
originRevList = data['revenue_origin'].tolist()
morphRevList = data['revenue_morph'].tolist()

i = 0
accurate = 0

while i < len(originRevList):
    originRev = str(originRevList[i])
    morphRev = str(morphRevList[i])
    originString = "".join(j for j in originRev if j.isdigit())
    morphString = "".join(j for j in morphRev if j.isdigit())
    if originString == morphString:
        accurate += 1
    i += 1
print(accurate)
print(len(originRevList))
result = accurate / len(originRevList)
print(result)

