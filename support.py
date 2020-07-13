#program imports last state: optional
#the program loads the first sentence and #options
#the user selects an option in that list
#the program returns a new sentence based on the choosen options

#the user can exit the program


"""
The program is a text based game that takes lets a user select sentences to reply to a person talking to him/her
Depending on the chosen line the user gets a new option choice from a follow up conversation.
So like a tree the user can go through different paths depending on his answers



"""


The_database_structure = """" 
The index for each line is build in numbers from its properties: Chapter | Sentence | Option
example, the second option choice in the first option menu in the first chapter will be 01 0001 02

chapter [xx] sentence [xxxx] option [xx]

The lines that are being fed to the user (to which you respond) are always 00, so 01 0000 00, 02 0001 00 etc

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



#het laatste cijfer
#print(216 - (216 // 10 * 10))

print((216 % 10) // 1)
print((216 % 100) // 10)
print((216 % 1000) // 100)

#de honderdtallen
#print((216 // 100 ))

# de tientallen
#print((216 % 100) // 10)
#print(216 / 1000)

i = 1
x = 0
n = 21334
while i >= 1:
    x = x + 1
    i = n // (10 ** x)

for i in range(x,1,-1):
    print((21334 % (10 * (x-i+1))) // (1 * (x-i+1) * 10) * 10 ** x )




