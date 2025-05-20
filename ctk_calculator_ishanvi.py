import customtkinter as ctk

# Setup customtkinter appearance
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Create main window
window = ctk.CTk()
window.geometry("312x400")
window.title("Calculator")

# Expression handling
expression = ""
input_text = ctk.StringVar()

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Input frame and field
input_frame = ctk.CTkFrame(window, width=312, height=50)
input_frame.pack(side="top", pady=10)

input_field = ctk.CTkEntry(input_frame, font=('Segoe UI', 20), textvariable=input_text, width=280, height=40, justify='right')
input_field.pack(ipady=8)

# Buttons frame
btns_frame = ctk.CTkFrame(window, width=312, height=272)
btns_frame.pack()

# Create button helper
def create_button(text, command, r, c, colspan=1):
    btn = ctk.CTkButton(btns_frame, text=text, width=70 * colspan, height=50, command=command)
    btn.grid(row=r, column=c, columnspan=colspan, padx=2, pady=2)

# First row
create_button("C", btn_clear, 0, 0)
create_button("/", lambda: btn_click("/"), 0, 1)
create_button("*", lambda: btn_click("*"), 0, 2)
create_button("-", lambda: btn_click("-"), 0, 3)

# Second row
create_button("7", lambda: btn_click("7"), 1, 0)
create_button("8", lambda: btn_click("8"), 1, 1)
create_button("9", lambda: btn_click("9"), 1, 2)
create_button("+", lambda: btn_click("+"), 1, 3)

# Third row
create_button("4", lambda: btn_click("4"), 2, 0)
create_button("5", lambda: btn_click("5"), 2, 1)
create_button("6", lambda: btn_click("6"), 2, 2)
create_button("=", btn_equal, 2, 3)

# Fourth row
create_button("1", lambda: btn_click("1"), 3, 0)
create_button("2", lambda: btn_click("2"), 3, 1)
create_button("3", lambda: btn_click("3"), 3, 2)
create_button(".", lambda: btn_click("."), 3, 3)

# Fifth row (Zero spans 2 columns)
create_button("0", lambda: btn_click("0"), 4, 0, colspan=4)

# Start the app
window.mainloop()

