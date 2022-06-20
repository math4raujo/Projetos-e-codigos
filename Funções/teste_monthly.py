def monthly(func, ini, fim):
    
    # FUNC é uma função dada
    # INI é a referência de início
    # FIM é a referência final

    anomes_aux = ini   
    
    while anomes_aux <= fim:

        func(anomes_aux)

        if anomes_aux % 100 == 12:
            anomes_aux = int(f"{anomes_aux//100+1}01")
        else:
            anomes_aux = anomes_aux + 1
        
# FUNCAO PARA EXEMPLO DE APLICAÇÃO
def ola(anomes):
    print(f"Ola, mundo {anomes}")

monthly(ola, 202201, 202212)
