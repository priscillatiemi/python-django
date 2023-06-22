notas = [8,9,10,7.5,4,6]

i = 0
total = 0
qtd = len(notas)
while i < qtd:
    total = total + notas [i]
    i = i + 1

print("O total das notas é:", total)
media = total / qtd
print("A media das notas: ", media)