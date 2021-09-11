import asyncpg
import databases
DATABASE_URL = "postgresql://user:password@postgresserver/db

class TestApiBd:
    def __init__(self, user: str, password: str, database: str, host: str, port: str):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

    async def ConnectBd(self):
        self.conn = await  asyncpg.connect(user=self.user, password=self.password,
                                           database=self.database, host=self.host, port=self.port)

    async def CreateCategory(self, heading: str, subtitle: str, description: str, subid: int = 0):
        row = await self.conn.fetchrow("select  сreateсategory($1::text,$2::text,$3::text,$4)", heading, subtitle,
                                       description, subid)
        return row.get("сreateсategory")

    async def GetCntQ(self, table: str, param: dict, is_and: bool = True):
        query = "SELECT COUNT(*) FROM    {0} WHERE ".format(table)
        flag_start = ""
        for key, value in param.items():
            if value is not None:
                if (type(value) == str):
                    query += "{0} {1} = '{2}' ".format(flag_start, key, value)
                else:
                    query += "{0} {1} = {2} ".format(flag_start, key, value)
                if flag_start == "":
                    if is_and is True:
                        flag_start = "AND"
                    else:
                        flag_start = "OR"

        row = await self.conn.fetchrow(query)
        return row.get("count")

    async def CreateUpdate(self, table: str, param: dict, where: dict, is_and: bool = True):
        query = "UPDATE {0} SET ".format(table)
        tmp = ""
        for key, value in param.items():
            if type(value) == str:
                query += "{0} {1}='{2}' ".format(tmp, key, value)
            else:
                query += "{0} {1}={2} ".format(tmp, key, value)
            if tmp == "":
                tmp = ","
        query += "WHERE "
        tmp = ""
        for key, value in where.items():
            if type(value) == str:
                query += "{0} {1}='{2}' ".format(tmp, key, value)
            else:
                query += "{0} {1}={2} ".format(tmp, key, value)
            if tmp == "":
                if is_and:
                    tmp = "AND"
                else:
                    tmp = "OR"
        return query

    async def EditCategory(self, id: int, heading: str, subtitle: str, description: str, subid: int):

        if heading is not None or subtitle is not None or description is not None or subid is not None:
            param = {}
            where = {}

            if heading is not None:
                param["heading"] = heading
            if subtitle is not None:
                param["subtitle"] = subtitle
            if description is not None:
                param["description"] = description
            if subid is not None:
                param["subid"] = subid
            where["id"] = id
            qu = await self.CreateUpdate("category", param, where)
            try:
                await self.conn.execute(qu)
                return True
            except:
                return False
        return False

    async def AddDocument(self, CategoryId: int, documentName: str, path_file: str):
        # binfile= await document.read()
        try:
            row = await self.conn.fetchrow("SELECT adddoc ($1,$2::text,$3::text)", CategoryId, documentName, path_file)
            return row.get("adddoc")
        except:
            pass
        return False

    async def GetAllCategory(self, subid: int = 0):
        row = await self.conn.fetch("SELECT heading,id,subtitle,description FROM public.category WHERE subid = $1",
                                    subid)
        return row

    async def DeleteDocument(self, name: str, categor_id: int):
        row = await self.conn.fetchrow("SELECT path  FROM document WHERE name=$1 and lincid=$2", name, categor_id)
        if row is not None:
            await self.conn.execute("DELETE FROM document WHERE name=$1 and lincid=$2", name, categor_id)
        # print(row)
        return row

    async def GetAllDocument(self, subid: int):
        row = await self.conn.fetch("SELECT name,id FROM public.document WHERE lincid = $1", subid)
        return row

    async def GetDocument(self, id: int):
        row = await self.conn.fetchrow("SELECT path FROM public.document WHERE id = $1", id)
        return row.get("path")

    async def Close(self):
        await self.conn.close()

    async def Reset(self):
        await self.Close()
        await self.ConnectBd()
# async def run():
#    conn = await asyncpg.connect(user='postgres', password='12345678',
# database='TestApi', host='127.0.0.1',port='5432')

#   row = await conn.fetch('''
#        SELECT * FROM public.category
#    ''')
#    print(row)
#    await conn.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())
