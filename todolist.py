import tkinter as tk
from tkinter import ttk

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(bg="#87CEEB")

        self.tasks = []

        self.task_entry = ttk.Entry(self.root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=5, pady=10)

        self.mark_button = ttk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.mark_button.grid(row=2, column=1, padx=5, pady=10)

        self.display_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.display_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.display_tasks()

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]['completed'] = True
            self.display_tasks()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")


def main():
    root = tk.Tk()

    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
