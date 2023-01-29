def calculadora(files):
    total = 0
    for x in files:
        if x.tipo == "Boleto" or x.tipo == "Aluguel" or x.tipo == "Financiamento":
            total -= float(x.valor)
        else:
            total += float(x.valor)
    return total


def identificadores(str):
    if str == "1":
        return "Débito"
    elif str == "2":
        return "Boleto"
    elif str == "3":
        return "Financiamento"
    elif str == "4":
        return "Crédito"
    elif str == "5":
        return "Recebimento Empréstimo"
    elif str == "6":
        return "Vendas"
    elif str == "7":
        return "Recebimento TED"
    elif str == "8":
        return "Recebimento DOC"
    elif str == "9":
        return "Aluguel"
