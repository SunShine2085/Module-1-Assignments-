#Name:  Chris Courville
#Date:  5/6/24
#Proj:  Data Project Practice

# Write a program that reads in the csv file linked above and outputs the mean, median, 
# and standard deviation for the fall & spring semesters. Make sure to write at least
# two functions in your final solution. The more generalizable you make your code, 
# the more you may be able to reuse it for your own project later.
import statistics
#Read in file
def output_stats(list):
    print("Mean: ", statistics.mean(list))
    print("Median: ", statistics.median(list))
    print("STD: ", statistics.stdev(list))


def line_count():
    for line in file:
        list = line.rstrip().split(",")
        if list[1] == 'Spring 2016':
            spring.append(eval(list[2]))
        else:
            fall.append(eval(list[2]))
#Data Variables
spring = []
fall = []

csv = "sample_grades.csv"
file = open(csv)
for line in file:
    line_count()
file.close()

print("Fall 2016:")
output_stats(fall)

print("Spring 2016:")
output_stats(spring)