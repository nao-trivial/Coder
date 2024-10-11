# Descrição

Se uma frase flui, a primeira letra de cada palavra será a mesma que a última letra da palavra anterior.

## Tarefa

Escreva um programa que receba uma string contendo uma frase e verifique se a primeira letra de cada palavra é a mesma que a última letra da palavra anterior. Se a condição for atendida, o programa deve retornar 'true'; caso contrário, ele deve retornar 'false'. O programa deve ignorar a diferenciação entre maiúsculas e minúsculas.

## Formato de Entrada

Uma string contendo uma frase com várias palavras.

## Formato de Saída

Uma string: 'true' ou 'false'.

## Exemplo de Entrada

this string gets stuck

## Exemplo de Saída

true

## Explicação

- A frase contém as palavras: "this", "string", "gets", "stuck".
- A última letra de "this" é "s", que é a mesma que a primeira letra de "string".
- A última letra de "string" é "g", que é a mesma que a primeira letra de "gets".
- A última letra de "gets" é "s", que é a mesma que a primeira letra de "stuck".
- Como todas as condições são atendidas, o programa retorna 'true'.

- Se, em algum ponto, a última letra de uma palavra não corresponder à primeira letra da palavra seguinte, o programa retornará 'false'.