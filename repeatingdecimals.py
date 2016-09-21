num = int(input("Numerator: "))
d = int(input("Denominator: "))

n = 9

while d % n != 0 or d % n*10 != 0:
    n = 9 + 10*n 
    
print(num / d)
print(n)
