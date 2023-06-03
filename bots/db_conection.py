import psycopg2 as db
import json
from datetime import datetime




def convertToBinaryData(filename):

   

    print("FOTO DESDE ACA", filename)
    # Convert digital data to binary format
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except:
        return 0

def write_file(data, path):
    # Convert binary data to proper format and write it on your computer
    with open(path, 'wb') as file:
        file.write(data)


def registerUser(name, photo):
   
   id = 0
   inserted = 0

   pic = convertToBinaryData(photo)
   print("Foto")
   print(photo)
  

   try:
        connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
        cursor = connection.cursor()      
      
        sql = "INSERT INTO asistencias.usuarios(name,photo) VALUES (%s,%s)"
        pic = convertToBinaryData(photo)  
        record_to_insert = (name, pic)
        # converting to its binary form        
        if pic:
            cursor.execute(sql,record_to_insert)   
            connection.commit()
            inserted = cursor.rowcount
            id = cursor.lastrowid
   except db.Error as e:
        print(f"Failed inserting image: {e}")
   finally:
        #if con.is_connected():
            cursor.close()
            connection.close()
   return {"id": id, "affected":inserted}



def getUser(name, path):
    id = 0
    rows = 0

    try:
       
        connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
        cursor = connection.cursor()  
        sql = "SELECT * FROM asistencias.usuarios WHERE name = %s"

        cursor.execute(sql, (name,))
        records = cursor.fetchall()

        for row in records:
            id = row[0]
            write_file(row[2], path)
            print(write_file(row[2], path))
        rows = len(records)
    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        #if con.is_connected():
            cursor.close()
            connection.close()
    return {"id": id, "affected": rows}



def getAllUser(user, path):

    try:    
        #con = connection.cursor()
        #cursor = con.cursor()
        connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
        cursor = connection.cursor()  
        
        sql = "SELECT * FROM asistencias.usuarios WHERE name = %s"
        cursor.execute(sql, (user,))
      
        records = cursor.fetchall()

        lista = []

        for row in records:      
            write_file(row[2], path)
            #lista.append(row)
        #return lista
    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
            cursor.close()
            connection.close()

def getNickName():
    try:    
        #con = connection.cursor()
        #cursor = con.cursor()
        connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
        cursor = connection.cursor()  
        sql = "SELECT * FROM asistencias.usuarios"

        cursor.execute(sql)
        records = cursor.fetchall()
        lista = []
        for row in records:                  
            lista.append(row[1])
        return lista
    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
            cursor.close()
            connection.close()

def insertAsistenccia(id):
    try:    
            
            #extramos información actual 
            info = datetime.now ()
            #Extraemos fecha
            fecha = info.strftime('%Y-%m-%d')
            #extraemos hora
            hora = info.strftime ('%H:%M:%S')

            print( fecha + hora)
            #con = connection.cursor()
            #cursor = con.cursor()
            connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
            cursor = connection.cursor()  

            

            sqlSelect = "select * from asistencias.reg_asistencia  where to_char(fecha_registro,'YYYY-MM-DD')  = %s and id_estudiante = %s"
            cursor.execute(sqlSelect, (fecha, int(id)))
            mobile_records = cursor.fetchall()

            if mobile_records:
                print("Ya fue tomada la asistencia")
            else:
                sql = "insert into asistencias.reg_asistencia(id_estudiante, fecha_registro) values(%s, %s)"
                record_to_insert = (int(id),fecha + " " + hora)
                cursor.execute(sql,record_to_insert)   
                connection.commit()
            
           
            """sql = "insert into asistencias.reg_asistencia(id_estudiante, fecha_registro) values(%s, %s)"
            record_to_insert = (11,fecha + " " + hora)
            cursor.execute(sql,record_to_insert)   
            connection.commit()"""

            
    except db.Error as e:
            print(f"Failed to read image: {e}")
    finally:
                cursor.close()
                connection.close()

def getUserByUsername(name):
    id = 0
    rows = 0

    try:
       
        connection = db.connect(user="postgres", password="admin",  host="127.0.0.1",  port="5432", database="universidad")
        cursor = connection.cursor()  
        sql = "SELECT * FROM asistencias.usuarios WHERE name = %s"

        cursor.execute(sql, (name,))
        records = cursor.fetchall()

        for row in records:
            return row[0]
        
    except db.Error as e:
        print(f"Failed to read image: {e}")
    finally:
        #if con.is_connected():
            cursor.close()
            connection.close()
    return {"id": id, "affected": rows}
        