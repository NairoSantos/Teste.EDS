
Documentação do Código....

Este código contém várias funções independentes que resolvem problemas distintos. Abaixo está a explicação de cada uma, detalhando a lógica utilizada.

1. Função calcular_soma
Propósito: Calcula a soma dos números de 1 até um índice predefinido (INDICE = 13).

Lógica:

Inicializa SOMA e K em 0.
Em um loop while, incrementa K e adiciona seu valor a SOMA até que K alcance o valor de INDICE.
Exibe o valor final de SOMA.
Saída: "O valor final de SOMA é: 91"

2. Função pertence_fibonacci
Propósito: Verifica se um número pertence à sequência de Fibonacci.

Lógica:

Inicializa os dois primeiros números da sequência (a = 0 e b = 1).
Em um loop, atualiza os valores de a e b somando os dois números consecutivos até que b seja maior ou igual ao número informado.
Se o número informado coincide com b ou é igual a 0, ele pertence à sequência; caso contrário, não pertence.
Exemplo de Entrada: numero = 21

Exemplo de Saída: "O número 21 pertence à sequência de Fibonacci."

3. Função analisar_faturamento
Propósito: Analisa o faturamento diário de uma distribuidora.

Lógica:

Remove valores não válidos (dias sem faturamento ou com faturamento 0).
Calcula o menor e maior faturamento entre os valores válidos.
Calcula a média mensal com base nos dias válidos e conta quantos dias tiveram faturamento acima dessa média.
Exemplo de Entrada: faturamento_diario = [100, 200, 0, 300, 400, 0, 0, 500, 600]

Exemplo de Saída:

Menor faturamento: R$100.00
Maior faturamento: R$600.00
Número de dias com faturamento acima da média mensal: 3
4. Função calcular_percentual_faturamento
Propósito: Calcula a porcentagem de contribuição de cada estado no faturamento mensal.

Lógica:

Soma o faturamento de todos os estados para obter o total.
Calcula o percentual de contribuição de cada estado em relação ao total.
Exemplo de Entrada:

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
Exemplo de Saída:

SP: 37.53%

RJ: 20.29%

MG: 16.19%

ES: 15.03%

Outros: 10.97%

5. Função inverter_string
Propósito: Inverte uma string fornecida.

Lógica:

Inicializa uma string vazia para armazenar o resultado invertido.
Adiciona cada caractere da string original à frente da string resultante em um loop.
Exibe a string original e a invertida.
Exemplo de Entrada: texto = "Exemplo de string"

Exemplo de Saída:

String original: Exemplo de string
String invertida: gnirts ed olpmexE
Fluxo Principal
O código executa todas as funções com exemplos de entradas fixas e exibe os resultados no console. Ele é modular, permitindo a reutilização das funções em outros contextos.
