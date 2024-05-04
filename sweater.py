temp = eval(input("Please enter the temperature: "))

#for i in range(3):
print(temp)
if temp > 90:
            print("Whoa!, its boiling")
elif temp >= 80 and  temp < 90:
            print("It's getting hot")
elif temp > 60 and temp < 80:
            print("A perfect day")
elif temp > 0 and temp < 60:
            print("Don't Forget your sweater")
else:
            print("Brr, you need a coat")