power = 1000
result = 2**power
list_result = list(str(result))
count = 0
for i in list_result:
    count += int(i)
print(count)