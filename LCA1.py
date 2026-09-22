# write a python program to create a dictionary,tuple and list of students and perform the following operations
#  on the dictionary:add,delete,update

student_list = ["satyam","pankaj","shubham","yash","pavan"]
student_tuple = ("satyam","pankaj","shubham","yash","pavan")
student_dict ={11:"satyam",12:"pankaj",13:"shubham",14:"yash",15:"pavan"}
print("list of students:")
print (student_list)
print("\ntuple of students")
print(student_tuple)
print("\ndictionary of students:")
print(student_dict)
#1 add a student to a dictionary
student_dict[16] = "pranjali"
print("\nafter adding a student:")
print(student_dict)
#2 delete a student from dictionary
del student_dict[14]
print("\nafter deleting a student:")
print(student_dict)
#3 update a students name
student_dict[13] = "piyush"
print("\nafter updating a student:")
print(student_dict)