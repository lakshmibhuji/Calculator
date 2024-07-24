import tkinter as tk
from tkinter import messagebox
def button_click(symbol):
 if symbol == '=':
 try:
 result = eval(entry.get())
 entry.delete(0, tk.END)
 entry.insert(tk.END, str(result))
 except Exception as e:
 messagebox.showerror("Error", "Invalid Input")
 elif symbol == 'C':
 entry.delete(0, tk.END)
 else:
 entry.insert(tk.END, symbol)
# Create main window
root = tk.Tk()
root.title("Calculator")
# Dark mode colors
root.config(bg="#2b2b2b")
button_color = "#333333"
text_color = "#ffffff"
# Entry field
entry = tk.Entry(root, width=35, borderwidth=5, bg=button_color, fg=text_color, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Define buttons
buttons = [
 ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
 ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
 ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
 ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
 ('C', 5, 0), ('^', 5, 1), ('√', 5, 2), ('!', 5, 3) # Additional operations: exponent (^), square root (√),
factorial (!)
]
# Create buttons
for (text, row, column) in buttons:
 button = tk.Button(root, text=text, padx=40, pady=20, bg=button_color, fg=text_color,
 font=("Arial", 12, "bold"), command=lambda symbol=text: button_click(symbol))
 button.grid(row=row, column=column)
# Run the main event loop
root.mainloop()
