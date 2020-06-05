from tkinter import messagebox


class InputError(Exception):
    def __init__(self):
        messagebox.showerror("Error", "wybierz numier miedzy 30 a 50!")


class LackOfProduct(Exception):
    def __init__(self):
        messagebox.showerror("Error", "skonczyl sie produkt!")


class NoMoneyToMakeChange(Exception):
    # def __init__(self):
    #     messagebox.showerror("Error", "Prosze wprowadzic odliczona kwote.")
    pass

