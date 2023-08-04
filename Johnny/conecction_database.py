# biblioteca padrão para uso com o PostgreSQL
import psycopg2

def criar_tabelas(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS livro (
                        id_livro SERIAL PRIMARY KEY, 
                        genero TEXT,
                        altura float,
                        largura float);""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS leitor (
                        cpf varchar(11) 
                        PRIMARY KEY, 
                        nome TEXT, 
                        rua TEXT, 
                        numero float, 
                        apartamento float);""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS emprestimo (
                        id_emprestimo SERIAL PRIMARY KEY,
                        id_livro INTEGER REFERENCES livro (id_livro),
                        cpf VARCHAR(11) REFERENCES leitor (cpf));""")

def popular_tabelas(cursor):
    cursor.execute("""INSERT INTO livro (id_livro, genero, altura, largura) VALUES
                    (1, 'Processamento de Imagens', 15.0, 10.0),
                    (2, 'Programação Web', 20.0, 15.0),
                    (3, 'Robótica', 15.0, 10.0),
                    (4, 'Inteligência Artificial', 22.0, 10.0);""")
    
    cursor.execute("""INSERT INTO leitor (cpf, nome, rua, numero, apartamento) VALUES
                    (11111111111, 'Jefferson Lovis', 'Caxangá', 13, 22),
                    (22222222222, 'João Marcos', 'Itapissuma', 14, 23),
                    (33333333333, 'Karolina Juliana', 'Várzea', 15, 24),
                    (44444444444, 'Bruno Campello', 'Polidoro', 16, 25);""")
    
    cursor.execute("""INSERT INTO emprestimo (id_emprestimo, id_livro, cpf) VALUES
                    (1, 2, 22222222222),
                    (2, 4, 44444444444),
                    (3, 4, 33333333333),
                    (4, 1, 33333333333),
                    (5, 3, 11111111111),
                    (6, 2, 11111111111);""")
    
def updating_names(cursor):
    cursor.execute("""UPDATE leitor
                    SET nome = 'Bruno Reis'
                    WHERE nome = 'Bruno Campello';""")
    
    cursor.execute("""UPDATE leitor
                    SET nome = 'Karoline Juliana'
                    WHERE nome = 'Karolina Juliana';""")

def mostrar_tabela(cursor, tabela):
    cursor.execute(f"SELECT * FROM {tabela};")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="Softex2023",
            host="localhost",
            port="5432",  # porta padrão do PostgreSQL
            database="estande"
        )

        cursor = connection.cursor()

        while True:
            print("\n============= MENU =============")
            print("1. Criar tabelas (pré definidas)")
            print("2. Popular tabelas")
            print("3. Mostrar conteúdo de uma tabela")
            print("4. Atualizar dados")
            print("5. Sair")
            escolha = input("Escolha uma opção (1/2/3/4/5): ")

            if escolha == '1':
                criar_tabelas(cursor)
                print("\nTabelas criadas com sucesso!")
            elif escolha == '2':
                popular_tabelas(cursor)
                print("\nTabelas populadas com sucesso!")
            elif escolha == '3':
                tabela = input("\nDigite o nome da tabela (livro/leitor/emprestimo): ")
                mostrar_tabela(cursor, tabela)
            elif escolha == '4':
                print("\nNomes atualizados!")
                updating_names(cursor)
            elif escolha == '5':
                print("\nEncerrando o programa.")
                break
            else:
                print("\nOpção inválida. Por favor, escolha uma opção válida.")

        connection.commit()
        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL:", error)

if __name__ == "__main__":
    main()
