a_set={23,34,55,67,89,98,176,78,90}
highest_num=0
for item in a_set:
    if item >highest_num:
        highest_num=item
print(highest_num)

a_list=[1,2,3,5,4,6,7,3,9,2]
# for index,value in range(len(a_list)):
for index, value in enumerate(a_list):
    print(f'{index:>5}{value:>8} {"*" * value}')

read_file=open("file.txt")
for line in read_file:
    print(line)