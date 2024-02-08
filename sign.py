from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pymysql

def login_user():
    if username.get() == '' or password.get() == '':
        messagebox.showerror("Empty Field", "Please enter both E-mail and password")
    else:
        try:
            con = pymysql.connect(host="localhost", user='root', password='2845', database='userdata')
            mycursor = con.cursor()

            query = 'select * from data where email=%s and password=%s'
            mycursor.execute(query, (username.get(), password.get()))
            row = mycursor.fetchone()

            if row is None:
                messagebox.showwarning('Warning', 'Username/Password is incorrect')
            else:
                get_email()
                get_username(username.get())
                login_window.destroy()
                messagebox.showinfo("Welcome", 'Login is Successful')
                import quize

        except Exception as e:
            messagebox.showerror('Error', f'Database Connectivity Issue: {str(e)}')

def get_email():
    email = username.get()
    with open("email.txt", "w") as file:
        file.write(email)

def get_username(email):
    try:
        con = pymysql.connect(host="localhost", user='root', password='2845', database='userdata')
        mycursor = con.cursor()

        query = 'SELECT username FROM data WHERE email=%s'
        mycursor.execute(query, (email,))
        row = mycursor.fetchone()

        if row:
            username = row[0]
            with open("username.txt", "w") as file:
                file.write(username)
                print(f"Username '{username}' written to username.txt")
        else:
            print("No username found for the given email.")

    except pymysql.Error as e:
        print(f"Error: {e}")

    finally:
        if con:
            con.close()
def user_entry(event):
    if username.get() == "E-mail":
        username.delete(0, END)

def password_entry(event):
    if password.get() == "Password":
        password.delete(0, END)

def hide():
    opens.config(file="closeye.png")
    password.config(show="*")
    eyebt.config(command=show)

def show():
    opens.config(file="openeye.png")
    password.config(show="")
    eyebt.config(command=hide)

def create():
    import signup

def forg():
    import forgot

login_window = Tk()
login_window.title("Login Page")
login_window.configure(bg="black")  # Set background color to black
# Set window size and center it on the screen
window_width = 300
window_height = 500
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Disable window resizing
login_window.resizable(False, False)

# All other widgets are placed on the right side using the grid manager
frame_right = Frame(login_window, bg="black")
frame_right.pack(side=RIGHT, padx=20, pady=10)

heading = Label(frame_right, text="USER LOGIN", font=('Microsoft Yaei UI Light', '23', 'bold'), bg="black", fg="white")
heading.grid(row=0, column=0, columnspan=2, pady=(10, 10))

username = Entry(frame_right, font=('Microsoft Yaei UI Light', 11), width=25, bd=0, fg="firebrick1", bg="black", insertbackground="white")
username.grid(row=1, column=0, columnspan=2, pady=(20, 10))
username.insert(0, "E-mail")
username.bind('<FocusIn>', user_entry)

Frame(frame_right, width=250, height=2, bg="firebrick1").grid(row=2, column=0, columnspan=2)

password = Entry(frame_right, font=('Microsoft Yaei UI Light', 11), width=25, bd=0, fg="firebrick1", bg="black", insertbackground="white", show="*")
password.grid(row=3, column=0, columnspan=2, pady=5)
password.insert(0, "Password")
password.bind('<FocusIn>', password_entry)

Frame(frame_right, width=250, height=2, bg="firebrick1").grid(row=4, column=0, columnspan=2)

opens = PhotoImage(file='openeye.png')
eyebt = Button(frame_right, image=opens, bd=0, bg='black', activebackground='black', cursor="hand2", command=hide)
eyebt.grid(row=3, column=1, pady=5)

fog = Button(frame_right, bd=0, text='Forgot Password? ', activebackground='black', cursor="hand2",
              font=('Microsoft Yaei UI Light', '9', 'bold'), bg="black", fg="firebrick1", command=forg)
fog.grid(row=6, column=0, columnspan=2, pady=5)

logbt = Button(frame_right, text='Login', font=('Open Sans', 16, 'bold'), fg='white', bg='firebrick1',
               activebackground='firebrick1', cursor='hand2', bd=0, width=19, command=login_user)
logbt.grid(row=7, column=0, columnspan=2, pady=(20, 5))

orlb = Label(frame_right, text="------------- OR -------------", font=('Open Sans', 16), fg='firebrick1', bg='black')
orlb.grid(row=8, column=0, columnspan=2, pady=(20, 5))

sinuplb = Label(frame_right, text="Don't have an account? ", font=('Open Sans', 9, 'bold'), fg='firebrick1',
                bg='black')
sinuplb.grid(row=10, column=0, columnspan=2, pady=(20, 0))

newbt = Button(frame_right, text='Create new one ', font=('Open Sans', 9, 'bold underline'), fg='blue',
               activebackground='black', cursor='hand2', bd=0, bg='black', command=create)
newbt.grid(row=11, column=0, columnspan=2, pady=(0, 20))

login_window.mainloop()
