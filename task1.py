import queue
import random
import time

# Створити чергу заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    request_id = random.randint(1000, 9999)  # Генерація унікального номера заявки
    request_queue.put(request_id)  # Додавання заявки до черги
    print(f"Заявку зареєстровано в черзі з номером: {request_id}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        request_id = request_queue.get()  # Видалення заявки з черги
        print(f"Заявку {request_id} опрацьовано")
        # Імітація обробки заявки (затримка на 1 секунду)
        time.sleep(1)
    else:
        print("Наразі немає заявок на опрацювання. Черга порожня.")

# Головний цикл програми
def main():
    while True:
        user_input = input("Введіть 'почати', щоб створити нову заявку, 'перейти' для передачі заявки на опрацювання, або 'вийти' для виходу з черги:   ").strip().lower()
        
        if user_input == 'почати':
            generate_request()
        elif user_input == 'перейти':
            process_request()
        elif user_input == 'вийти':
            print("Роботу з програмою завершено.")
            break
        else:
            print("Невірна команда. Будь ласка, введіть 'почати', 'перейти', або 'вийти'.")

if __name__ == "__main__":
    main()