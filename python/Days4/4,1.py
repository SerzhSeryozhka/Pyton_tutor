q=int(input('Введите балы через Enter'))
s=int(input('Введите балы через Enter'))
e=int(input('Введите балы через Enter'))
r=int(input('Введите балы через Enter'))
t=int(input('Введите балы через Enter'))
w=(s+q+e+r+t)/5
if w>=90:
    if s>=85 and q>=85 and e>=85 and r>=85 and t>=85:
        print(w,'Otlichno')
    else:
        print('Ocheny nhorosho')
elif w>=75:
    if s>=75 or q>=75 or e>=75 or r>=75 or t>=75:
        print(w,'Horosho')
    else:
        print(w,'Horosho s zamechaniem')
else:
    if q<50 or s<50 or e<50 or r<50 or t<50:
        print(w,'Neudovletvoritelno')
    else:
        print(w,'Udovletvoritelno')
