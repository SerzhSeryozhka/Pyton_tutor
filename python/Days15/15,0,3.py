# ______________Task_3_____________
def count_unique_words (str):
     return len(set(str.split())) 
# Примеры использования
print(count_unique_words("Hello world Hello"))  # 2
print(count_unique_words("This is a test This is only a test"))  # 5

