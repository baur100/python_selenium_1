import pyodbc


class DbAdapter:
    server = "aurorasqlserverdev.database.windows.net"
    db_name = "lbrdev"
    @classmethod
    def get_all(cls):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'mTDsj3BNe1J3!'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        cursor = cnxn.cursor()
        cursor.execute("SELECT * from dbo.Books")
        row = cursor.fetchone()
        return row
    @classmethod
    def get_by_id(cls,id):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'mTDsj3BNe1J3!'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        cursor = cnxn.cursor()
        cursor.execute(f"SELECT * from dbo.Books where id={id}")
        row = cursor.fetchone()
        return row
    @classmethod
    def delete_by_id(cls,id):
        server = 'aurorasqlserverdev.database.windows.net'
        database = 'lbrdev'
        username = 'aurorasqladmin'
        password = 'mTDsj3BNe1J3!'
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        cursor = cnxn.cursor()
        cursor.execute(f"DELETE FROM dbo.books WHERE id={id}")
        while row:
            # print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
