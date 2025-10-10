# Análise do Código de Conversão de Moeda

## Código Completo
```python
pesos = int(input())
dollars = int(input())

# 1 peso = 0.02 dollars
exchange = 0.02 * pesos 

if exchange > dollars:
    print("Dollars")
else:
    print("Pesos")
```

## 🔍 Explicação Passo a Passo

1. Entrada de Dados

```python
pesos = int(input())
dollars = int(input())
```

· Recebe dois valores do usuário:
  · Quantidade em pesos
  · Quantidade em dólares
· int() garante que os valores sejam números inteiros

## 2. Conversão de Moeda

```python
exchange = 0.02 * pesos
```

· Taxa de câmbio fixa: 1 peso = 0.02 dólares
· Converte o valor em pesos para dólares
· Exemplo: 100 pesos = 100 × 0.02 = 2 dólares

## 3. Tomada de Decisão

```python
if exchange > dollars:
    print("Dollars")
else:
    print("Pesos")
```

· Compara o valor convertido com os dólares disponíveis
· Dollars: é melhor levar dólares (quando o valor convertido é maior)
· Pesos: é melhor manter pesos (quando o valor convertido é menor ou igual)

###💡 Pontos de Aprendizado

Conceitos Matemáticos

· Conversão de moeda e taxas de câmbio
· Multiplicação com decimais: 0.02 × quantidade
· Comparação entre valores monetários

Programação

1. Múltiplas entradas: Como receber vários inputs
2. Operadores:
   · Aritméticos: * (multiplicação)
   · Comparação: > (maior que)
3. Estruturas condicionais:
   · if/else para decisões binárias
   · Condicional simples com dois caminhos

## 📊 Exemplos Práticos

Cenário 1: 500 pesos vs 8 dólares

```
Pesos: 500
Dólares: 8
Conversão: 500 × 0.02 = 10 dólares
10 > 8 → "Dollars"
```

Cenário 2: 300 pesos vs 10 dólares

```
Pesos: 300
Dólares: 6
Conversão: 300 × 0.02 = 6 dólares
6 == 6 → "Pesos"
```

Cenário 3: 200 pesos vs 5 dólares

```
Pesos: 200
Dólares: 5
Conversão: 200 × 0.02 = 4 dólares
4 < 5 → "Pesos"
```

## 🎯 Objetivo do Programa

Decidir qual moeda oferece maior valor de compra:

· Se pesos convertidos valem mais → escolher "Dollars"
· Se dólares valem mais ou igual → escolher "Pesos"

## ⚠️ Observações Importantes

Sobre a Taxa de Câmbio

· O código usa taxa fixa (0.02)
· Na realidade, taxas de câmbio variam constantemente
· Esta é uma simplificação para fins educacionais

Comportamento do Else

```python
else:
    print("Pesos")
```

· Esta condição cobre dois casos:
  · exchange < dollars (valor convertido é menor)
  · exchange == dollars (valores são iguais)
· Em ambos, a escolha é "Pesos"

## 🚀 Melhorias Possíveis

1. Taxa de câmbio variável:

```python
taxa = float(input("Digite a taxa de câmbio: "))
```

1. Mostrar valores calculados:

```python
print(f"Valor convertido: {exchange} dólares")
```

1. Validação de entrada:

```python
if pesos < 0 or dollars < 0:
    print("Erro: valores não podem ser negativos")
```

1. Casos decimais:

```python
pesos = float(input())  # Permitir valores decimais
```

---

Última atualização: {data}

```

Este material inclui:
- Explicação detalhada de cada parte do código
- Exemplos práticos com cálculos
- Conceitos matemáticos e de programação
- Observações sobre limitações e melhorias
- Formatação clara para facilitar o aprendizado

Você pode adaptar conforme o nível dos seus alunos e adicionar mais exemplos se necessário!
```