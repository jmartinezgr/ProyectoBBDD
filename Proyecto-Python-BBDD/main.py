from Usuarios import acciones

hazel = acciones.acciones()


print("""
Acciones disponibles:
    -registro 
    -login
""")
while True:
    accion = input("¿que quieres hacer?: ")
    if accion.lower() == "registro":
        print("\nOkey vamos a registrarte")
        break
    elif accion.lower() == "login":
        print("\nOkey, Vamos a ingresar al sistema...")
        break
    else:
        print("""!No existe esa accion intentalo de nuevo¡
            
Tal vez te sirva conocer los comandos: Para registrarte escribe:"registro"
                                       Para entrar a tu cuenta escribe:"login"
        
        """)

accion.lower()

if accion == "registro":
    hazel.registro()
if accion == "login":
    hazel.login()




        

