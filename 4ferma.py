def inverse_element_2(a, n):
   

    if n == 1:
        return None

    return pow(a, n - 2, n)


if __name__ == "__main__":
    a = 5
    n = 18
    x = inverse_element_2(a, n)
    print("Мультиплікативне обернений елемент a^(-1) по модулю числа n = %d: %d" % (n, x))
