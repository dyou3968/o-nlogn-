# creates file with inputed text
def textToFile(text):
    testFile = open(r"myFile.txt", "w+")
    testFile.write(text)
    testFile.close()

text = "Hello world"
textToFile(text)

# reads file and returns text
def fileToText(file):
    fileString = ""
    if (".txt" in file):
        fileString = f"{file}"
    else:
        fileString = f"{file}.txt"
    currFile = open(fileString, "r+")
    return currFile.read()

fileName = "myFile.txt"
print(fileToText(fileName))