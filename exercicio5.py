combustivel = str(input("Digite o tipo de combustível que você colocou:")). strip().capitalize()
litro = float(input ("Digite a quantidade de litros que você colocou:"))
gasolina = 2.50
alcool = 1.90
custo1 = litro * alcool
custo2 = litro * gasolina

if combustivel == "A":
 print(custo1)

if litro <= 20:
 desconto1 = (custo1 * 3)/100
 print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto1,custo1-desconto1))

elif litro > 20:
 desconto2 = (custo1 * 5)/100
 print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto2,custo1-desconto2))

elif combustivel == "G":
 print(custo2)

if litro <= 20:
 desconto3 = (custo2 * 4)/100
 print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto3,custo2-desconto3))

elif litro > 20:
 desconto4 = (custo2 * 6)/100
 print("O desconto de combustível foi de : {} e o preço agora é {}".format(desconto4,custo2-desconto4))


