# # -----Задача №1------
# q=input("Напиши что-то: ")
# if len(q)<5:
#     print(len(q),'сообщение длина меньше 5')
# elif len(q)<10:
#     print(len(q),'длина от 5 до 10')
# elif len(q)>10:
#     print(len(q),'строка больше 10 символов')
# # -----Задача №2------
# q=input("Напиши что-то: ")
# q=q.split()
# if len(q)>0:
#     print('Есть подстроки разбитые пробелом.')
# -----Задача №3------
# q=input("Напиши что-то: ")
# if '?' in q:
#     q=q.split('?',2)
#     print('знаки удалены "?"','строка без знаков',q)
# else: 
#     print('знаков не было "?" ','введённая строка: ',q)
# -----Задача №4 ------
w='Team Spirit'
e='Team Falcons'
if len(w)>len(e):
    print('Win: Team Spirit')
else:
    print('Win: Team Falcons')