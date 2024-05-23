from tkinter import *
from tkinter import ttk, messagebox
import persona_datos as crud


# Ventana
v = Tk()
ancho = 450
alto = 400

x_v = v.winfo_screenwidth() // 2 - ancho // 2
y_v = v.winfo_screenheight() // 2 - alto // 2

pos = str(ancho) + "x" + str(alto) + "+" + str(x_v) + "+" + str(y_v)
v.geometry(pos)
v.state("zoomed")
v.configure(bg="#000000")  # Cambiado a negro

################################## VARIABLES #####################################
txt_id = StringVar()
txt_cedula = StringVar()
txt_nombre = StringVar()
txt_apellido = StringVar()
txt_direccion = StringVar()
txt_correo = StringVar()
txt_edad = StringVar()
################################## FUNCIONES #####################################


def creditos():
    messagebox.showinfo("Creditos",
                        """
                        Creados por: OSCAR JAVIER CASTELBLANCO
                        --------------------------------------
                        Email: lubianka01@gmail.com
                        --------------------------------------
                        Bogotá-Colombia
                        --------------------------------------
                        Marzo de 2024  
                        """
                        )


def salir():
    respuesta = messagebox.askquestion(
        "Salir", "¿Desea salir de la aplicación?")
    if respuesta == "yes":
        v.destroy()


def llenar_tabla():
    tabla.delete(*tabla.get_children())
    respuesta = crud.find_all()
    personas = respuesta.get("personas")
    for fila in personas:
        row = list(fila)
        row.pop(0)
        row = tuple(row)
        tabla.insert("", END, text=id, values=row)


def limpiar_campos():
    txt_edad.set("")
    txt_cedula.set("")
    txt_nombre.set("")
    txt_apellido.set("")
    txt_direccion.set("")
    txt_correo.set("")
    e_cedula.focus()


def guardar():
    if txt_edad.get().isnumeric():
        persona = {"cedula": txt_cedula.get(),
                   "edad": int(txt_edad.get()),
                   "nombre": txt_nombre.get(),
                   "apellido": txt_apellido.get(),
                   "direccion": txt_direccion.get(),
                   "correo": txt_correo.get(), }
        respuesta = crud.save(persona)
        if respuesta.get("respuesta"):
            llenar_tabla()
            messagebox.showinfo("OK", respuesta.get("mensaje"))
            limpiar_campos()
        else:
            messagebox.showerror("Upps!!!", respuesta.get("mensaje"))

    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Upps!!!", "La EDAD debe ser un número..")


def consultar():
    if txt_cedula.get() != "":
        respuesta = crud.find(txt_cedula.get())
        if respuesta.get("respuesta"):
            persona = respuesta.get("persona")
            txt_nombre.set(persona.get("nombre"))
            txt_apellido.set(persona.get("apellido"))
            txt_direccion.set(persona.get("direccion"))
            txt_correo.set(persona.get("correo"))
            txt_edad.set(persona.get("edad"))
        else:
            e_cedula.focus()
            limpiar_campos()
            messagebox.showerror("Upps!!!", "NO Exite el trabajador..")

    else:
        e_cedula.focus()
        limpiar_campos()
        messagebox.showerror(
            "Upps!!!", "Debe ingresar la cedula del trabajador..")


def actualizar():
    if txt_edad.get().isnumeric():
        persona = {"cedula": txt_cedula.get(),
                   "edad": int(txt_edad.get()),
                   "nombre": txt_nombre.get(),
                   "apellido": txt_apellido.get(),
                   "direccion": txt_direccion.get(),
                   "correo": txt_correo.get(), }
        respuesta = crud.update(persona)
        if respuesta.get("respuesta"):
            llenar_tabla()
            messagebox.showinfo("OK", respuesta.get("mensaje"))
            limpiar_campos()
        else:
            messagebox.showerror("Upps!!!", respuesta.get("mensaje"))

    else:
        txt_edad.set("")
        e_edad.focus()
        messagebox.showerror("Upps!!!", "La EDAD debe ser un número..")


def eliminar():
    if txt_cedula.get() != "":

        respuesta = crud.find(txt_cedula.get())
        if respuesta.get("respuesta"):
            persona = respuesta.get("persona")
            respuesta = messagebox.askquestion("Confirmar", "¿Deseas eliminar a {} {} ?".format(
                persona.get("nombre"), persona.get("apellido")))

            if respuesta == "yes":
                respuesta = crud.delete(persona.get("id"))
                if respuesta.get("respuesta"):
                    llenar_tabla()
                    limpiar_campos()
                    messagebox.showinfo("OK", respuesta.get("mensaje"))
                else:
                    messagebox.showwarning(
                        "Upps!!!!", "No se logró eliminar el trabajadpr"+respuesta.get("mensaje"))
        else:
            messagebox.showwarning("Upps!!!!", "No existe la persona")
            limpiar_campos()

    else:
        e_cedula.focus()
        messagebox.showerror("Upps!!!", "Se debe ingresar la Cedula..")


################################## FIN_FUNCIONES #################################
################################## GUI ###########################################
fuente = ("Press Start 2P", 14)
fuente_2 = ("Press Start 2P", 40)
# Cambiado a morado intenso (#FF00FF) y verde intenso es (#00FF00)
fg_color = "#FF00FF"
pk_color = "#FFFF00"

# Colores de fondo para los widgets
bg_color = "#262626"  # Fondo negro
bg_color_alt = "#1c1c1c"  # Fondo alternativo

