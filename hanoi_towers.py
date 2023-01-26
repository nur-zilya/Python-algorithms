def hanoi(n, i=1, k=3):
    if (n == 1):
        print(f'Переложить диск 1 со стержня номер {i} на стержень номер {k}')
    else:
        tmp = 6 - i - k
        hanoi(n-1, i, tmp)
        print(f'Переложить диск {n} со стержня {i} на стержень {k}')
        hanoi(n-1, tmp, k)


n = input("Введите количество дисков: ")
n = int(n)
# from_pin = input("С какого стержня? ")
# from_pin = int(from_pin)
# to = input("На какой стержень? ")
# to = int(to)

hanoi(n, 1, 3)