import connection as con
import sqlite3


def save(persona):
    persona = dict(persona)
    db = con.conectar()
    cursor = db.cursor()

    try:
        columnas = ', '.join(persona.keys())
        valores = tuple(persona.values())
        sql = f"""
            INSERT INTO personas ({columnas}) VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, valores)
        db.commit()
        creada = cursor.rowcount > 0
        if creada:
            cursor.close()
            db.close()
            return {"respuesta": creada, "mensaje": "Trabajador creado"}
        else:
            cursor.close()
            db.close()
            return {"respuesta": creada, "mensaje": "No se puede registrar al trabajador"}

    except sqlite3.IntegrityError as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje = "Ya existe una persona con ese correo"
        elif "UNIQUE" in str(ex) and "cedula" in str(ex):
            mensaje = "Ya existe una persona con esa cedula"
        else:
            mensaje = str(ex)
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": mensaje}


def find_all():
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        if personas:
            cursor.close()
            db.close()
            return {"respuesta": True, "personas": personas, "mensaje:": "Listado ok"}
        else:
            cursor.close()
            db.close()
            return {"respuesta": False, "personas": personas, "mensaje:": "No hay trabajadore registrado"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": str(ex)}


def find(cedula_persona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM personas WHERE cedula='{cedula}'".format(cedula=cedula_persona))
        res = cursor.fetchall()
        if res:
            info = res[0]
            persona = {"id": info[0],
                       "cedula": info[1],
                       "edad": info[2],
                       "nombre": info[3],
                       "apellido": info[4],
                       "direccion": info[5],
                       "correo": info[6], }

            cursor.close()
            db.close()
            return {"respuesta": True, "persona": persona, "mensaje:": "Trabajador encontrado!!"}
        else:
            cursor.close()
            db.close()
            return {"respuesta": False,  "mensaje:": "No existe el trabajador"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": str(ex)}


def update(persona):
    try:
        db = con.conectar()
        cursor = db.cursor()
        persona = dict(persona)
        cedula_persona = persona.get('cedula')
        persona.pop('cedula')
        valores = tuple(persona.values())
        sql = """
        UPDATE personas
        SET edad=?, nombre=?, apellido=?, direccion=?, correo=?
        WHERE cedula='{cedula}'
        """.format(cedula=cedula_persona)
        cursor.execute(sql, (valores))
        modificada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        if modificada:
            return {"respuesta": modificada, "mensaje": "Trabajador actualizado"}
        else:
            return {"respuesta": modificada, "mensaje": "No existe el trabajador con ese numero de cedula"}
    except Exception as ex:
        if "UNIQUE" in str(ex) and "correo" in str(ex):
            mensaje = "Ya existe una persona con ese correo"
        else:
            mensaje = str(ex)
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": mensaje}


def delete(id_persona):
    try:
        db = con.conectar()
        cursor = db.cursor()

        sql = """
        DELETE FROM personas
        WHERE id='{id}'
        """.format(id=id_persona)
        cursor.execute(sql)
        eliminada = cursor.rowcount > 0
        db.commit()
        cursor.close()
        db.close()
        if eliminada:
            return {"respuesta": eliminada, "mensaje": "Trabajador elimininado"}
        else:
            return {"respuesta": eliminada, "mensaje": "No existe el trabajador con ese Id"}
    except Exception as ex:
        cursor.close()
        db.close()
        return {"resspuesta": False, "mensaje": str(ex)}
