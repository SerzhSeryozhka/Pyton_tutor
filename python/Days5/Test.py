lst = [2,3,1,8,9,4,6,8,7]
minimum = lst[0]
maximum = lst[0]
print(maximum,minimum)
for i in lst:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print('max',maximum)
print('min',minimum)