
import re
cerseiSpeech = "The Mad King's daughter has ferried an arm of savages to " \
               "our shores, mindless unsullied soldiers who would destroy " \
               "your castles and your holdfasts, Dothraki heathens who " \
               "will burn your villages to the ground, rape and enslave " \
               "your women, and butcher your children without a second " \
               "thought... You remember the mad king, you remember the " \
               "horrors he inflicted on his people. His daughter is no " \
               "different. In Essos her brutality is already legendary. " \
               "She crucified hundreds of noblemen in Slavers Bay. And " \
               "when she got bored of that, she them to her dragons. " \
               "It is my solemn duty to protect the people and I will, but " \
               "I need your help my lords. We must stand together, all of " \
               "us, if we hope to stop her."

def search(textCheck,num):
    if num == 0:
        if re.match(textCheck, cerseiSpeech):
            print("Pattern Matched!")
            print(re.match(textCheck, cerseiSpeech))
        else:
            print("No pattern match.")
    elif num == 1:
        if re.search(textCheck, cerseiSpeech):
            print("Pattern Matched!")
            print(re.search(textCheck, cerseiSpeech))
        else:
            print("No pattern match.")
    else:
        print("Try Again")

def chal43(fileNum = 0, stringCheck = 'parrot'):
    if fileNum == 0:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/empty.txt"
    elif fileNum == 1:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/cheese.txt"
    elif fileNum == 2:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/accounts.txt"
    elif fileNum == 3:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/poem.txt"
    elif fileNum == 4:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/pipe.txt"
    elif fileNum == 5:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/parrot.txt"
    elif fileNum == 6:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/fixed-length.txt"
    else:
        return "Not This time"
    S = stringCheck


    fileText = open(P, 'rt')
    fileTextRead = fileText.read()
    checkList = re.findall(str(S), fileTextRead)
    fileText.close()
    return(len(checkList))

def chal45(fileNum = [0,0], strings= ['Hello','Not Today Batman']):
    P = []
    for i in fileNum:
        if fileNum[i] == 0:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/empty.txt")
        elif fileNum[i] == 1:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/cheese.txt")
        elif fileNum[i] == 2:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/accounts.txt")
        elif fileNum[i] == 3:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/poem.txt")
        elif fileNum[i] == 4:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/pipe.txt")
        elif fileNum[i] == 5:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/parrot.txt")
        elif fileNum[i] == 6:
            P.append("C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/fixed-length.txt")
        else:
            return "Not This time"
    I = str(P[0])
    O = str(P[1])
    S = str(strings[0])
    T = str(strings[1])

    fileText = open(I, 'rt')
    fileTextRead = fileText.read()
    fileText.close()
    checkList = re.sub(str(S), str(T), fileTextRead) 
    fileText = open(O, 'wt')
    fileText.write(checkList)
    fileText.close()

def chal53(fileNum = 6, F = 'Adam', L = "Smithers", B = "00000000"):
    if fileNum == 0:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/empty.txt"
    elif fileNum == 1:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/cheese.txt"
    elif fileNum == 2:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/accounts.txt"
    elif fileNum == 3:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/poem.txt"
    elif fileNum == 4:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/pipe.txt"
    elif fileNum == 5:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/parrot.txt"
    elif fileNum == 6:
        P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/fixed-length-copy.txt"
    else:
        return "Not This time"
    
    fileText = open(P,'rt')
    fileTextRead = fileText.read()
    fileText.close()
    newList = ""
    start = 0
    fixedLength = 40
    while (len(fileTextRead)-start >= fixedLength):
        record = fileTextRead[start:start+fixedLength]
        if F in record and L+" " in record:
            record = record[:-len(B)] + B
        newList += record
        start+=fixedLength

    fileText = open(P, 'wt')
    fileText.write(newList)
    fileText.close()
    
