digits = '1122'
result = int()

for i, d in enumerate(digits):

    ni = (i+1) % len(digits)
    n = digits[ni]

    if d == n:
        result += int(d)
        
 
print('Tulemus: ', result)
