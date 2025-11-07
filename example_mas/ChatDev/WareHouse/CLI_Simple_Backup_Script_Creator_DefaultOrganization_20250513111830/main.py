'''
Main application file for the Backup Script Creator. Initializes the GUI and handles user interactions.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from backup_script_generator import generate_rsync_script, generate_tar_script
class BackupScriptCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Backup Script Creator")
        self.source_dirs = []
        self.target_dir = ""
        self.create_widgets()
    def create_widgets(self):
        # Source Directories
        self.source_label = tk.Label(self.root, text="Source Directories:")
        self.source_label.pack()
        self.source_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.source_listbox.pack()
        self.add_source_button = tk.Button(self.root, text="Add Source Directory", command=self.add_source_directory)
        self.add_source_button.pack()
        # Target Directory
        self.target_label = tk.Label(self.root, text="Target Directory:")
        self.target_label.pack()
        self.target_entry = tk.Entry(self.root)
        self.target_entry.pack()
        self.select_target_button = tk.Button(self.root, text="Select Target Directory", command=self.select_target_directory)
        self.select_target_button.pack()
        # Script Generation
        self.generate_rsync_button = tk.Button(self.root, text="Generate Rsync Script", command=self.generate_rsync_script)
        self.generate_rsync_button.pack()
        self.generate_tar_button = tk.Button(self.root, text="Generate Tar Script", command=self.generate_tar_script)
        self.generate_tar_button.pack()
    def add_source_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_dirs.append(directory)
            self.source_listbox.insert(tk.END, directory)
    def select_target_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.target_dir = directory
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert(0, directory)
    def generate_rsync_script(self):
        if not self.source_dirs or not self.target_dir:
            messagebox.showerror("Error", "Please select source and target directories.")
            return
        script = generate_rsync_script(self.source_dirs, self.target_dir)
        self.save_script(script, "backup_rsync.sh")
    def generate_tar_script(self):
        if not self.source_dirs or not self.target_dir:
            messagebox.showerror("Error", "Please select source and target directories.")
            return
        script = generate_tar_script(self.source_dirs, self.target_dir)
        self.save_script(script, "backup_tar.sh")
    def save_script(self, script, filename):
        file_path = filedialog.asksaveasfilename(defaultextension=".sh", initialfile=filename)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(script)
            messagebox.showinfo("Success", f"Script saved to {file_path}")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = BackupScriptCreatorApp(root)
        root.mainloop()
    except tk.TclError:
        print("Error: No display environment available. Please ensure you have access to a graphical display or use a virtual display.")