# def name_age_display():
#     student={}
#     for counter in range (3):
#         name_str = input("enter name")
#         age_int = int(input("enter age"))
#         student[name_str]= age_int
#
#
#     return student

# for counter in range (3):
# print(name_age_display())

# for counter in range(3):
#     name_str = input("enter your name: ")
#     age_int = int(input("enter age: "))
#     print("Name",name_str,"Age",age_int)

# Teachers_Practice(List of tuple)
# records = []
#
# for _ in range(3):
#     print("hello")
#
# names=["james", "shina", "ade"]
#
# for name in names:
#     print(name)

def get_name_age():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    return  name,age


def collect_and_store_name_age():
    name, age = get_name_age()
    records.append((name, age))


records = []

for _ in range(3):
    collect_and_store_name_age()




print(records)