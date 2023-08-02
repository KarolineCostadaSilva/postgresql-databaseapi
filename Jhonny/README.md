# JOHNNY CLEITON

<div>
  <div style="display: inline_block"><br>
    <img align="center" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain.svg" /> -- foi criado o minimundo abaixo para que possam ser modeladas e construídas tabelas com python utilizando o PostgreSQL.
  </div>
</div>



### Minimundo

Rielson gostaria de construir um banco de dados para testar suas habilidades, então ele definiu um problema que tinha uma estante com livros de computação, altura, largura e um identificador para cada livro que estava nela, e uma pessoa que adora ler que tem um nome, um CPF, um endereço com rua, número e apartamento. Rielson decidiu que as regras seriam: a pessoa pode pegar quantos livros quiser da estante e mais de uma pessoa poderia tirar livros da estante.

#### Tarefas:

- Fazer modelo relacional e lógico do minimundo.
- Construir um arquivo de conexão com o PostgreSQL.
- Construir e popular as tabelas com Python.
- Fazer algumas consultas simples como:
    - Quantos livros tem na estante?
    - Qual pessoa pegou qual livro?
    - Onde está este livro? (retornar endereço da pessoa que pegou o livro)

## Modelo Relacional

Identificando as ENTIDADES seguidas de seus ATRIBUTOS:

- LIVRO - ID, gênero (literário), altura, largura
- LEITOR - cpf, nome, rua, número, apartamento

|  LIVRO   |          |          |          |  
| -------- | -------- | -------- | -------- | 
|     ID   | gênero   | altura   | largura  |          

|  LEITOR  |          |          |          |              | 
| -------- | -------- | -------- | -------- | ------------ | 
|   CPF    |   nome   |   rua    |  número  | apartamento  | 

Como o enunciado fala da situação de retirada de livros da estante por diversas pessoas, foi necessário criar uma nova entidade chamada EMPRÉSTIMO onde liga o identificador do livro com o identificador (CPF) do leitor.

- EMPRESTIMO - ID_empréstimo, ID_livro, cpf

| EMPRESTIMO     |          |          |     
| -------------- | -------- | -------- | 
| ID_emprestimo  | ID_livro |   cpf    |

## Modelo Conceitual

Para explicar melhor o relacionamento entre as entidades, foi elaborado um diagrama ENTIDADE-RELACIONAMENTO (ER) referente ao modelo conceitual do Banco de Dados do enunciado.



