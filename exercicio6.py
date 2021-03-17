def preco_maca(quantidade_kg):
    preco_total = 0
    if quantidade_kg <= 5:
        preco_total = quantidade_kg * 2.50
    else:
        preco_total = quantidade_kg * 2.20
    if preco_total > 25:
        preco_total = preco_total - (preco_total * 10)/100
    return preco_total

def preco_morango(quantidade_kg):
    preco_total = 0
    if quantidade_kg <= 5:
        preco_total = quantidade_kg * 1.80
    else:
        preco_total = quantidade_kg * 1.50
    if preco_total > 25:
        preco_total = preco_total - (preco_total * 10)/100
    return preco_total

maca_kg = float(input('Qual é a quantidade de maças?  '))
valor_total = preco_maca(maca_kg)
print('O valor é: ', valor_total)

morango_kg = float(input('Qual é a quantidade de morangos? '))
valor_total = preco_morango(morango_kg)
print('O valor é: ', valor_total)









