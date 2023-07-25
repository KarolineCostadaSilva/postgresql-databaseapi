import psycopg2 #instalação do módulo
from psycopg2 import Error

class conection():
    def __init__(self, user, password, host, port, database):
        # Connect to an existing database
        try:
            self.connection = psycopg2.connect(user = user,
                                                password = password,
                                                host = host,
                                                port = port,
                                                database = database)
            # Create a cursor to perform database operations
            self.cursor = self.connection.cursor()
            # Print PostgreSQL details
            print("PostgreSQL server information")
            print(self.connection.get_dsn_parameters(), "\n")
            # Executing a SQL query
            self.cursor.execute("SELECT version();")
            # Fetch result
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")


if __name__ == '__main__':
    conection()