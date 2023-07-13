def Ackermann(m, n) :
    if m == 0 :
        return n + 1
    elif m > 0 and n == 0 :
        return Ackermann(m - 1, 1)
    return Ackermann(m - 1, Ackermann(m, n - 1))

cantidad = int(input())
for i in range(cantidad) :
    m = int(input())
    n = int(input())
    retorno = Ackermann(m, n)
    print(retorno)
