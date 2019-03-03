from random import randint

words = ['самовар', 'весна', 'лето']
word = words[randint(0, 2)]
letter = randint(0, len(word) - 1)
print(word[:letter] + '?' + word[letter + 1:])
if input('Введите букву: ') == word[letter]:
    print('Победа!\n', 'Слово: ', word, sep='')
else:
    print('Увы! Попробуйте в другой раз.\n', 'Слово: ', word, sep='')