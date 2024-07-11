# # # -----Задача №1-----
# # age=int(input("Введите аозрост в годах: "))
# # if age>64:
# #     print('Полубог')
# # elif age>=18:
# #         print('Взрослый')
# # elif age>=13:
# #         print('Подросток')
# # elif age>=2:
# #         print('Ребёнок')
# # elif age>=0:
# #         print('Младенец')
# # else: age>=999 
# # print('Бессмертный')
# # # ------Задача №2-------
# import random
# # nekoe_chislo=random.randint(1,100)
# # if nekoe_chislo%2==0 and nekoe_chislo%3==0 and nekoe_chislo%5!=0:
# #        print(nekoe_chislo," Делется на 2, делется на 3 но не на 5")
# # elif nekoe_chislo%2==0 and nekoe_chislo%3==0 and nekoe_chislo%5==0:
# #        print(nekoe_chislo,' : Всё круто делится')
# # elif nekoe_chislo%5==0:
# #        print(nekoe_chislo,' :Делется на 5')
# # else:
# #       print(nekoe_chislo," :Не делится на 2,3 и 5")
# # ------Задача №3-------
# a=int(random.randint(1,5))
# # a=int(input("Введите целое число: "))
# if a%2==0:
#        print(a,' Чётное')
# else: print(a,' Нечётное')
# # ------Задача №4-------
# a=int(input("Введите колличество дней в году и узнайте весокостный он: "))
# if a%366==0:
#        print('да')
# elif a<365 or a>366:
#        print('ошибка')
# else: print(' Нет')
a=int(input("Введите год: "))
if a%4==0 and a%100!=0 and a%400:
       print('Високосный')
else: print("нет")
