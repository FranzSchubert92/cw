def getVowelCount(inputStr):
    return sum(1 for x in inputStr if x.lower() in "aeiou")
