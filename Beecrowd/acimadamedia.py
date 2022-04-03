# ACIMA DA MÉDIA

def transforma_int(lista_num):
    l = len(lista_num)
    list_convert = []
    for i in range(l):
        convert = int(lista_num[i])
        list_convert.append(convert)

    return list_convert

def above_avg(avg, n, lista_avg):
    cont_above_avg = 0
    for i in range(n):
        if lista_avg[i] > avg:
            cont_above_avg += 1
    return (cont_above_avg/n)*100

def main():
    # NÚMERO DE CASOS DE TESTE
    C = int(input())

    for i in range(C):
        # NÚMERO DE PESSOAS
        N_avg = input()

        N_avg_int = transforma_int(N_avg.split())

        foravg = N_avg_int[1:]

        avg = sum(foravg)/N_avg_int[0]

        print("%.3f" % (above_avg(avg, N_avg_int[0], foravg)), end="")
        print("%")

main()

