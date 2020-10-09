from tkinter import *
import os


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("sucess")
    screen3.geometry("150x100")
    Label(screen3, text="Login sucess").pack()
    Button(screen3, text="ok", command=delete2).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("sucess")
    screen4.geometry("150x100")
    Label(screen4, text="Password not recognised").pack()
    Button(screen4, text="ok", command=delete3).pack()


def user_not_recognised():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("sucess")
    screen5.geometry("150x100")
    Label(screen5, text="Username not recognised").pack()
    Button(screen5, text="ok", command=delete4).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="registration successful", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()
    else:
        user_not_recognised()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("400x300")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x350")
    screen.title("Notes")
    Label(text="notes", bg="grey", width="300", height="2", font=("Calibri, 13")).pack()
    Label(text="").pack()
    Button(text="Login", foreground='black', width="30", height="2", command=login).pack()
    Label(text="").pack()
    Button(text="Register", fg='#A877BA', width="30", height="2", command=register).pack()

    screen.mainloop()


main_screen()
