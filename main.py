import tkinter as tk
from tkinter import filedialog, messagebox
from update import update_incorporation_state

def run_ui():
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("HTML files", "*.htm;*.html")])
        if file_path:
            html_entry.delete(0, tk.END)
            html_entry.insert(0, file_path)

    def submit():
        html_path = html_entry.get().strip()
        new_state = state_entry.get().strip()
        xsd_path = "msft-20250430.xsd"

        if not html_path or not new_state:
            messagebox.showerror("Error", "Please select an HTML file and enter a new state.")
            return

        try:
            update_incorporation_state(html_path, new_state)
            messagebox.showinfo("Success", f"Incorporation state updated to: {new_state}")
        except Exception as e:
            messagebox.showerror("Update Failed", str(e))

    # Setup UI
    root = tk.Tk()
    root.title("8-K State Update Tool")

    tk.Label(root, text="HTML File:").grid(row=0, column=0, sticky="e")
    html_entry = tk.Entry(root, width=50)
    html_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse...", command=select_file).grid(row=0, column=2)

    tk.Label(root, text="New State:").grid(row=1, column=0, sticky="e")
    state_entry = tk.Entry(root, width=20)
    state_entry.grid(row=1, column=1, sticky="w")

    tk.Button(root, text="Update State", command=submit).grid(row=2, column=1, pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_ui()
