#WAP to include all kinds of arguments

def positional_args(a,b):
    return a+b
	
def keyword_args(x,start,end,step=1):
    return x[start:end:step]

def variable_args(*args):
    for x in args:
	    print x

def kw_args(*args,**kwargs):
    x=input("Enter a no to understand args: ")
    stud_details=input("Enter stud details in DICT format: ")
		
		
def mix_args(a,b=10,*args,c=20,**kwargs):
    return (a+b)
    c,y=input("Enter 2 input number: ")
    return (c-y)
	details=input("Enter DICT details: ")
	

if __name__=='__main__':
    
    #result=positional_args(10,20)
    #print result
	
    #result=keyword_args("Rohit",2,5)
    #print result
	
    #result=variable_args(1,"All args are valid", [10,20,"rohit",40])
    #print result
	
    #result=kw_args()
    #print result
	
    result=mix_args(10,10)
    print result