tre=[1,2,3,4,5,6,7,8,9]
q=0
for i in tre:
    if i%2==0:    
        q+=i
print(q)
# --------
numbers = [int(input()) for i in range(int(input()))]
sum_even = sum(num for num in numbers if num % 2 == 0)
print(sum_even)