print('Oi essa é a sua calculadora ')

num_1 = float(input('Por favor, digite um numero: '))
escolha = input('Digite sua operação: (+), (-), (*), (/) ')
num_2 = float(input('Por favor, digite outro numero: '))

if escolha == '+':
    soma = num_1 + num_2
    print('A soma é: ', soma)

elif escolha == '-':
    sub = num_1 - num_2
    print('A subtração é: ', sub)

elif escolha == '*':
    mult = num_1 * num_2
    print('A multiplicação é: ', mult)
else:
    div = num_1 / num_2
    print('A divisão é : ', div)


  

