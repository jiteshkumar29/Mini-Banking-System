
# Basic GUI Calculator using Tkinter
import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            entry_var.set(result)
            expression = result
        except:
            entry_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    else:
        expression += text
        entry_var.set(expression)

# Main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

expression = ""
entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font="Arial 18", relief=tk.RAISED, border=3)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

# Run the app
root.mainloop()
