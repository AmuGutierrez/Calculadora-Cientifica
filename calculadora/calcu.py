from tkinter import StringVar
import customtkinter as ctk
from config import bg_b, text_b, hover_b, hover_o, bg_o

amu = ctk.CTk(fg_color="#ffffff")
amu.title("Calculadora de Amu :)")

# -> --------------| Configuración de la ventana |-------------- <-

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Calcula la posición para centrar la ventana
width = 280
height = 420

screen_width = amu.winfo_screenwidth()
screen_height = amu.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)

amu.geometry(f"{width}x{height}+{x}+{y}")
amu.maxsize(280, 420)
amu.minsize(280, 420)

# -> --------------| configuracion del Output |-------------- <-

expression = StringVar()

def add_output(char):
    global expression
    ops = ['.', 'x', '+', '-', '÷']
    last_char = expression.get()[-1] if len(expression.get())>0 else ''
    if char in ops:
        if last_char in ops:
            return
    expression.set(expression.get() + char)

# -> --------------| Funciones |-------------- <-

def calculate():
    global expression
    try:
        result = eval(expression.get())
        if isinstance(result, float):
            result = round(result, 3)
        expression.set(str(result))
    except Exception as e:
        expression.set('') # <- Simbolisa un error xd

def delete_last():
    global expression
    exp = expression.get()
    if exp:
        new_exp = exp[:-1]
        expression.set(new_exp)

def plus_minus():
    global expression
    exp = expression.get()
    if exp:
        if exp[0] !='-':
            exp = '-' + exp
        elif exp[0] == '-':
            exp = exp[1:]
    expression.set(exp)

# -> --------------| interfaz |-------------- <-

output = ctk.CTkEntry(amu, textvariable= expression, fg_color="transparent", border_width=0, justify="right", width=280, height=80, font=("Arial", 30))
output.grid(row=0, column=0, columnspan=4, sticky="nsew")

# --> -------| Botones fila 1 |------- <--

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="%", command= lambda: add_output('%'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=1, column=0, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="-/+", command= plus_minus, border_width=1, border_color="gray", width=62, height=60, font=("Arial", 25), text_color=text_b, hover_color=hover_b)
buttons.grid(row=1, column=1, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="C", command= lambda: expression.set('') , border_width=1, border_color="gray", width=62, height=60, font=("Arial", 25), text_color=text_b, hover_color=hover_b)
buttons.grid(row=1, column=2, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="⌫", command= delete_last, border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=1, column=3, pady=4, padx=2)

# --> -------| Botones fila 2 |------- <--

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="1", command= lambda: add_output('1'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=2, column=0, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="2", command= lambda: add_output('2'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=2, column=1, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="3", command= lambda: add_output('3'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=2, column=2, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="÷", command= lambda: add_output('/'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=2, column=3, pady=4, padx=2)

# --> -------| Botones fila 3 |------- <--

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="4", command= lambda: add_output('4'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=3, column=0, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="5", command= lambda: add_output('5'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=3, column=1, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="6", command= lambda: add_output('6'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=3, column=2, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="x", command= lambda: add_output('*'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=3, column=3, pady=4, padx=2)

# --> -------| Botones fila 4 |------- <--

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="7", command= lambda: add_output('7'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=4, column=0, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="8", command= lambda: add_output('8'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=4, column=1, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="9", command= lambda: add_output('9'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=4, column=2, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="-", command= lambda: add_output('-'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=4, column=3, pady=4, padx=2)

# --> -------| Botones fila 5 |------- <--

buttons = ctk.CTkButton(amu,fg_color=bg_b, text=".", command= lambda: add_output('.'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=5, column=0, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="0", command= lambda: add_output('0'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 20), text_color=text_b, hover_color=hover_b)
buttons.grid(row=5, column=1, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_o, text="=", command= calculate, border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_o)
buttons.grid(row=5, column=2, pady=4, padx=2)

buttons = ctk.CTkButton(amu,fg_color=bg_b, text="+", command= lambda: add_output('+'), border_width=1, border_color="gray", width=62, height=60, font=("Arial", 30), text_color=text_b, hover_color=hover_b)
buttons.grid(row=5, column=3, pady=4, padx=2)

amu.mainloop()

config.py

# -> --------------| Botones [Números & signos] |-------------- <-

bg_b = "#f8f8f8"
hover_b = "#f0f0f0"
text_b = "#292929"

# -> --------------| Botón [Sígno igual] |-------------- <-

bg_o = "#4f9851"
hover_o = "#3d7c3f"
