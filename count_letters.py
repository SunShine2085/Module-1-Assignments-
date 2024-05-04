#Name:  Chris Courville
#Proj:  Count number of leters in a list
#Date:  5/4/24



def count_letters(list, letter):
    num_l = 0
    i = 0
    while i < len(list):
        num_l += list[i].lower().count(letter.lower())
        i += 1
    return num_l

def main():
    print(count_letters(["HELLO","goodbye","1234","Oooh!"], 'O'))
    print("count_letters", count_letters(["HELLO","goodbye","1234","Oooh!" ], 'O') == 6 )
main()