def chal55(P = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/pipe-copy.txt",
           F = 'Adam', L = "Smithers", B = "00000000"):
    # ----------------------------------------------------------------
    # 
    # Our Helper functions:
    # 
    # ----------------------------------------------------------------

    #
    # Loads the file at filepath 
    # Returns a 2d array with the data
    # 
    def load2dArrayFromFile(filepath):
      # Your code goes here:
        fileText = open(filepath, 'rt')
        tempRecord = []
        for i in fileText:
            tempRecord.append(i.split("|"))
        fileText.close()
        return tempRecord
    #
    # Searches the 2d array 'records' for firstname, lastname.
    # Returns the index of the record or -1 if no record exists
    # 
    def findIndex(records, firstname, lastname):
      # Your code goes here:
        for i in range(len(records)):
            if records[i][0] == firstname and records[i][1] == lastname:
                return (i)
        return (-1)
          
    # Sets the birthday of the record at the given index
    # Returns: nothing
    def setBirthday(records, index, newBirthday):
      # Your code goes here:
        records[index][-1] = str(newBirthday) + "\n"
  
    # Convert the 2d array back into a string
    # Return the text of the 2d array
    def makeTextFrom2dArray(records):
      # Your code goes here:
        newList = ""
        for i in records:
            newList += '|'.join(i)
        return (newList)

    # ----------------------------------------------------------------
    # 
    #  Our main code body, where we call our functions.
    #  
    # ----------------------------------------------------------------

    # Load our records from the file into a 2d array
    records= load2dArrayFromFile(P)

    # Find out which index, if any, has the name we are hunting
    indexWeAreHunting= findIndex(records, F, L)

    # Set the birthday record to the one we were passed
    setBirthday(records, indexWeAreHunting, B)

    # Convert the records into a text string
    output= makeTextFrom2dArray(records)

    # Your code goes here
    # write the text string out to the file
    fileText = open(P,"wt")
    fileText.write(output)
    fileText.close()

def chal56(F1 = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/accounts-copy.txt",
           F2 = "C:/Users/joshu/Documents/SNHU School Related/IT-140/Scripts/Challenges/testFiles/accounts-action.txt"):
    def fileLoading(File):
        fileText = open(File,'rt')
        tempRecord = []
        for i in fileText:
            tempRecord.append(i.split("|"))
            tempRecord[-1][-1] =str(tempRecord[-1][-1])[:-1] 
    
        fileText.close()
        return tempRecord

    def accountVerify(actInfo, actAction):
  
        for i in range(len(actInfo)):
        #If it finds a matching account number and pin continue
            if actAction[2] == actInfo[i][0] and actAction[3] == actInfo[i][1]:
                #if the command is add
                if actAction[0]== "add":
                    actInfo[i][2] =  int(actInfo[i][2])+int(actAction[1])
                    actInfo[i][2] = str(actInfo[i][2])
                #if the command is sub and the account has sufficient funds
                elif actAction[0]== "sub" and int(actAction[1]) <= int(actInfo[i][2]):
                    actInfo[i][2] =  int(actInfo[i][2]) - int(actAction[1])
                    actInfo[i][2] = str(actInfo[i][2])
  

    actInfo = fileLoading(F1)
    actActionList = fileLoading(F2)


    for i in actActionList:
        accountVerify(actInfo, i)

  
    fileText = open(F1, "wt")
    newList = ""
    for i in actInfo:
        newList += '|'.join(i) +"\n"
    fileText.write(newList)
    fileText.close()


def chal6RE(pattern = "regular[ -:&]expression"):
    search_string='''This is a string to search for a regular expression like regular expression or 
                    regular-expression or regular:expression or regular&expression'''
    match1 = re.findall(pattern,search_string)
    print(match1)
    if match1 is not None:
        print(pattern+ " matched")
    else:
        print(pattern, " did not match")
def chal8RE(pattern = "regular[-:&]expression"):
    search_string='''This is a string to search for a regular expression like regular expression or regular-expression or regular:expression or regular&expression'''

    substitution= "regular expression"

    replace_result = re.sub(pattern, substitution, search_string)
    print(replace_result)