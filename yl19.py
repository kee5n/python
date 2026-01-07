# Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv.

text = input('Sisesta tekst: ').lower()

# letters = 'aeiouõäüö'

# def letters_counter(word):
#     counter = 0
#     for i in letters :
#         if i in word :
#             counter += 1
#     return counter

# print(letters_counter(text))

letters = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü']

count = sum(1 for l in text if l in letters)
print(count)