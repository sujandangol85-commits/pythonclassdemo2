# # 1.Lists

# #indexing of lists:

# students=["ram","shyam","Hari","gita","rita"]
# #           0      1       2      3     4
# #          -5     -4      -3     -2     -1

# #slicing

# print(students[1:4:2])

# #methods

# students.append("nita")
# students.insert(0,"sujan")
# students.sort()
# removed_student=students.pop()
# print(students)
# print(removed_student)

# # 2.Tuples

# fruits = ("Apple","Banana","Orange","Mango")
# print(type(fruits))

#3.dictionary

students={
    "Ram":"Janakpur",
    "Shyam":"Kathmandu",
    "Hari":"Bhaktapur",
    "Rita":"Lalitpur"
}
print(type(students))

for studentName,studentAddress in students.items():
    print(f"Name={studentName}, Address={studentAddress}")

