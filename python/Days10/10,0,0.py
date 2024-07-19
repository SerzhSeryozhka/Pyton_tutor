c,z,x=0,0,0
print("Введите 'quit' для завершения")
while True:
    c = input("Введите число (или 'quit' для завершения): ")
    if c=='quit':
        break
    if z <= 2:
        if z < 2:
            if z < 1:
                q = int(c)
            elif z < 2:
                w = int(c)
            z += 1
        else:
            # c=input("Введите знак операции (или 'quit' для завершения): ")
            if c=='+':
                x= q+w
            elif c =='-':
                x= q-w
            elif c =='*':
                x=q*w
            elif c == '/':
                x= q/w
            z=0
            print(x)
# # Калькулятор двух чисел
# a = input("Введите знак операции, число (или 'quit' для завершения):  ")
# if a=="*" or a=="/" or a=="+" or a=="-":
#     q
# else:
#     z=