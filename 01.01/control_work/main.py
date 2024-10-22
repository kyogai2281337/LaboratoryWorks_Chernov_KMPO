import sqlite3
from db.models.user import User
from qt.carcas import init_app
def main():
    runtimeMode = "auth" # ! role there
    db = sqlite3.connect("data.db")
    db.row_factory = sqlite3.Row

    user = User(db)
    user.Migrate()
    user.Create("db1", "2020-01-01", "bio1", 4, "89992231313", "db", "root1")
    user.Create("crt1", "2020-01-01", "bio3", 4, "89992231315", "chart", "root2")
    # ! mainWin - debug ancestor
    app, win = init_app(db, runtimeMode)
    
if __name__ == "__main__":
    main()