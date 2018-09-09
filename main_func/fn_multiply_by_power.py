#WAP to accept a number from user as well as the power by which to multiply

def power(num1,pow):
    num1=input("Enter a number: ")
    pow=input("Enter value for power: ")
    return num1**pow

if __name__=='__main__':
    res=power(2,2)
    print res
