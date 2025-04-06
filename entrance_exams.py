import tkinter as tk
from tkinter import messagebox

# Data storage sets
njee = set()
ncet = set()
nneet = set()

selected = {
    "JEE": False,
    "CET": False,
    "NEET": False
}

# Main application window
root = tk.Tk()
root.title("Exam Candidate Analyzer")
root.geometry("500x500")

def submit_candidates(exam):
    global njee, ncet, nneet
    
    if selected[exam]:
        messagebox.showinfo("Notice", f"You've already entered data for {exam}.")
        return
    
    input_str = entry.get().strip()
    if not input_str:
        messagebox.showerror("Error", "Please enter at least one name.")
        return
    
    names = set(input_str.split())

    if exam == "JEE":
        njee = names
    elif exam == "CET":
        ncet = names
    elif exam == "NEET":
        nneet = names

    selected[exam] = True
    messagebox.showinfo("Success", f"Names added for {exam}")
    entry.delete(0, tk.END)

def show_analysis_menu():
    analysis_window = tk.Toplevel(root)
    analysis_window.title("In-Depth Analysis")

    def perform_analysis(choice):
        if choice == 1:
            result = njee | ncet | nneet
        elif choice == 2:
            result = njee & ncet
        elif choice == 3:
            result = ncet - njee
        elif choice == 4:
            result = njee & ncet & nneet
        else:
            return

        messagebox.showinfo("Result", f"Result: {', '.join(result) if result else 'No matches'}")

    tk.Label(analysis_window, text="Choose Analysis Type", font=("Arial", 12)).pack(pady=10)

    options = [
        ("CET or JEE or NEET", 1),
        ("CET and JEE", 2),
        ("CET but not JEE", 3),
        ("JEE and CET and NEET", 4),
        ("Exit", 5)
    ]

    for text, val in options:
        tk.Button(analysis_window, text=text, width=30, command=lambda v=val: (
            analysis_window.destroy() if v == 5 else perform_analysis(v)
        )).pack(pady=5)

# Layout
tk.Label(root, text="Enter candidate names (space-separated):", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Submit JEE Names", command=lambda: submit_candidates("JEE")).pack(pady=5)
tk.Button(root, text="Submit CET Names", command=lambda: submit_candidates("CET")).pack(pady=5)
tk.Button(root, text="Submit NEET Names", command=lambda: submit_candidates("NEET")).pack(pady=5)

tk.Button(root, text="In-Depth Analysis", bg="#4CAF50", fg="white", command=show_analysis_menu).pack(pady=20)

tk.Button(root, text="Exit", bg="red", fg="white", command=root.quit).pack(pady=10)

root.mainloop()
