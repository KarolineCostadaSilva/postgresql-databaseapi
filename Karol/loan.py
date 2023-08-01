import datetime
from book import Book
from person import Person
class Loan:
    def __init__(self, loan_date, Book, Person):
        self.loan_date = loan_date
        self.id_book = Book.get_id()
        self.cpf = Person.get_cpf()

    # get
    def get_loan_date(self):
        return self.loan_date

    def get_id_book(self):
        return self.id_book

    def get_cpf(self):
        return self.cpf

    # set
    def set_loan_date(self):
        self.loan_date = datetime.date.today()
        return 'Loan date changed successfully!'

    def set_id_book(self, id_book):
        self.id_book = id_book
        return 'Book ID changed successfully!'

    def set_cpf(self, cpf):
        self.cpf = cpf
        return 'CPF changed successfully!'
