value = [1,4,3,2,6,7,5,9,10];

oddList = []
evenList = []
counter=0;
for counter in range (len(value)):
 if counter%2==1:
    oddList.append(counter)
 else:
    evenList.append(counter)



number1= sorted(evenList)
number2=sorted(oddList);


number1.extend(number2)
print(number1)

