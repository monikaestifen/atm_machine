"""Klasa zawierajaca operacje obslugujace interfejs"""

import copy
import time
from tkinter import FALSE
from tkinter import getdouble
from tkinter import StringVar
from Vending_Machine import Machine

class Operations(Machine):
    """Pobieranie wartosci wprowadzanych przez interfejs"""
    flag = 0

    def __init__(self, master):

        super(Operations, self).__init__()
        self.ok_clicked = False
        self.master = master
        self.input1 = 0
        self.input2 = 0
        self.input_text1 = StringVar()
        self.input_text1.set(self.input1)
        self.input_coinn = StringVar()
        self.input_coinn.set(self.input2)
        chosen_noo = 0
        self.coin = ""
        self.number = ""
        self.chosen_no = chosen_noo
        self.price = 0
        self.price1 = 0
        self.exit = False

    def but_click(self, item):
        """
        Jesli produkt jest na stanie, wyprowadza jego cene na ekran,
        lub  jesli wprowadzony zostal bledny numer, wyprowadzi informacji o braku dostepnosci.
        """

        self.number = self.number + str(item)
        self.input_text1.set(self.number)

        if len(self.number) > 1:
            expression2 = copy.copy(self.number)
            # info ile do zaplaty

            self.master.after(1000, lambda: self.input_text1.set(
                "cena:  " + str(Machine().zwroc_cene(int(expression2)))))

            if int(self.number) < 30 or int(self.number) > 50:
                time.sleep(1.00)
                self.input_text1.set("wybierz nr od 30 do 50!")

            self.chosen_no = copy.deepcopy(self.number)  # zwrca kopie numeru wybranego
            # sprawdzam czy produkt jest w slowniku

            if (Machine().update_availability(self.number)) == FALSE:
                self.input_text1.set("produkt niedostepny")
                self.flag = 1
                # clear fun
                self.clear_all()

            self.number = ""

    def get_but_click(self) -> object:
        """Zwraca wybrany przez uzytkownika numer produktu"""
        return self.chosen_no

    def coin_click(self, which_coin):
        """Po wprowadzeniu monety, ile jescze trzeba doplacic aby zakupic produkt."""

        if self.ok_clicked:

            if not self.exit:

                self.coin = getdouble(which_coin)
                self.input_coinn.set(self.coin)  # wyswietla na ekranie wrzycona monete

                entered_no = int(float(self.get_but_click()))  # dziala jednorazowo
                self.price = round(self.price, 2)

                if not self.price:

                    self.price = Machine().zwroc_cene(entered_no)
                    self.price = self.price - self.coin

                    if self.price > 0:
                        self.input_coinn.set("brakuje : " + str(abs(round(self.price, 2))))

                    elif self.price < 0:
                        self.clear_coin_window()
                        coin_list = (Machine().make_change(abs(self.price)))
                        self.input_coinn.set("wydaje reszte: " + str(coin_list))
                        self.exit = True
                        self.ok_clicked = False
                        self.master.after(5000, lambda: self.clear_all())

                    else:
                        time.sleep(1.00)
                        self.input_coinn.set("prosze odebrac pordukt")
                        self.exit = True
                        self.ok_clicked = False
                        self.master.after(5000, lambda: self.clear_all())

                else:
                    self.price = self.price - self.coin
                    self.input_coinn.set("")
                    if self.price > 0:
                        self.input_coinn.set("brakuje : " + str(abs(round(self.price, 2))))

                    elif self.price < 0:
                        self.clear_coin_window()
                        coin_list = (Machine().make_change(abs(self.price)))
                        self.input_coinn.set("wydaje reszte : " + str(coin_list))
                        self.exit = True
                        self.ok_clicked = False
                        self.master.after(5000, lambda: self.clear_all())

                    else:
                        time.sleep(1.00)
                        self.input_coinn.set("prosze odebrac pordukt")
                        self.exit = True
                        self.ok_clicked = False
                        self.master.after(5000, lambda: self.clear_all())


        else:
            self.input_coinn.set("zatwierdz operacje")

    def clear_coin_window(self):
        """Czysci okno gdzie mamy monety."""
        self.input_coinn.set("")

    def clear_all(self):
        """Czysci okna."""
        self.number = ""
        self.input_text1.set("")
        self.price = 0
        self.input_coinn.set("")

    def ok_fun(self, item):
        """Funkcja uruchamiana po zatwierdzeniu operacji guzikiem 'OK'. """
        if item == 'OK':
            self.ok_clicked = True
            self.exit = False
            time.sleep(1.00)
            self.input_text1.set("wrzuc pieniadze")
            if self.flag == 1:
                self.input_text1.set("wybierz inny produkt")

    def cancel_fun(self, item):
        """Funkcja uruchamiana po nacisnieciu guzika 'C'. """

        if item == 'C':
            self.number = ""
            self.input_text1.set("")

    def stop(self, item):
        """Funkcja uruchamiana po nacisnieciu guzika 'STOP'."""
        if item == 'STOP':
            self.number = ""
            self.input_text1.set("")
            self.price = ""
            self.input_coinn.set("")