import tkinter as tk
from tkinter import ttk, messagebox









app = tk.Tk()
app.title("Formulario de datos personales")

ttk.Label(app,text="ID: ").grid(column=0,row=0)
entry_id = ttk.Entry(app)
entry_id.grid(column=1,row=0)