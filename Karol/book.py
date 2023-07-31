class Book:
    def __init__(self, title, computation, height, width):
        self.title = title
        self.computation = computation
        self.height = height
        self.width = width

    # get
    def get_title(self):
        return self.title

    def get_computation(self):
        return self.computation

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    # set
    def set_title(self, title):
        self.title = title
        return 'Title changed successfully!'

    def set_computation(self, computation):
        self.computation = computation
        return 'Computation changed successfully!'

    def set_height(self, height):
        self.height = height
        return 'Height changed successfully!'

    def set_width(self, width):
        self.width = width
        return 'Width changed successfully!'