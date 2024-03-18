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

def fibonacci(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        val2 = x - 1
        return x + val2   
print(fibonacci(7))

def sum_character_x(x):
    x = str(x)
    
    if len(x) <= 1:
        return x
    else:
        lst = list()
        for i in x:
            lst.append(i)
        
        lst_int = list()
        for k in lst:
            lst_int.append(int(k))
        
        return sum(lst_int)
print(sum_character_x(12345))

def remove_duplicatas_sem_ordenar(lista):
    elementos_vistos = set()
    lista_sem_duplicatas = []
    
    for elemento in lista:
        if elemento not in elementos_vistos:
            lista_sem_duplicatas.append(elemento)
            elementos_vistos.add(elemento)
    
    return lista_sem_duplicatas

print(remove_duplicatas_sem_ordenar([2, 3, 2, 1, 4, 5, 6, 5]))



