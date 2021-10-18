def fibonacci_number(x):
    a = 1
    b = 1
    for _ in range(x-1):
        c = a + b
        a = b
        b = c
    return b


fibonacci_list = []
for i in range(10):
    fibonacci_list.append(fibonacci_number(i))
print(fibonacci_list)
