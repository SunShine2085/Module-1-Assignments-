#Name:  Chris Courville
#Proj:  AVERAGE_NEGE_EVENS
#Date:  5/3/24

# list = [0,1,2,-2,-3,-4,3,4]
def average_neg_evens(list):
    sum_n_e = 0
    cnt_n_e = 0
     
    for i in list:
        if i < 0 and (i % 2) == 0:
            sum_n_e += i
            cnt_n_e += 1

    avg_n_e = sum_n_e / cnt_n_e
         
    return avg_n_e


def main():
    #test avg neg even
    print(average_neg_evens([0,1,2,-2,-3,-4,3,4])) # working function call
    print('average_neg_evens', average_neg_evens([0,1,2,-2,-3,-4,3,4]) == -3)

main()
