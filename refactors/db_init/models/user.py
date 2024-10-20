from models.abs import ABSCRUDModel

class User(ABSCRUDModel):
    """
    ! This is the representation of an ABSCRUDModel.
    ? This class is used to define a user model.
    ? The user object is created empty, and the fields are set after calling Create or Read methods.
    """

    def __init__(self, db):
        """
        ! Initialize User with a database connection
        ? The user fields are set later through Create or Read.
        """
        super().__init__(db)
        self.id = None
        self.username = None
        self.dateBirth = None
        self.bio = None
        self.age = None

    def Migrate(self):
        """
        ! Creates the users table if it does not exist
        """
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username VARCHAR(50), 
                dateBirth DATE, 
                bio TEXT, 
                age INTEGER
            )
        """)

    def Create(self, username, date, bio, age):
        """
        ! Inserts a new user into the database
        ? Sets the user's fields after successful insertion.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "INSERT INTO users (username, dateBirth, bio, age) VALUES (?, ?, ?, ?)",
            (username, date, bio, age)
        )
        self.db.commit()

        # ? Retrieve the ID of the newly inserted user and update the object's fields
        self.id = cursor.lastrowid
        self.username = username
        self.dateBirth = date
        self.bio = bio
        self.age = age

    def Read(self, id):
        """
        ! Fetches a user from the database by ID and updates the object's fields
        ? Returns True if the user was found, False otherwise.
        """
        user = self.db.execute(
            "SELECT * FROM users WHERE id = ?", (id,)
        ).fetchone()

        if user:
            self.id = user['id']
            self.username = user['username']
            self.dateBirth = user['dateBirth']
            self.bio = user['bio']
            self.age = user['age']
            return True
        return False

    def Update(self, id, username=None, date=None, bio=None, age=None):
        """
        ! Updates fields of the user in the database.
        ? Only updates the fields that are provided.
        """
        if username is not None:
            self.db.execute("UPDATE users SET username = ? WHERE id = ?", (username, id))
        if date is not None:
            self.db.execute("UPDATE users SET dateBirth = ? WHERE id = ?", (date, id))
        if bio is not None:
            self.db.execute("UPDATE users SET bio = ? WHERE id = ?", (bio, id))
        if age is not None:
            self.db.execute("UPDATE users SET age = ? WHERE id = ?", (age, id))

    def Delete(self, id):
        """
        ! Deletes the user from the database by ID
        """
        self.db.execute("DELETE FROM users WHERE id = ?", (id,))
        self.db.commit()

    def __str__(self):
        """
        ! Returns a string representation of the user object
        """
        return f"User(id={self.id}, username={self.username}, dateBirth={self.dateBirth}, bio={self.bio}, age={self.age})"
