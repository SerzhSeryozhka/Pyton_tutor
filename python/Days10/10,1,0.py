# Перевод чисел с римского на арабский.


def rom_to_arb(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for c in s:
        value = roman[c]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value

    return result

# Использование функции
print ("Переводчик римских чисел: ")
while True:
    e = input ("Введите римское число или 'quit' для завершения: ")
    if e =='quit':
        break
    while e!='quit':
        print (f"Арабское число = {rom_to_arb(e)}")
        break

# roman_num = "LDXIVI"
# arabic_num = rom_to_arb(roman_num)
# print(arabic_num)
