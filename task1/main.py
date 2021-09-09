# Дано: число N
# Требуется: Написать функцию, возвращающую все простые числа до N

def get_primes(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            primes.append(num)
    return primes


print(get_primes(int(input('Please enter a number: '))))

