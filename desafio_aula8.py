# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***


dados = {}

nome1 = input('Digite seu nome: ')
idade1 = int(input('Digite sua idade: '))
acesso1 = int(input('senha: '))

nome2 = input('Digite seu nome: ')
idade2 = int(input('Digite sua idade: '))
acesso2 = int(input('senha: '))

nome3 = input('Digite seu nome: ')
idade3 = int(input('Digite sua idade: '))
acesso3 = int(input('senha: '))

dados['nomes'] = [nome1,nome2,nome3]
dados['idades'] = [idade1,idade2,idade3]
dados['acessos'] = [acesso1,acesso2,acesso3]

print(dados)

login = input('Digite seu nome: ')
print('-------------------------------------------------')
senha = int(input('Digite sua senha: '))
print('-------------------------------------------------')
if login in dados['nomes'] and senha in dados['acessos']:
    print('Bem-vindo ao nosso sistema de quartos')
    
   
    print('--------------------------------------------------')

    print('Escolha seu quarto', dados['nomes'][0])

    print('--------------------------------------------------')

    quartos = ['simples','Duplo','luxo']
    valores = [100.00, 150.00, 250.00]
    print('opções de quartos: ', quartos)
    print('--------------------------------------------------')
    sua_alternativa = int(input('escolha seu quarto pelo id: 0 simples --, 1 Duplo --, 2 luxo: '))
    print('--------------------------------------------------')
    quantidade_dias = int(input('digite a quantidade de dias que você ficará hospedado: '))
    print('--------------------------------------------------')

    calculo = quantidade_dias*valores[sua_alternativa]
    print('Você escolheu o quarto:', quartos[sua_alternativa],'e a quantidade de dias é de: ', quantidade_dias)
    print('----------------------------------------------------')
    print('O seu total é de: R$', calculo)

    print('--------------------------------------------------')

    print('Escolha seu quarto:', dados['nomes'][1])

    print('--------------------------------------------------')

    quartos = ['simples','Duplo','luxo']
    valores = [100.00, 150.00, 250.00]
    print('opções de quartos: ', quartos)
    print('--------------------------------------------------')
    sua_alternativa = int(input('escolha seu quarto pelo id: 0 simples --, 1 Duplo --, 2 luxo: '))
    print('--------------------------------------------------')
    quantidade_dias = int(input('digite a quantidade de dias que você ficará hospedado: '))
    print('--------------------------------------------------')

    calculo = quantidade_dias*valores[sua_alternativa]
    print('Você escolheu o quarto:', quartos[sua_alternativa],'e a quantidade de dias é de: ', quantidade_dias)
    print('----------------------------------------------------')
    print('O seu total é de: R$', calculo)

    print('--------------------------------------------------')
    print('Escolha seu quarto', dados['nomes'][2])


    print('--------------------------------------------------')

    quartos = ['simples','Duplo','luxo']
    valores = [100.00, 150.00, 250.00]
    print('opções de quartos:', quartos)
    print('--------------------------------------------------')
    sua_alternativa = int(input('escolha seu quarto pelo id: 0 simples --, 1 Duplo --, 2 luxo: '))
    print('--------------------------------------------------')
    quantidade_dias = int(input('digite a quantidade de dias que você ficará hospedado: '))
    print('--------------------------------------------------')

    calculo = quantidade_dias*valores[sua_alternativa]
    print('Você escolheu o quarto:', quartos[sua_alternativa],'e a quantidade de dias é de: ', quantidade_dias)
    print('----------------------------------------------------')
    print('O seu total é de: R$', calculo)
else:
    print('Há algo errado, tente novamento')
