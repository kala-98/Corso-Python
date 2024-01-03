
def calcola_vocali(nome):
    vocali = "aeiou"
    verifica = 0
    dizionario = {}
    dizionarioOrdinato = {}
    lista = []
    somma_vocali = 0

    for letter in nome.lower():
        if letter in vocali:
            verifica = 1
            if letter in dizionario:
                dizionario[letter] += 1
            else:
                dizionario[letter] = 1
    
    if verifica == 1:
        for i in dizionario.values():
            somma_vocali += i

        dizionarioOrdinato = sorted(dizionario.items(), key=lambda x: x[1], reverse=True)
    
        for x, y in dizionarioOrdinato:
            lista.append(f"{x} - {y}")

        print(f"Il nome {nome} contiene al suo interno {somma_vocali} {'vocali totali, distribuite in questo modo:' if somma_vocali > 1 else 'vocale:'}")

        for index, elemento in enumerate (lista, 1):
            print(f"{index}: {elemento}")
    else:
        print("Il nome che hai inserito non presenta vocali")

calcola_vocali("Adriano")