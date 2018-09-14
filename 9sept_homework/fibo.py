
def fibo(n):

    i=0

    a=0
    b=1

    while(i<n):
        if(i<=1):
            num=i
        else:
            num=a+b
            a=b
            b=num
        print num
        i+=1
    
        
if __name__=='__main__':

    n=input("Enter a Number for range: ")
    fibo(n)