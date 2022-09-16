from re import U
import Usuarios.usuario as us
import notas.acciones as ac

class encri:
    def encriptar(self,clave):
        return ''.join(reversed(clave))

ec = encri()

class acciones:
    def registro(self):
        lista = []
        lista.append(input("Ingrese su nombre: "))
        lista.append(input("Ingrese su apellido: "))
        while True:
            x = input("Ingrese su correo: ")
            if x.isspace() or len(x)<3:
                print("Debes ingresar un correo valido")
            else:
                lista.append(x)
                break
                
        while True:
            x = input("Ingrese su contraseña: ")
            if x.isspace() or len(x)<8:
                print("Debes ingresar una contraseña de minimo 8 caracteres")
            else:
                lista.append(ec.encriptar(x))
                break
        
        usuario = us.usuario(lista)
        registro = usuario.registrar()

        if registro[0]>=1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email: {registro[1].correo}")
        else:
            print("No te has registrado correctamente")
    
    def login(self):
        try:
            while True:
                info = []
                x = input("Ingrese su correo: ")
                if x.isspace() or len(x)<3:
                    print("Debes ingresar un correo valido")
                else:
                    info.append(x)
                    break
                    
            while True:
                x = input("Ingrese su contraseña: ")
                if x.isspace() or len(x)<8:
                    print("Contraseña invalida")
                else:
                    info.append(ec.encriptar(x))
                    break
            usuario = us.usuario(['',''] + info)
            login = usuario.identificar()
            if info[0] == login[3]:
                print(f"Bienvenido {login[1]} te has registrado en el sistema el: {login[5]}")
                self.proximasacciones(login)
        except TypeError:
            print("La contraseña o el correo tienen algun error, vuelve a intentarlo")
            self.login()

    def proximasacciones(self,usuario):
        print("""
        Acciones disponibles:
        -Crear notas (crear)
        -Mostrar notas (mostrar)
        -Cambiar notas (cambiar)
        -eliminar notas (eliminar)
        -eliminar usuario (eliminar usuario)
        -salir(salir)
        """)
        
        haz = ac.acciones2()
        while True:
            accion = input("¿Cual eliges?: ")
            accion.lower()
            if accion == "crear":
                haz.crear(usuario)
            elif accion == "mostrar":
                haz.mostrar(usuario)
            elif accion == "cambiar":
                haz.cambiar(usuario)
            elif accion == "eliminar":
                haz.erase(usuario)
            elif accion == "eliminar usuario":
                pass
            elif accion == "salir":
                print(f"Hasta luego {usuario[1]}")
                print("Cerrando ... ")
                exit()
            else:
                print("Has introducido una accion invalida")
            
                



        
