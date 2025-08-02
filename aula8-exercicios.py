# EXERCÍCIOS 1: 
# Utilize condicionais

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
num = int(input('Digite um numero: '))
if num > 0:
    print('é positivo')
elif num == 0:
    print('Esse numero é zero')
else:
    print('Esse numero é negativo')



# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
idade = int(input('Digite sua idade: '))
if idade >=16:
    print('Você pode votar ')
else:
    print('Voce ainda não pode votar')


# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
num = 0
if num  % 2 == 0:
    print('é par')
else:
    print('É impar')
# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

num1 = int(input('Digite um numero de um a tres: '))
num2 =int(input('Digite um numero de um a tres: '))
num3 =int(input('Digite um numero de um a tres: '))
if num1 ==num2==num3:
    print('É equilatero')
elif num1 != num2 != num3:
    print( 'É escaleno')
else: 
    print('É isósceles')




# # 5*

# # Determine se um número é múltiplo de 5 e 7.
num = 35
if num % 5 == 0 and num % 7 ==0:
    print('É multiplo de 5 e 7')
else: 
    print('Não é multiplo')

# 6*
# print('Verifique se um número é positivo e maior que 10')

num = 2
print(num)
if num <=10:
   print(False)
elif num >=10:
    print(True)

# 7*
# Verifique se um número é divisível por 3 ou 5.
num = 15
if num % 3 == 0 or num % 5 == 0:
    print(True, 'é divisível')
else:
    print('Não é')
