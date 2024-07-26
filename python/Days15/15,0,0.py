# ______________Task_1_____________

def validate_password (trusher_password):
    spisok_Zaglav=[]
    spisok_cifr=[]
    spisok_simvolov=[]
    tr_pas1 = trusher_password.upper()
    tr_pas= list(trusher_password) 
    num = '1234567890'
    simb = "!@#$%^&*"
    sp_pas = ''
    for t in trusher_password:
        for g in num: 
            for v in simb:
                if t != g :
                    sp_pas += t
                    t+=1
    print(sp_pas)
# Длина не менее 8 символов
    if len(trusher_password)>=8:
# Хотя бы 1 заглавная
        for i in tr_pas1:
            for j in tr_pas:
                if i == j:
                    spisok_Zaglav.append(i)
                    if len(spisok_Zaglav)!=0:
# Хотя бы 1 цифру
                        for u in trusher_password:
                            for y in '1234567890':
                                if u ==y:
                                    spisok_cifr.append(u)
                                    if len(spisok_cifr)!=0:
# Хотябы 1 спецсимвол из этих "!@#$%^&*"
                                        for  w in trusher_password:
                                            for e in "!@#$%^&*":
                                                if w == e:
                                                    spisok_simvolov.append(w)
                                                    if len(spisok_simvolov)!=0:
                                                        return True
                                                    else:
                                                        return False
                                    else:
                                        return False
                        else:
                            return False
# Проверка корректности ввода пароля.
# Написать функцию. которая принимает строку(пароль) и проверяет его на соответствие следующим условиям.

# Примеры использования
print(validate_password("Password1!"))  # True
print(validate_password("password1!"))  # False
print(validate_password("Password!"))   # False
print(validate_password("Password1"))   # False
