from collections import deque

def is_palindrome(s):
    # Видалити пробіли та привести до нижнього регістру
    s = ''.join(s.split()).lower()
    
    # Створити двосторонню чергу
    char_deque = deque(s)
    
    # Порівнювати символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестові приклади
test_strings = [
    "hello",
    "зараз",
    "Was it a car or a cat I saw",
    "Гарна погода!"
]

for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' -> {result}")