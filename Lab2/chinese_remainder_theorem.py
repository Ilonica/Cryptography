# gcd — НОД(b % a, a), x и y — коэффициенты Безу, выраженные из (b % a, a) * x1 + a * y = НОД(b % a, a).
# в общем виде решаем уравнение a * x + m * y = 1
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

# обратный элемент к a по модулю m.
def inverse_mod(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Обратный элемент не существует, так как {a} и {m} не взаимно просты.")
    else:
        return x % m # т.к. x может быть отрицательным или больше m

def chinese_remainder_theorem(a_list, m_list):
    # проверяем модули на взаимную простоту
    for i in range(len(m_list)):
        for j in range(i + 1, len(m_list)):
            if gcd(m_list[i], m_list[j]) != 1:
                raise ValueError("Модули не попарно взаимно просты.")

    # вычисляем M = m1*m2*...*mk
    M = 1
    for m in m_list:
        M *= m

    # вычисляем Mi = M/mi и обратные числа к ним
    x = 0
    for a, m in zip(a_list, m_list):
        Mi = M // m
        # b — обратный элемент к Mi по модулю m
        b = inverse_mod(Mi, m)
        x += a * Mi * b

    return x % M

if __name__ == "__main__":
    a_list = [2, 15, 5]
    m_list = [5, 17, 12]

    try:
        x = chinese_remainder_theorem(a_list, m_list)
        print(f"Решение системы сравнений с помощью КТО: x = {x}")
    except ValueError as e:
        print(e)
