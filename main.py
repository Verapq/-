def calc_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

def run_diffie_hellman():
    print("= Протокол Диффи-Хеллмана =")

    g = int(input("Введите значение g (основание): "))
    p = int(input("Введите значение p (модуль): "))

    secret_a = int(input("Секретный ключ участника A: "))
    secret_b = int(input("Секретный ключ участника B: "))

    public_a = pow(g, secret_a, p)
    public_b = pow(g, secret_b, p)

    print("Публичный ключ A:", public_a)
    print("Публичный ключ B:", public_b)

    shared_key_a = pow(public_b, secret_a, p)
    shared_key_b = pow(public_a, secret_b, p)

    print("Общий ключ, полученный A:", shared_key_a)
    print("Общий ключ, полученный B:", shared_key_b)

    if shared_key_a == shared_key_b:
        print("Ключ успешно установлен! Секретный ключ:", shared_key_a)
    else:
        print(" Ошибка! Ключи не совпадают.")

def run_rsa():
    print("= Алгоритм RSA =")

    p = int(input("Введите первое простое число p: "))
    q = int(input("Введите второе простое число q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    print(f"n = {n}")
    print(f"φ(n) = {phi}")

    while True:
        e = int(input("Введите e (взаимно просто с φ(n)): "))
        if calc_gcd(e, phi) == 1:
            break
        print("e не подходит, попробуйте снова.")

    d = mod_inverse(e, phi)

    print("Публичный ключ: (e =", e, ", n =", n, ")")
    print("Приватный ключ: (d =", d, ", n =", n, ")")

    m = int(input("Введите сообщение для шифрования (целое число < n): "))
    encrypted = pow(m, e, n)
    print("Зашифрованное сообщение:", encrypted)

    decrypted = pow(encrypted, d, n)
    print("Расшифрованное сообщение:", decrypted)

#меню
def main():
    print("Выберите режим работы:")
    print("1 — RSA")
    print("2 — Диффи-Хеллман")

    mode = input("Ваш выбор: ")

    if mode == "1":
        run_rsa()
    elif mode == "2":
        run_diffie_hellman()
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()
