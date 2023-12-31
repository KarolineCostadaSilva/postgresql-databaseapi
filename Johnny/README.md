# JOHNNY CLEITON

<div>
  <div style="display: inline_block"><br>
    <img align="center" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain.svg" /> -- foi criado o minimundo abaixo para que possam ser modeladas e construídas tabelas com python utilizando o PostgreSQL.
  </div>
</div>



## MINIMUNDO

Rielson gostaria de construir um banco de dados para testar suas habilidades, então ele definiu um problema que tinha uma estante com livros de computação, altura, largura e um identificador para cada livro que estava nela, e uma pessoa que adora ler que tem um nome, um CPF, um endereço com rua, número e apartamento. Rielson decidiu que as regras seriam: a pessoa pode pegar quantos livros quiser da estante e mais de uma pessoa poderia tirar livros da estante.

#### Tarefas:

- Fazer modelo relacional e lógico do minimundo.
- Construir um arquivo de conexão com o PostgreSQL.
- Construir e popular as tabelas com Python.
- Fazer algumas consultas simples como:
    - Quantos livros tem na estante?
    - Qual pessoa pegou qual livro?
    - Onde está este livro? (retornar endereço da pessoa que pegou o livro)

## MODELAGEM

Identificando as ENTIDADES seguidas de seus ATRIBUTOS:

- LIVRO - ID, gênero (literário), altura, largura
- LEITOR - CPF, nome, rua, número, apartamento

|  LIVRO   |          |          |          |  
| -------- | -------- | -------- | -------- | 
| ID_livro | genero   | altura   | largura  |          

|  LEITOR  |          |          |          |              | 
| -------- | -------- | -------- | -------- | ------------ | 
|   CPF    |   nome   |   rua    |  numero  | apartamento  | 

Como o enunciado fala da situação de retirada de livros da estante por diversas pessoas, foi necessário criar uma nova entidade chamada EMPRÉSTIMO onde liga o identificador do livro com o identificador (CPF) do leitor.

- EMPRESTIMO - ID_empréstimo, ID_livro, CPF

| EMPRESTIMO     |          |          |     
| -------------- | -------- | -------- | 
| ID_emprestimo  | ID_livro |   CPF    |

### Modelo Conceitual

Para explicar melhor o relacionamento entre as entidades, foi elaborado um diagrama ENTIDADE-RELACIONAMENTO (ER) referente ao modelo conceitual do Banco de Dados do enunciado. O diagrama pode ser conferido abaixo:


<div style="display: block"><br>
  <img  height="250" alt="coding-time" src="assets/modelo-conceitual.png">
</div>

### Modelo Lógico

Em seguida foi feita a conversão da modelagem conceitual para a lógica onde é possível ver as chaves estrangeiras e o tipo de cada atributo. O diagrama pode ser conferido abaixo:

<div style="display: block"><br>
  <img  height="250" alt="coding-time" src="assets/modelo-logico.png">
</div>

### Modelagem Física (SQL)

Por último foi realizada a modelagem física na linguagem SQL, onde foi criada uma database chamada de "estande" com as tabelas das entidades representadas nos modelos anteriores. O Script do SQL pode ser conferido [aqui](https://github.com/KarolineCostadaSilva/postgresql-databaseapi/blob/main/Johnny/Script.sql).

## CODIFICAÇÃO EM PYTHON

Para construir um arquivo de conexão com o PostgreSQL utilizando Python, foi necessário instalar a biblioteca "psycopg2". Após isso, foi realizada uma codificação básica que demonstra a conexão com o banco de dados seguida da criação e população das tabelas. O código pode ser conferido [aqui](https://github.com/KarolineCostadaSilva/postgresql-databaseapi/blob/main/Johnny/conecction_database.py) e conta com um simples menu em que o usuário pode comandar as seguintes tarefas: criação das tabelas, população das tabelas e opção de mostrar conteúdo de uma tabela em específico.
