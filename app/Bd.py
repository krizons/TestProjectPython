# import asyncpg
import databases
import sqlalchemy
from BdModel import Category, Document


# DATABASE_URL = "postgresql://user:password@postgresserver/db"


class TestApiBd:
    def __init__(self, bd_url:str) -> object:
        self.conn = databases.Database(bd_url)
        self.document = Document
        self.category = Category

    async def ConnectBd(self):
        pass
        await  self.conn.connect()
        # self.conn = await  asyncpg.connect(user=self.user, password=self.password,
        #                                   database=self.database, host=self.host, port=self.port)

    async def CreateCategory(self, heading: str, subtitle: str, description: str, subid: int = 0):
        try:
            qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(self.category).where(
                self.category.c.heading == heading,
                self.category.c.subid == subid)
            row = await self.conn.fetch_one(qu)

            if row[0] == 0:
                qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(self.category).where(
                    self.category.c.id == subid)
                row = await self.conn.fetch_one(qu)
                if row[0] > 0 or subid == 0:
                    await self.conn.execute(self.category.insert(),
                                            {"heading": heading, "subtitle": subtitle, "description": description,
                                             "subid": subid})
                return True
        except:
            pass
        return False

    async def EditCategory(self, id: int, heading: str, subtitle: str, description: str, subid: int):

        if heading is not None or subtitle is not None or description is not None or subid is not None:
            param = {}
            if heading is not None:
                param["heading"] = heading
            if subtitle is not None:
                param["subtitle"] = subtitle
            if description is not None:
                param["description"] = description
            if subid is not None:
                param["subid"] = subid
            qu = self.category.update().where(self.category.c.id == id).values(param)
            try:
                await self.conn.execute(qu)
                return True
            except:
                return False
        return False

    async def AddDocument(self, CategoryId: int, documentName: str, path_file: str):
        # binfile= await document.read()
        try:
            qu = sqlalchemy.select([sqlalchemy.func.count()]).select_from(self.category).where(
                self.category.c.id == CategoryId)
            row = await self.conn.fetch_one(qu)
            if row[0] != 0:
                qu = self.document.insert()

                row = await self.conn.fetch_one(qu, {"lincid": CategoryId, "name": documentName,
                                                     "path": path_file})
                return True
        except:
            pass
        return False

    async def GetAllCategory(self, subid: int = 0):
        qu = self.category.select().where(self.category.c.subid == subid)
        row = await self.conn.fetch_all(qu)
        return row

    async def DeleteDocument(self, name: str, categor_id: int):
        qu = self.document.select("path").where(self.document.c.name == name, self.document.c.lincid == categor_id)
        row = await self.conn.fetch_one(qu)
        if row is not None:
            qu = self.document.delete().where(self.document.c.name == name, self.document.c.lincid == categor_id)
            await self.conn.execute(qu)
        # print(row)
        return row

    async def GetAllDocument(self, subid: int):
        qu = self.document.select("name", "id").where(self.document.c.lincid == subid)
        row = await self.conn.fetch_all(qu)
        return row

    async def GetDocument(self, id: int):
        qu = self.document.select("name", "id").where(self.document.c.id == id)
        row = await self.conn.fetch_one(qu)
        return row.get("path")

    async def Close(self):
        await self.conn.disconnect()

    async def Reset(self):
        await self.Close()
        await self.ConnectBd()
