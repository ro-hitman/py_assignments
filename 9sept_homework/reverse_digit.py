def rev_dig(x):

    rev=0
    while(x!=0):
        rem=x%10
        rev=rev*10+rem
        x=x/10
    print rev

if __name__=='__main__':
    x=input("Enter a number: ")
    rev_dig(x)