# # -----Задача №1-----
# age=int(input("Введите аозрост в годах: "))
# if age>64:
#     print('Полубог')
# elif age>=18:
#         print('Взрослый')
# elif age>=13:
#         print('Подросток')
# elif age>=2:
#         print('Ребёнок')
# elif age>=0:
#         print('Младенец')
# else: age>=999 
# print('Бессмертный')
# ------Задача №2-------
import random
nekoe_chislo=random.randint(1,100)
if nekoe_chislo%2==0 and nekoe_chislo%3==0 and nekoe_chislo%5!=0:
       print(nekoe_chislo," Делется на 2, делется на 3 но не на 5")
elif nekoe_chislo%2==0 and nekoe_chislo%3==0 and nekoe_chislo%5==0:
       print(nekoe_chislo,' : Всё круто делится')
elif nekoe_chislo%5==0:
       print(nekoe_chislo,' :Делется на 5')
else:
      print(nekoe_chislo," :Не делится на 2,3 и 5")