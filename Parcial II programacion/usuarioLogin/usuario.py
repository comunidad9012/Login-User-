class Usuario():

    cantidadUsuarios=0

    def __init__(self,nombreUser,password):
        self.nombreUser=nombreUser   ## nombre del usuario
        self.password=password       ## contraseña para ese usuario

        self.conexion=False  ## estado de la conexion
        self.intentos=3      ## intentos permitidos para ingresar la contraseña

        Usuario.cantidadUsuarios+=1 ## Suma la cantidad de usuarios que se van creando


    def conectarUser(self,contrasenia=None):

        if contrasenia==None:
            mypass=input("ingrese su contraseña: ")
        else:
            mypass=contrasenia

        if mypass==self.password:               ## compreba si la contraseña ingresadaa es igual a la creada
            print("ESTA CONECTADO")
            self.conexion=True              ## cambia el estado de la conexion como desconectada a conectada
            return True
        else:
            self.intentos-=1
            if self.intentos > 0:
                print("ERROR - Contraseña incorrecta, intente nuevamente")
                if contrasenia!=None:
                    return False
                print("Intentos restantes",self.intentos) ## muestra los intentos restantes en el de ingresar mal la contraseña
                self.conectarUser() ## vuelve a llamar a la funcion en caso de ingresar mal la contraseña
            else:
                print("ERROR - NO SE PUDO CONECTAR")

    def desconectarUser(self):
        if self.conexion:
            print("USUARIO DESCONECTADO")
            self.conexion=False ## cambia el estado de la conexios de conectado a desconectado
        else: 
            print("ERROR - NO INICIO")

    def __str__(self):
        if self.conexion:
            conect="conectado"
        else:
            conect="desconectado"
        return f"Usuario: {self.nombreUser} Estado: {conect}"
