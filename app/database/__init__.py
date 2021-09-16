from databases import Database
from .db_model import document, category
import os
#ApiDB: MyDB = MyDB(os.environ["DATABASE_URL"])
#ApiDB: MyDB = MyDB("postgresql://postgres:12345678@localhost:5432/TestApi")
ApiDB: Database = Database("postgresql://postgres:12345678@localhost:5432/TestApi")
