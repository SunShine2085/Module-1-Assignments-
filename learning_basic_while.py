#Name:  Chris Courville
#Proj:  Learning Basic While
#Date:  5/4/24

# j = 4
# while j > -4:
#    print(j)
#    j -= 1


# str = "Hello" 
# builder = ""
# i = 0
# while i < len(str):
#    builder += str[i].swapcase() 
#    print(i, builder)
#    i += 1
# print(str, "->", builder)


# x = 0
# i = 1
# while x < 20:
#   if x > 5:
#     x += 15
#   else:
#     x += 1
#   print(i, x)
#   i += 1


# string = "HELLO"
# x = 0
# while string[x] != 'L':
#    print(string[x], end = ("..."))
#    x += 1
# print("\n", string, "first L is at", x)


# Assume the user enters the following:
# hello goodbye cat dog DONE done
# list = []
# prompt = "Please enter word, 'done' to finish "
# response = input(prompt)
# while response != "done":
#     list.append(response)
#     response = input(prompt)
# print(sorted(list))


# x = 0
# while x < 20:
#   if x > 5:
#     if x % 2 == 0:
#       x *= 2
#     else:
#       x *= -1
#   else:
#     x += 10
#   x += 1
# print(x)

# # 1a
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# # 1b
# x = 2
# while x < 12:
#     print(x)
#     x += 3

# # 1c
# y = -10
# while y <= 0:
#     print(y, end=" ")
#     y += 2
# print()

# # 1d
# z = 0
# while z < 4:
#     print(4 * "*")
#     z += 1

## 2
# string = "CSCI 150"
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1

## 3
# list = []
# prompt = "Please enter a number ('0' to finish)"
# response = eval(input(prompt))
# while response != 0:
#     list.append(response)
#     response = eval(input(prompt))
# print(sorted(list))
# print(sum(list))
# print(sum(list)/len(list))

# def well(x):
#     t = -3
#     while t < x:
#         if t < 0:
#             t += x
#         else:
#             t *= 2
#     return t
# print(well(5))


# def zero_counter():
#     cnt_z = 0
#     user_input = ""
#     while user_input != "Q":
#         user_input = (input("Please Enter a Number, (Q to quit): "))
#         cnt_z += user_input.count("0")
#     return cnt_z

# def main():
#     print("you have", zero_counter(), "zero's")
# main()#Works


# def count_fricatives(list):
#     fric = "fsvz"
#     cnt_f = 0
#     for string in list:
#         for char in fric:
#             cnt_f += string.lower().count(char)
#     return cnt_f

# def main():
#     print(count_fricatives(["Zebra"," ligthsaber","1234 JOYS!"]))
#     print("count_fricatives", count_fricatives(["Zebra"," ligthsaber","1234 JOYS!"]) == 3)
# main()#Works


# def why11(list):
#     y = 1
#     j = 0
#     while j < len(list) and y < 11:
#         x = list[j]
#         if x < 0:
#             y -= x
#         elif x % 2 == 0:
#             y += x
#         j +=2
#     return y

# print(why11([4,-1,-5,2,1,3,7,-8]))

