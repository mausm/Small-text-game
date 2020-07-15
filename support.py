#DONE:
#the program loads the first sentence and #options -> Done
#the user selects an option in that list -> Done
#the program returns a new sentence based on the choosen options -> Done
#the user can exit the program -> Done
#give the user the ability to add and edit single lines in the db



#TODO:
#program imports last state: optional
#user can save his name and his progress (other db table)
#ensure that the id (see below) is unique  UNIQUE 
#user can import his name and it can be used in the sentences user_name = input("please enter your name:") .replace("<user_name>", user_name)

"""
The program is a text based game that takes lets a user select sentences to reply to a person talking to him/her
Depending on the chosen line the user gets a new option choice from a follow up conversation.
So like climbing a tree the user can go through different paths depending on his answers
"""


The_database_structure = """" 
The index for each line is build in numbers from its properties: Chapter | Sentence | Option
example, the second option choice in the first option menu in the first chapter will be 1 1 2

chapter [xx] sentence [xxxx] option [xx]

The lines that are being fed to the user (to which you respond) are always 0, so 1 0 ->0, 2 1 ->0 etc

The relationship between the sentences are stored in field destination, which is the index-code of the sentence where 
the questions leads to 

The content is the actual sentence the user sees


id | Chapter | Sentence | Option | Destination | Content


SECONDARY DATABASE:
Here we store the users statistics

Username | Last_sentence | RSS 

Last_sentence = the sentence on which the user ended his last session
RSS = relationship score, how nice they are to the different npcs 

"""
