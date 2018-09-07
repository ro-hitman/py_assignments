#WAP to accept a num from user and check whether it is multiple of 128 or not

num1=input("Enter a number: ")

if (num1&127==0):
    print "{} is a Multiple of 128".format((num1))
else:
    print "{} is NOT a Multiple of 128".format((num1))