
ganhou = 0

jogada_X = int(input('Jogada do JX: '))

jogo_acabou = False

a = b = c = d = e = f = g = h = i = 0

a_jogada = b_jogada = c_jogada = d_jogada = e_jogada = f_jogada = g_jogada = h_jogada = i_jogada = 0

while not jogo_acabou:

    # Para o jogador X
    if jogada_X == 1 and a == 0:
        a = 3**8
        a_jogada = 1
    elif jogada_X == 2 and b == 0: 
        b = 3**7
        b_jogada = 1
    elif jogada_X == 3 and c == 0:
        c = 3**6
        c_jogada = 1
    elif jogada_X == 4 and d == 0:
        d = 3**5
        d_jogada = 1
    elif jogada_X == 5 and e == 0:
        e = 3**4
        e_jogada = 1
    elif jogada_X == 6 and f == 0:
        f = 3**3
        f_jogada = 1
    elif jogada_X == 7 and g == 0:
        g = 3**2
        g_jogada = 1
    elif jogada_X == 8 and h == 0:
        h = 3**1
        h_jogada = 1
    elif jogada_X == 9 and i == 0:
        i = 3**0
        i_jogada = 1

    # Para o jogador O
    jogada_O = int(input('Jogada do JO: '))

    if jogada_O == 1 and a == 0:
        a = 2 * 3**8
        a_jogada = 2
    elif jogada_O == 2 and b == 0: 
        b = 2 * 3**7
        b_jogada = 2
    elif jogada_O == 3 and c == 0:
        c = 2 * 3**6
        c_jogada = 2
    elif jogada_O == 4 and d == 0:
        d = 2 * 3**5
        d_jogada = 2
    elif jogada_O == 5 and e == 0:
        e = 2 * 3**4
        e_jogada = 2
    elif jogada_O == 6 and f == 0:
        f = 2 * 3**3
        f_jogada = 2
    elif jogada_O == 7 and g == 0:
        g = 2 * 3**2
        g_jogada = 2
    elif jogada_O == 8 and h == 0:
        h = 2 * 3**1
        h_jogada = 2
    elif jogada_O == 9 and i == 0:
        i = 2 * 3**0
        i_jogada = 2

    tabuleiro = a + b + c + d + e + f + g + h + i

    # Precisamos checar se alguém venceu

    if (a_jogada == b_jogada == c_jogada and a_jogada != 0) or (d_jogada == e_jogada == f_jogada and d_jogada != 0) or \
        (g_jogada == h_jogada == i_jogada and g_jogada != 0) or (a_jogada == d_jogada == g_jogada and a_jogada != 0) or \
        (b_jogada == e_jogada == h_jogada and b_jogada != 0) or (c_jogada == f_jogada == i_jogada) and c_jogada != 0 or \
        (a_jogada == e_jogada == i_jogada and a_jogada != 0) or (c_jogada == e_jogada == g_jogada and c_jogada != 0):      

        jogo_acabou = True

    # Se alguém venceu, quem foi
    if jogo_acabou:

        if a_jogada == b_jogada == c_jogada:
            ganhou = a_jogada
        if d_jogada == e_jogada == f_jogada:
            ganhou = d_jogada
        if g_jogada == h_jogada == i_jogada:
            ganhou = g_jogada
        if a_jogada == d_jogada == g_jogada:
            ganhou = a_jogada
        if b_jogada == e_jogada == h_jogada:
            ganhou = b_jogada
        if c_jogada == f_jogada == i_jogada:
            ganhou = c_jogada
        if a_jogada == e_jogada == i_jogada:
            ganhou = a_jogada
        if c_jogada == e_jogada == g_jogada:
            ganhou = c_jogada

        print(f'o jogador {ganhou} ganhou')

    # Jogador X joga novamente
    if not jogo_acabou:
        jogada_X = int(input('Jogada do JX: '))
