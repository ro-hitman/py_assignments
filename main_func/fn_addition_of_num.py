#Program to accept numbers from user and print their addition
'''
#Without function
num1 = input("\n Enter 1st number for addition: ")
#print num1

num2 = input("\n Enter 2nd number for addition: ")
#print num2

sum = num1 + num2

print "\n Addition of" , num1 , "and" , num2 , "is: ", sum 
'''


def add_num(num1,num2):
    
    return num1+num2
	
if __name__=='__main__':

    sum=add_num(10,20)
