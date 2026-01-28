length_list = []
for i in range(1, 1000000):
    count = 0
    x = i
    check = True
    while check:
        if x == 1:
            length_list.append(count)
            check = False
        if x%2 == 0:
            x = x//2
        else:
            x = 3*x+1
        count += 1
print(length_list.index(max(length_list)))
