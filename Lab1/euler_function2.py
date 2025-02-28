def euler_phi(n):
    if n == 1:
        return 1

    result = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            # убираем текущее p из n
            while n % p == 0:
                n //= p
            # вычисляем n * (1 - 1/p)
            result *= (p - 1)
            result //= p
        # прибавляем 1, чтобы пройти найти все простые множители
        p += 1

    # если остался простой делитель больше 1
    if n > 1:
        result *= (n - 1)
        result //= n

    return result

if __name__ == "__main__":
    n = int(input("Введите начение n: "))
    euler = euler_phi(n)
    print(f"Значение функции Эйлера для числа {n} = {euler}")
