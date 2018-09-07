#WAP a program to accept 3 nos and display whether triangle can be formed or not

a,b,c = input("Enter 3 SIDES of a triangle: ")

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print "Triangle cannot be formed"
else:
    print "Triangle can be formed"
	