from tkinter import *
from tkinter import messagebox as MessageBox
from curpgenerate.curp import CurpGenerator
import re

class CurpApplication:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Generador de CURP")
        self.root.geometry("500x600")
        self.root.configure(bg="#040D12")  # Fondo principal

        # Título
        title_frame = Frame(self.root, bg="#040D12")  # Fondo oscuro del título
        title_frame.pack(pady=20)
        title_label = Label(title_frame, text="Calculadora de CURP", font=("Helvetica", 20, "bold"), bg="#040D12", fg="#93B1A6")
        title_label.grid(row=0, column=0)

        # Contenedor principal para formularios
        form_frame = Frame(self.root, bg="#183D3D", padx=20, pady=20)  # Fondo de formulario
        form_frame.pack(pady=10, fill="both", expand=True)

        # Campos de entrada
        self.crear_label_entry(form_frame, "Nombre:", "entrada_nombre", 0)
        self.crear_label_entry(form_frame, "Apellido Paterno:", "entrada_apellido_paterno", 1)
        self.crear_label_entry(form_frame, "Apellido Materno:", "entrada_apellido_materno", 2)
        self.crear_label_entry(form_frame, "Fecha de Nacimiento (dd-mm-yyyy):", "entrada_fecha_nacimiento", 3)

        # Género
        self.genero_var = StringVar()
        self.genero_var.set("H")
        self.crear_dropdown(form_frame, "Género:", self.genero_var, ["H", "M"], 4)

        # Estado de nacimiento
        self.estado_var = StringVar()
        self.estado_var.set("AS")
        estados = ["AS", "BC", "BS", "CC", "CL", "CM", "CS", "CH", "DF", "DG", "GT", "GR", "HG",
                   "JC", "MC", "MN", "MS", "NT", "NL", "OC", "PL", "QT", "QR", "SP", "SL", "SR",
                   "TC", "TS", "TL", "VZ", "YN", "ZS"]
        self.crear_dropdown(form_frame, "Estado de Nacimiento:", self.estado_var, estados, 5)

        # Botón para calcular CURP
        button_frame = Frame(self.root, bg="#040D12")
        button_frame.pack(pady=20)
        boton_calcular = Button(button_frame, text="Calcular CURP", command=self.calcular_curp,
                                bg="#5C8374", fg="white", font=("Helvetica", 12, "bold"), width=20)  # Botón verde oscuro
        boton_calcular.grid(row=0, column=0)

        # Etiqueta de Resultado
        result_frame = Frame(self.root, bg="#040D12")
        result_frame.pack(pady=10)
        self.resultado_label = Label(result_frame, text="", font=("Helvetica", 14, "bold"), bg="#040D12", fg="#93B1A6")  # Color claro para resultado
        self.resultado_label.grid(row=0, column=0)

    def crear_label_entry(self, frame, texto_label, nombre_entry, row):
        label = Label(frame, text=texto_label, font=("Helvetica", 10, "bold"), bg="#183D3D", fg="#93B1A6")  # Fondo verde oscuro y texto claro
        label.grid(row=row, column=0, sticky="w", pady=5)
        entry = Entry(frame, width=30, font=("Helvetica", 12), bg="#5C8374", fg="#040D12", insertbackground="#040D12")  # Entrada verde medio con texto oscuro
        entry.grid(row=row, column=1, pady=5, padx=10)
        setattr(self, nombre_entry, entry)

    def crear_dropdown(self, frame, texto_label, variable, opciones, row):
        label = Label(frame, text=texto_label, font=("Helvetica", 10, "bold"), bg="#183D3D", fg="#93B1A6")  # Fondo verde oscuro y texto claro
        label.grid(row=row, column=0, sticky="w", pady=5)
        dropdown = OptionMenu(frame, variable, *opciones)
        dropdown.config(width=25, font=("Helvetica", 10), bg="#5C8374", fg="#040D12", activebackground="#183D3D", activeforeground="#93B1A6")  # Menú verde medio con texto oscuro
        dropdown.grid(row=row, column=1, pady=5, padx=10)

    def calcular_curp(self):
        try:
            # Validación de formato de fecha
            if not re.match(r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$", self.entrada_fecha_nacimiento.get()):
                MessageBox.showerror("Error", "Por favor, ingrese una fecha válida en formato dd-mm-yyyy.")
                return

            # Generar CURP
            generador_curp = CurpGenerator(
                self.entrada_nombre.get(),
                self.entrada_apellido_paterno.get(),
                self.entrada_apellido_materno.get(),
                self.entrada_fecha_nacimiento.get(),
                self.genero_var.get(),
                self.estado_var.get()
            )
            resultado = generador_curp.calculateCurp()
            self.resultado_label.config(text=f"CURP: {resultado}")

        except Exception as e:
            MessageBox.showerror("Error", f"Por favor, completa todos los campos correctamente. Detalles: {e}")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = CurpApplication(root)
    root.mainloop()