num = int(input("Numerator: "))
d = int(input("Denominator: "))

n = 9
print(num / d)


for x in list(range(1, 50)):
    if n % d == 0:
        break 
    if (n*10) % d == 0:
        n = 10*n
        break
    else:
        n = 9 + 10*n

print(n)

#once top part works, put number n into a list with all its digits
#sort to tell how many zeros, how many nines
#will give number of repeating digits (# of nines), # of 0 = non repeating 