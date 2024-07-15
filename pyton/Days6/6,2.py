list1 = [1,2,2,3,4]
list2 = [2,2,3,5]
q=set(list1)
w=set(list2)
e=[]
for i in w:
    for l in q:
        if i==l:
            e.append(i)
print(f"Уник1: {q}, уник2: {w},общь. уник: {e}")
# _________________________________________________
c = list(set(list1) & set(list2))
r = list(q & w)
print(c, r)