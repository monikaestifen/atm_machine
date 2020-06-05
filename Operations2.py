"""Klasa zawierajaca operacje obslugujace interfejs"""

import copy
import some_exceptions as exceptions
import time
from tkinter import messagebox
from tkinter import StringVar
from tkinter import getdouble
from projekt.Vending_Machine import Machine


class Operations(Machine):
    """Pobieranie wartosci wprowadzanych przez interfejs"""
    flag = True

    def __init__(self, master):

        super().__init__()
        self.__ok_clicked = False
        self.__master = master
        self.input_text1 = StringVar()
        self.input_text1.set(0)
        self.input_coinn = StringVar()
        self.input_coinn.set(0)
        self.__coin = ""
        self.__number = ""
        self.__chosen_no = 0
        self.__price = 0
        self.__exit = False
        self.__input_length = 0
        self.__thrown_exception = False

    def button_click(self, item):
        """
        Jesli produkt jest na stanie, wyprowadza jego cene na ekran,
        lub  jesli wprowadzony zostal bledny numer, wyprowadzi informacji o braku dostepnosci.
        """

        self.__number = self.__number + str(item)
        self.input_text1.set(self.__number)
        self.__input_length = len(self.__number)

        if self.__input_length > 1:
            expression2 = copy.copy(self.__number)
            # info ile do zaplaty

            self.__master.after(1000, lambda: self.input_text1.set(
                "cena:  " + str(Machine().zwroc_cene(int(expression2)))))

            if int(self.__number) < 30 or int(self.__number) > 50:
                time.sleep(1.00)
                self.clear_all()
                raise exceptions.InputError

            self.__chosen_no = copy.deepcopy(self.__number)  # zwrca kopie numeru wybranego
            # sprawdzam czy produkt jest w slowniku

            if not (Machine().update_availability(self.__number)):
                self.input_text1.set("produkt niedostepny")
                self.flag = False
                # clear fun
                self.clear_all()
                raise exceptions.LackOfProduct

            self.__number = ""

    def get_button_click(self) -> object:
        """Zwraca wybrany przez uzytkownika numer produktu"""
        return self.__chosen_no

    def coin_click(self, which_coin):
        """Po wprowadzeniu monety, ile jescze trzeba doplacic aby zakupic produkt."""

        entered_no = int(float(self.get_button_click()))  # dziala jednorazowo
        self.__coin = getdouble(which_coin)
        self.input_coinn.set(self.__coin)  # wyswietla na ekranie wrzucona monete

        if self.__ok_clicked:
            print(self.__ok_clicked)

            if not self.__exit:  # jesli jeszcze nie zakonczyl operacji -> czyli jeszcze brakuje pieniedzy

                if self.__price is 0:
                    self.__price = round(Machine().zwroc_cene(entered_no), 2)

                self.__price = round(self.__price - self.__coin, 2)
                print(self.__price, self.__coin)

                if not self.__thrown_exception:

                    if self.__price > 0:
                        self.input_coinn.set("brakuje : " + str(abs(round(self.__price, 2))))

                    elif self.__price < 0:
                        try:
                            self.clear_coin_window()
                            coin_list = (Machine().make_change(abs(self.__price)))
                            self.input_coinn.set("wydaje reszte: " + str(coin_list))
                            self.__exit = True
                            self.__ok_clicked = False
                            self.__master.after(1000, lambda: self.clear_all())

                        except exceptions.NoMoneyToMakeChange:
                            print("tylko odliczona kwota")
                            self.__thrown_exception = True
                            self.clear_all()

                            messagebox.showerror("Error", "Prosze wprowadzic odliczona kwote.")

                    elif self.__price == 0:
                        time.sleep(1.00)
                        self.input_coinn.set("prosze odebrac pordukt")
                        self.__exit = True
                        self.__ok_clicked = False
                        self.__master.after(1000, lambda: self.clear_all())

                else:
                    if self.__price > 0:
                        self.input_coinn.set("brakuje : " + str(abs(round(self.__price, 2))))
                    elif self.__price == 0:
                        time.sleep(1.00)
                        self.input_coinn.set("prosze odebrac pordukt")
                        self.__exit = True
                        self.__ok_clicked = False
                        self.__master.after(1000, lambda: self.clear_all())
                    elif self.__price < 0:
                        self.__ok_clicked = False
                        self.input_coinn.set("tylko odliczona kwota")
                        self.__master.after(1000, lambda: self.clear_all())
                        raise exceptions.NoMoneyToMakeChange
        else:
            self.input_coinn.set("zatwierdz operacje")

    def clear_coin_window(self):
        """Czysci okno gdzie mamy monety."""
        self.input_coinn.set("")

    def clear_all(self):
        """Czysci okna."""
        self.__number = ""
        self.input_text1.set("")
        self.__price = 0
        self.input_coinn.set("")

    def ok_function(self, item):
        """Funkcja uruchamiana po zatwierdzeniu operacji guzikiem 'OK'. """
        self.__ok_clicked = True

        if item == 'OK':
            if self.__input_length < 2:
                self.clear_all()
                raise exceptions.InputError

            self.__exit = False
            self.__exit2 = True
            time.sleep(1.00)
            self.input_text1.set("wrzuc pieniadze")
            if not self.flag:
                self.input_text1.set("wybierz inny produkt")

    def cancel_function(self, item):
        """Funkcja uruchamiana po nacisnieciu guzika 'C'. """

        if item == 'C':
            self.__number = ""
            self.input_text1.set("")

    def stop(self, item):
        """Funkcja uruchamiana po nacisnieciu guzika 'STOP'."""
        if item == 'STOP':
            self.__number = ""
            self.input_text1.set("")
            self.__price = ""
            self.input_coinn.set("")
