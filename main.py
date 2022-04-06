from tkinter import *
from calculator import *
import os

def calc():
    calc = Calculator(log_un_ver)
    calc.mainloop()

def success():
    successwindow = Toplevel(main_screen)
    successwindow.title("Success")
    succTxt = Label(successwindow, text="Login Successful")
    succBtn = Button(successwindow, text="Open Calculator", command=calc)

    succTxt.grid(row=0, column=0, ipadx=10, ipady= 10)
    succBtn.grid(row=1, column=0, ipadx=10, ipady= 10)


def login():
    global log_un_ver
    log_un_ver = userEnt.get()
    log_pw_ver = passEnt.get()

    userlist = os.listdir()

    if log_un_ver in userlist:
        file1 = open(log_un_ver, "r")
        pw = file1.read().splitlines()
        if log_pw_ver in pw:
            print("Login Successful")
            success()
        else:
            print("Incorrect Password")
    else:
        print("Incorrect Username")

    userEnt.delete(0, END)
    passEnt.delete(0, END)


def register():
    file = open(regUsername.get(), "w")
    file.write(regPassword.get())
    file.close()

    regUserEnt.delete(0, END)
    regPassEnt.delete(0, END)


def registerscreen():
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")

    global regUsername
    global regPassword
    global regUserEnt
    global regPassEnt

    regUsername = StringVar()
    regPassword = StringVar()

    regUserlab = Label(register_screen, text="Enter Desired Username").grid(row=0, column=0, ipadx=10, ipady=10)
    regUserEnt = Entry(register_screen, textvariable=regUsername)
    regPasslab = Label(register_screen, text="Enter Desired Password").grid(row=1, column=0, ipadx=10, ipady=10)
    regPassEnt = Entry(register_screen, textvariable=regPassword, show="*")
    regButton = Button(register_screen, text="Register", command=register, width=40).grid(row=2, column=0, columnspan=2, ipadx=10, ipady=10)

    regUserEnt.grid(row=0, column=1, ipadx=10, ipady=10)
    regPassEnt.grid(row=1, column=1, ipadx=10, ipady=10)


def main_screen():
    global main_screen
    main_screen = Tk()
    main_screen.title("Account")

    global username
    global password
    global userEnt
    global passEnt

    username = StringVar()
    password = StringVar()

    userlab = Label(main_screen, text="Enter Username").grid(row=0, column=0, ipadx=10, ipady=10)
    userEnt = Entry(main_screen, textvariable = username)
    passlab = Label(main_screen, text="Enter Password").grid(row=1, column=0, ipadx=10, ipady=10)
    passEnt = Entry(main_screen, textvariable = password, show="*")

    userEnt.grid(row=0, column=1, ipadx=10, ipady=10)
    passEnt.grid(row=1, column=1, ipadx=10, ipady=10)

    logbutton = Button(main_screen, text="Login", command=login, width=20).grid(row=2, column=0, ipadx=10, ipady=10)
    regbutton = Button(main_screen, text="Register", command=registerscreen, width=20).grid(row=2, column=1, ipadx=10, ipady=10)

    main_screen.mainloop()


if __name__ == "__main__":
    main_screen()