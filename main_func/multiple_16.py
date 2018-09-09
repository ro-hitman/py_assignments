
def mult_16(num1):

    if(num1&15==0):
        print "{} IS multiple of 16" .format((num1))
    else:
        print "{} Not multiple of 16" .format((num1))
		
if __name__=='__main__':
    res=mult_16(33)
    #print res