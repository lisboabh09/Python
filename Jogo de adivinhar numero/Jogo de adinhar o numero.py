import random
#variaveis declaradas
chute = 0
chances = 7
tentativas = 1
jogador = ''
# sistema de sorteio número entre 1 e 100
numero_secreto = random.randint(1, 100)

print('#######################################################')
print('##### SEJA BEM VINDO AO JOGO DE ADIVINHAR NUMEROS #####')
print('######### INFORME UM NÚMERO E TENTE ACERTAR ###########')
print('################ VOCÊ TEM SETE CHANCES ################')
print('##################### BOA SORTE #######################')
print('#######################################################')
print('')
print('')

#codigo pra inserir usuário
jogador = input('Digite seu nome: ')
print('Chute um número entre 1 e 100')

#declaração de testes
while tentativas <= 7:
    chute = int(input('Digite o número: '))

    if chute < numero_secreto:
        print('Você errou. Seu número é menor que o sorteado,'
        ' tente novamente.)')
        print('Tentativa % d de % d' % (tentativas, chances))
    elif chute == numero_secreto:
        print('PARABÉNS!!!!!', jogador)
        print('Você acertou com % d tentativcas' % tentativas)
        tentativas = 7
    else:
        print('Você errou, Seu número é maior que o sorteado,'
            ' tente novamente')
        print('Tentativa % d de % d' % (tentativas, chances))

    if tentativas == 6:
        print('Última tentativa')
    elif tentativas == 7:
        print('### Game Over###')

# a cada tentativa de erro soma - se 1 a tentativa chegando a 8 acaba
    tentativas = tentativas + 1

