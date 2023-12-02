def gcdex(a, b):
   

    # Початкові значення x і y: x = 0, y = 1.
    x, y = 0, 1

    # Поки b != 0:
    while b != 0:

        # Обчислити q і r, як частку і залишок від ділення a на b.
        q, r = a // b, a % b

        # Обновити значення x і y: x = y - q * x, y = x.
        x, y = y - q * x, x

        # Обновити значення a і b: a = b, b = r.
        a, b = b, r

    return a, x, y


#Тест
if __name__ == "__main__":
    a = 612
    b = 342
    d, x, y = gcdex(a, b)
    print("Найбільший спільний дільник a і b:", d)
    print("x:", x)
    print("y:", y)
