num = int(input("Numerator: "))
d = int(input("Denominator: "))

n = 9
print(num / d)

#while d % n != 0 or d % n*10 != 0:
    #n = 9 + 10*n 

if d % n != 0 or d % n*10 != 0:
    n = 9 + 10*9

print(n)

