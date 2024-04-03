def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
# print(fact(1))

def soma_numeros_naturais(x):
    if x == 1:
        return 1
    else:
        return x + soma_numeros_naturais(x - 1)
# print(soma_numeros_naturais(5))

def fibonacci(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        val2 = x - 1
        return x + val2   
# print(fibonacci(7))

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
# print(sum_character_x(12345))


def remove_duplicatas_sem_ordenar(lista):
    elementos_vistos = set()
    lista_sem_duplicatas = []
    
    for elemento in lista:
        if elemento not in elementos_vistos:
            lista_sem_duplicatas.append(elemento)
            elementos_vistos.add(elemento)
    
    return lista_sem_duplicatas

# print(remove_duplicatas_sem_ordenar([2, 3, 2, 1, 4, 5, 6, 5]))


def warn_the_sheep(queue):
    
    posicoes = []
    if queue:
        nums_queue = list(reversed(queue))
        for posicao_item in enumerate(nums_queue, 1):
            posicoes.append(posicao_item)
        
        posicao_lobo = ''
        for i in posicoes:
            if i[1] == 'wolf':
                posicao_lobo = i[0]
        posicao_ovelha = posicao_lobo - 1   
        
        teste = []
        for i in enumerate(queue):
            teste.append(i)
        if teste[-1][1] == 'wolf':
            return "Pls go away and stop eating my sheep"

        return f"Oi! Sheep number {posicao_ovelha}! You are about to be eaten by a wolf!"
        
#print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf']))



def shorten_to_date(long_date):

    long_date_list = list(long_date)
    index_virgula = list(long_date).index(',')
    
    a = long_date_list[:index_virgula]
    return "".join(a)
#print(shorten_to_date("Tuesday January 29, 10pm"))


def array(string):
    #remover o primeiro e ultimo item
    a = list(string.replace(',', ''))[1:-1]
    
    return " ".join(a)
    #return str(str(a).replace('[', '').replace(']', ''))


# print(array('1,2,3,4,5'))
from unicodedata import normalize
def reverse_letter(st):

    lista_separados = ['.', ',', ':', '"', '?', '!', ';',
                    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    trans = {ord(i): '' for i in lista_separados}
    new_st = st.translate(trans)
    
    new_st_inverted = new_st[::-1]
    return new_st_inverted
# print(reverse_letter("ultr53o?n")) # nortlu
def sum_cubes(n):
    
    sequencia_n = []
    for i in range(n, 0, -1):
        sequencia_n.append(i)

    n_ao_cubo = []
    for i in sequencia_n:
        n_ao_cubo.append(i ** 3)
    return sum(n_ao_cubo)

#print(sum_cubes(123))



def teste():
    
    return

