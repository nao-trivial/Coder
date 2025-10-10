# Análise do Código de Simulação Financeira - Hovercrafts

## Código Completo
```python
vendas = int(input())

# produção de 10 hovercrafts
gastos = 2 * 10 ** 6 * 10 

# seguro
gastos += 1 * 10 ** 6 
lucro = vendas * 3 * 10 ** 6

if lucro == gastos:
   print("Broke Even")
elif lucro < gastos:
   print("Loss")
elif lucro > gastos:
   print("Profit")
```

🔍 Explicação Passo a Passo

1. Entrada de Dados

```python
vendas = int(input())
```

· Captura o número de hovercrafts vendidos (entrada do usuário)
· int() converte o input para número inteiro

2. Cálculo de Gastos

```python
gastos = 2 * 10 ** 6 * 10
```

· Custo de produção: $2.000.000 por hovercraft × 10 unidades
· Notação científica: 10 ** 6 = 1.000.000 (1 milhão)
· Total: $20.000.000 em produção

```python
gastos += 1 * 10 ** 6
```

· Acréscimo de $1.000.000 em seguro
· Operador += adiciona ao valor existente
· Total de gastos: $21.000.000

3. Cálculo de Lucro

```python
lucro = vendas * 3 * 10 ** 6
```

· Receita por venda: $3.000.000 por hovercraft
· Lucro total = Vendidos × $3.000.000

4. Análise Financeira

```python
if lucro == gastos:
   print("Broke Even")
elif lucro < gastos:
   print("Loss")
elif lucro > gastos:
   print("Profit")
```

· Broke Even: Empate (receita = despesas)
· Loss: Prejuízo (receita < despesas)
· Profit: Lucro (receita > despesas)

💡 Pontos de Aprendizado

Conceitos Matemáticos

· Notação exponencial: 10 ** 6 = 1.000.000
· Ordem das operações
· Comparações numéricas (> , < , ==)

Programação

1. Tipos de dados: Conversão com int()
2. Operadores:
   · Aritméticos: * ** +=
   · Comparação: == < >
3. Estruturas de controle:
   · if/elif para decisões múltiplas
   · Condicionais encadeadas

📊 Exemplo Prático

Cenário 1: 7 Vendas

```
Gastos: $21.000.000
Lucro: 7 × 3.000.000 = $21.000.000
Resultado: "Broke Even"
```

Cenário 2: 5 Vendas

```
Gastos: $21.000.000
Lucro: 15.000.000
Resultado: "Loss"
```

Cenário 3: 10 Vendas

```
Gastos: $21.000.000
Lucro: 30.000.000
Resultado: "Profit"
```

🚀 Melhorias Possíveis

1. Adicionar validação de entrada negativa
2. Mostrar valores calculados
3. Incluir margem de lucro percentual
4. Criar simulação com variáveis de custo ajustáveis

---

Última atualização: 10/10/2025

```

Este material:
- Explica o código linha por linha
- Destaca conceitos matemáticos e de programação
- Oferece exemplos práticos
- Sugere melhorias futuras
- Usa formatação clara para melhor compreensão

Você pode adaptar as seções conforme a necessidade específica da sua turma!
```