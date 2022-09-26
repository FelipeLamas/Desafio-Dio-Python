""" 
# 1° Desafio Formação Python

T = input() # recebe o texto
arr = len(T) # Verifica quantos caracteres tem 

if arr <= 140: # Faz a verficação
    print("TWEET")
else:
    print("MUTE")

#################################################

# 2° Desafio Formação Python

months_dict = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
    10: 'October', 11: 'November', 12: 'December'
}

m = int(input())

if m in months_dict.keys():
    print(months_dict[m])


    ##############################################################################################

    3° Desafio este não entendi muito bem preciso estudar.

n = int(input())

while(n > 0):

    a = input("Informe o valor de A: ")
    b = input("Informe o valor de B: ")
    n = n - 1

    if len(a) >= len(b):
        if (a[(len(a) - len(b)):]) == b:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")
    
"""
