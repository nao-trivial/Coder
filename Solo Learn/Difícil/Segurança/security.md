# Descrição

Você está encarregado da segurança em um cassino, e há um ladrão tentando roubar o dinheiro do cassino! Você deve verificar os diagramas de segurança para garantir que sempre haja um guarda entre o ladrão e o dinheiro. 

Há apenas um local com dinheiro, um ladrão, e qualquer número de guardas em cada andar do cassino.

## Tarefa

Avalie um andar do cassino para determinar se há um guarda entre o dinheiro e o ladrão. Se não houver, você deve soar o alarme.

## Formato de Entrada

Uma string de caracteres que inclui $ (dinheiro), T (ladrão), e G (guarda), que representa o layout do andar do cassino. 
Espaços no andar que não são ocupados por dinheiro, ladrão ou guarda são representados pelo caractere `x`.

## Formato de Saída

Uma string que diz 'ALARM' se o dinheiro estiver em perigo ou 'quiet' se o dinheiro estiver seguro.

## Exemplo de Entrada

xxxxxGxx$xxxT

## Exemplo de Saída

ALARM

## Explicação

- Na string 'xxxxxGxx$xxxT', o dinheiro ($) está à esquerda e o ladrão (T) está à direita. 
- Como não há um guarda (G) entre o dinheiro e o ladrão, o dinheiro está em perigo, e a saída será 'ALARM'.
- Se houvesse um guarda entre o ladrão e o dinheiro, a saída seria 'quiet', indicando que o dinheiro está seguro.
