import sqlite3
from models.user import User

def main():
    database_connection = sqlite3.connect("data.db")

    # * dict-like output, for me this is better, bc we can query like that:
    # ? SELECT * from users                                    | dict 
    # ? SELECT id, username, dateBirth, bio, age from users    | tuple
    # * So that`s the reason why we use sqlite3.Row
    database_connection.row_factory = sqlite3.Row

    user = User(database_connection)
    user.Migrate()

    # * Creating
    user.Create("user1", "2020-01-01", "bio1", 4)
    print(user)  # * __str__ output
    user.Update(1, bio="Updated one.")
    # * checking reading by id 
    new_user = User(database_connection)
    if new_user.Read(1):
        print(new_user)  # ! __str__ if self.found
    else:
        print("User not found.") # ! unless
    
    # * Deleting user after checkout
    user.Delete(1)
        

if __name__ == "__main__":
    main()
