nome = "Adriano"
vocali = "aeiou"
dizionario = {}

for letter in nome.lower():
    if letter in vocali:
        if letter in dizionario:
            dizionario[letter] += 1
        else:
            dizionario[letter] = 1

lista = []
somma_vocali = 0
for i in dizionario.values():
    somma_vocali += i

for x, y in dizionario.items():
    lista.append(f"{x} - {y}")


print(f"Il nome {nome} contiene al suo interno {somma_vocali} vocali totali, distribuite in questo modo:")

for index, elemento in enumerate (lista, 1):
    print(f"{index}: {elemento}")