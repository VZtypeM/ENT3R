def fibonacci_list(x):
    if x == 0:
        return []
    if x == 1:
        return [1]

    fibonacci_numbers = [1, 1]

    for _ in range(x-2):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

    return fibonacci_numbers


print(fibonacci_list(20))
