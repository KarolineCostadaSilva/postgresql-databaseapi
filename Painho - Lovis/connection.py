from mysql.connector import Error
import mysql.connector as MC


class ConnectDB():
    """Class with methods to establish a connection to the database"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        self.configure_db()
        self.connect = MC.connect(**self.con)
        self.cursor = self.connect.cursor()

    def configure_db(self):
        """Stores the parameters for accessing the Database"""
        try:
            self.con = {
                'host': "localhost",
                'user': "root",
                'passwd': "Softex2023",
                'database': "farmacia"}
            # print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: {err}")

    def execute(self, query, values=None):
        """Executes the connection to the database"""
        self.cursor.execute(query, values)
        self.cursor.commit()

    def disconnect(self):
        """Closes the database"""
        self.cursor.close()