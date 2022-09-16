from calendar import c
import Usuarios.conexion as co
import hashlib
conn = co.conectar()

database = conn[0]
cursor = conn[1]

class nota:
    def __init__(self, usuario_id,titulo = "Nota sin titulo",descripcion = ""):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    def guardar(self):
        sl = "Insert into notas Values(null,%s,%s,%s,NOW())"
        nota = (self.usuario_id,self.titulo,self.descripcion)

        cursor.execute(sl,nota)
        database.commit()

        return [cursor.rowcount,self]
    
    def listar(self):
        sl = f"Select * from notas where usuario_id = {self.usuario_id}"

        cursor.execute(sl)
        result = cursor.fetchall()

        list(result)
        x = list(map(lambda x:list(x),result))

        return x

    def cambiar(self,titulo,cambio):
        sl = f"Update notas set descripcion = '{cambio}' where usuario_id = {self.usuario_id} and titulo = '{titulo}'"

        cursor.execute(sl)
        database.commit()
        
        return [cursor.rowcount,self]
    def eliminar(self,titulo):
        sl = f"delete from notas where usuario_id = {self.usuario_id} and titulo like '%{titulo}%'"
        cursor.execute(sl)
        database.commit()
        return [cursor.rowcount,self]
    def titulos(self):
        sl = f"SELECT `titulo` FROM `notas` WHERE usuario_id = {self.usuario_id}"
        cursor.execute(sl)

        x = cursor.fetchall()
        return x
        
    
    

class cambiocuenta():
    def cambiarcontraseña(self,id,pssc):
        cifrado = hashlib.sha256()
        cifrado.update(pssc.encode('utf8'))
        
        sl = f"Update usuarios set password = '{cifrado.hexdigest()}' where id = {id}"

        cursor.execute(sl)
        database.commit()

        return [cursor.rowcount,self]

