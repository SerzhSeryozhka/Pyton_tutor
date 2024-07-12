# # ----------Task 1
# tre=[2,1,3,4,6,9,5,8,7]
# q = tre[0]
# for i in tre:
#     if q>i:
#         q=i
#     if q<i:
#         q=i
# print("min: ",q)
# print("max: ",q)
# #  ---------Task 2
# import random
# tre=[random.randint(10,100)]
# print (tre)
# q=0
# for i in tre:
#     q+=i
# print(q/len(tre))
# # --------Task 3
# str= input("Введите текст: ")
# strk=str.lower().split()
# unique_str = list(set(strk))
# print(unique_str)
# # --------Task 4 ------------------------------
# from collections import Counter
# emails = ["личное", "работа", "работа", "важное", "реклама", "личное", "работа"]

# # for email in emails:
#     # if email 
# word_counter = Counter(emails)# Счетчик повторяющихся слов
# unique_words = list(set(emails))
# print("Уникальные слова: ")
# for word in unique_words:
#     print(word)
# print("Слова и их количество: ")
# for word, count in word_counter.items():
#     print(word + ":", count)
# -------Task 5---------------------------
str=input()
strk=str.lower().split()
skok=list(set(strk))
count=[0]*len(skok)
for st in str:
    if st in skok:
        ind=skok.index(str)
        count[ind]+=1
print(skok, ":", count)