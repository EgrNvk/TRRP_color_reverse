import tkinter as tk

def show_color():
    global r 
    global g 
    global b
    try:
        r = int(entry_r.get())
        g = int(entry_g.get())
        b = int(entry_b.get())

        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError

        root.configure(bg=f"#{r:02x}{g:02x}{b:02x}")
    except:
        root.configure(bg="red")  
        
def invert_color():
    global r 
    global g 
    global b
    r = 255 - r
    g = 255 - g 
    b = 255 - b
    root.configure(bg=f"#{r:02x}{g:02x}{b:02x}")

# начальные значения
r = g = b = 255

root = tk.Tk()
root.title("RGB Reverse")
root.geometry("500x500")

# поля ввода
tk.Label(root, text="R:").pack()
entry_r = tk.Entry(root)
entry_r.pack(pady=3)

tk.Label(root, text="G:").pack()
entry_g = tk.Entry(root)
entry_g.pack(pady=3)

tk.Label(root, text="B:").pack()
entry_b = tk.Entry(root)
entry_b.pack(pady=3)

# кнопки
tk.Button(root, text="Show color", command=show_color).pack(pady=5)
tk.Button(root, text="Reverse", command=invert_color).pack()

root.mainloop()

#final
