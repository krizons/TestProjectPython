import sqlalchemy

metadata = sqlalchemy.MetaData()
Document = sqlalchemy.Table(
    "document",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("lincid", sqlalchemy.Integer, nullable=False, unique=True),
    sqlalchemy.Column("id", sqlalchemy.Integer, nullable=False, primary_key=True, autoincrement=True),
    sqlalchemy.Column("path", sqlalchemy.String, nullable=False))
Category = sqlalchemy.Table(
    "category",
    metadata,
    sqlalchemy.Column("heading", sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("subtitle", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("image", sqlalchemy.String),
    sqlalchemy.Column("subid", sqlalchemy.Integer, unique=True),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True))
