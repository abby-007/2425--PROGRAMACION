import tkinter as tk
from tkinter import messagebox, ttk


class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas POO")
        self.root.geometry("500x400")

        # Variables
        self.tareas = []

        # Crear interfaz
        self._crear_widgets()

    def _crear_widgets(self):
        """Configura todos los componentes de la interfaz."""
        # Frame principal
        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada
        self.entrada_tarea = ttk.Entry(frame, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)
        self.entrada_tarea.bind("<Return>", lambda e: self.agregar_tarea())  # Evento Enter

        # Botón "Añadir"
        btn_agregar = ttk.Button(frame, text="Añadir Tarea", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tareas (Treeview para mejor visualización)
        self.lista_tareas = ttk.Treeview(frame, columns=("completada"), show="headings", height=15)
        self.lista_tareas.heading("#0", text="Tarea")
        self.lista_tareas.heading("completada", text="Estado")
        self.lista_tareas.column("#0", width=300)
        self.lista_tareas.column("completada", width=100, anchor="center")
        self.lista_tareas.grid(row=1, column=0, columnspan=2, pady=10, sticky=tk.NSEW)

        # Evento doble clic para marcar como completada
        self.lista_tareas.bind("<Double-1>", lambda e: self.marcar_completada())

        # Frame para botones inferiores
        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=5)

        # Botón "Marcar como Completada"
        btn_completar = ttk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.pack(side=tk.LEFT, padx=5)

        # Botón "Eliminar"
        btn_eliminar = ttk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self):
        """Añade una tarea a la lista."""
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entrada_tarea.delete(0, tk.END)  # Limpiar campo
        else:
            messagebox.showwarning("Error", "¡Escribe una tarea válida!")

    def marcar_completada(self):
        """Cambia el estado de la tarea seleccionada."""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            index = self.lista_tareas.index(seleccion[0])
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada."""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            index = self.lista_tareas.index(seleccion[0])
            del self.tareas[index]
            self.actualizar_lista()

    def actualizar_lista(self):
        """Actualiza el Treeview con las tareas actuales."""
        self.lista_tareas.delete(*self.lista_tareas.get_children())
        for tarea in self.tareas:
            estado = "✔️" if tarea["completada"] else "Pendiente"
            self.lista_tareas.insert("", tk.END, text=tarea["texto"], values=(estado,))


# Iniciar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()