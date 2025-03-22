import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title('Aplicación de Agenda Personal')
        self.root.geometry('600x400')

        # Inicializo la lista de eventos
        self.eventos = []

        # Creo un Frame para la entrada de datos
        entrada_frame = tk.Frame(self.root)
        entrada_frame.pack(pady=10)

        # Etiqueta y selector de fecha
        tk.Label(entrada_frame, text='Fecha:').grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(entrada_frame, width=12, background='darkblue', foreground='white', date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la hora
        tk.Label(entrada_frame, text='Hora:').grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(entrada_frame)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y campo de entrada para la descripción
        tk.Label(entrada_frame, text='Descripción:').grid(row=2, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(entrada_frame, width=30)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Creo un Frame para los botones
        botones_frame = tk.Frame(self.root)
        botones_frame.pack(pady=10)

        # Botón para agregar evento
        agregar_btn = tk.Button(botones_frame, text='Agregar Evento', command=self.agregar_evento)
        agregar_btn.grid(row=0, column=0, padx=10)

        # Botón para eliminar evento
        eliminar_btn = tk.Button(botones_frame, text='Eliminar Evento Seleccionado', command=self.eliminar_evento)
        eliminar_btn.grid(row=0, column=1, padx=10)

        # Botón para salir de la aplicación
        salir_btn = tk.Button(botones_frame, text='Salir', command=self.root.quit)
        salir_btn.grid(row=0, column=2, padx=10)

        # Configuro TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.root, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.descripcion_entry.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos.')
            return

        # Agrego el evento a la lista y lo muestro en la interfaz
        self.eventos.append((fecha, hora, descripcion))
        self.tree.insert('', 'end', values=(fecha, hora, descripcion))

        # Limpio las entradas
        self.hora_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning('Advertencia', 'Por favor, seleccione un evento para eliminar.')
            return

        confirmacion = messagebox.askyesno('Confirmación', '¿Estás seguro de que deseas eliminar este evento?')
        if confirmacion:
            for item in seleccion:
                self.tree.delete(item)

if __name__ == '__main__':
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()