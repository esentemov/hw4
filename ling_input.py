import random

print("Сейчас можно будет ввести слова в наш словарик")
print("Если хотите остановить ввод слов, напишите stop в английском")

slovar = {}

while True:
    key = input("Введите слово на английском:\n")
    if key == 'stop':
        break
    value = input("Введите слово на русском:\n")
    slovar[key] = value

print(slovar)
print("Пора потренироваться, ошибок у нас не более 3")
# randword = random.choice(list(slovar.keys()))
# print(randword)

errors = 0
bonus = 0

# for keys in slovar.keys():
for key in random.sample(slovar.keys(), len(slovar)):
    print('Введите значение слова: ' + key)
    answer = input("Вы считаете, что это слово переводится как ").lower().strip()
    if slovar[key] == answer:
        bonus += 1
        print("Отлично, ваш счет составляет :", bonus)
    elif errors > 2:
        print("game over")
        break
    else:
        errors += 1
        print("Правильное слово было: ", slovar[key])
        print("Количество ошибок", errors)
