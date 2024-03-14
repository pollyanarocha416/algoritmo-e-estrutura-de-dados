def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
print(fact(1))

def soma_numeros_naturais(x):
    if x == 1:
        return 1
    else:
        return x + soma_numeros_naturais(x - 1)
print(soma_numeros_naturais(5))

def fibo(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        val2 = x - 1
        return x + val2
print(fibo(3))