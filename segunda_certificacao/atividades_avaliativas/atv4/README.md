# Atividade Avaliativa 4 -- Processamento de Arquivo em Python

Crie uma função em Python que leia um arquivo de texto chamado
**comandos.txt**.\
Cada linha desse arquivo representará um comando que o programa deve
interpretar e executar.

## Formato do arquivo

O arquivo **comandos.txt** poderá conter linhas nos seguintes formatos:

1.  `SOMA x y` -- o programa deve exibir a soma de x e y
2.  `MULT x y` -- o programa deve exibir o produto de x e y
3.  `DOBRO x` -- o programa deve exibir o dobro de x
4.  `TEXTO mensagem...` -- o programa deve imprimir a mensagem
    exatamente como está após o comando
5.  `SAIR` -- quando o programa ler este comando, deve parar
    imediatamente

## Exemplo de arquivo comandos.txt

    TEXTO Iniciando operações...
    SOMA 10 5
    MULT 7 3
    DOBRO 9
    TEXTO Finalizando cálculos
    SAIR
    SOMA 1 1   # Esta linha não deve ser executada

## O que a função deve fazer

1.  Abrir o arquivo `comandos.txt` para leitura.
2.  Ler linha por linha.
3.  Identificar o comando (primeira palavra da linha).
4.  Executar a ação correspondente.
5.  Tratar erros simples, como:
    -   linhas vazias\
    -   comandos desconhecidos\
    -   números faltando

## Saída esperada (para o exemplo acima)

    Iniciando operações...
    15
    21
    18
    Finalizando cálculos

## Desafio extra (opcional)

-   Armazene todas as respostas num arquivo de saída **resultado.txt**.
-   Conte quantas operações matemáticas foram realizadas.
-   Permita comentários no arquivo (linhas começando com `#` devem ser
    ignoradas\`).
