# Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, 
# võrdhaarseteks ja võrdkülgseteks. Kirjutada programm, 
# mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena kolmnurga liigi. 
# Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab üldse eksisteerida. 
# Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

sideA = float(input('Sisesta esimese külje pikkus: '))
sideB = float(input('Sisesta teise külje pikkus: '))
sideC = float(input('Sisesta kolmanda külje pikkus: '))

if (sideA > sideB + sideC) or (sideB > sideA + sideC) or (sideC > sideA + sideB):
    print('Seliste külgedega ei saa moodustada kolmnurka.')
else:
    if (sideA == sideB) and (sideB == sideC) and (sideA == sideC):
        print('See kolmnurk on võrdkülgne.')
    elif (sideA == sideB) or (sideB == sideC) or (sideA == sideC):
        print('See kolmnurk on võrdhaarne.')
    else:
        print('See kolmnurk on erikülgne.')