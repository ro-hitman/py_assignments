#WAP to accept 2 string from user and jumble(swap 1st 2 chars of both string) them. eg: dog, dinner = dig donner

str1=input("Enter a 1st string: ")
str2=input("Enter 2nd string: ")

print str1 + "\n" + str2

jumble_result = str2[:2] + str1[2:]+ "\t" + str1[:2] + str2[2:]
print jumble_result

 