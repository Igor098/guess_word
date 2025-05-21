from random import choice, random

import requests
from unicodedata import category

from data import animals

def replace_char_at_index(original_string, indices, new_char):
    new_word = list(original_string)  # Преобразуем строку в список, чтобы можно было менять элементы
    for index in indices:
        if 0 <= index < len(new_word) and new_word[index] == '*':  # Дополнительная проверка
            new_word[index] = new_char  # Заменяем символ в списке
    return "".join(new_word)  # Преобразуем список обратно в строку


categories = requests.get("http://172.16.1.223:8000/v1/category/all")
category_object = categories.json()

r_cat = choice(category_object.get("categories"))

response = requests.get("http://172.16.1.223:8000/v1/word/random", params={"category": r_cat})
word_object = response.json()

print(word_object.get("tell"))
word = word_object.get("word").lower()
check = False

encrypted = '*' * len(word)

print(f'Загаданное слово: {encrypted}')
while check == False:
    answer = str(input("Ваш ответ: ")).upper()
    if len(answer) == 1:
        if answer in word:
            print(f"Буква {answer} есть в слове!")
            indexes = [i for i, letter in enumerate(word) if answer in letter]
            encrypted = replace_char_at_index(encrypted, indexes, answer)
            if "*" not in encrypted:
                print(f"Вы угадали, это {encrypted}")
                check = True
            else:
                print(f'Загаданное слово: {encrypted}')


        else:
            print(f"Буквы {answer} нет в слове!")
    elif answer == word:
        print(f"Вы угадали! Это {word}!")
        check = True

    else:
        print(f"Вы не угадали, это не {answer}. Попробуйте ещё раз")