# Estilo de borde
borde_estilo = "flat"

# Estilo de resaltado
resaltado_estilo = "flat"

# Espacio alrededor del texto
padx_val = 10
pady_val = 5

Label(v, text="CEDULA: ", anchor="w", justify="left", width=10, bg=bg_color, fg=pk_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=0, column=0, padx=40, pady=5)
Label(v, text="NOMBRE: ", anchor="w", justify="left", width=10, bg=bg_color, fg=fg_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=1, column=0, padx=10, pady=5)
Label(v, text="APELLIDO: ", anchor="w", justify="left", width=10, bg=bg_color, fg=fg_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=2, column=0, padx=10, pady=5)
Label(v, text="DIRECCION: ", anchor="w", justify="left", width=10, bg=bg_color, fg=fg_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=3, column=0, padx=10, pady=5)
Label(v, text="CORREO: ", anchor="w", justify="left", width=10, bg=bg_color, fg=fg_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=4, column=0, padx=10, pady=5)
Label(v, text="EDAD: ", anchor="w", justify="left", width=10, bg=bg_color, fg=fg_color,
      font=fuente, padx=padx_val, pady=pady_val).grid(row=5, column=0, padx=10, pady=5)

# INPUTS
e_cedula = ttk.Entry(v, font=fuente, textvariable=txt_cedula)
e_nombre = ttk.Entry(v, font=fuente, textvariable=txt_nombre)
e_apellido = ttk.Entry(v, font=fuente, textvariable=txt_apellido)
e_direccion = ttk.Entry(v, font=fuente, textvariable=txt_direccion)
e_correo = ttk.Entry(v, font=fuente, textvariable=txt_correo)
e_edad = ttk.Entry(v, font=fuente, textvariable=txt_edad)

e_cedula.grid(row=0, column=1)
e_nombre.grid(row=1, column=1)
e_apellido.grid(row=2, column=1)
e_direccion.grid(row=3, column=1)
e_correo.grid(row=4, column=1)
e_edad.grid(row=5, column=1)
e_cedula.focus()
################################## IMAGENES #################################
icon_new = PhotoImage(file="icon_new.png")
icon_find = PhotoImage(file="icon_find.png")
icon_update = PhotoImage(file="icon_update.png")
icon_delete = PhotoImage(file="icon_delete.png")

################################## BOTONES #################################

ttk.Button(v, text="GUARDAR", command=guardar, image=icon_new,
           compound=LEFT).place(x=40, y=340)
ttk.Button(v, text="CONSULTAR", command=consultar, image=icon_find,
           compound=LEFT).place(x=200, y=340)
ttk.Button(v, text="ACTUALIZAR", command=actualizar, image=icon_update,
           compound=LEFT).place(x=350, y=340)
ttk.Button(v, text="ELIMINAR", command=eliminar, image=icon_delete,
           compound=LEFT).place(x=500, y=340)

Label(v, text="CRUD RETRO", font=fuente_2,
      bg="#FFFF00").place(x=800, y=150)

style = ttk.Style()
style.theme_use("alt")
style.configure("Treeview.Heading", background="#000000",
                foreground="#00FF00", font=("Press Start 2P", 12))

style.configure("Treeview.Column", background="#000000",
                foreground="#00FF00", font=("Press Start 2P", 12))

tabla = ttk.Treeview(v)
tabla.place(x=40, y=450)
tabla["columns"] = ("CEDULA", "EDAD", "NOMBRE",
                    "APELLIDO", "DIRECCION", "CORREO")

tabla.column("#0", width=0, stretch=NO)
tabla.column("CEDULA", width=140, anchor=CENTER)
tabla.column("EDAD", width=100, anchor=CENTER)
tabla.column("NOMBRE", width=300, anchor=CENTER)
tabla.column("APELLIDO", width=300, anchor=CENTER)
tabla.column("DIRECCION", width=170, anchor=CENTER)
tabla.column("CORREO", width=270, anchor=CENTER)

tabla.heading("#0", text="")
tabla.heading("CEDULA", text="Cedula")
tabla.heading("EDAD", text="Edad")
tabla.heading("NOMBRE", text="Nombre")
tabla.heading("APELLIDO", text="Apellido")
tabla.heading("DIRECCION", text="Direccion")
tabla.heading("CORREO", text="Correo")

################################## MENU #################################

menu_top = Menu(v)

menu_archivo = Menu(menu_top, tearoff=0)
menu_archivo.add_command(label="Creditos", command=creditos)
menu_archivo.add_command(label="Salir", command=salir)
menu_top.add_cascade(label="Archivo", menu=menu_archivo)

menu_limpiar = Menu(menu_top, tearoff=0)
menu_limpiar.add_command(label="Limpiar Campos", command=limpiar_campos)
menu_top.add_cascade(label="Limpiar", menu=menu_limpiar)

menu_crud = Menu(menu_top, tearoff=0)
menu_crud.add_command(label="Guardar", command=guardar,
                      image=icon_new, compound=LEFT)
menu_crud.add_command(label="Consultar", command=consultar,
                      image=icon_find, compound=LEFT)
menu_crud.add_command(label="Actualizar", command=actualizar,
                      image=icon_update, compound=LEFT)
menu_crud.add_command(label="Eliminar", command=eliminar,
                      image=icon_delete, compound=LEFT)
menu_top.add_cascade(label="SCRUD", menu=menu_crud)


v.config(menu=menu_top)
llenar_tabla()
v.mainloop()
