# Beecrowd 1169 - Trigo no Tabuleiro

from math import pow

def ngraos(ncasas):
    """
    Recebe o número de casos do tabuleiro que serão ocupadas e retorna a quantidade de graõs.
    O número de grãos dobra a cada casa (acumala 2 elevado a n).
    :param ncasas: int
    :return: ngraos_final: int
    """
    ngraos_final = 0
    for i in range(ncasas):
        ngraos_final += pow(2, i)
    return ngraos_final

def converte(num):
    """
    Recebe o número de grãos e retorna o peso em Kg's.
    Cada 12 grãos equivalem a 1 grama.
    :param num: int
    :return: pesograos: int
    """
    # Número de grãos para grama
    pesograos = num/12
    # Gramas para Kg
    pesograos = pesograos/1000
    return int(pesograos)

def main():
    # Número de casos teste
    N = int(input())
    for i in range(N):
        X = int(input())
        print("%d kg" % (converte(ngraos(X))))

main()