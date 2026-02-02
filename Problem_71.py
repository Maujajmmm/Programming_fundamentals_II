import math
list_fractions = []
for d in range(2,1000000):
    for n in range((3*d)//7 - 1, (3*d)//7 + 1):
        if not n <= 0:
            if math.gcd(n,d) == 1:
                list_fractions.append([n,d])
x = [1, 10]
for i in list_fractions:
    if (i[0]/i[1]) < 3/7:
        if i[0]/i[1] > x[0]/x[1]:
            x = i
print(x)
