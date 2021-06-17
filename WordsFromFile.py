def myFunction():
    filename = input("Enter the filename : ")
    file = open(filename)
    fileList = file.readlines()
    totalWords = 0
    for sentence in fileList:
        totalWords = totalWords + len(sentence.split())
    print(totalWords)
        
myFunction()


