from .Bd import MyDB
import os
#ApiDB: MyDB = MyDB(os.environ["DATABASE_URL"])
ApiDB: MyDB = MyDB("postgresql://postgres:12345678@localhost:5432/TestApi")
