# НОД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# функция Эйлера
def euler_phi(n):
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
        p += 1
    if n > 1:
        result *= (n - 1)
        result //= n

    return result

def congruence(a, b, m):
    d = gcd(a, m)

    if b % d != 0:
        return "Решение не существует, так как b не делится на НОД(a, m)"

    # Упрощаем сравнение разделив его на НОД
    a //= d
    b //= d
    m //= d

    if gcd(a, m) != 1:
        return "Решение не существует, так как a и m не взаимно просты после упрощения"

    # Вычисляем x = a^(ϕ(m)-1) * b по модулю m
    phi_m = euler_phi(m)
    a_inv = pow(a, phi_m - 1, m)
    x = (a_inv * b) % m
    return x

if __name__ == "__main__":
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    m = int(input("Введите m: "))

    solution = congruence(a, b, m)
    print("Решение сравнения:", solution)
