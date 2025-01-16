def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    print("O valor final de SOMA é:", SOMA)

def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero or numero == 0:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

def analisar_faturamento(faturamento_diario):
    faturamento_valido = [valor for valor in faturamento_diario if valor > 0]
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

    print(f"Menor faturamento: R${menor_faturamento:.2f}")
    print(f"Maior faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

def calcular_percentual_faturamento(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())
    for estado, valor in faturamento_estados.items():
        percentual = (valor / total_faturamento) * 100
        print(f"{estado}: {percentual:.2f}%")

def inverter_string(texto):
    string_invertida = ""
    for char in texto:
        string_invertida = char + string_invertida
    print(f"String original: {texto}")
    print(f"String invertida: {string_invertida}")

if __name__ == "__main__":
    calcular_soma()

    numero = 21
    pertence_fibonacci(numero)

    faturamento_diario = [100, 200, 0, 300, 400, 0, 0, 500, 600]
    analisar_faturamento(faturamento_diario)

    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    calcular_percentual_faturamento(faturamento_estados)

    texto = "Exemplo de string"
    inverter_string(texto)
