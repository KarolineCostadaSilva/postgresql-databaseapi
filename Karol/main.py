from database_manager import DatabaseManager

db_name = "livraria"
db_user = "postgres"
db_password = "Softex2023"
db_host = "localhost"
db_port = "5432"

db_manager = DatabaseManager(db_name, db_user, db_password, db_host, db_port)

# Criar e popular as tabelas
db_manager.create_tables()
db_manager.populate_tables()
# db_manager.drop_tables()

# Consultas
num_books = db_manager.count_books()
print(f"Total de livros na estante: {num_books}")

books_by_person = db_manager.get_books_by_person()
print("Livros emprestados por pessoa:")
for person, book in books_by_person:
    print(f"{person}: {book}")

book_id = 2  # Exemplo de ID de livro para obter a localização
location = db_manager.get_book_location(book_id)
print(f"A localização do livro de ID {book_id} é: {location}")

db_manager.close_connection()
