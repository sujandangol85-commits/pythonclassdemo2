# import sys

# print(sys.version)

# if(54>34):
#  print("Yes") 
# """indent(tab space is mandatory or it will raise error)
#  indent char ota space nai hunuparxxa vanne xna tara best practice xhai four
#  tara if euta block of code vitra kai euta kai duita kai char ota diyoki chai error auxa , consistent hunuprx"""



student_records = []

with open("student.txt", "r") as file:
    records = file.readlines()
    print(records)
    for record in records[1:]:
        name, mark1, mark2 = record.strip().split(",")
        mark1 = int(mark1)
        mark2 = int(mark2)
        student_records.append((name, mark1, mark2))

print(f"{'Name':<10}{'Mark1':<10}{'Mark2':<10}")
print("-" * 30)
for name, mark1, mark2 in student_records:
    print(f"{name:<10}{mark1:<10}{mark2:<10}")


    


        

