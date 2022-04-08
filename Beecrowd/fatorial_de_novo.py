# beecrowd - 1429
# Fatorial de Novo!

def fatia_num(num):
    """
    Retorna uma lista contendo os algarismos de um número num inteiro.
    :param num: inteiro
    :return fatias: list
    """
    fatias = []
    while num >= 1:
        a = num % 10
        fatias.append(a)
        num = int(num/10)
    return fatias

def fatorial(num):
    """
    Caso receba um número maior que 0 retorna o fatorial desse número. Caso contrário retorna 1.
    :param num: inteiro
    :return num: inteiro
    """
    if num > 0:
        x = num-1
        while x >= 1:
            num *= x
            x -= 1
        return num
    else: return 1

def metodo_acm(num):
    """
    Aplica o método ACM - A curious method - dado no exercício
    :param num: inteiro
    :return: num_acum: inteiro
    """
    algs = fatia_num(num)
    n = len(algs)
    num_acum = 0
    for i in range(n):
        num_acum += fatorial(i+1)*algs[i]
    return num_acum

def main():
    """
    Função principal.
    """
    teste = int(input())
    while teste != 0:
        print(metodo_acm(teste))
        teste = int(input())

main()