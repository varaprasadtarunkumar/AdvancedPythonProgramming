import tkinter as tk

def update_label():
    label_var.set("Checked" if check_var.get() else "Unchecked")

root = tk.Tk()
root.title("Simple Checkbutton Example")

check_var = tk.BooleanVar()

check_button = tk.Checkbutton(root, text="Check me", variable=check_var, command=update_label)

label_var = tk.StringVar()
label = tk.Label(root, textvariable=label_var)
label.pack()

check_button.pack()
root.mainloop()
