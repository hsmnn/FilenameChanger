import os, glob, sys
from progress.bar import Bar
if __name__ == "__main__":
    #Some var declarations
    repeat = True
    wordToAdd = ""
    path = ""
    while repeat:
        #Chose the option
        choice = input("Select the action you want to run :\r\n1) Rename files\r\n2) Exit\r\n")
        #Option selector
        if choice == "1" :
            #Set the word to add
            wordToAdd = input("Enter the word you want to add at the end of the file : ")
            #Set the path
            path = input("Enter the folder path : ")
            #Get the number of file in the folder
            fileNumber = 0
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.find(wordToAdd) == -1:
                        fileNumber += 1
            #Create the loading bar. The max number is the number of file in the folder
            bar = Bar('Renaming', max=fileNumber)
            for root, dirs, files in os.walk(path):
                for file in files:
                    #Get the file without the extension
                    fileName = os.path.splitext(file)[0]
                    #Get only the extension
                    ext = os.path.splitext(file)[1]
                    #Build the new filename
                    newFileName = fileName + wordToAdd + ext

                    #Verify if the filename already contains the word to add
                    if fileName.find(wordToAdd) == -1:
                        #Rename the file
                        os.rename(path + file, path + newFileName)
                        bar.next()
                print("\r\nFiles successfully renamed !")
        elif choice == "2" :
            exit()
        else :
            print("This not an option. Please try again.")
