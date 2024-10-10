# Descrição

Você administra uma fábrica de hovercrafts. Sua fábrica fabrica dez hovercrafts por mês. Dado o número de clientes que você conseguiu nesse mês, será que você obteve lucro? Custa 2.000.000 para construir um hovercraft, e você os vende por 3.000.000 cada. Além disso, você paga 1.000.000 a cada mês em seguro.

## Tarefa

Determine se você obteve lucro, prejuízo ou se ficou no ponto de equilíbrio com base em quantos dos dez hovercrafts você conseguiu vender no mês.

## Formato de Entrada

Um número inteiro que representa o número de hovercrafts vendidos naquele mês.

## Formato de Saída

Uma string que diz 'Profit' (Lucro), 'Loss' (Prejuízo) ou 'Broke Even' (Empatou).

## Exemplo de Entrada

5

## Exemplo de Saída

Loss

## Explicação

- O custo para fabricar 10 hovercrafts é de 20.000.000 (10 * 2.000.000).
- O custo do seguro é de 1.000.000, totalizando 21.000.000 de custos fixos no mês.
- Se você vendeu 5 hovercrafts, a receita foi de 15.000.000 (5 * 3.000.000).
- Como a receita (15.000.000) foi menor que os custos (21.000.000), o resultado foi um prejuízo ('Loss').

- Se o número de vendas gerar uma receita igual aos custos totais, o resultado será 'Broke Even'.
- Se a receita for maior que os custos, o resultado será 'Profit'.
