#WAP to accept 2 strings from user and check if 2nd string is right rotation of 1st eg: 1st: manager 2: germana

def rightrot(*args):
    str1 = input("Enter a 1st sting: ")
    str2 = input("Enter a 2nd string: ")

    print str2 in (str1+str1)
	
if __name__=='__main__':
    rightrot()