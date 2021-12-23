our_dictionary={
    "one": "buckle my shoes",
    "two":"knock at the door",
    'three':"pick up sticks",
    'four':"lay them straigh"
}

print(our_dictionary)

our_dictionary["five"]="a big fat head"
print(our_dictionary)
for x in our_dictionary:
    print(x+":"+our_dictionary[x])

for x in our_dictionary.values():
    print(x)
for x,y in our_dictionary.items():
    print(x,y)

num=[2,2,3,5,2,3,1,0,5]
dic={}

# for x in num:
#     if x in dic:
#         count=dic[x]
#     else:
#         count = 0
#     dic[x]=count+1

# for  key,value in dic.items():
#     print(key,value)
# print(dic)

for y in num:
    if y in dic:
        dic[y]+=1
    else:
        dic[y]=1
print(dic)

text=('this is sample text with several words '
      'this is more sample text with some different words')

word_counts={}

for word in text.split():
    # update existing key-value pair
    if word in word_counts:
        word_counts[word]+=1
    else:
        # insert new key-value pair
        word_counts[word]=1
print (f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

from collections import Counter

text=('this is sample text with several words '
      'this is more sample text with some different words')

counter=Counter(text.split())
print(counter)

for x, count in sorted(counter.items()):
    print(f'{x:<12}{count}')

# roll dice
import random
numbers=[random.randrange(1,7)for i in range(100)]
from collections import Counter
counter=Counter(numbers)
for value, count in sorted(counter.items()):
  print(f'{value:<4}{count}')