def fibonacci_number(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return fibonacci_number(x-1) + fibonacci_number(x-2)


fibonacci_numbers = []
for i in range(20):
    fibonacci_numbers.append(fibonacci_number(i))
print(fibonacci_numbers)
