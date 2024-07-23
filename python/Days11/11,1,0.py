# # ___________Task_1__________

# def is_even(a):
#     return a%2==0
# print(is_even(4))  # True
# print(is_even(7))  # False
# print(is_even(0))  # True
# print(is_even(-2)) # True
# print(is_even(-3)) # False

# # ___________Task_2__________

# def maxs(a,c,d):
#     if a>=c and a>=d:
#         return a
#     elif c>=a and c>=d:
#         return c
#     else:
#         return d
    
# def max_of_three(q,a,z):
#     return max(q,a,z)
# print(maxs(3, 7, 5))  # 7
# print(maxs(10, 10, 10))  # 10
# print(maxs(-5, 0, -2))  # 0
# print(max_of_three(3, 7, 5))  # 7
# print(max_of_three(10, 10, 10))  # 10
# print(max_of_three(-5, 0, -2))  # 0

# # ___________Task_3__________

# def reverse_string(q):
#     return q[::-1]
# print(reverse_string("hello"))  # "olleh"
# print(reverse_string("Python"))  # "nohtyP"
# print(reverse_string("12345"))  # "54321"

# # ___________Task_4__________

# def sg (w):
#     q = 0
#     a ='aeyuioйуеёыаоэяию'
#     for i in w:
#         if i in a:
#             q+=1
#     return q
# s = input()
# print(sg(s))

# ___________Task_4__________

def gen_tab(a):
    int(a)
    q=0
    for i in range(1,11):
        print(f'{a} x {q} = {a*q}' )
        q+=1
gen_tab(2)
gen_tab(9)