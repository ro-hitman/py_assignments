
def is_primerange(*args):

    for n in range(low_range,up_range+1):
        if n>1:
            for i in xrange(2,n):
                if (n%i)==0:
                    break
            else:
                print n


if __name__=='__main__':

    low_range=input("Enter value for low range: ")
    up_range=input("Enter value for upper range: ")

    #print "Prime nos between given range are: "

    is_primerange()
   
