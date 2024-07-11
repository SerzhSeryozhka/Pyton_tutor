# q=5
# w=0
# while q>w:
#     r=int(input("Введите число: "))
#     w+=1
#     r+=r
#     e=r/5
#     if e>=90:
#         if r>=85:
#             print(e,"Otlichno")
#         else:
#          print('Ocheny nhorosho')
#     elif e>=75:
#         if r>=75:
#           print(e,'Horosho')
#         else:
#             print(e,'Horosho s zamechaniem')
#     else:
#         if r<50:
#             print(e,'Neudovletvoritelno')
#         else:
#             print(e,'Udovletvoritelno')
#     print(e)
# Программа для определения стоимости билета на киносеанс

# Пользователь вводит возраст
age = int(input("Введите ваш возраст: "))

# Пользователь отвечает на вопрос о наличии студенческого билета
student_ticket = input("Есть ли у вас студенческий билет? (да/нет): ").lower()

# Расчет стоимости билета
if age < 18:
    if student_ticket == "да":
        price = 5
    else:
        price = 20
elif 18 <= age < 60:
    if student_ticket == "да":
        price = 12
    else:
        price = 40
else:
    if student_ticket == "да":
        price = 99
    else:
        price = 999

print(f"Стоимость билета составляет: {price}")