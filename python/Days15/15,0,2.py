# ______________Task_2_____________

def is_palindrome (numb):
    if str(numb) == str(numb)[::-1]:
        return True
    else:
        return False
print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
print(is_palindrome(1221)) # True
print(is_palindrome(-121)) # False
