from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as MessageBox
from usuario import Usuario

ventanaPrincipal=Tk()
nombreUsuario=StringVar()
contraseñaUsuario=StringVar()
listaUsuarios=[]

def createGUI():

    ##VENTANA PRINCIPAL
    #ventanaPrincipal=Tk()
    ventanaPrincipal.title("Login Usuario")

    ##MAIN FRAME
    frameContenedor=Frame(ventanaPrincipal) ##ventana principal esta contenida en el frame
    frameContenedor.pack() ## empaquetamos
    frameContenedor.config(width=500,height=350)#,bg="lightgreen")

    ## LABEL= ETIQUETAS DE TEXTOS
    ## textos y titulos

    titulo=Label(frameContenedor,text="Login de usuario",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=15,pady=15,columnspan=2)#los padx,y son los espacios alrededor del elemento
    ## el .grid() es para agregar a la interfaz los contenidos
    nombreLabel=Label(frameContenedor,text="Nombre: ")
    nombreLabel.grid(column=0,row=1)
    contraseñaLabel=Label(frameContenedor,text="Contraseña: ")
    contraseñaLabel.grid(column=0,row=2)


    ## ENTRADAS DE TEXTOS

    #nombreUsuario=StringVar()
    nombreUsuario.set("") ## seteamos un valor por defecto
    IngresarNombre=Entry(frameContenedor,textvariable=nombreUsuario)
    IngresarNombre.grid(column=1,row=1)

    #contraseñaUsuario=StringVar()
    contraseñaUsuario.set("")
    IngresarContraseña=Entry(frameContenedor,textvariable=contraseñaUsuario,show="*")
    ## show="*" mostrara asteriscos en lugar de la contraseña

    IngresarContraseña.grid(column=1,row=2)

    ## BOTONES

    BotonInicioSesion=ttk.Button(frameContenedor,text="Iniciar sesion", command=iniciarSesion)
    BotonInicioSesion.grid(column=1,row=3,ipadx=7,ipady=7,padx=15,pady=15)

    BotonRegistrar=ttk.Button(frameContenedor,text="Registrarse",command=registrarUsuario)
    BotonRegistrar.grid(column=0,row=3,ipadx=7,ipady=7,padx=15,pady=15)

    

    ventanaPrincipal.mainloop()

def iniciarSesion():
    for user in listaUsuarios:
        if user.nombreUser==nombreUsuario.get():
            test = usuario1.conectarUser(contraseñaUsuario.get())
            if test==True:
                MessageBox.showinfo("conectado",f"Se inicio sesion en [ {user.nombreUser} ] con éxito")
            else:
                MessageBox.showerror("ERROR", "Contraseña incorrecta")
            break

    else:
        MessageBox.showerror("ERROR", "No hay usuarios registrados con ese nombre")


def registrarUsuario():
    nombre = nombreUsuario.get()
    contra = contraseñaUsuario.get()
    nuevoUsuario=Usuario(nombre,contra)
    listaUsuarios.append(nuevoUsuario)
    MessageBox.showinfo("USUARIO REGISTRADO",f"El usuario [ {nombre} ] re registro con ¡¡ EXITO !!")
    nombreUsuario.set("")# Una vez registrado el cuadro se vulve en blanco
    contraseñaUsuario.set("") #igual se pone blanco la casilla

if __name__=="__main__":
    ##usuario1=Usuario(input("Ingrese un nombre: "),input("Ingrese una contraseña: ")) #si el nombre del archivo es main que llame a la funcion create gui
    usuario1= Usuario("mauricio","1234")
    listaUsuarios.append(usuario1)
    createGUI()

#ventanaPrincipal.mainloop() ##ejecuta la ventana donde se va a ejecutar los procesos
