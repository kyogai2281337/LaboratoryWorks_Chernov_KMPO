from db.models.abs import ABSCRUDModel

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
        self.phone = None
        self.username = None
        self.dateBirth = None
        self.bio = None
        self.age = None
        self.role = None # * db or chart
        self.passwd = None

    def GetList(self):
        """
        ! Returns a list of all users in the database
        ? The list is limited by the limit parameter.
        ? The page parameter specifies the page number.
        """
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT id, username, dateBirth, bio, age, role, phone FROM users")
        users = []
        for row in cursor.fetchall():
            user = User(self.db)
            user.id = row['id']
            user.username = row['username']
            user.dateBirth = row['dateBirth']
            user.bio = row['bio']
            user.age = row['age']
            user.role = row['role']
            user.phone = row['phone']
            users.append(user)
        return users

    def Migrate(self):
        """
        ! Creates the users table if it does not exist
        """
        self.db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username VARCHAR(50), 
                dateBirth DATE, 
                phone VARCHAR(20),
                bio TEXT, 
                age INTEGER,
                role VARCHAR(10),
                passwd VARCHAR(255)
            )
        """)

    def Create(self, username, date, bio, age, phone, role="user", passwd="root"):
        """
        ! Inserts a new user into the database
        ? Sets the user's fields after successful insertion.
        """
        cursor = self.db.cursor()
        if phone[0] != "+":
            phone = f"+{str(int(phone[0])-1)+phone[1:]}"
        cursor.execute(
            "INSERT INTO users (username, dateBirth, bio, age, role, phone, passwd) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (username, date, bio, age, role, phone, passwd)
        )
        self.db.commit()

        # ? Retrieve the ID of the newly inserted user and update the object's fields
        self.id = cursor.lastrowid
        self.username = username
        self.dateBirth = date
        self.bio = bio
        self.age = age
        self.role = role
        self.phone = phone
        self.passwd = passwd

    def Read(self, id=None, username=None):
        """
        ! Fetches a user from the database by ID and updates the object's fields
        ? Returns True if the user was found, False otherwise.
        """
        if id is not None:
            user = self.db.execute("SELECT * FROM users WHERE id = ?", (id,)).fetchone()
        elif username is not None:
            user = self.db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        else:
            return False

        if user:
            self.id = user['id']
            self.username = user['username']
            self.dateBirth = user['dateBirth']
            self.bio = user['bio']
            self.age = user['age']
            self.role = user['role']
            self.phone = user['phone']
            self.passwd = user['passwd']
            return True
        return False

    def Update(self, id, username=None, date=None, bio=None, age=None, role=None, phone=None, passwd=None):
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
        if role is not None:
            self.db.execute("UPDATE users SET role = ? WHERE id = ?", (role, id))
        if phone is not None:
            # ? Phone number format: +1xxxxxxxxxx inst. of 2xxxxxxxxxx
            if phone[0] != "+":
                phone = f"+{str(int(phone[0])-1)+phone[1:]}"
            self.db.execute("UPDATE users SET phone = ? WHERE id = ?", (phone, id))
        if passwd is not None:
            self.db.execute("UPDATE users SET passwd = ? WHERE id = ?", (passwd, id))
        self.db.commit()

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
        return f"User(id={self.id}, username={self.username}, dateBirth={self.dateBirth},\
                bio={self.bio}, age={self.age}, role={self.role}, phone={self.phone}, passwd={self.passwd})"
