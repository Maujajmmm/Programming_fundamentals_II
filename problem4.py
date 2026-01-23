pal_list = {}
for i in range(100,1000):
    for j in range(100,1000):
        k = str(i * j)
        if k == k[::-1]:
            pal_list[k] = [i,j]
print(max(pal_list))
print(pal_list[max((pal_list))])
