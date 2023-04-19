userDigits = []
fourDigits = []

for i in range(0,4):
    digit = input("Please Enter A Digit: ")
    userDigits.append(digit)

    
for a in range(0,4):
    for b in range(0,4):
        for c in range(0,4):
            for d in range(0,4):
                if a!=b and b!=c and c!=d and a!=d and a!=c and b!= d:
                    print(userDigits[a]+userDigits[b]+userDigits[c]+userDigits[d])
