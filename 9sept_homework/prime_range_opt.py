def is_primerange(*args):

    for n in range(low_range,up_range+1):
        if n<2:
            return False
        elif n==2 or n==3:
            return True
        elif n%2==0:
            return False
        else:
            for i in xrange(3,n//2+2):
                if (n%i)==0:
                    break
            else:
                print n

if __name__=='__main__':

    low_range=input("Enter value for low range: ")
    up_range=input("Enter value for upper range: ")

    print "Prime nos between given range are: "

    is_primerange()