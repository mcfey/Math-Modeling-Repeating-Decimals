num = int(input("Numerator: "))
d = int(input("Denominator: "))

n = 9
print(num / d)


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
#else:  
    #n = 9
    #for x in list(range(1, 50)):
        #for x in list(range(1, 20)):
            #if (n* (10*x)) % d == 0:
                #n = (10*x)*n
                #break
        #else: 
            #n = 9 + 10*n

print(n)

repeats = len(str(n))

print( "Repeating numbers" + repeats)



#once top part works, put number n into a list with all its digits
#sort to tell how many zeros, how many nines
#will give number of repeating digits (# of nines), # of 0 = non repeating 