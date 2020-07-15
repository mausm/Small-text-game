import sqlite3

DATABASE_NAME = "Hopeloos_spel_data.db"


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


def create_table():
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("""CREATE TABLE Sentences (id integer, Chapter integer,
                        Sentence integer, Option integer, Destination integer, Content text);""")





def get_sentence(index):
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute("SELECT Chapter,Sentence,Destination,Content FROM Sentences WHERE id = ?", (index,))

        sentence_info = cursor.fetchone()
    return sentence_info # is a tuple of the sentence and the destination of the sentence


def options(Chapter, Sentence):
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT Content,Destination FROM Sentences WHERE Chapter =  ? AND Sentence = ?', (Chapter, Sentence))

        sentence_info = cursor.fetchall()
    return sentence_info # is a tuple of the sentence and the destination of the sentence


# this one is for the import excel file
def insert_large_dataset(Dataset):
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        query = "INSERT INTO Sentences VALUES (?,?,?,?,?,?)"
        #(id, Chapter, Sentence, Option, Destination, Content)
        records_to_insert = Dataset

        cursor.executemany(query,records_to_insert)

    return True

# this part is to add or modify one line
def change_sentence(index, tuple_of_info):
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()

        index = (index,)
        val = tuple_of_info + index
        query = "UPDATE Sentences SET Chapter = ?, Sentence = ?, Option = ?, Destination = ? ,Content = ? WHERE id = ?"
        cursor.execute(query, val)

def add_sentence(tuple_of_info):
    with DatabaseConnection(DATABASE_NAME) as connection:
        cursor = connection.cursor()


        val = tuple_of_info
        query = "INSERT INTO Sentences VALUES (?,?,?,?,?,?)"
        cursor.execute(query, val)
