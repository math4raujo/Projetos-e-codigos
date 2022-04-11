from math import pow

def listaexpoentes(num):
    """
    Recebe num e retorna a lista de expoentes de potências de base 2 que somadas resultam em num.
    :param num: int
    :return: expoentes: list
    """
    i = 0
    expoentes = []
    while True:
        if pow(2, i) > num:
            if num > 0:
                expoentes.append(i-1)
            num = num - pow(2, i-1)
            i = 0
        else:
            i += 1
        if num < 0: break
    return expoentes

def converBin(num):
    """
    Recebe um número inteiro num e converte num para base 2 (em binário).
    :param num: int
    :return: finalNum: int
    """
    expoentes = listaexpoentes(num)
    maior = expoentes[0]
    finalNum = ''
    for i in range(maior, -1, -1):
        if i in expoentes:
            finalNum += '1'
        else:
            finalNum += '0'
    return int(finalNum)

print(converBin(1559))