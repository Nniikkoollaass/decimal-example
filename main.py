#import datetime

#from decimal import *

#getcontext().prec = 6

#print(Decimal(1)/Decimal(7))

#print(Decimal(3.14))

#a = input("Рядок запрошення: ")

#x = 1111

#print(f"Значення x: {x}")

#print(f"Value x: {x+x}")

#print(bool(0))
#print(bool({}))
#print(bool(()))
#print(bool([]))
#print(bool(None))

#list_1 = ['1', '22', '33', '10', '45', '465', '']
#list_2 = ['a', 'b']
#list_1.extend(list_2)
#list_1.insert(0, '123')
#print(list_1)
#list_1.reverse()
#print(list_1)
#list_1.clear()
#print(len(list_1))

#dictionaty = {1: 123, 2: 456, 3: 789}
#dictionaty['lol'] = 'yey'
#del dictionaty[3]
#print(dictionaty)
#dictionaty[1] = 12321
#print(dictionaty[1])
#print(963 in dictionaty)
#print(dictionaty.pop(1))
#print(dictionaty)
#dictionaty.update({7: 78963258})
#print(dictionaty.get(77))

#my_set = set('hello')
#my_set_2 = {1, 2, 3, 4, 5, 5}
#print(my_set)
#print(my_set_2)
#list_1 = [1, 1, 2, 2, 2 , 11, 11]
#set_from_list = set(list_1)
#list_from_set = list(set_from_list)
#print(list_from_set)
#set_from_list.add(1111)
#print(set_from_list)
#set_from_list.discard(0)
#set_from_list.discard(1111)
#print(set_from_list)

#a = {1, 2 , 3}
#b = {3, 4 , 5}

#print(a & b)
#print(a.intersection(b))

#print(a - b)
#print(b.difference(a))
#print(a ^ b)
#print(a.symmetric_difference(b))

#print(a | b)
#print(a.union(b))

#s = "Hello world"
#s_upper = s.upper()
#print(s_upper)  # Виведе 'HELLO'
#print(s_upper.lower())
#print(s_upper)
#print(s_upper.startswith("H"))
#print(s_upper.endswith("O"))
#s_lower = s_upper.lower()
#s_capitalize = s_lower.capitalize()
#print(s_capitalize)
#s_title = s_lower.title()
#print(s_title)

#print("123".isdigit())  # True
#print("hello".isalpha())  # True
#print(" ".isspace())  # True

#name = 'Bob'
#print('Hello, {}'.format(name))

#age = 14
#print('Hello, {}. You are {} year old.'.format(name, age))
#print('Hello, {name}. You are {age} year old.'.format(name='Anna', age = 15))
#print('Hello, {1}. You are {0} years old.'.format(age, name))
#print(f'Hello, {name}, you are {age}')

#zriz = "My girlfriend"
#first_seven = zriz[:7]
#print(first_seven)

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#reverse_numbers = numbers[::-1]
#print(reverse_numbers)

#a = [1, 2, 3]
#b = a
#c = [1, 2, 3]

#print(a is b)  # True
#print(a is c)  # False

#num = int(input())
#if num % 3 == 0 and num % 5 == 0:
 #   print("FizzBuzz")
#elif num % 3 == 0:
 #   print("Fizz")
#elif num % 5 == 0:
 #   print("Buzz")
#else:
 #   print(num)

#x = y = 0
#if x >= 0:
 #   if y >= 0:  # x > 0, y > 0
  #      print("Перша чверть")
   # else:  # x > 0, y < 0
    #    print("Четверта чверть")
#else:
 #   if y >= 0:  # x < 0, y > 0
  #      print("Друга чверть")
   # else:  # x < 0, y < 0
    #    print("Третя чверть")

#some_good = False
#really = "Good" if some_good else "Bad"
#really_or = some_good or "Not at all"

#print(really)
#print(really_or)

#fruit = "xxx"
#match fruit:
 #   case "apple":
  #      print("This is an apple.")
   # case "banana":
    #    print("This is a banana.")
    #case "orange":
    #    print("This is an orange.")
    #case _:
    #    print("Unknown fruit.")

#some_point = (55, -1569)

#match some_point:
 #   case (0, 0):
  #      print('Точка в центрі координат')
   # case (0, y):
    #    print(f"Точка лежить на осі Y: y={y}")
    #case (x, 0):
     #   print(f"Точка лежить на осі Х: х={x}")
    #case (x, y):
    #    print(f"Точка має координати: x={x}, y={y}")
    #case _:
    #    print("Це не точка")

#colors = ["green", "white", "orange"]

