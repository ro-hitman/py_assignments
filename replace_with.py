#WAP to accept a string from user replace the occurance of 1st char in remianing part of string with * eg: babble = ba**le

str1= input("Enter a string: ")

res=str1[0]
str1=str1.replace(res[0],'*')
str1=res+str1[1:]
print str1