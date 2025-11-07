'''
Handles the graphical user interface for the Git Branch Cleanup Tool.
Uses tkinter for the GUI.
'''
import tkinter as tk
from tkinter import messagebox
from git_branch_manager import GitBranchManager
class GitBranchGUI:
    def __init__(self):
        self.manager = GitBranchManager()
        self.root = tk.Tk()
        self.root.title("Git Branch Cleanup Tool")
        self.branch_listbox = tk.Listbox(self.root, width=50, height=15)
        self.branch_listbox.pack(pady=20)
        self.update_branch_list()
        self.delete_button = tk.Button(self.root, text="Delete Selected Branch", command=self.delete_selected_branch)
        self.delete_button.pack(pady=10)
    def update_branch_list(self):
        '''
        Updates the list of branches in the GUI.
        '''
        self.branch_listbox.delete(0, tk.END)
        branches = self.manager.list_merged_branches() + self.manager.list_inactive_branches()
        for branch in branches:
            self.branch_listbox.insert(tk.END, branch)
    def delete_selected_branch(self):
        '''
        Deletes the selected branch from the GUI.
        '''
        selected_indices = self.branch_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No Branch Selected", "Please select a branch to delete.")
            return
        for index in selected_indices:
            branch_name = self.branch_listbox.get(index)
            if messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete branch '{branch_name}'?"):
                try:
                    self.manager.delete_branch(branch_name)
                    self.update_branch_list()
                    messagebox.showinfo("Branch Deleted", f"Branch '{branch_name}' has been deleted.")
                except subprocess.CalledProcessError as e:
                    messagebox.showerror("Error Deleting Branch", str(e))
    def run(self):
        '''
        Runs the GUI.
        '''
        self.root.mainloop()