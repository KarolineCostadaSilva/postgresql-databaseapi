from abc import ABC, abstractmethod
from bd.python.carregar_bd import ManipuladorBD


class Repository(ABC):
    """Abstract class to connect to the database with model methods
    for other classes that inherit from it."""

    @abstractmethod
    def __init__(self):
        """When instantiated, a connection to the database will be established,
        which will be passed on to the inheriting classes."""

        self._bd = ManipuladorBD()

    @abstractmethod
    def add(self):
        """Abstract class method."""

    @abstractmethod
    def select(self):
        """Abstract class method."""

    @abstractmethod
    def update(self):
        """Abstract class method."""

    @abstractmethod
    def delete(self):
        """Abstract class method."""

    @abstractmethod
    def return_instances(self):
        """Abstract class method."""
