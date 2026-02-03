bottom = 2
top = 1
tri_num_list = [1]
for i in range(1,100000):
    tri_num_list.append(top + bottom)
    top = top + bottom
    bottom += 1
    count = 0
    for j in range(1, int(top**0.5) + 1):
        if (top) % j == 0:
            if j * j != top:
                count += 2
            else:
                count += 1


    if count > 500:
        print(top)
        break

# print(tri_num_list)