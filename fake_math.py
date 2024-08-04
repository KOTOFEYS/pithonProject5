def divide(first, second):
    if second == 0:
        return 'Ошибка'
    return first / second
    divide(first, second)


result1 = divide(69, 3)
result2 = divide(3, 0)
print(result1)
print(result2)