# number_str =input("Number:")
# the_sum=0
# counter = 0
# while counter<=2:
#     number=int(number_str)
#     if number%2==0:
#         print("you head")
#     else:
#         print("this number is not an even number")
#         continue
#         counter+=1



def average(nums):
    total=sum(nums)
    size=len(nums)
    average =total/size
    return average

score=[56,67,67,45,34,45]
avg_score=average(score)
print(avg_score)
