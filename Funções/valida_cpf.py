CPF = 'XXX.XXX.XXX-XX'
sem_dig = CPF[:-3].replace('.','')
cpf_compara = CPF.replace('.', '')
cpf_compara = cpf_compara.replace('-', '')

# dig 1
lista_soma = []
for p, r in enumerate(range(10, 1, -1)):
    prod_dig = int(sem_dig[p]) * r
    lista_soma.append(prod_dig)

soma = sum(lista_soma)

dig1 = 11 - (soma % 11)

if dig1 > 9:
    dig1 = 0

# dig2
novo_cpf = sem_dig + f'{dig1}'
lista_soma = []
for p, r in enumerate(range(11, 1, -1)):
    prod_dig = int(novo_cpf[p]) * r
    lista_soma.append(prod_dig)

soma = sum(lista_soma)

dig2 = 11 - (soma % 11)

if dig2 > 9:
    dig2 = 0

novo_cpf = novo_cpf + f'{dig2}'

if novo_cpf == cpf_compara:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')