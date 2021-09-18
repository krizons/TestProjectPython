from databases import Database
from .db_model import document, category
from conf import settings

ApiDB: Database = Database(settings.DATABASE_URL)
