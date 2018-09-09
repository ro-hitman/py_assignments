# WAP to accept 2 nos from user and display their power

def pow(*args):
    num = input("Enter a number: ")
    pow = input("Enter power by which u want to multiply: ")

    result = num**pow
    print result

	
if __name__=='__main__':

    pow()