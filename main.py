import data, sys

# create the database if it doesn't exist




def current_sentence(index=1):
   destination = data.get_sentence(index)
   return destination # this is the destination,  the second value of the is the desct


def give_the_options(option_list, amount):

    for i in range(1, amount):
        sentence = option_list[i][0] # ik moet even in de return functie van de database duiken welke
        print(i, sentence, "\n") #option_list[i-1]


def test_if_db_exist(currentsentence):
    try:
        current_sentence(currentsentence)

    except:
        data.create_table()
        print("a new table is created, now you need to fill it with data!")


def menu():
    index = 1
    while True:


        # starting point of the program. Returns the first sentence first time
        index = current_sentence(index) # the current location
        # index = tuple of (Sentence, Destination, Chapter, Sentence)
        #this is the sentence to wich the player reacts
        print(index[3])
        # shows the user all possible options from the index tuple, which is all the data from the row that index is on
        option_list = data.options(index[0],index[1]) # use the chapter nr and the sentence nr to get all the options with the db functions
        #print(option_list)
        amount_of_options = len(option_list) # how many option there are for this sentence

        # formula prints the options on screen
        give_the_options(option_list, amount_of_options)


        while True:
            user_answer = input("What will you say? (1-{}): ".format(amount_of_options-1))
            try:
                # if the user accidentally enters the dot after his/her answer
                user_answer.replace(".", "")
                user_answer = int(user_answer)
                # Here the index becomes a single value, as an id, so the next index can be a tuple again
                index = option_list[user_answer][1]
                break
            except:
                if input("If you want to quit press q") == "q":
                    sys.exit(0)
                else:
                    pass






# when you run the program it checks if there is already a database by running a check on the first sentence
# if that fails it creates it in a sql-lite (or similar) database
test_if_db_exist(1)

menu()