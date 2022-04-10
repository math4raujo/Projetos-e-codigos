from math import sqrt

def primo(num):
    """
    Recebe um inteiro num e decide se num é primo.
    Se for primo retorna True, caso contrário retorna False.
    :param num: int
    :return: decision: boolean
    """
    raiz = int(sqrt(num))
    for i in range(2, raiz+1):
        if num % i == 0:
            return False
    else:
        return True

def main():
    # Casos teste
    N = int(input())
    for i in range(N):
        X = int(input())
        if primo(X):
            print("Prime")
        else:
            print("Not Prime")

main()