"""Plik z wyjatkami"""

from tkinter import messagebox


class InputError(Exception):
    """rzuca wyjatek kiedy input jest < 30 i > 50."""
    def __init__(self):
        messagebox.showerror("Error", "wybierz numier miedzy 30 a 50!")


class LackOfProduct(Exception):
    """rzuca wyjatek kiedy skonczyl sie dany produkt"""
    def __init__(self):
        messagebox.showerror("Error", "skonczyl sie produkt!")


class NoMoneyToMakeChange(Exception):
    """rzuca wyjatek kiedy nie moze wydac resty"""
    pass
