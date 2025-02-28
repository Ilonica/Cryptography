import math

# проверка на простоту
def is_prime(n):
    if n < 2:
        return False
    # у любого составного числа есть собственный делитель, не превосходящий квадратного корня из числа.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_primitive_root(g, m):
    # проверяем, что g^{m-1} ≡ 1 mod m
    if pow(g, m - 1, m) != 1:
        return False

    # проверяем, что g^l != 1 mod m для всех 1 <= l < m-1
    for l in range(1, m - 1):
        if pow(g, l, m) == 1:
            return False

    return True

#  находм все первообразные корни g по модулю m.
def find_primitive_roots(m):
    primitive_roots = []
    # перебираем все числа от 1 до m-1
    for g in range(1, m):
        if is_primitive_root(g, m):
            primitive_roots.append(g)
    return primitive_roots

if __name__ == "__main__":
    m = int(input("Введите модуль m: "))

    if not is_prime(m):
        print(f"Модуль: {m} не является простым числом.")
    else:
        primitive_roots = find_primitive_roots(m)
        if not primitive_roots:
            print(f"Первообразных корней по модулю {m} не существует.")
        else:
            print(f"Первообразные корни по модулю {m}: {primitive_roots}")
