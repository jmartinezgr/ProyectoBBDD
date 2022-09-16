import datetime
import hashlib
import Usuarios.conexion as con

connect = con.conectar()
database = connect[0]
cursor = connect[1]

class usuario:

    def __init__(self,x):
        self.nombre = x[0]
        self.apellidos = x[1]
        self.correo = x[2]
        self.pss = x[3]

    def registrar(self):
        
        cifrado = hashlib.sha256()
        cifrado.update(self.pss.encode('utf8'))
               
        user = (self.nombre,self.apellidos,self.correo,cifrado.hexdigest(),datetime.datetime.now())
        sl = "Insert into usuarios values(null,%s,%s,%s,%s,%s)"

        try:    
            cursor.execute(sl,user)
            database.commit()
            return [cursor.rowcount,self]
        except:
            return [0,self]
        

    
    def identificar(self):
        sl = "select * from usuarios where email = %s and password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.pss.encode('utf8'))

        usuario = (self.correo, cifrado.hexdigest())

        cursor.execute(sl,usuario)

        return cursor.fetchone()
        