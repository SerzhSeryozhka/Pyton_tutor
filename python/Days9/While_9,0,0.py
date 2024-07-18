'''# ________________________Task_1____________________________________

tar_a = 100000
deposit = 5000
p_of_i = 0.01
step = 0
chek = 0
while step<tar_a:
    step+=deposit
    step+=step*p_of_i
    chek+=1
print(f' Для накопления {tar_a} необходимо {chek} месяцев, итого: {step}')'''
'''# ________________________Task_1____________________________________

cel = 105000
ezhednevno = 6500
schet = 0
step = 0
while step<cel:
    step+=ezhednevno
    schet+=1
print(f"Для достижения - {cel}, потребуется - {schet}, итого - {step}")'''
'''# ________________________Task_2____________________________________
import random
w_sum = 1880000

step = 0
days = 0
while step < w_sum:
    pers_1 =random.randint(2000,5000)
    pers_2 =random.randint(3000,8000)
    pers_3 =random.randint(1000,15000)
    pers_4 =random.randint(20000,50000)
    pers_5 =random.randint(12000,30000)
    step += (pers_1+pers_2+pers_3+pers_4+pers_5)
    days +=1
print (f"Для достижения - {w_sum}, потребуется - {days}, итого - {step}")'''
'''# ________________________Task_3____________________________________

catalog = ['book1', 'book2', 'book3', 'book4', 'book5']  # Каталог книг
borrowed_books = set()  # Множество взятых книг
users = {}  # Словарь пользователей и их взятых книг
# Симуляция работы библиотеки
days_passed = 0
events = [
   {'action': 'borrow', 'user': 'Alice', 'book': 'book1'},
   {'action': 'borrow', 'user': 'Bob', 'book': 'book2'},
   {'action': 'return', 'user': 'Alice', 'book': 'book1'},
   {'action': 'borrow', 'user': 'Alice', 'book': 'book3'},
   {'action': 'borrow', 'user': 'Charlie', 'book': 'book1'},
   {'action': 'return', 'user': 'Bob', 'book': 'book2'},
   {'action': 'borrow', 'user': 'Charlie', 'book': 'book5'},
]
import random

catalog = ['book1', 'book2', 'book3', 'book4', 'book5']  # Каталог книг
borrowed_books = set()  # Множество взятых книг
users = {}  # Словарь пользователей и их взятых книг
events = [
   {'action': 'borrow', 'user': 'Alice', 'book': 'book1'},
   {'action': 'borrow', 'user': 'Bob', 'book': 'book2'},
   {'action': 'return', 'user': 'Alice', 'book': 'book1'},
   {'action': 'borrow', 'user': 'Alice', 'book': 'book3'},
   {'action': 'borrow', 'user': 'Charlie', 'book': 'book1'},
   {'action': 'return', 'user': 'Bob', 'book': 'book2'},
   {'action': 'borrow', 'user': 'Charlie', 'book': 'book5'},
]

def simulate_library(days):
    for day in range(days):
        if random.random() < (day / 100):  # Случайное пополнение events в зависимости от роста days_passed
            action = random.choice(['borrow', 'return'])
            user = random.choice(['Alice', 'Bob', 'Charlie'])
            book = random.choice(catalog)
            events.append({'action': action, 'user': user, 'book': book})

simulate_library(days_passed)  # Вызов функции для симуляции работы библиотеки

# Вывод результатов events
for event in events:
    print(event)'''
# ________________________Task_4____________________________________

'''s=[]
c=0
while c<10:
    u = input('ввести число ')
    s.append(int(u))
    c+=1
ss=[]
SS=[]
for i in s:
    if i%2==0:
        ss.append(i)
    # else:
    #     SS.append(i)
print(ss)
# print(SS)'''
# ________________________Task_4____________________________________

l1 = [1,2,4]
l2 = [1,3,4]
