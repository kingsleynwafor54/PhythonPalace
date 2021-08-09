sample = [[1, 2, 3], [1, 0, 0], [0, 2, 0], [1, 1, 1], [1, 2, 3]]
sample1 = sample[0]
sample2 = sample[1]
sample3 = sample[2]
sample4 = sample[3]
sample5 = sample[4]
sample.clear()
k=0
for count in sample1:

    k = count + k
if not (k == 3):
    sample.append(sample1)
x=0
for count in sample2:

    x = count+x
if not (x == 3):

    sample.append(sample2)

for count in sample3:
    k = 0
    k += count
if not (k == 3):
    # print(sample3)
    sample.append(sample3)
y=0
for count in sample4:

    y = count+y
if not (y == 3):
    # print(sample3)
    sample.append(sample4)

for count in sample5:

    k = count+k
    print(k)
if not (k == 3):
   sample.append(sample5)

print(sample)
