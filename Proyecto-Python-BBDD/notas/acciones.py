import notas.nota as nt
import hashlib


class acciones2:
    def crear(self,usuario):
        print(f"ok! {usuario[1]} vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        if titulo.isspace() or len(titulo)<1:
            titulo = "Nota sin nombre"
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = nt.nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0]>=1:
            print(f"Perfecto, la nota: {nota.titulo} ha sido guardada correctamente")
        else:
            print(f"\nOh, no se a podido guardar la nota")
    def mostrar(self,usuario):
        print(f"\nVale {usuario[1]} estas son tus notas: ")

        nota = nt.nota(usuario[0])
        notas = nota.listar()

        for i in  notas:
            print("----------------------------")
            print(f"Titulo de la nota: {i[2]}")
            print(f"Contenido: {i[3]}\n")

        
    
    def cambiar(self,usuario):
        print("Vamos a cambiar una nota")
        while True:
            tc = input("Cual es el titulo de la nota:")
            if tc.isspace() or len(tc)<1:
                print("Titulo no valido, vuelve a ingresarlo")
            else:
                break
        dc = input("Ingresa el nuevo contenido de la nota: ")

        nota = nt.nota(usuario[0])
        info = nota.cambiar(tc,dc)

        if info[0]>=1:
            print("La nota se ha cambiado exitosamente")
        else:
            print("Ha ocurrido un error")

    def erase(self,usuario):
        
        print("Vamos a borrar una nota")

        
        nota = nt.nota(usuario[0])
        titulo = input("Introduce el titulo de la nota a borrar: ")
        eliminar = nota.eliminar(titulo)

        if eliminar[0]>=1:
            print("Hemos borrado la nota")
        else:
            print("Ha ocurrido algo")
        



        

        




