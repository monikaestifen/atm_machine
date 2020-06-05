from tkinter import Button
from tkinter import Entry
from tkinter import Frame
from tkinter import Tk
from projekt.Operations2 import Operations


class EkranGuziki():
    """klasa budujaca interfejs."""

    def __init__(self, master):
        self.__master = master
        ops = Operations(self.__master)  ##tworze obiekt klasy OPERATIONS
        self.__buttons = []
        __COLOR_BLACK = "black"
        __COLOR_GREEN = "green"
        __COLOR_WHITE = "#fff"
        __COLOR_GRAY = "gray"
        __COLOR_RED = "red"
        __CURSOR_TYPE = "hand2"
        __no_button = 1
        __WIDTH_BUTTON = 10
        __HEIGHT_BUTTON = 1
        __COIN_VALUES_STR = ["1gr", "2gr", "5gr", "10gr", "20gr", "50gr", "1zl", "2zl", "5zl"]
        __COIN_VALUES = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
        input_text = ops.input_text1

        # WYSWITLACZ
        input_field = Entry(self.__master, font=('arial', 18, 'bold'), textvar=input_text, width=40, bg='powder blue',
                            bd=0)
        input_field.place(x=250, y=50, width=227.5, height=85)

        # GUZIKI
        buttons_frame = Frame(self.__master, bg=__COLOR_GRAY)
        buttons_frame.place(x=250, y=120)

        # guziki na panelu z cyframi do produktow
        for x in range(3, 0, -1):
            for y in range(3):
                self.__buttons.append(
                    Button(buttons_frame, text=str(__no_button), fg=__COLOR_RED, width=10, height=3, bd=0,
                           bg=__COLOR_WHITE, cursor=__CURSOR_TYPE,
                           command=lambda __no_button=__no_button: ops.button_click(__no_button)).grid(row=x, column=y))
                __no_button += 1

        Button(buttons_frame, text="0", fg=__COLOR_BLACK, width=10, height=3, bd=0, bg=__COLOR_WHITE,
               cursor=__CURSOR_TYPE,
               command=lambda: ops.button_click(0)).grid(row=4, column=1)
        Button(buttons_frame, text="OK", fg=__COLOR_GREEN, width=10, height=3, bd=0, bg=__COLOR_WHITE,
               cursor=__CURSOR_TYPE,
               command=lambda: ops.ok_function('OK')).grid(row=4, column=2)
        Button(buttons_frame, text="C", fg=__COLOR_GREEN, width=10, height=3, bd=0, bg=__COLOR_WHITE,
               cursor=__CURSOR_TYPE,
               command=lambda: ops.cancel_function('C')).grid(row=4, column=0)

        # ----------coins-----------------
        input_coin = ops.input_coinn
        # money screen frame
        money_screen = Entry(self.__master, width=100, bg=__COLOR_WHITE, text=input_coin)
        money_screen.place(x=40, y=50, width=200, height=80)

        # money buttons frame
        money_frame = Frame(self.__master, width=100, bg=__COLOR_GRAY)
        money_frame.place(x=40, y=140, height=200)

        # STOP button
        stop_button_frame = Frame(self.__master, width=50, bg=__COLOR_RED)
        stop_button_frame.place(x=320, y=350, height=50)

        #  GUZIKI
        i = 0
        for v in __COIN_VALUES:
            Button(money_frame, text=__COIN_VALUES_STR[i], fg=__COLOR_BLACK, width=__WIDTH_BUTTON, height=__HEIGHT_BUTTON, bd=0,
                   bg=__COLOR_WHITE,
                   cursor=__CURSOR_TYPE,
                   command=lambda v=v: ops.coin_click(v)).grid(row=i, column=0)
            i += 1

        Button(stop_button_frame, text="STOP", padx=10, pady=50, fg=__COLOR_BLACK, width=10, height=1, bd=0,
               bg=__COLOR_RED, cursor=__CURSOR_TYPE, command=lambda: ops.stop('STOP')).pack()


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500")
    root.resizable(0, 0)
    root.configure(background="light green")  # zielone tlo
    root.title("Automat")
    opr = Operations(root)
    ekran = EkranGuziki(root)
    root.mainloop()
