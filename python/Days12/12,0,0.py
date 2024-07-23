# # # # Написать функцию, которая пишет текст в центре прямоугольной рамки (из символов #)
# # # # В качестве входных параметров - выводимый текст, ширина и высота прямоугольной рамки
# # # #
# # # # Пример:
# # # #
# # # #   > print_in_box("Hello, World!", 17, 5)
# # # #
# # # #   #################
# # # #   #               #
# # # #   # Hello, World! #
# # # #   #               #
# # # #   #################

# # def word_in_box(text,width, height):
# #      if len(text) > width - 2:
# #         print ("Текст не помещается")
# #      else: 
# #          horizontal_border = "#" * width
# #          vertical_border = "#" + "| |" * (width - 2) + "#"
# def is_lucky_number(e):
#     e=str(e)
#     l = len(e)
#     c = l/2
#     lef_ch = e[:c]
#     rit_ch = e[c:]
#     if l%2!=0:
#         lef_ch = e[:c+1]
        
#         return e
# print(is_lucky_number(1236))  # False, так как 12 и 36 оба делятся на 2
# print(is_lucky_number(1234))  # False, так как 12 и 34 оба делятся на 2
# print(is_lucky_number(1230))  # True, так как 12 и 30 оба делятся на 2


def equality(Baza):
    Baza = {}
    i=0
    while i<2:
        cur1= input("Код валюты ")
        cur2 = input('Номинал ')
        Baza = {cur1:cur2}
        i+=1
        print(Baza)
print(equality)