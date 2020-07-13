import data as db_formulas
import pandas as pd

print("For old excel files (.xlsx) you have to install the xlrd module")

File_name = "testdata.xlsx" #"string with file path and file name" # r'Path where the Excel file is stored\File name.xlsx'
Column_names = ['id',"Chapter","Sentence","Option", "Destination", "Content"]



data = pd.read_excel(File_name)
df = pd.DataFrame(data, columns= Column_names)

def check_data(df):
    if len(df.iloc[1,]) != 6:
        print("the amount of columns is incorrect")
        return False
    else:
        return True


# if one value is NaN, then the column name in excel was different than the list above
values_for_query = [tuple(item) for item in df.to_numpy()]

print(values_for_query)


db_formulas.insert_large_dataset(values_for_query)
