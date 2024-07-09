# Задача №1
a='str'
b='oka'
print(a+b)
# Задача №2
print(len(a))
print(len(b))
print(len(a+b))
# Задача №3
srez='я пришел за вами'
srezal=srez[2:8]
print(srezal)
# Задача №4
n="erik@mail.ru"
m=n.split("@")
m=str(m)
m=m.replace('[','')
m=m.replace(']','')
m=m.replace("'",'')
m=m.split(".")
m=str(m)
m=m.replace('[','')
m=m.replace(']','')
m=m.replace("'",'')
print(m)