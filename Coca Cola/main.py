def cocacola(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("CocaCola")
        elif i % 3 == 0:
            print("Coca")
        elif i % 5 == 0:
            print("Cola")
        else:
            print(i)


n = 20
cocacola(n)