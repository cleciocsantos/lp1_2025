# 🐍 Atividade Avaliatva 3

---

## 🧮 Questão 1 — Validação de número inteiro

Crie a função `valida_inteiro(mínimo, máximo)` que lê um número inteiro do teclado e o retorna **se ele estiver entre o mínimo e o máximo**.  

Caso o número **não esteja dentro dos limites estabelecidos** ou o usuário **digitar algo diferente de um número inteiro**, a função deve pedir novamente para digitar até que o número obedeça ao critério.  

Utilize **exceções** para lidar com os erros dentro da função.

**💡 Exemplo de uso esperado:**
```python
numero = valida_inteiro(1, 10)
print(f"Você digitou: {numero}")
```

---

## 🎓 Questão 2 — Simulação de notas de uma turma

Crie um programa em Python que simule as **notas de uma turma** em uma prova.

O programa deve:

1. Sortear **notas aleatórias entre 0 e 10** para **10 alunos**;  
2. Armazenar as notas em uma **lista**;  
3. Exibir **todas as notas sorteadas**;  
4. Calcular e mostrar:
   - a **média da turma**;  
   - a **maior** e a **menor** nota;  
   - a **quantidade de alunos acima da média**;  
   - a **quantidade de aprovados e reprovados**, considerando **média 6,0** como aprovação.  

O programa deve utilizar **funções** para organizar as tarefas.

**💻 Dica:**  
Use o módulo `random` para gerar as notas aleatórias e crie funções para:
- gerar as notas;
- calcular estatísticas;
- classificar aprovados e reprovados;
- exibir os resultados.
