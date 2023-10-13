def romano_a_entero(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    entero = 0
    anterior = 0
    for letra in romano[::-1]:
        valor = valores[letra]
        if valor >= anterior:
            entero += valor
        else:
            entero -= valor
        anterior = valor
    return entero

print(romano_a_entero('MMXXIII'))