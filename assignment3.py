import tkinter as tk
from tkinter import messagebox

# ---------------------------
# Event handler functions
# ---------------------------
def displayData():
    first = entFirst.get()
    last = entLast.get()
    email = entEmail.get()
    phone = entPhone.get()
    
    message = f"Personal Information:\n\nFirst Name: {first}\nLast Name: {last}\nEmail: {email}\nPhone: {phone}"
    messagebox.showinfo("Submitted Data", message)

def clear():
    entFirst.delete(0, tk.END)
    entLast.delete(0, tk.END)
    entEmail.delete(0, tk.END)
    entPhone.delete(0, tk.END)

# ---------------------------
# Main window setup
# ---------------------------
root = tk.Tk()
root.title("Personal Information Form")
root.geometry("500x300")

# Force window on top (Mac fix)
root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes,'-topmost', False)

# ---------------------------
# LabelFrame for Personal Info
# ---------------------------
lblFrPerson = tk.LabelFrame(root, text="Personal Information", padx=10, pady=10)
lblFrPerson.pack(padx=10, pady=10, fill="both", expand=True)

# First Name
lblFirst = tk.Label(lblFrPerson, text="*First Name:", bg="blue", fg="white")
lblFirst.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entFirst = tk.Entry(lblFrPerson)
entFirst.grid(row=0, column=1, padx=5, pady=5)

# Last Name
lblLast = tk.Label(lblFrPerson, text="*Last Name:", bg="blue", fg="white")
lblLast.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entLast = tk.Entry(lblFrPerson)
entLast.grid(row=1, column=1, padx=5, pady=5)

# Email
lblEmail = tk.Label(lblFrPerson, text="Email:", bg="blue", fg="white")
lblEmail.grid(row=2, column=0, sticky="w", padx=5, pady=5)
entEmail = tk.Entry(lblFrPerson)
entEmail.grid(row=2, column=1, padx=5, pady=5)

# Phone
lblPhone = tk.Label(lblFrPerson, text="Phone:", bg="blue", fg="white")
lblPhone.grid(row=3, column=0, sticky="w", padx=5, pady=5)
entPhone = tk.Entry(lblFrPerson)
entPhone.grid(row=3, column=1, padx=5, pady=5)

# ---------------------------
# Buttons Frame
# ---------------------------
fraButtons = tk.Frame(root)
fraButtons.pack(pady=10)

btnS = tk.Button(fraButtons, text="Submit", width=5, command=displayData)
btnS.pack(side=tk.LEFT, padx=5)

btnR = tk.Button(fraButtons, text="Reset", width=5, command=clear)
btnR.pack(side=tk.LEFT, padx=5)

btnQ = tk.Button(fraButtons, text="Quit", width=5, command=root.destroy)
btnQ.pack(side=tk.LEFT, padx=5)

# ---------------------------
# Run the application
# ---------------------------
root.mainloop()