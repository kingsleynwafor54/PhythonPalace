data=( "red","green","blue","pink","brown","brown")
# Tuple fetching Items
# print(data[0:5])
# for x in range(len(data)):
#     print(data[x])s
# add element to a list
a_list=list(data)
# using insert
a_list.insert(3,'violet')
a_list.append("white")
b_tuple=(a_list)
data=tuple(a_list)


print(data)
print(a_list)
print("Printing a new tuple")
print(data)


c_tuple=(10,20,30,40,50)
sum=0
for x in c_tuple:
  sum+=x
print(sum)