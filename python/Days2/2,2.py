# Срез это начать перед первым индексом и закончить перед последнимю
my_str='Пример строки'
substring=my_str[1:4]
print(substring) #рим

subs=my_str[-5:-1]
print(subs) #трок

subm=my_str[0:9:2]
print(subm) #Пие т

substring = my_str[:5]
print(substring) #Приме

substring = my_str[5:]
print(substring) #р строки

substring = my_str[:]
print(substring) #Пример строки

substring = my_str[::-1]
print(substring) #икортс ремирП

for i in my_str[::2]:
    print(i)
#выведет пие тои построчно