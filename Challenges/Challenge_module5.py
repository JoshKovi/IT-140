
def generateString(char,val):
    value = ''
    for i in range(val):
        value = value + char

    return value
#print(generateString(character, count))

def isRed(largeString):
    if largeString.find("red") != -1:
        return True
    else:
        return False

#print(isRed(text))
