#Exibir cabeçalho com o nome do programa de calculo de média de notas

print ('######################################################')
print('O Programa de calcular média das notas está em uso!')
print ('######################################################')

#Solicita entrada de dados com o nome do aluno
aluno = input('Insira o nome do aluno: ')
#Solicita entrada de dados com o nome da matéria
materia = input('Insira o nome da matéria: ')

#entrada das notas e as converte em numero.
#a entrada de dodos recebe strings
#por isso converter em float

n1 = float (input('Insira a primeira nota: '))
n2 = float (input('Insira a segunda nota: '))
n3 = float (input('Insira a terceira nota: '))
n4 = float (input('Insira a quarta nota: '))

#calculo da média das notas
#colocamos entre parentesis para definir a ordem do calculo.

media = ( n1 + n2 + n3 + n4 ) / 4

#reporte para o usuário da situação se aprovado ou não
# % s apresenta o valor na forma de string
# % .2f apresenta o valor na de float com duas casas decimai
#Entre parenteses os valores que serão informados ao usuário.
if media < 7:
    print('Aluno % s, foi reprovado em % s a média de suas notas foram: % .2f.'
        % (aluno, materia, media))
else:
    print('Aluno % s, foi aprovado em % s a média de suas notas foram: % .2f.'
        % (aluno, materia, media))
#frase para finalizar o uso da ferramenta.
print ('######################################################')
print('Obrigado por usar o programa de média de notas')
print ('######################################################')