# Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta number.
# Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.


aasta = int(input('Sisesta aasta: '))

def liigAsta(aasta):
    
    if (aasta % 400 == 0) or (aasta % 4 == 0 and aasta % 100 != 0):
        return ('Liigaasta')
    else:
        return ('Lihtaasta')
    