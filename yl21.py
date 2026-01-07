# yl21
# Arvu arvamise mäng. 
# Arvuti mõtleb välja arvu nullist sajani.
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)

import random
 
random_num = int(random.randint(0, 100))

player_num = int(input('Sisesta oma number, et võita 0 - 100: '))

if player_num == random_num:
    print('Saa võitsid, number oli', random_num)

else: 
    print('Sa kaotasid, number oli', random_num)