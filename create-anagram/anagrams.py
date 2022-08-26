import requests

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

text = response.content.decode('cp1251')

list_words = text.split("\n")
anagram_list = []

user_word = input("Введите слово, к которому вы хотите подобрать анаграму\n")
user_sorted_word = sorted(user_word)

for word in list_words:
    sorted_word = sorted(word)
    if sorted_word == user_sorted_word and user_word != word:
        anagram_list.append(word)


if len(anagram_list) < 1 :
    print("Вам нужен более крупный словарь, либо новое имя!")
else:
    print(*anagram_list, sep="\n")
