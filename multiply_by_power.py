#WAP to accept a number from user as well as the power by which to multiply

num1=input("Enter a number: ")
pow=input("Enter power by which you wish to multiply: ")

res=num1**pow

print "{}'s power of {} = " .format(pow,num1), res
