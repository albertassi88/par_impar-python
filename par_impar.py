from random import randint

numero = randint(1, 10)

opcao = {}
opcaoigual = ""
for n in range(1, 3):
    par_impar = input(f'Jogador {n} você quer "Par" ou "Impar"? ')
    while(par_impar != 'par') & (par_impar != 'impar'):
        par_impar = input(f'Jogador {n}. Favor digitar "par" ou "impar"!')

    while par_impar == opcaoigual:
        par_impar = input(f'O jogador 1 ja escolheu {par_impar.upper()}! Favor escolher a outra opção.')

        while(par_impar != 'par') & (par_impar != 'impar'):
            par_impar = input(f'Jogador {n}. Favor digitar "par" ou "impar"!')
    opcao.update({par_impar:n})
    opcaoigual = par_impar

for chave in opcao.keys():
    if (chave == 'par') & (numero % 2 == 0):
        print(f'{numero} é {chave.upper()}. O jogador {opcao[chave]} venceu!')
    elif (chave == 'impar') & (numero %2 == 1):
        print(f'{numero} é {chave.upper()}. O jogador {opcao[chave]} venceu!')

