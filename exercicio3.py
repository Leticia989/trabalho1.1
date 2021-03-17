
def operacoes(num1, num2, operador):
    if operador == '+':
        operacao = num1 + num2
    elif operador == '-':
        operacao = num1 - num2
    elif operador == '*':
        operacao = num1 * num2
    elif operador == '/':
        operacao = num1 / num2
    else:
        print('Você não escolheu nenhuma operação')

    return operacao


n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
operador = input('Escolha uma operação: soma(+), subtração(-), multiplicação(*) ou divisão(/) ')

resultado = operacoes(n1, n2, operador)
print('O resultado da operação é: ', resultado,)

if resultado % 2 == 0:
    print('Número é par')
else:
    print('Número é ímpar')

if resultado < 0:
    print('Número é negativo')
else:
    print('O Número é positivo')

print(type(resultado))

