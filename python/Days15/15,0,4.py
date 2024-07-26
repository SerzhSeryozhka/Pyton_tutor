# ______________Task_4_____________
# Подсчёт повторения елементов в строке
def char_frequency( strok):
    count_dikt = {}
    for w in strok:
        if w in count_dikt:
            count_dikt[w] += 1  #Запись в словарь
        else:
            count_dikt[w] = 1
    return count_dikt
# Примеры использования
print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(char_frequency("abracadabra"))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
