
def sum_of_digits(x):

    rem=0
    while(x!=0):
        y=x%10
        rem=rem+y
        x=x/10
    print rem
		
if __name__=='__main__':

    x=input("!!!!!!!!!!!!!!!!!ENTER any number: ")
    sum_of_digits(x)
    