
def sum_of_digits(x):

    even=0
    odd=0
    while(x!=0):
        y=x%10
        if (y%2==0):
		    even=even+y
        else:
		    odd=odd+y
			
        x=x/10
    print "EVEN NUMBER sum is: ",even
    print "ODD NUMBER sum is : ",odd
		
if __name__=='__main__':

    x=input("!!!!!!!!!!!!!!!!!ENTER any number: ")
    sum_of_digits(x)
    