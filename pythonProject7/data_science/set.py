a_set={45,True,"burger",34.90}

print(type(a_set))


for item in a_set:
    print(item)
# checking if an item exist in a set
print("cake" in a_set)
print("burger" in a_set)


a_set.add("rice")
print(a_set)
a_set.discard(True)
print(a_set)
a_set.discard(False)
a_set.remove(45)
print(a_set)

a_set.pop()
print(a_set)
a_set.clear()
print(a_set)
print(len(a_set))