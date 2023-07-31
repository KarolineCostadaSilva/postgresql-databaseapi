from book import Book
from person import Person
from loan import Loan
import psycopg2

class DatabaseManager:
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.conn = self.connect_to_db()

    def connect_to_db(self):
        try:
            conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            print("Database connection established.")
            return conn
        except psycopg2.Error as e:
            print("Error connecting to database:", e)
            return None

    # Cria as tabelas no banco de dados
    def create_tables(self):
        try:
            cursor = self.conn.cursor()

            # Tabela Livro
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Book (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    height FLOAT,
                    width FLOAT
                )
            """)

            # Tabela Pessoa
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Person (
                    cpf VARCHAR(11) PRIMARY KEY,
                    name TEXT,
                    street TEXT,
                    number INTEGER,
                    apartment TEXT
                )
            """)

            # Tabela Emprestimo
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Loan (
                    id_loan SERIAL PRIMARY KEY,
                    loan_date DATE,
                    id_book INTEGER REFERENCES Book (id),
                    cpf VARCHAR(11) REFERENCES Person (cpf)
                )
            """)

            # Comitando as alterações
            self.conn.commit()

            print("Tabelas criadas com sucesso.")
        except psycopg2.Error as e:
            print("Erro ao criar as tabelas:", e)
            self.conn.rollback()

    def populate_tables(self):
        try:
            cursor = self.conn.cursor()

            # Inserindo dados na tabela Livro
            cursor.execute("""
                INSERT INTO Book (title, height, width)
                VALUES
                    ('Livro A', 20.0, 15.0),
                    ('Livro B', 18.5, 12.5),
                    ('Livro C', 22.0, 16.0)
            """)

            # Inserindo dados na tabela Pessoa
            cursor.execute("""
                INSERT INTO Person (cpf, name, street, number, apartment)
                VALUES
                    ('11111111111', 'Fulano da Silva', 'Rua 1', 123, 'Apto 101'),
                    ('22222222222', 'Beltrana Souza', 'Rua 2', 456, 'Apto 202')
            """)

            # Comitando as alterações
            self.conn.commit()

            print("Dados populados nas tabelas com sucesso.")
        except psycopg2.Error as e:
            print("Erro ao popular as tabelas:", e)
            self.conn.rollback()

    def count_books(self):
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM Book")
            count = cursor.fetchone()[0]

            return count
        except psycopg2.Error as e:
            print("Erro ao contar os livros:", e)
            return None

    def get_books_by_person(self):
        try:
            cursor = self.conn.cursor()

            cursor.execute("""
                SELECT p.name, b.title
                FROM Loan l
                JOIN Person p ON l.person_cpf = p.cpf
                JOIN Book b ON l.book_id = b.id
            """)
            books_by_person = cursor.fetchall()

            return books_by_person
        except psycopg2.Error as e:
            print("Erro ao obter os livros por pessoa:", e)
            return None

    def get_book_location(self, book_id):
        try:
            cursor = self.conn.cursor()

            cursor.execute("""
                SELECT p.street, p.number, p.apartment
                FROM Loan l
                JOIN Person p ON l.person_cpf = p.cpf
                WHERE l.book_id = %s
            """, (book_id,))
            location = cursor.fetchone()

            return location
        except psycopg2.Error as e:
            print("Erro ao obter a localização do livro:", e)
            return None

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexão com o banco de dados encerrada.")
