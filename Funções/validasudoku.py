sudoku = [[4,2,6,5,7,1,3,9,8], [8,5,7,2,9,3,1,4,6], [1,3,9,4,6,8,2,7,5], [9,7,1,3,8,5,6,2,4],
          [5,4,3,7,2,6,8,1,9], [6,8,2,1,4,9,7,5,3], [7,9,4,6,3,2,5,8,1], [2,6,5,8,1,4,9,3,7],
          [3,1,8,9,5,7,4,6,2]]

#print(sudoku[8][0])

def solucao(mat):
    valido = True
    # SOMA DAS LINHAS
    for i in range(9):
        selected_list = mat[i].copy()
        selected_list.sort()
        #print(selected_list)
        for j in range(1, 10):
            if j not in selected_list:
                valido = False
                break
        #print(valido)
    # SOMA DAS COLUNAS
    for i in range(9):
        # CRIAR UMA LISTA COM A COLUNA I
        selected_list = []
        for j in range(9):
            selected_list.append(mat[j][i])
        #print(selected_list)
        selected_list.sort()
        for j in range(1, 10):
            if j not in selected_list:
                valido = False
                break
        #print(valido)
    # SOMA DOS QUADRADOS
    for i in range(0, 9, 3):
        selected_list = []
        for j in range(i, 3 + i):
            for k in range(0, 3):
                selected_list.append(mat[k][j])
        #print(selected_list)
        for j in range(1, 10):
            if j not in selected_list:
                valido = False
                break

        selected_list = []
        for j in range(i, 3 + i):
            for k in range(3, 6):
                selected_list.append(mat[k][j])
        #print(selected_list)
        for j in range(1, 10):
            if j not in selected_list:
                valido = False
                break

        selected_list = []
        for j in range(i, 3 + i):
            for k in range(6, 9):
                selected_list.append(mat[k][j])
        #print(selected_list)
        for j in range(1, 10):
            if j not in selected_list:
                valido = False
                break

    return valido

print(solucao(sudoku))