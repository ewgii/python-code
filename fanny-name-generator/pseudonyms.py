import sys, random

print("Добро пожаловать в игру 'Генератор дурацких имен'")
print("Имена, состоят из двух слов. Первое слово - это погода плюс часть тела")
print("Фамилии состоят из слов, образованных из чувств и эмоций людей")

first =  ('Яснозуб', 'Пасмурнорот', 'Дождливоглаз', 'Солнечноух', 'Ветрошей', 'Штиленос')
last = ('Смехов', 'Улыбков', 'Плаксин', 'Завидовов', 'Рассержанов', 'Задумчивов')

while True:
    first_name = random.choice(first)
    last_name = random.choice(last)
    print("{} {}".format(first_name, last_name), file=sys.stderr)
    try_again = input("Попробовать еще? (Нажмите Enter, либо 'n', чтобы выйти)\n")
    if try_again.lower() == "n":
        break