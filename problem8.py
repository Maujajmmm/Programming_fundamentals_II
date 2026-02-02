factors = {} #this keeps track of how many of each prime factor is in final number
prime_list = []
num_range = 20
for i in range(2, num_range): #Creates a list of prime numbers
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
    if is_prime:
        prime_list.append(i)
for i in range(1, num_range): #going through all numbers that will be factors
    for j in prime_list: #looping through prime numbers and eventually find all prime factors of i
        if i%j == 0:
            count = 0
            k = i #dummy variable
            while True: #now checking how many of j is in i
                k = k/j
                count += 1
                if not k%j == 0:
                    break
            if j in factors: #if this i has more j than a prior check, then add that to the dictionary
                if count > factors[j]:
                    factors[j] = count

            else: #if this is the first appearance of j in i then just add it to dictionary
                factors[j] = count
product = 1
for i in factors: #now finding product
    product = product * i ** factors[i]
print(factors)
print(product)