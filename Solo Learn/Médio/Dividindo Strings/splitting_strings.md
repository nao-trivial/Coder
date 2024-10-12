# Tarefa: Dividir uma Palavra em Partes Iguais

## Descrição

Você recebe uma palavra e deseja dividi-la em partes iguais, de acordo com um número fornecido, sendo cada parte do tamanho desse número.

## Objetivo

Escreva um programa que receba uma string e um número como entrada. Divida a string em partes iguais com base no número fornecido e exiba as partes separadas por hífens. A última parte do resultado conterá o restante, já que a string de entrada pode não se dividir uniformemente pelas partes fornecidas.

## Formato de Entrada

Dois inputs:
1. Uma string.
2. Um número inteiro.

## Formato de Saída

Uma string representando as partes separadas por hífens.

## Exemplo de Entrada

```plaintext
hello
2

Exemplo de Saída

he-ll-o

Explicação

A string hello foi dividida em partes de tamanho 2.

As partes são: he, ll e o.

O resultado é: he-ll-o.


Dicas

1. Utilize um laço para iterar pela string e dividi-la em partes do tamanho fornecido.


2. Caso a string não possa ser dividida igualmente, a última parte conterá o restante dos caracteres.

