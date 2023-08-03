create database estande;

--------------------------------------------------------

--TABELA LIVRO
CREATE TABLE IF NOT EXISTS livro (
id_livro SERIAL PRIMARY KEY, --SERIAL é uma extensão específica do PostgreSQL para declarar colunas de identificação únicas 
genero TEXT,
altura float,
largura float);

--TABELA LEITOR
CREATE TABLE IF NOT EXISTS leitor (
cpf varchar(11) PRIMARY KEY,
nome TEXT,
rua TEXT,
numero float,
apartamento float);

--TABELA EMPRESTIMO
CREATE TABLE IF NOT EXISTS emprestimo (
id_emprestimo SERIAL PRIMARY KEY,
id_livro INTEGER REFERENCES livro (id_livro),
cpf VARCHAR(11) REFERENCES leitor (cpf));

--------------------------------------------------------

--POPULANDO AS TABELAS

--TABELA LIVRO
INSERT INTO livro (id_livro, genero, altura, largura) VALUES
(1, 'Processamento de Imagens', 15.0, 10.0),
(2, 'Programação Web', 20.0, 15.0),
(3, 'Robótica', 15.0, 10.0),
(4, 'Inteligência Artificial', 22.0, 10.0);

--TABELA LEITOR
INSERT INTO leitor (cpf, nome, rua, numero, apartamento) VALUES
(11111111111, 'Jefferson Lovis', 'Caxangá', 13, 22),
(22222222222, 'João Marcos', 'Itapissuma', 14, 23),
(33333333333, 'Karolina Juliana', 'Várzea', 15, 24),
(44444444444, 'Bruno Campello', 'Polidoro', 16, 25);

--TABELA EMPRESTIMO
INSERT INTO emprestimo (id_emprestimo, id_livro, cpf) VALUES
(1, 2, 22222222222),
(2, 4, 44444444444),
(3, 4, 33333333333),
(4, 1, 33333333333),
(5, 3, 11111111111),
(6, 2, 11111111111);

--------------------------------------------------------

--VER LISTA DE TABELAS CRIADAS
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'; --fornece a lista de tabelas existentes no esquema "public" do banco de dados conectado

--------------------------------------------------------

--OBSERVANDO AS TABELAS
SELECT * FROM livro;
SELECT * FROM leitor;
SELECT * FROM emprestimo;

--------------------------------------------------------

--CONSERTANDO O NOME DO COLEGA QUE CONFUNDI
UPDATE leitor
SET nome = 'Bruno Reis'
WHERE nome = 'Bruno Campello';
