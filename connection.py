import sqlite3


def conectar():
    con = sqlite3.connect("db")
    cursor = con.cursor()
    try:
        sql = """
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cedula INTEGER NOT NULL UNIQUE,
                edad INTEGER NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT DEFAULT 'NO TIENE',
                correo TEXT NOT NULL UNIQUE
            )"""
        cursor.execute(sql)
        return con
    except Exception as ex:
        print("Error de conexion:", ex)
    finally:
        cursor.close()
