# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” 
# (ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

file_name = input('Sisesta faili nimi: ')

parts = file_name.split('.')

extension = parts[-1]

print('Faili laiend on: ' + extension)

