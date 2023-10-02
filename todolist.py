import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=30, font=('Arial', 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        add_button = tk.Button(root, text='Add Task', font=('Arial', 14), command=self.add_task)
        add_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.task_listbox = tk.Listbox(root, width=40, height=10, font=('Arial', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        delete_button = tk.Button(root, text='Delete Task', font=('Arial', 14), command=self.delete_task)
        delete_button.grid(row=2, column=0, padx=10, pady=10)
        
        clear_button = tk.Button(root, text='Clear All', font=('Arial', 14), command=self.clear_tasks)
        clear_button.grid(row=2, column=1, padx=10, pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
        
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        
    def clear_tasks(self):
        self.tasks = []
        self.update_task_listbox()
        
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()