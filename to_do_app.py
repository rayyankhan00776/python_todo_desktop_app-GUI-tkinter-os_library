import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import time
import json

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("500x500")
        self.root.configure(bg="#f8f9fa")

        # Define the base directory for saving tasks
        self.directory = r"E:\python\to do"
        self.file_base_name = "tasks_"
        
        # Ensure the directory exists
        self.ensure_directory_exists()
        
        # Determine the current file path
        self.file_path = self.get_current_file_path()
        
        # Load existing tasks
        self.tasks = self.load_tasks()
        
        # Create GUI components
        self.create_widgets()
        
    def ensure_directory_exists(self):
        """Ensure the directory for saving tasks exists."""
        if not os.path.exists(self.directory):
            try:
                os.makedirs(self.directory)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to create directory: {e}")
    
    def get_current_file_path(self):
        """Generate a unique file path based on the current timestamp."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.directory, f"{self.file_base_name}{timestamp}.json")
    
    def create_widgets(self):
        """Create and place GUI components."""
        # Title Label
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 20, "bold"), bg="#f8f9fa")
        self.title_label.pack(pady=15)
        
        # Search Frame
        self.search_frame = tk.Frame(self.root, bg="#f8f9fa")
        self.search_frame.pack(pady=(0, 10), padx=20, fill=tk.X)
        
        tk.Label(self.search_frame, text="Search:", bg="#f8f9fa", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(self.search_frame, font=("Helvetica", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_tasks, bg="#007bff", fg="white", font=("Helvetica", 12), relief=tk.RAISED)
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        # Create listbox for tasks
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#ffffff", selectbackground="#c4e0ff", activestyle='none')
        self.task_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 10))
        
        # Populate listbox with tasks
        self.update_listbox()
        
        # Button Frame
        self.button_frame = tk.Frame(self.root, bg="#f8f9fa")
        self.button_frame.pack(pady=10, padx=20, fill=tk.X)
        
        # Create buttons
        self.create_buttons()
        
    def create_buttons(self):
        """Create and place buttons for task management."""
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#28a745", fg="white", font=("Helvetica", 12), relief=tk.RAISED)
        self.add_button.pack(side=tk.LEFT, padx=5)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="#dc3545", fg="white", font=("Helvetica", 12), relief=tk.RAISED)
        self.delete_button.pack(side=tk.LEFT, padx=5)
        
        self.edit_button = tk.Button(self.button_frame, text="Edit Task", command=self.edit_task, bg="#007bff", fg="white", font=("Helvetica", 12), relief=tk.RAISED)
        self.edit_button.pack(side=tk.LEFT, padx=5)

        # This line has a mistake: it should be self.mark_as_done instead of self.edit_button
        self.edit_button = tk.Button(self.button_frame, text="Mark As Read", command=self.edit_task, bg="#007bff", fg="white", font=("Helvetica", 12), relief=tk.RAISED)
        self.mark_as_done.pack(side=tk.LEFT, padx=5)

    def search_tasks(self):
        """Filter tasks based on search entry."""
        search_term = self.search_entry.get().strip().lower()
        if search_term:
            filtered_tasks = [task for task in self.tasks if search_term in task.lower()]
        else:
            filtered_tasks = self.tasks
        self.update_listbox(filtered_tasks)
        
    def add_task(self):
        """Prompt for a new task and add it to the list."""
        task = self.prompt_for_task("Add Task")
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.save_tasks()
        
    def delete_task(self):
        """Delete the selected task from the list."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
        
    def edit_task(self):
        """Edit the selected task."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            old_task = self.tasks[selected_task_index[0]]
            new_task = self.prompt_for_task("Edit Task", old_task)
            if new_task:
                self.tasks[selected_task_index[0]] = new_task
                self.update_listbox()
                self.save_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to edit.")
    
    def mark_as_done(self):
        """Mark the selected task as done."""
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks[selected_task_index[0]]["completed"] = True
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("No Selection", "Please select a task to mark as done.")
        
    def prompt_for_task(self, title, initial_value=""):
        """Prompt the user for a task."""
        prompt_window = tk.Toplevel(self.root)
        prompt_window.title(title)
        prompt_window.geometry("300x150")
        prompt_window.configure(bg="#f8f9fa")
        
        tk.Label(prompt_window, text="Task:", bg="#f8f9fa", font=("Helvetica", 12)).pack(pady=10)
        task_entry = tk.Entry(prompt_window, font=("Helvetica", 12))
        task_entry.insert(0, initial_value)
        task_entry.pack(pady=10)
        
        task = None
        def on_ok():
            nonlocal task
            task = task_entry.get().strip()
            if task:
                prompt_window.destroy()
            else:
                messagebox.showwarning("Invalid Input", "Task cannot be empty.")
        
        button_frame = tk.Frame(prompt_window, bg="#f8f9fa")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="OK", command=on_ok, bg="#28a745", fg="white", font=("Helvetica", 12)).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Cancel", command=prompt_window.destroy, bg="#dc3545", fg="white", font=("Helvetica", 12)).pack(side=tk.RIGHT, padx=10)
        
        self.root.wait_window(prompt_window)
        return task
        
    def update_listbox(self, tasks=None):
        """Update the listbox with current tasks."""
        self.task_listbox.delete(0, tk.END)
        if tasks is None:
            tasks = self.tasks
        for task in tasks:
            self.task_listbox.insert(tk.END, task)
        
    def save_tasks(self):
        """Save tasks to a JSON file."""
        try:
            with open(self.file_path, "w") as file:
                json.dump({"tasks": self.tasks}, file, indent=4)
            print(f"Tasks saved to: {self.file_path}")  # Debug print
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {e}")

    def load_tasks(self):
        """Load tasks from a JSON file."""
        tasks = []
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    data = json.load(file)
                    tasks = data.get("tasks", [])
                    print(f"Tasks loaded from: {self.file_path}")  # Debug print
        except json.JSONDecodeError:
            messagebox.showwarning("Warning", "Task file is empty or corrupted.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {e}")
        return tasks

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
