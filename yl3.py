# yl3
# Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9.
# Arvuta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, 
# siis on vaja väljastada tulemus 2 + 	22 + 222 = 246). Ära kasuta korrutamistehet.
# Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

n = (input('Sisesta number 1-9: '))

a = n + n
b = n + n + n

c = int(n)
d = int(a)
e = int(b)
f = int(c + d + e)

print(c, '+', d, '+', e, '=', f)


# Õpetaja

