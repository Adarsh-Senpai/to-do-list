import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("To-Do List")


tasks = []


def update_tasks():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, task)


def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_tasks()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")


def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        task = tasks_listbox.get(selected_task_index)
        tasks.remove(task)
        update_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")


def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?"):
        tasks.clear()
        update_tasks()


task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", width=30, command=add_task)
add_task_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=45, height=10)
tasks_listbox.pack(pady=10)

delete_task_button = tk.Button(root, text="Delete Task", width=30, command=delete_task)
delete_task_button.pack(pady=5)

clear_tasks_button = tk.Button(root, text="Clear All Tasks", width=30, command=clear_tasks)
clear_tasks_button.pack(pady=5)

root.mainloop()









