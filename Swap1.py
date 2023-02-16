''' To swap two numbers'''
x= int(input("Enter First Value(x):"))
y= int(input("Enter Second Value(y):"))

x=x+y
y=x-y
x=x-y

print ("Value of x after swapping: {0}\nValue of y after swapping: {1}".format(x,y))
