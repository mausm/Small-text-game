import data as db_formulas
import pandas as pd

print("For old excel files (.xlsx) you have to install the xlrd module")

Column_dict = \
    {0:"id",
     1:"Chapter",
     2:"Sentence",
     3:"Option",
     4:"Destination",
     5:"Content"
    }


def check_data(df):
    if len(df.iloc[1,]) != 6:
        print("the amount of columns is incorrect")
        return False
    else:
        return True

while True:
    if input("Do you want to import an excel file? y/n" != "y":
        break
    
    File_name = input("Please select the name of the file (including .xlsx/.xls): ") 
    #File_name = "testdata.xlsx" #"string with file name" 
    Column_names = ['id',"Chapter","Sentence","Option", "Destination", "Content"]



    data = pd.read_excel(File_name)
    df = pd.DataFrame(data, columns= Column_names)
    
    
    # if one value is NaN, then the column name in excel was different than the list above
    if check_data(df):
        values_for_query = [tuple(item) for item in df.to_numpy()]
    else:
        print("The data has a wrong amount of columns"
    print(values_for_query)


    db_formulas.insert_large_dataset(values_for_query)



while True:
    user_choice = input("Do you want to insert a new sentence (1) or add a sentence (2) or quit (3)")
    if user_choice == "1":
        tuple_for_db = []
        for _,y in Column_dict.items():
            tuple_for_db.append(input("What is the value for {}: ".format(y)))

        #replace index in case user made a misstake
        tuple_for_db[0] = int(tuple_for_db[1] + tuple_for_db[2] + tuple_for_db[3])
        tuple_for_db = tuple(tuple_for_db)

        try:
            db_formulas.add_sentence(tuple_for_db)
            print("added the value to the db")
        except:
            print("Sorry, something went wrong")

    elif user_choice == "2":
        chosen_index = input("What is the index of the row you want to change: ")
        tuple_from_db = db_formulas.get_sentence(int(chosen_index))
        #to change a specific value
        tuple_from_db = list(tuple_from_db)

        print(tuple_from_db)
        for item in tuple_from_db:
            if input("Do you want to change this item: {}  y/n ".format(item)) == "y":
                tuple_from_db[tuple_from_db.index(item)] = input("Type the new value in here: ")
        tuple_from_db.insert(0,int(chosen_index))
        tuple_from_db = tuple(tuple_from_db)
        try:
            db_formulas.change_sentence(tuple_from_db[0], tuple_from_db[1:])
        except:
            print("Sorry, something went wrong")
    else:
        break
