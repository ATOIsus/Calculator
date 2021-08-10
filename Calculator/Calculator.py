from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

eqn_str = ""


def fun_click(num):
    global eqn_str

    eqn_str = eqn_str + str(num)
    eqn.set(eqn_str)


def fun_equal():
    try:
        global eqn_str
        total = str(eval(eqn_str))
        eqn.set(total)

        eqn_str = ""

    except BaseException as e:
        eqn.set("Error")
        eqn_str = ""
        messagebox.showerror("Error", str(type(e))[6:-1] + " : " + str(e))
        eqn.set("")


def fun_clear():
    global eqn_str
    eqn_str = ""
    eqn.set("")


root = Tk()
root.title("Calculator")
root.maxsize(height=450, width=300)
root.minsize(height=450, width=300)
root.iconbitmap("cal.ico")


try:
    img0 = Image.open("bg.jpg")
    resiz_img0 = img0.resize((300, 450), Image.ANTIALIAS)
    covered_img0 = ImageTk.PhotoImage(resiz_img0)
    lbl0 = Label(root, image=covered_img0, height=450, width=300).place(x=0, y=0)

    img1 = Image.open("ob.jpg")
    resiz_img = img1.resize((250, 400), Image.ANTIALIAS)
    covered_img = ImageTk.PhotoImage(resiz_img)
    lbl1 = Label(root, image=covered_img, height=400, width=250).place(x=22, y=22)

    eqn = StringVar()
    eqn_str_entry = Entry(root, textvariable=eqn, width=30, borderwidth=5, font=("Aerial Black", 24), bg="Black",
                          fg="Crimson").place(x=23, y=22, width=250, height=100)

    btn_1 = Button(root, text=' 1 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(1)).place(x=29, y=129)
    btn_2 = Button(root, text=' 2 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(2)).place(x=79, y=129)
    btn_3 = Button(root, text=' 3 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(3)).place(x=129, y=129)
    btn_4 = Button(root, text=' 4 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(4)).place(x=179, y=129)
    btn_5 = Button(root, text=' 5 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(5)).place(x=225, y=129)

    btn_6 = Button(root, text=' 6 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(6)).place(x=29, y=202)
    btn_7 = Button(root, text=' 7 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(7)).place(x=79, y=202)
    btn_8 = Button(root, text=' 8 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(8)).place(x=129, y=202)
    btn_9 = Button(root, text=' 9 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(9)).place(x=179, y=202)
    btn_0 = Button(root, text=' 0 ', font=("Aerial Black", 14), fg='Crimson', bg='Black', padx=3, pady=14,
                   command=lambda: fun_click(0)).place(x=225, y=202)

    plus = Button(root, text='+', fg='Crimson', bg='Black', font=("Aerial Black", 19), padx=2, pady=8,
                  command=lambda: fun_click("+")).place(x=29, y=275)
    minus = Button(root, text='-', fg='Crimson', bg='Black', font=("Aerial Black", 20), padx=5, pady=5,
                   command=lambda: fun_click("-")).place(x=79, y=275)
    multiply = Button(root, text='*', fg='Crimson', bg='Black', font=("Aerial Black", 20), padx=4, pady=5,
                      command=lambda: fun_click("*")).place(x=129, y=275)
    divide = Button(root, text='/', fg='Crimson', bg='Black', font=("Aerial Black", 20), padx=6, pady=5,
                    command=lambda: fun_click("/")).place(x=179, y=275)
    Decimal = Button(root, text='.', fg='Crimson', bg='Black', font=("Aerial Black", 25), padx=2, pady=0,
                     command=lambda: fun_click(".")).place(x=225, y=275)

    exponent = Button(root, text='**', fg='Crimson', bg='Black', font=("Aerial Black", 18), padx=2, pady=1,
                      command=lambda: fun_click("**")).place(x=29, y=349)
    modulo = Button(root, text='%', fg='Crimson', bg='Black', font=("Aerial Black", 18), padx=1, pady=1,
                    command=lambda: fun_click("%")).place(x=79, y=349)
    clear = Button(root, text='Clr', fg='Crimson', bg='Black', font=("Aerial Black", 16), padx=0, pady=3,
                   command=fun_clear).place(x=129, y=349)
    equal = Button(root, text='=', fg='Crimson', bg='Black', font=("Aerial Black", 14), padx=30, pady=4,
                   command=fun_equal).place(x=179, y=349)


except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))
    root.destroy()


else:
    root.mainloop()
