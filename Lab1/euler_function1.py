def euler_phi(n):
    count = 0
    # Находим НОД между всеми числами от 1 до n
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input("Введите начение n: "))
    euler = euler_phi(n)
    print(f"Значение функции Эйлера для числа {n} = {euler}")
