#WAP to accept a string from user assume that it contains followed by 'not bad' and replace by 'good' 

str1 = input("Enter a string: ")

pattern1 = input("Enter a pattern to be searched in string: ")

print "Found " + pattern1 + " in: " + str1

newstr = str1.replace(pattern1,"good")

print "Replaced string is: ", newstr
