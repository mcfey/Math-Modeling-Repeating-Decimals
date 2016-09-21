num = int(input("Numerator: "))   
d = int(input("Denominator: "))

n = 9                               
print(num / d)                      
                
for a in list(range(1, 10)):        
    if 10**a*(num/d) % 1 == 0:       
        n = 10**a
        break
   
else:
    for x in list(range(1, 50)):
        if n % d == 0:
            break
        else: 
            for y in list(range(1, 10)):
                if n*10**y % d ==0:
                    n = n*10**y
                    break
            else:
                n = 9 + 10*n


print(n)

nstring = str(n)
nonrepeats = n.count(0)
repeats = nstring.count(9)

Print("Nonrepeating decimals:" + nonrepeats)
Print("Repeating decimals:" + repeats)





 