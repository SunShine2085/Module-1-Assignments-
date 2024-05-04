#Name:  Chris Courville
#Proj:  List and Strings Practice
#Date:  5/3/24

#1 create a list of 20 numbers input by user and prints the mean of the list.
import statistics



# list = []
# for i in range(20):
#     list.append(eval(input('Please enter a number: ')))
# print(statistics.mean(list))

#2 Write a function mangle that takes a string as a parameter and returns the string after performing the following operations:
#   i.  Convert the string to all upper case letters
#   ii. Remove the third character
#   iii. Removing the third to last character

def mangle(string):
    string = string.upper()
    string = string[0:2]+string[3:-3]+string[-2:]
    return string

def count_e(list): 
    num_e = 0 #sum -- aggregate values
    for string in list:
        num_e += string.upper().count("E")
    return num_e

def count_vowels(list):
    num_v = 0
    for string in list:
        upper = string.upper()
        for vowel in "AIEOU":
             num_v += upper.count(vowel)
    return num_v

def main():
    #test mangle
    print(mangle('hellothere')) # working function call
    test_input = ['hellothere', '42 degrees celsius', 'eeeeeee']
    test_ouput = ['HELOTHRE', '42DEGREES CELSUS', 'EEEEE']
    for i in range(len(test_input)):
        print("Mangle", test_input[i]+":", mangle(test_input[i])==test_ouput[i])
    
    #test count_e
    print(count_e(['hi', 'hello', 'EEK!'])) # working function call
    print('count_e', count_e(['hi', 'hello', 'EEK!']) == 3) 

    #test count_vowels
    print(count_vowels(['hi', 'hello', 'oof!'])) # working function call
    print('count_vowels', count_vowels(['hi', 'hello', 'oof!']) == 5)


    

main()

