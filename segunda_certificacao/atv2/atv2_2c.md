# 🧮 ATIVIDADE AVALIATIVA 2 — 2ª CERTIFICAÇÃO  
### 💡 Valor: **1,0 ponto** — *Trabalho em trio*

---

## 🥅 Exercício 1

Considere que a lista `gols = [2, 0, 4, 1, 4]` contém o número de gols marcados por um time em 5 partidas do campeonato.  

Crie um programa em **Python** que utilize essa lista para:

- Indicar o **maior número de gols marcados** em uma partida.

> 💬 **Dica:**  
> A estratégia para encontrar o maior valor de uma lista é parecida com a de pesquisa.  
> Em vez de usar uma variável para indicar se achou, usa-se uma variável para indicar o **maior valor atual**, comparando-a a cada elemento da lista.  
> Veja o exemplo no arquivo `pesquisa_lista.py` como referência.

### 💻 Exemplo de execução
```python
Gols marcados nas partidas: [2, 0, 4, 1, 4]
Maior número de gols: 4
```

---

## 🎓 Exercício 2

Crie um programa em **Python** que armazene informações sobre **3 alunos**, onde cada aluno deve conter:  
- Nome (*string*),  
- Nota 1 (*float*),  
- Nota 2 (*float*).

> 💬 **Dica:**  
> Crie uma **lista** para cada aluno e depois uma lista chamada `turma` que contenha os alunos criados.  
> Veja o exemplo do arquivo `lista_de_listas.py` se não lembrar como fazer isso.

O programa deve:

- Exibir o **nome**, **notas** e **média** de cada aluno;  
- Calcular e mostrar a **média geral da turma**.

### 💻 Exemplo de execução
```
=== RELATÓRIO DE NOTAS ===
Aluno: Ana
Nota 1: 8.0
Nota 2: 7.5
Média: 7.75
--------------------
Aluno: Bruno
Nota 1: 6.0
Nota 2: 5.5
Média: 5.75
--------------------
Aluno: Carla
Nota 1: 9.0
Nota 2: 8.5
Média: 8.75
--------------------
Média geral da turma: 7.42
```

---

## 🧑‍💻 Exercício 3

Modifique o programa do **Exercício 2** para permitir que os **usuários cadastrem os alunos**, em vez de iniciar com os alunos já cadastrados.

O programa agora deve:

- Permitir o **cadastro** até o usuário digitar `"sair"` no campo do nome;  
- Exibir o nome, notas e média de cada aluno;  
- Calcular e mostrar a **média geral da turma**.

### 💻 Exemplo de execução
```
=== Cadastro de Alunos ===
Digite "sair" para encerrar o cadastro.

Nome do aluno: Ana
Nota 1: 8
Nota 2: 7.5
-------------------------
Nome do aluno: Bruno
Nota 1: 6
Nota 2: 5.5
-------------------------
Nome do aluno: Carla
Nota 1: 9
Nota 2: 8.5
-------------------------
Nome do aluno: sair

=== RELATÓRIO DE NOTAS ===

Aluno: Ana
Nota 1: 8.0
Nota 2: 7.5
Média: 7.75
--------------------
Aluno: Bruno
Nota 1: 6.0
Nota 2: 5.5
Média: 5.75
--------------------
Aluno: Carla
Nota 1: 9.0
Nota 2: 8.5
Média: 8.75
--------------------
Média geral da turma: 7.42
```

---

## ⚽ Exercício 4

Modifique o programa do **Exercício 1** para permitir que o **usuário informe o número de gols** marcados pelo time em várias partidas (quantidade definida pelo usuário).

O programa agora deve:

- Solicitar ao usuário **quantas partidas** deseja registrar;  
- Ler o número de **gols em cada partida** e armazenar em uma lista;  
- Exibir todos os valores da lista;  
- Indicar o **maior número de gols marcados**.

### 💻 Exemplo de execução
```
Quantas partidas deseja registrar? 6
Quantos gols o time marcou na 1ª partida? 1
Quantos gols o time marcou na 2ª partida? 3
Quantos gols o time marcou na 3ª partida? 0
Quantos gols o time marcou na 4ª partida? 2
Quantos gols o time marcou na 5ª partida? 3
Quantos gols o time marcou na 6ª partida? 1

Gols marcados nas partidas: [1, 3, 0, 2, 3, 1]
Maior número de gols: 3
```
