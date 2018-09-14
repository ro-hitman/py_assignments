
num=input("Enter a number: ")
tmp=0
x=num
while(x!=0):
    y=x%10
    #print y	
    tmp=y**3	
    x=x//10

if (num==tmp):
    print "Armstrong"
else:
    print "Not Armstrong"

