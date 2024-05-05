#Name:  Chris Courville
#Proj:  Using Files
#Date:  5/5/24

# datafile = open("add.txt")
# for line in datafile:
#     print(line.rstrip())
# datafile.close()
import filecmp

prompt = "Enter the next line in the file: "

outfilename = input("What is the name of your output file? ")
numLines = eval(input("How many lines do you want to write? "))

#create a new file object, in "write" mode
dataFile = open(outfilename, "w") # a to append

for x in range(numLines):
    userinput = input(prompt)
    #write user's input to the file
    print(userinput, file=dataFile)
dataFile.close()

