from math import pow

def listaexpoentes(num, base):
    """
    Recebe num e retorna a lista de expoentes de potências de base base que somadas resultam em num.
    :param num: int
    :return: expoentes: list
    """
    i = 0
    expoentes = []
    while True:
        if pow(base, i) > num:
            if num > 0:
                expoentes.append(i-1)
            num = num - pow(base, i-1)
            i = 0
        else:
            i += 1
        if num < 0: break

    return expoentes, expoentes[0]

def coeficientes(exps):
    """
    Recebe uma lista com valores duplicados de expoentes de um número na base 16 e retorna uma lista com os algarismos
    deste número na base 16 (hexadecimal).
    :param exps: list
    :return: coefs: list
    """
    tot_n = len(exps)
    coefs = []
    for i in range(tot_n):
        contaj = 0
        for j in range(i, tot_n):
            if exps[j] == exps[i] and exps[j] != exps[i-1]:
                contaj += 1
        if contaj > 0:
            coefs.append(contaj)

    if len(coefs) == 0:
        coefs.append(len(exps))

    return coefs

def converteBase16(coefs):
    """
    Recebe os algarismos de um número na base 16 (hexadecimal) e os formata para a base 16.
    :param coefs: list
    :return: numFinal: int
    """
    algarismos = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                  '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    n = len(coefs)
    numFinal = ""
    for i in range(n):
        numFinal += algarismos[str(coefs[i])]
    return numFinal

def converteBase10(num):
    """
    Converte um número de base 16 (hexadecimal) para base 10.
    :param num: str
    :return: finalNum: int
    """
    algarismos = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
                  '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
    # TEMOS PROBLEMAS NO ZER0
    # ERRO DE CHAVE
    strnum = str(num)
    nalgs = len(strnum)
    finalNum = 0
    for i in range(1, nalgs+1):
        finalNum += int(algarismos[strnum[(-1)*i]]) * pow(16, i-1)
        if algarismos[strnum[(-1)*i]] == 0:
            finalNum += pow(16, i)

    return int(finalNum)


def main():
    """
    Função principal.
    :return: 0
    """
    entrada = input()
    while entrada != '-1':

        if entrada[1:2] == "x" and entrada[2:] != "":
            number = converteBase10(entrada[2:])
            print(number)
        else:
            if entrada[1:2] != "x":
                exps, maior = listaexpoentes(int(entrada), 16)
                coefs = coeficientes(exps)
                number = "0x" + str(converteBase16(coefs))
                if int(entrada) % 16 == 0:
                    number += maior*'0'

                print(number)

        entrada = input()

main()

