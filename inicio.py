import customtkinter as ctk
from main import CalculadoraMatrices


class PantallaInicio(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.title("Menú de Inicio")
        self.geometry("700x500")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        # Contenedor principal redondeado para que se vea bien
        self.container = ctk.CTkFrame(self, corner_radius=25)
        self.container.pack(expand=True, fill="both", padx=30, pady=30)

        # Título dentro del contenedor
        self.titulo = ctk.CTkLabel(
            self.container,
            text="Calculadora de Matrices",
            font=("Arial Rounded MT Bold", 24)
        )
        self.titulo.pack(pady=40)

        # Variables de las operaciones, tama;os en el frame
        self.tipo_matriz = ctk.StringVar(value="Cuadrada")
        self.size_matriz = ctk.StringVar(value="3x3")
        self.operacion_matriz = ctk.StringVar(value="Suma")
        

        # Frame de opciones
        frame_opciones = ctk.CTkFrame(self.container, corner_radius=20, fg_color=("#1c1f26", "#2c2f36"))
        frame_opciones.pack(pady=25)

        ctk.CTkLabel(frame_opciones, text="Tipo de matriz:", font=("Arial", 16)).grid(row=0, column=0, padx=15, pady=10)
        ctk.CTkOptionMenu(frame_opciones, variable=self.tipo_matriz, values=["Cuadrada", "Rectangular"],
                          command=self.actualizar_size , corner_radius=15).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkLabel(frame_opciones, text="Tamaño:", font=("Arial", 16)).grid(row=1, column=0, padx=15, pady=10)
        self.menu_tamaños = ctk.CTkOptionMenu(frame_opciones, variable=self.size_matriz, values=["2x2", "3x3", "4x4"],
                                              corner_radius=15)
        self.menu_tamaños.grid(row=1, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(frame_opciones, text="Operación:", font=("Arial", 16)).grid(row=2, column=0, padx=15, pady=10)
        self.menu_operaciones = ctk.CTkOptionMenu(frame_opciones, variable=self.operacion_matriz,
                                                  values=["Suma", "Resta", "Multiplicación", "Determinante",
                                                          "Inversa", "Cofactores", "Gauss-Jordan"],
                                                  corner_radius=15)
        self.menu_operaciones.grid(row=2, column=1, padx=10, pady=10)

        # Botón principal
        ctk.CTkButton(self.container,
                      text="Calcular",
                      font=("Arial Rounded MT Bold", 18),
                      height=55,
                      corner_radius=25,
                      fg_color="#1E90FF",
                      hover_color="#4682B4",
                      command=self.abrir_calculadora).pack(pady=35)

        # Créditos
        ctk.CTkLabel(self.container,
                     text="Proyecto desarrollado en Python por ---",
                     font=("Arial", 13, "italic"),
                     text_color="gray").pack(side="bottom", pady=10)

    def actualizar_size (self, tipo):
        if tipo == "Cuadrada":
            self.menu_tamaños.configure(values=["2x2", "3x3", "4x4"])
            self.size_matriz.set("3x3")
        else:
            self.menu_tamaños.configure(values=["2x3", "3x2"])
            self.size_matriz.set("2x3")

    def abrir_calculadora(self):
        self.destroy()
        root = ctk.CTk()
        app = CalculadoraMatrices(root,
                                  tamaño=self.size_matriz.get(),
                                  operacion=self.operacion_matriz.get())
        root.mainloop()


if __name__ == "__main__":
    app = PantallaInicio()
    app.mainloop()