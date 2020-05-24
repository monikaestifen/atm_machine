import time
from tkinter import *
import copy
import Vending_Machine

"""Klasa zawierajaca operacje operacje obslugujace interfejs"""
class Operations(Vending_Machine.Machine):

    flag = 0

    def __init__(self, master):
        super(Vending_Machine.Machine).__init__()
        self.master = master
        self.input1 = 0
        self.input2 = 0
        self.input_text1 = StringVar()
        self.input_text1.set(self.input1)
        self.input_coinn = StringVar()
        self.input_coinn.set(self.input2)
        coinn = ''
        numberr = ''
        chosen_noo = 0
        self.coin = coinn
        self.number = numberr
        self.chosen_no = chosen_noo
        self.price = 0
        self.price1 = 0

    """Funkcja obslugujaca wprowadzanie numerow produktow."""
    """Jesli produkt jest na stanie, wyprowadza jego cene na ekran, lub  jesli wprowadzony zostal bledny numer, wyprowadzi informacji o braku dostepnosci."""
    def but_click(self, item):
        self.number = self.number + str(item)
        self.input_text1.set(self.number)

        if len(self.number) > 1:
            expression2 = copy.copy(self.number)
            self.input_text1.set(
                "cena:  " + str(Vending_Machine.Machine().zwroc_cene(int(expression2))))  # info ile do zaplaty

            if int(self.number) < 30 or int(self.number) > 50:
                time.sleep(1.00)
                self.input_text1.set("wybierz nr od 30 do 50!")
                # self.input_text1.set('')
            self.chosen_no = copy.deepcopy(self.number)  # zwrca kopie numeru wybranego
            ##sprawdzam czy produkt jest w slowniku

            if (Vending_Machine.Machine().update_availability(self.number)) == FALSE:
                self.input_text1.set("produkt niedostepny")
                self.flag = 1
                # clear fun
                self.clear_all()

            self.number = ""


    def get_but_click(self) -> object:  # wiemy jaki nr został wpisany
        return self.chosen_no

    """Funkcja wyswietla informacje po wprowadzeniu monety, ile jescze trzeba doplacic aby zakupic produkt."""
    def coin_click(self, which_coin):
        self.coin = getdouble(which_coin)
        self.input_coinn.set(self.coin)  # wyswietla na ekranie wrzycona monete

        entered_no = int(float(self.get_but_click()))  # dziala jednorazowo
        self.price = round(self.price, 2)
        ##
        if not self.price:
            self.price = Vending_Machine.Machine().zwroc_cene(entered_no)
            self.price = self.price - self.coin

            if self.price > 0:
                self.input_coinn.set("brakuje : " + str(abs(round(self.price,2))))

            elif self.price < 0:
                self.clear_coin_window()
                listC = (Vending_Machine.Machine().dpMakeChange(abs(self.price)))
                self.input_coinn.set("wydaje reszte: " + str(listC))
                time.sleep(4.00)

            else:
                time.sleep(1.00)
                self.input_coinn.set("prosze odebrac pordukt")

        else:
            self.price = self.price - self.coin
            self.input_coinn.set("")
            if self.price > 0:
                self.input_coinn.set("brakuje : " + str(abs(round(self.price,2))))

            elif self.price < 0:
                self.clear_coin_window()
                listC = (Vending_Machine.Machine().dpMakeChange(abs(self.price)))
                self.input_coinn.set("wydaje reszte : " + str(listC))

            else:
                time.sleep(1.00)
                self.input_coinn.set("prosze odebrac pordukt")

    def clear_coin_window(self):
        self.input_coinn.set("")

    def clear_all(self):
        time.sleep(2.00)
        self.number = ""
        self.input_text1.set("")
        self.price = ""
        self.input_coinn.set("")

    def ok_fun(self, item):
        if item == 'OK':
            time.sleep(1.00)
            self.input_text1.set("wrzuc pieniadze")
            if self.flag == 1:
                self.input_text1.set("wybierz inny produkt")

    """Funkcja uruchamiana po nacisnieciu guzika 'C'. """
    def cancel_fun(self, item):
        if item == 'C':
            self.number = ""
            self.input_text1.set("")

    """Funkcja uruchamiana po nacisnieciu guzika 'STOP'."""
    def stop(self, item):
        if item == 'STOP':
            self.number = ""
            self.input_text1.set("")
            self.price = ""
            self.input_coinn.set("")