#match colors:
 #   case ["green", "white", _]:
  #      print("There are green and white lights")
   # case ["white", _, _]:
    #    print("There is white light")
    #case _:
     #   print("it is darkness")

#alphabet = "qwertyuiopasdfghjklzxcvbnm"
#long = len(alphabet)
#count = 0
#for char in alphabet:
#    count += 1
#    if count == long:
#        print(char)
#        break
#    print(char, end="->")

#for i in range(55):
#    print(i, end="&")

#list_fruits = ["watermelon", "ananas", "bluberry", "kiwi"]
#states = ["old", "fresh", "new", "grren"]

#for index, value in enumerate(list_fruits):
   # print(index, value)
#for fruit, state in zip(list_fruits, states):
#    print(f"It is your {state} {fruit}, yummy ;)")

#yoyo = {
 #   "one": "Yep",
  #  "two": "Nope",
   # "three": "Just guess"
#}

#for key in yoyo.keys():
 #   print(key)

#for val in yoyo.values():
 #   print(val)

#for key, val in yoyo.items():
 #   print(f"Your digets: {key} - {val}")

#val = 'a'
#try:
#    val = int(val)
#except ValueError:
#    print(f"val {val} is not a number")
#else:
#    print(val > 0)
#finally:
#    print("This will be printed anyway")

#def some_some (a: int, b: int) -> int:
#    return 7

#def key_parameters (a: int, message-"Hello", b=10, c=8):
#    return message

#def real_cost(base: int, discount: int = 0) -> int:
#    return base * (1 - discount)

#price_bread = 15
#price_butter = 50
#price_sugar = 60

#current_price_bread = real_cost(price_bread)
#current_price_butter = real_cost(price_butter, 0.05)
#current_price_sugar = real_cost(price_sugar, 0.07)

#print(f'Нова вартість хліба: {current_price_bread}')
#print(f'Нова вартість масла: {current_price_butter}')
#print(f'Нова вартість цукру: {current_price_sugar}')

#def concatenate(*args) -> str:
#    result = ""
#    for arg in args:
#        result += arg
#    return result

#print(concatenate("Hello", " ", "world", "!"))

#def concatenate(*args) -> str:
#    result = " "
##    for arg in args:
 #       result += arg
 #   return result
#def concatenate(*args) -> str:
#    result = ""
#    for arg in args:
#        result += arg
#    return result

#print(concatenate("Hello", " ", "world", "!"))

#def greet(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

#greet(name="Alice", age=25)

# Факторіал числа
#def factorial(n) -> int:
#    return 1 if n == 0 else n*factorial(n-1)
#print(factorial(5))

#Числа Фібоначчі
#def fibonacci(n):
#    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
#print(fibonacci(10))

#def fibonacci(n):
#    if n <= 1: # базовий випадок
#        return n
#    else:
#        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок#

#print(fibonacci(10)) # виведе 55

#now = datetime.datetime.now()
#print(now)
#print(now.date())
#print(now.time())

# Створення об'єктів date і time
#date_part = datetime.date(2023, 12, 14)
#time_part = datetime.time(12, 30, 15)

# Комбінування дати і часу в один об'єкт datetime
#combined_datetime = datetime.datetime.combine(date_part, time_part)

#print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

# Створення об'єкта datetime з конкретною датою
#specific_date = datetime.datetime(year=2020, month=1, day=7)

#print(specific_date)  # Виведе "2020-01-07 00:00:00"

# Створення об'єкта datetime з конкретною датою і часом
#specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

#print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

# Створення об'єкта datetime
#now = datetime.now()

# Отримання номера дня тижня
#day_of_week = now.weekday()

# Поверне число від 0 (понеділок) до 6 (неділя)
#print(f"Сьогодні: {day_of_week}")  

#from datetime import timedelta
#delta = timedelta(
 #   days=50,
 #   seconds=27,
 #   microseconds=10,
 #   milliseconds=29000,
 #   minutes=5,
 #   hours=8,
 #   weeks=2
#)
#print(delta)

#from datetime import datetime, timedelta

#now = datetime.now()
#future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
#print(future_date)
#print(future_date.toordinal())

# homework 1 - 10- 15
#name = input("Your name? ")
#email = input("Your email? ")
#age = int(input("Your age? "))
#height = float(input("Your height? "))
#is_active = True if input("Do you want get messages from the website? Please, enter nothing nothig if you don't want to.") else False

cat = {}
info = {"status": "vaccinated", "breed": True}
cat["nick"] = "Marsik"
cat["age"] = 7
cat["characteristics"] = ["kind", "beautiful"]

age = cat.get("age")

cat.update(info)

print(cat)
print(age = " ")



print(age)