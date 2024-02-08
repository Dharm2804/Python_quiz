from tkinter import *
import tkinter as tk

def animate_text(sentence, index=0):
    if index < len(sentence):
        label.config(text=sentence[:index+1])
        root.after(100, animate_text, sentence, index+1)
    else:
        root.after(1000, show_login_page)

def show_login_page():
    root.destroy()
    import sign

root = tk.Tk()
root.title("Dynamic Sentence Animation")
root.geometry("320x200")
root.configure(bg="black")

window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Disable window resizing
root.resizable(False, False)

sentence = "Welcome to My Login Page....."
label = tk.Label(root, font=("Helvetica", 16, 'bold'), bg='black', fg='white')
label.pack(pady=(root.winfo_reqheight() - label.winfo_reqheight()) // 2)

# Start the animation
animate_text(sentence)

root.mainloop()
