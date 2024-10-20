import pytest
import sqlite3
from models.user import User

@pytest.fixture
def database_connection():
    """
    ! Creates a new in-memory database for each test
    ? Ensures that the database starts empty for every test run.
    """
    connection = sqlite3.connect(":memory:")  # * Use in-memory database for tests
    connection.row_factory = sqlite3.Row  # ? So we can query results as dicts
    yield connection
    connection.close()

def test_create_user(database_connection):
    """
    ! Test creating a user and verifying __str__ output
    """
    user = User(database_connection)
    user.Migrate()
    
    user.Create("user1", "2020-01-01", "bio1", 4)
    
    assert str(user) == "User(id=1, username=user1, dateBirth=2020-01-01, bio=bio1, age=4)"

def test_read_user(database_connection):
    """
    ! Test reading a user from the database
    """
    user = User(database_connection)
    user.Migrate()

    user.Create("user1", "2020-01-01", "bio1", 4)
    
    new_user = User(database_connection)
    assert new_user.Read(1)  # ? Should return True since user exists
    assert new_user.username == "user1"
    assert new_user.bio == "bio1"

def test_update_user(database_connection):
    """
    ! Test updating a user's data
    """
    user = User(database_connection)
    user.Migrate()

    user.Create("user1", "2020-01-01", "bio1", 4)
    
    user.Update(1, bio="Updated one.")
    
    updated_user = User(database_connection)
    updated_user.Read(1)
    
    assert updated_user.bio == "Updated one."

def test_delete_user(database_connection):
    """
    ! Test deleting a user from the database
    """
    user = User(database_connection)
    user.Migrate()

    user.Create("user1", "2020-01-01", "bio1", 4)
    
    # * Check if user exists
    assert user.Read(1)
    
    # * Delete the user
    user.Delete(1)
    
    # * Ensure user no longer exists
    deleted_user = User(database_connection)
    assert not deleted_user.Read(1)  # ? Should return False since user is deleted
