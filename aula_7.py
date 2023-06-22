# idade = input("Digite a idade:\n ")
# idade = int(idade)
# print("É maior de idade?\n" ,idade >= 18)
# print(type(idade))


#exercicio 1
# numero = input("Digite um numero inteiro:\n")
# numero = int(numero)
# print("True é par e False é impar: ", numero % 2 == 0)

#exercicio 2
# a = 5
# b = 10
# x = True
# y = False
# print((x or y) and (a < b))
# print((x or y) and not (a < b ))

#exercicio 3
# resultado = ((2 + 3) * 2) ** 2
# print(resultado)

#exercicio 4
valor_compra = input("Valor de compra: ")
valor_frete = input("Valor frete: ")
cliente_cadastrado = input("Sim ou nao: ")

valor_compra = float(valor_compra)
valor_frete = float(valor_frete)
valor_total = valor_compra + valor_frete

resultado = print("Cupom pode ser utilizado?\n", valor_total > 100.0 and cliente_cadastrado == "sim")



