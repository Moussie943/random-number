import random
number = random.randint(0, 5)
print("Попробуй угадать число от 0 до 5!")
user_number = int(input("Введи число: "))

attempts = 0
while user_number != number and attempts < 3:
    print("Не угадал")
    user_number = int(input("Введи число: "))
    attempts += 1

if user_number == number :
   print(f"Это верно, я загадал число {user_number}")
   print("Ты выиграл")
else :
   print("Ты проиграл")
