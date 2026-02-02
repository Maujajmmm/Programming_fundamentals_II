def sum_of_squares(n):
    result = 0
    for i in range(n+1):
        result += i**2
    return result
def square_of_sum(n):
    result = 0
    for i in range(n+1):
        result += i
    result = result ** 2
    return result
print(square_of_sum(100)-sum_of_squares(100))