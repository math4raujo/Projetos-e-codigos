def monthly(func, ini, fim):
    
    # FUNC é uma função dada
    # INI é a referência de início
    # FIM é a referência final

    anomes_aux = ini   
    
    while anomes_aux <= fim:
        if anomes_aux % 100 == 12:
            anomes_aux = int(f"{anomes_aux//100+1}01")
        else:
            mes_aux = round((anomes_aux/100 - anomes_aux//100)*100 + 1)
            anomes_aux = int(f"{anomes_aux//100}{mes_aux}")
        
        func(anomes_aux)

# FUNCAO PARA EXEMPLO DE APLICAÇÃO
def ola(anomes):
    print(f"Ola, mundo {anomes}")

monthly(ola, 202111, 202111)

