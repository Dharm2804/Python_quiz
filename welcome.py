import tkinter as tk
from tkinter import messagebox

def start_quiz():
    # Add your quiz logic here
    messagebox.showinfo("Quiz Started", "Quiz has started!")
    root1.destroy()
    import quize

def show_certificate():
    messagebox.showinfo("Certificate", "Congratulations! You've completed the quiz.")

def animate_header():
    # Add your animation logic here
    pass

# Create main window
root1 = tk.Tk()
root1.title("Quiz Application")

# Set window size and position
window_width = 400
window_height = 300
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root1.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Welcome header
welcome_label = tk.Label(root1, text="Welcome to the Quiz", font=("Helvetica", 16), fg="blue")
welcome_label.pack(pady=20)

# Start Quiz button
start_button = tk.Button(root1, text="Start Quiz", command=start_quiz, bg="green", fg="white", padx=20, pady=10)
start_button.pack(pady=10)

# Show Certificate button
certificate_button = tk.Button(root1, text="Show Certificate", command=show_certificate, bg="orange", fg="white", padx=20, pady=10)
certificate_button.pack(pady=10)

# Animate the header (you can customize this according to your needs)
animate_header()

# Run the main loop
root1.mainloop()
