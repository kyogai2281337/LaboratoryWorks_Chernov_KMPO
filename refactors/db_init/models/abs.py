from abc import ABC, abstractmethod

class ABSCRUDModel(ABC):
    """
    ! An abstract base class for models providing CRUD operations.
    ? All models inheriting from this class should implement the CRUD operations.
    """

    def __init__(self, db):
        """
        ! Initialize with a database connection.
        :param db: The database connection.
        """
        self.db = db

    @abstractmethod
    def Migrate(self):
        """
        ! Migrate the database schema for the model.
        ? This method should handle creating or altering database tables.
        """
        pass

    @abstractmethod
    def Create(self):
        """
        ! Create a new entry in the database.
        """
        pass

    @abstractmethod
    def Read(self, id=None):
        """
        ! Read a record from the database.
        :param id: ID of the record to read (optional).
        """
        pass

    @abstractmethod
    def Update(self, id, **kwargs):
        """
        ! Update an existing record in the database.
        :param id: ID of the record to update.
        :param kwargs: Fields to update.
        """
        pass

    @abstractmethod
    def Delete(self, id):
        """
        ! Delete a record from the database.
        :param id: ID of the record to delete.
        """
        pass
