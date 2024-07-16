user=int(input('Возраст: '))
stud=input('Есть ли у вас студенческий (да/нет): ').upper()
poisk='ДА'
a=stud.find(poisk)
if user<18:
    if a==0:
        print('Стоимость: 5')
    else:
        print('Стоимость: 20')
elif user>18 and user<60:
    if a==0:
        print('Стоимость: 12')
    else:
        print('Стоимость: 40')
else:
    if a==0:
        print('Стоимость: 99')
    else:
        print('Стоимость: 999')