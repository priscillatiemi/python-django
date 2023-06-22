# i = 10
# while i <= 100: 
#     print(i)
#     i = i + 1
# print("Fim.")
# print(i)

total = 0
while True:
    valor = float(input("Digite o valor da compra:\n"))
    total = total + valor
    continuar = input("Deseja continuar?(s/n)\n")
    if continuar != "s":
        break
print("O valor total da compra: R$", total)