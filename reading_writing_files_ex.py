#Name:  Chris Courville
#Proj:  Using Files
#Date:  5/5/24

# datafile = open("add.txt")
# for line in datafile:
#     print(line.rstrip())
# datafile.close()
import filecmp

# prompt = "Enter the next line in the file: "

# outfilename = input("What is the name of your output file? ")
# numLines = eval(input("How many lines do you want to write? "))

# #create a new file object, in "write" mode
# dataFile = open(outfilename, "w") # a to append

# for x in range(numLines):
#     userinput = input(prompt)
#     #write user's input to the file
#     print(userinput, file=dataFile)
# dataFile.close()

# 1 writing files practice
# datafile = open("add.txt")
# for line in datafile:
#     print("-", line.rstrip())
# datafile.close()


# 2 

# outfilename = input("File Name?: ")
# dataFile = open(outfilename,"w" )
# prompt = "Enter a number, 0 to quit: "
# userinput = eval(input(prompt))
# while userinput != 0:
#     print(userinput, file=dataFile)
#     userinput = eval(input(prompt))
# dataFile.close()

#3
# def count_lines(filename):
#     t = 0
#     for line in open(filename):
#         t += 1
#     return filename + ':' + str(t)

# def main():
#     list = ["text1.txt", "text2.txt", "text3.txt"]
#     datafile = open("counts.txt","w")
#     for file in list:
#         print(count_lines(file), file =datafile)
#     datafile.close()
# main()

#4
# def count_lines_words(filename):
#     t = 0
#     tw = 0
#     for line in open(filename):
#         t += 1
#         tw += len(line.split(" "))
#     return filename + ':' + str(t), "lines,", str(tw), "words"

# def main():
#     list = ["text1.txt", "text2.txt", "text3.txt"]
#     datafile = open("counts.txt","w")
#     for file in list:
#         print(count_lines_words(file), file =datafile)
#     datafile.close()
# main()



list = ["text1.txt", "text2.txt", "text3.txt"]
datafile = open("counts.txt","w")
tot_l = 0
tot_w = 0
for file in list:
    t = 0
    tw = 0
    for line in open(file):
        t += 1
        tw += len(line.split(" "))
    tot_l += t
    tot_w += tw
    print(file, ':', str(t), "lines,", str(tw), "words", file=datafile)
print("TOTAL:" , str(tot_l), "lines,", str(tot_w), "words", file=datafile)