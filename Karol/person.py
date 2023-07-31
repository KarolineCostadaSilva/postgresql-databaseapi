class Person:
    def __init__(self, cpf, name, street, number, apartment):
        self.cpf = cpf
        self.name = name
        self.street = street
        self.phone_number = number
        self.apartment = apartment

    # get
    def get_cpf(self):
        return self.cpf

    def get_name(self):
        return self.name

    def get_street(self):
        return self.street

    def get_phone_number(self):
        return self.phone_number

    def get_apartment(self):
        return self.apartment

    # set
    def set_cpf(self, cpf):
        self.cpf = cpf
        return 'CPF changed successfully!'

    def set_name(self, name):
        self.name = name
        return 'Name changed successfully!'

    def set_street(self, street):
        self.street = street
        return 'Street changed successfully!'

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
        return 'Phone number changed successfully!'

    def set_apartment(self, apartment):
        self.apartment = apartment
        return 'Apartment changed successfully!'

