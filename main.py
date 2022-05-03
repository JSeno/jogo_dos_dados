"""
TODO: Fazer loop, melhorar a lógica da carteira.
Jogo de dados

Você tem  R$ 100.00 na sua carteira e é viciado em jogos, e temos um jogo de dados. Você escolhe  os números dos 3 dados
e aposta neles entre 1, 5, 10.
"""

import random


print('Seja muito bem vindo à nossa mesa de dados!')
print('+--------------------------------------------------------------------------------------------------------+')
print('Aqui é muito simples, você escolhe os números que cairão nos dados se acertar ganha o que foi apostado,'
      '\nmultiplicando o valor apostado por 2 caso acerte 1 dado 3 caso acerte 2 dados e 6 caso acerte todos os dados.')
print('+--------------------------------------------------------------------------------------------------------+')
print('\n')

my_wallet = float(100.00)

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print('Atualmente você tem R$', my_wallet, 'na sua carteira.')
print('\n')
print('Vamos jogar!')
print('\n')
print('Quanto você quer apostar?')

bet = float(input())
my_wallet_bet = my_wallet - bet
print('R$', my_wallet_bet)
print('\n')
print('Você escolheu apostar R$', bet, 'para cada dado.')
print('\n')
print('Escolha os números dos dados que você quer apostar.')

print('Dado 1:')
dice_1_bet = int(input())
print('Dado 2:')
dice_2_bet = int(input())
print('Dado 3:')
dice_3_bet = int(input())

print('O resultado dos dados foi:')
print('Dado 1:', dice_1, 'Dado 2:', dice_2, 'Dado 3:', dice_3)
print('E você apostou:')
print('Dado 1:', dice_1_bet, 'Dado 2:', dice_2_bet, 'Dado 3:', dice_3_bet)
print('\n')

dados_acertados = 0
if dice_1 == dice_1_bet:
    dados_acertados += 1
if dice_2 == dice_2_bet:
    dados_acertados += 1
if dice_3 == dice_3_bet:
    dados_acertados += 1

if dados_acertados == 3:
    print('Você acertou todos os dados!')
    print('Você ganhou R$', bet * 6)
    my_wallet = my_wallet + bet * 6
elif dados_acertados == 2:
    print('Você acertou 2 dados!')
    print('Você ganhou R$', bet * 2)
    my_wallet = my_wallet + bet * 2
elif dados_acertados == 1:
    print('Você acertou 1 dado!')
    print('Você ganhou R$', bet)
    my_wallet = my_wallet + bet

print(my_wallet)





