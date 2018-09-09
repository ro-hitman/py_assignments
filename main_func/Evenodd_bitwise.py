#WAP to accept a number and check if Even/Odd using bitwise operator

def evenodd(num1):
    num1=input("Enter a number: ")

    if(num1&1==1):
        print "%d Number is ODD" %num1
    else:
        print "%d Number is EVEN" %num1 
		
if __name__=='__main__':
    evenodd(9)
	
	