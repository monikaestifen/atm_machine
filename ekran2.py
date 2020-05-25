from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Tk

import Vending_Machine
from Operations2 import Operations

automat = Vending_Machine.Machine()

"""klasa budujaca interfejs."""


class EkranGuziki(Operations):

    def __init__(self, master):
        Operations.__init__(self, master)

        ops = Operations(master)  ##tworze obiekt klasy OPERATIONS
        input_text = ops.input_text1

        # WYSWITLACZ
        input_field = Entry(self.master, font=('arial', 18, 'bold'), textvar=input_text, width=40, bg='powder blue',
                            bd=0)
        input_field.place(x=250, y=50, width=227.5, height=85)

        # GUZIKI
        buttons_frame = Frame(self.master, bg="grey")
        buttons_frame.place(x=250, y=120)

        no_button = 1
        self.buttons = []

        for x in range(3, 0, -1):
            for y in range(3):
                self.buttons.append(Button(buttons_frame, text=str(no_button), fg="red", width=10, height=3, bd=0, bg="#fff",
                                           cursor="hand2", command=lambda no_button=no_button: ops.but_click(no_button)).grid(row=x,
                                                                                                         column=y))
                no_button += 1

        Button(buttons_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: ops.but_click(0)).grid(row=4, column=1)
        Button(buttons_frame, text="OK", fg="green", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: ops.ok_fun('OK')).grid(row=4, column=2)
        Button(buttons_frame, text="C", fg="green", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
               command=lambda: ops.cancel_fun('C')).grid(row=4, column=0)

        # ----------coins-----------------
        input_coin = ops.input_coinn
        # money screen frame
        money_screen = Entry(ops.master, width=100, bg="white", text=input_coin)
        money_screen.place(x=40, y=50, width=150, height=80)

        # money buttons frame
        money_frame = Frame(ops.master, width=100, bg="grey")
        money_frame.place(x=40, y=140, height=200)

        # STOP button
        stop_button_frame = Frame(ops.master, width=50, bg="red")
        stop_button_frame.place(x=350, y=350, height=50)

        #  GUZIKI
        width_button = 10
        height_button = 1
        coin_values_str = ["1gr", "2gr", "5gr", "10gr", "20gr", "50gr", "1zl", "2zl", "5zl"]
        coin_values = {"1gr": 0.01, "2gr": 0.02, "5gr": 0.05, "10gr": 0.1, "20gr": 0.2, "50gr": 0.5,
                       "1zl": 1.0, "2zl": 2.0, "5zl": 5.0}
        for i in range(9):
            for k, v in coin_values.items():
                Button(money_frame, text=coin_values_str[i], fg="black", width=width_button, height=height_button, bd=0, bg="#fff",
                       cursor="hand2",
                       command=lambda v=v: ops.coin_click(v)).grid(row=i, column=0)

        Button(stop_button_frame, text="STOP", padx=10, pady=50, fg="black", width=10, height=1, bd=0,
               bg="red", cursor="hand2", command=lambda: ops.stop('STOP')).pack()


root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.configure(background="light green")  # zielone tlo
root.title("Automat")
opr = Operations(root)
ekran = EkranGuziki(root)
root.mainloop()

# koniec
