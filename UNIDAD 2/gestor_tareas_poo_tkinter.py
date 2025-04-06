import tkinter as tk
from tkinter import messagebox, ttk


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        # Configuración de atajos de teclado
        self.root.bind("<Escape>", lambda e: self.root.quit())
        self.root.bind("<Delete>", lambda e: self.delete_task())
        self.root.bind("d", lambda e: self.delete_task())
        self.root.bind("c", lambda e: self.mark_completed())

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(main_frame, font=("Arial", 12))
        self.task_entry.pack(fill=tk.X, pady=5)
        self.task_entry.bind("<Return>", lambda e: self.add_task())  # Enter para añadir

        # Botón para añadir tarea
        add_button = tk.Button(main_frame, text="Añadir Tarea (Enter)", command=self.add_task)
        add_button.pack(fill=tk.X, pady=2)

        # Lista de tareas (Treeview para mejor visualización)
        self.task_list = ttk.Treeview(main_frame, columns=("status"), selectmode="browse")
        self.task_list.heading("#0", text="Tarea")
        self.task_list.heading("status", text="Estado")
        self.task_list.column("status", width=100, anchor="center")
        self.task_list.pack(fill=tk.BOTH, expand=True, pady=5)

        # Frame para botones de acción
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=5)

        complete_button = tk.Button(button_frame, text="Marcar como Completada (C)", command=self.mark_completed)
        complete_button.pack(side=tk.LEFT, expand=True, padx=2)

        delete_button = tk.Button(button_frame, text="Eliminar Tarea (D/Delete)", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, expand=True, padx=2)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.task_list.insert("", tk.END, text=task_text, values=("Pendiente"))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def mark_completed(self):
        selected_item = self.task_list.selection()
        if selected_item:
            current_status = self.task_list.item(selected_item, "values")[0]
            new_status = "Completada" if current_status == "Pendiente" else "Pendiente"
            self.task_list.item(selected_item, values=(new_status))

            # Cambiar color para feedback visual
            tags = ("completed",) if new_status == "Completada" else ()
            self.task_list.item(selected_item, tags=tags)
            self.task_list.tag_configure("completed", foreground="gray", font=("Arial", 10, "italic"))

    def delete_task(self):
        selected_item = self.task_list.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Eliminar esta tarea?")
            if confirm:
                self.task_list.delete(selected_item)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()