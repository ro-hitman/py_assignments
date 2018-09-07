#Program to accept string & start,end,step value for slicing from user

slice_str = input("Enter a string to be sliced: ")
#print slice_str

start_index = input ("\n Enter startIndex: ")
end_index = input ("\n Enter endIndex: ") 
step_value = input("\n Enter stepValue: ")

print "[" , start_index , ":" , end_index, ":", step_value, "]"
print "\n Your slicing result is: " + slice_str [start_index:end_index:step_value]
