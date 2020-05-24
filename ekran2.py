from tkinter import *
from tkinter import Tk


import Vending_Machine
import Operations2


automat = Vending_Machine.Machine()  # obiekt = nazwapliku.nazwaklasy()

"""klasa budujaca interfejs."""
class EkranGuziki(Operations2.Operations):

    def __init__(self, master):
        Operations2.Operations.__init__(self, master)


        ops = Operations2.Operations(master)  ##tworze obiekt klasy OPERATIONS
        input_text = ops.input_text1
        Operations2.Operations.get_but_click(ops)

        # WYSWITLACZ
        input_field = Entry(self.master, font=('arial', 18, 'bold'), textvar=input_text, width=40, bg='powder blue',
                            bd=0)
        input_field.place(x=250, y=10, width=227.5, height=85)

        # GUZIKI
        buttons_frame = Frame(self.master, bg="grey")
        buttons_frame.place(x=250, y=100)


        # second row
        seven = Button(buttons_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: ops.but_click(7)).grid(row=1, column=0)
        eight = Button(buttons_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: ops.but_click(8)).grid(row=1, column=1)
        nine = Button(buttons_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: ops.but_click(9)).grid(row=1, column=2)

        # 3rd row
        four = Button(buttons_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: ops.but_click(4)).grid(row=2, column=0)
        five = Button(buttons_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: ops.but_click(5)).grid(row=2, column=1)
        six = Button(buttons_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: ops.but_click(6)).grid(row=2, column=2)

        one = Button(buttons_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: ops.but_click(1)).grid(row=3, column=0)
        two = Button(buttons_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: ops.but_click(2)).grid(row=3, column=1)
        three = Button(buttons_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: ops.but_click(3)).grid(row=3, column=2)
        zero = Button(buttons_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: ops.but_click(0)).grid(row=4, column=1)
        ok = Button(buttons_frame, text="OK", fg="green", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: ops.ok_fun('OK')).grid(row=4, column=2)
        clear = Button(buttons_frame, text="C", fg="green", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                    command=lambda: ops.cancel_fun('C')).grid(row=4, column=0)

        # ----------coins-----------------
        input_coin = ops.input_coinn
        # money screen frame
        money_screen = Entry(ops.master, width=100, bg="white", text=input_coin)
        money_screen.place(x=20, y=50, width=150, height=80)

        # money buttons frame
        money_frame = Frame(ops.master, width=100, bg="grey")
        money_frame.place(x=20, y=200, height=200)

        #STOP button
        stop_button_frame = Frame(ops.master, width=50, bg="red")
        stop_button_frame.place(x=350, y=350, height=50)

        #  GUZIKI
        jeden_gr = Button(money_frame, text="1gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: ops.coin_click(0.01)).grid(row=1, column=0)
        dwa_gr = Button(money_frame, text="2gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: ops.coin_click(0.02)).grid(row=2, column=0)
        piec_gr = Button(money_frame, text="5gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: ops.coin_click(0.05)).grid(row=3, column=0)
        dziesiec_gr = Button(money_frame, text="10gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                             command=lambda: ops.coin_click(0.10)).grid(row=4, column=0)
        dwadziescia_gr = Button(money_frame, text="20gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                                command=lambda: ops.coin_click(0.20)).grid(row=5, column=0)
        piecdziesiat_gr = Button(money_frame, text="50gr", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                                 command=lambda: ops.coin_click(0.50)).grid(row=6, column=0)
        jeden_zl = Button(money_frame, text="1zl", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                          command=lambda: ops.coin_click(1.00)).grid(row=7, column=0)
        dwa_zl = Button(money_frame, text="2zl", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                        command=lambda: ops.coin_click(2.00)).grid(row=8, column=0)
        piec_zl = Button(money_frame, text="5zl", fg="black", width=10, height=1, bd=0, bg="#fff", cursor="hand2",
                         command=lambda: ops.coin_click(5.00)).grid(row=9, column=0)

        stop_button = Button(stop_button_frame, text="STOP", padx=10, pady=50, fg="black", width=10, height=1, bd=0, bg="red", cursor="hand2",
                         command=lambda: ops.stop('STOP')).pack()

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.configure(background="light green")  # zielone tlo
root.title("Automat")
opr = Operations2.Operations(root)
ekran = EkranGuziki(root)

root.mainloop()

# koniec
