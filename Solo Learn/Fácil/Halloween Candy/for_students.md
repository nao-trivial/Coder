
## 📌 Introdução

Este código resolve um problema matemático simples mas fundamental em programação: cálculo de percentual com arredondamento para cima. O contexto é de um cenário onde precisamos determinar uma quantidade mínima para atingir uma meta específica.

## 🔍 Objetivo do Código

Calcular qual percentual de casas representa pelo menos 50% da população, considerando que cada visita deve ser a uma casa diferente.

## 📝 Explicação do Código

```python
houses = int(input())
```

Entrada de dados: Captura o número total de casas.

```python
resultado = (2 * 100)/houses
```

Cálculo base:

· 2 * 100 = 200 (representa 200% quando distribuído igualmente)
· Dividido pelo número de casas = percentual por casa
· Por que 2? Porque precisamos de pelo menos 50% + 1 (para garantir maioria)

```python
if resultado > int(resultado):
    resultado += 1
    print(int(resultado))
else:
    print(int(resultado))
```

### Lógica de arredondamento:

· Se o resultado tem parte decimal → arredonda para cima
· Se é inteiro → mantém o valor

## 🎯 Importância Pedagógica

1. Conversão de Tipos

```python
int(input())  # string → inteiro
int(resultado) # float → inteiro
```

Conceito: Manipulação de tipos de dados é fundamental em programação.

2. Lógica de Arredondamento

```python
if resultado > int(resultado):
    resultado += 1
```

Conceito: Demonstra como implementar arredondamento customizado quando funções built-in não estão disponáveis.

3. Pensamento Matemático

· Compreensão de percentuais
· Cálculo de maioria simples (50% + 1)
· Diferença entre valores inteiros e decimais

4. Estruturas de Controle

· Uso de if/else para tomada de decisão
· Condições baseadas em comparação numérica

## 💡 Aplicações Práticas

Cenários Reais:

· Sistemas eleitorais: Calcular votos mínimos para vitória
· Business intelligence: Metas de vendas por região
· Jogos: Pontuação mínima para passar de fase
· Distribuição: Recursos por unidade

## 🚀 Versão Otimizada

```python
import math

houses = int(input())
percent_per_house = 100 / houses
min_houses = math.ceil(50 / percent_per_house)
print(min_houses)
```

## 📚 Lições Aprendidas

1. Arredondamento manual vs funções especializadas
2. Conversão implícita entre float e int
3. Projeto de algoritmos para problemas matemáticos
4. Clareza de código vs otimização prematura

🎓 Exercícios Sugeridos

1. Modifique para calcular 60% em vez de 50%
2. Implemente usando math.ceil()
3. Adicione validação para entrada zero
4. Crie versão que retorna fração em vez de percentual

---

Este código é um excelente exemplo introdutório para: programação básica, manipulação numérica e resolução de problemas do mundo real com abordagem computacional.