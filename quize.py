import tkinter as tk
from tkinter import messagebox
import requests
import html
import random
import smtplib
import certificate as ac
import openpyxl
from openpyxl.drawing.image import Image
def get_question():
    if questions_asked >= max_questions:
        show_final_score()
        return

    # Fetch a random question from the Open Trivia Database API
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = response.json()

    if data["response_code"] == 0:
        question_data = data["results"][0]
        display_question(question_data)
    else:
        messagebox.showerror("Error", "Failed to fetch question")

def display_question(question_data):
    global score
    global questions_asked

    # Extract question and choices from the API response
    question = html.unescape(question_data["question"])
    choices = [html.unescape(choice) for choice in question_data["incorrect_answers"]]
    correct_choice = html.unescape(question_data["correct_answer"])

    # Shuffle the choices and insert the correct choice at a random position
    choices.insert(random.randint(0, len(choices)), correct_choice)

    # Update the GUI
    question_label.config(text=question)
    score_label.config(text=f"Score: {score}")
    create_choice_buttons(choices, correct_choice)

def create_choice_buttons(choices, correct_choice):
    # Clear previous choice buttons
    for widget in choices_frame.winfo_children():
        widget.destroy()

    # Create new choice buttons
    for choice in choices:
        button = tk.Button(choices_frame, text=choice, command=lambda c=choice: check_answer(c, correct_choice), font=("Helvetica", 12), bg="#2196F3", fg="white")
        button.pack(side="left", padx=10)

def check_answer(selected_choice, correct_choice):
    global score
    global questions_asked

    questions_asked += 1

    if selected_choice == correct_choice:
        score += 1
        messagebox.showinfo("Correct", "Correct answer!")
    else:
        messagebox.showerror("Incorrect", f"Wrong answer! The correct answer is: {correct_choice}")

    # Get the next question
    get_question()

def show_final_score():
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    with open("username.txt", "r") as file:
                usernames1 = file.read()
# Load your photo
    
    messagebox.showinfo("Quiz Completed", f"You have completed the quiz!\nYour final score is: {score}")
    send_ml()
    


def send_ml():
    with open("username.txt", "r") as file:
                usernames = file.read()
    mark=(score * 100)/max_questions  
    messagebox.showinfo("Completed", f"check your mail")
    ac.generate_certificate_and_send_email(usernames, mark)
    


root = tk.Tk()
root.title("Random Quiz App")
root.configure(bg="#e6e6e6")  # Background color

question_label = tk.Label(root, text="", wraplength=400, justify="center", font=("Helvetica", 14, "bold"), bg="#e6e6e6")
question_label.pack(pady=10)

choices_frame = tk.Frame(root, bg="#e6e6e6")
choices_frame.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12), bg="#e6e6e6")
score_label.pack(pady=10)

next_question_button = tk.Button(root, text="Next Question", command=get_question, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
next_question_button.pack(pady=10)

score = 0
questions_asked = 0
max_questions = 10
get_question()

# Center the window on the screen
root.geometry("600x400+400+200")

root.mainloop()
