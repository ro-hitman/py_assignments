
def palindrome(x):

    temp=x
    rev=0
    while(x!=0):
        digi=x%10
        rev=rev*10+digi
        x=x/10
    if(rev==temp):
        print "Number is PALINDROME"
    else:
        print "Number is not PALINDROME"

if __name__=='__main__':

    x=input("Enter a number: ")
    palindrome(x)