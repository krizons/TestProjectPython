import sqlalchemy

metadata = sqlalchemy.MetaData()
document = sqlalchemy.Table(
    "document",
    metadata,
    sqlalchemy.Column("name", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("lincid", sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column("id", sqlalchemy.Integer, nullable=False, primary_key=True, autoincrement=True),
    sqlalchemy.Column("path", sqlalchemy.String, nullable=False),
    sqlalchemy.UniqueConstraint('name', 'lincid', name='name_lincid_unique')
    )
category = sqlalchemy.Table(
    "category",
    metadata,
    sqlalchemy.Column("heading", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("image", sqlalchemy.String, nullable=False),
    sqlalchemy.Column("subtitle", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("subid", sqlalchemy.Integer),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True),
    sqlalchemy.UniqueConstraint('heading', 'subid')
    )
