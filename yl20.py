# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
# 8 x 0 = 0
# 	8 x 1 = 8
# 	8 x 2 = 16
# 	…
# 	8 x 12 = 96
# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

num = 12

x_num = int(input('Sisesta arv: '))

for i in range(0, num + 1):
    ans = (i * x_num)
    print(i, 'x', x_num, '=', ans)


