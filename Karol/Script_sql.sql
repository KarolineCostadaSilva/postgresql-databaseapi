-- CREATE database livraria;
-- \c livraria -- comando semelhante a USE db_name em mysql
---------------------------------------------------
-- ver todas as tabelas criadas no banco de dados

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

---------------------------------------------------
CREATE TABLE IF NOT EXISTS book (
id SERIAL PRIMARY KEY,
title TEXT,
computation text,
height FLOAT,
width FLOAT);

CREATE TABLE IF NOT EXISTS person (
cpf VARCHAR(11) PRIMARY KEY,
name TEXT,
street TEXT,
number INTEGER,
apartment TEXT);

CREATE TABLE IF NOT EXISTS Loan (
id_loan SERIAL PRIMARY KEY,
loan_date DATE,
id_book INTEGER REFERENCES Book (id),
cpf VARCHAR(11) REFERENCES Person (cpf));

-------------------------------------------------------------

INSERT INTO Book (title, computation, height, width)
values
('Livro A', 'Dados', 20.0, 15.0),
('Livro B', 'Machine Learning', 18.5, 12.5),
('Livro C', 'Robotica', 22.0, 16.0);

INSERT INTO Person (cpf, name, street, number, apartment)
values
('11111111111', 'Fulano da Silva', 'Rua 1', 123, 'Apto 101'),
('22222222222', 'Beltrana Souza', 'Rua 2', 456, 'Apto 202');

insert into Loan (loan_date, id_book, cpf)
values
(CURRENT_DATE, 1, '11111111111'),
(CURRENT_DATE, 2, '22222222222'),
(CURRENT_DATE, 1, '11111111111');

--------------------------------------------------------------
select * from book;
select * from person;
select * from loan;

--------------------------------------------------------------
drop table book;
drop table person;
drop table loan;
