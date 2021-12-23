# my_food_item_list = ["garri", "peak milk", "bournvita",
#                      "cornflakes", "buscuit"]
#
# print(my_food_item_list)
#
# print(my_food_item_list[-(len(my_food_item_list))])
#
# print(my_food_item_list[::-1])
# print(my_food_item_list.reverse())
#
# my_food_item_list.append('omo')
# my_food_item_list += ["sweet"]
# print(my_food_item_list)
#
# a_list = []
# for list in range(1, 7):
#     a_list += [list]
#
# print(a_list)
#
# b_list = [10, 20, 30, 40]
# c_list = [25, 35]
# d_list = b_list + c_list
# print(d_list)
#
# for i in range(len(d_list)):
#     print(f"{i}:{d_list[i]}")
#
#
# def list_multiplication(numbers):
#     for counter in range(len(numbers)):
#         numbers[counter] = counter **3
#     return numbers
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(list_multiplication(numbers))
#
# character=[]
# character+="HappyBirthday"
# print(character)
#
# # Creating an empty tuple
# student_tuple=()
# print(student_tuple)
#
# print(len(student_tuple))
# student_tuple="John","Green",3.3
# print(student_tuple)
# print(len(student_tuple))
#
# teacher_tuple=("Pete","Morgan",2)
# for i in range(len(teacher_tuple)):
#     print(teacher_tuple[i])
#
# # Tuple may contain mutable object
# customer_tuple=('Amanda','Blue',[98,75,87])
#
# customer_tuple[2][1]=58
# print(customer_tuple)
#
# # print(a_list+customer_tuple)
# first_name, second_name, grades = customer_tuple
# print(first_name)
# print(f'{first_name} {second_name} {grades}')
#
# # Swapping Values Via Packing and Unpacking
# number1=99
# number2=22
#
# number1, number2 =(number2, number1)
#
# # Accessing Indices and Values Safely with built-in function enumerate
colors=['red','orange','yellow']
print(list(enumerate(colors)))

for index, value in enumerate(colors):
    print(f"{index}: {value}")


#Creating a primitive bar chart
numbers=[19,3,15,7,11,6,1]

print("\nCreating a bar chart from numbers: ")

print(f'Index{"Value":>8} Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*"*value }')


#Create the list names containing three name st