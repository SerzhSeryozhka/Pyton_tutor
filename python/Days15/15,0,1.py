# ______________Task_1_____________

def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_digit = False
    special_chars = "!@#$%^&*"
    has_special = False

    for c in password:
        if 'A' <= c <= 'Z':     # Длина не менее 8 символов
            has_upper = True
        if '0' <= c <= '9':     # Хотя бы 1 цифру
            has_digit = True
        if c in special_chars:  # Хотябы 1 спецсимвол из этих "!@#$%^&*"
            has_special = True

    return has_upper and has_digit and has_special      #Сложение результатов

# Примеры использования
print(validate_password("Password1!")) # True
print(validate_password("password1!")) # False
print(validate_password("Password!")) # False
print(validate_password("Password1")) # False
