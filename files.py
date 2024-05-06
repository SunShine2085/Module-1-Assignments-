#Practice with files and dictionaries
#Count the number of lettters in a file using dictionary
#By:    Chris Courville
#Date:  5/6/24

letters = ["A", "B", "C","D","F"]
counts = {}
file = "letter-grades.txt"
for line in open(file):
    letter = line.replace("\n", "")
    count = counts.get(letter, 0)
    counts[letter] = count + 1

print("Letter counts: ")
for l in letters:
    print(l + ":", counts.get(l,0))
