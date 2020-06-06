"""tworzenie testow funkcji"""

import unittest
from math import fabs
from tkinter import Tk
from Operations2 import Operations
from Vending_Machine import Machine
from Vending_Machine import check_if_number_exists
import some_exceptions as exceptions


class MyTestCase(unittest.TestCase):
    """klasa tworzaca testy, zgodnie z wytycznymi"""

    def test_get_price(self):
        """1. Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie."""
        self.assertEqual(Machine().zwroc_cene(32), 3.00)

    def test_make_no_change(self):
        """2. Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty."""

        test_machine = Operations(Tk())
        test_machine.button_click(36)
        test_machine.ok_function(36)
        test_machine.coin_click(1.0)
        test_machine.coin_click(1.0)
        test_machine.coin_click(0.6)

        change = Machine().make_change(fabs(test_machine.get_current_amount_test()))
        self.assertEqual(change, [])

    def test_make_change(self):
        """3. Wrzucenie większej kwoty, zakup towaru - oczekiwana reszta."""

        test_machine2 = Operations(Tk())
        test_machine2.button_click(36)
        test_machine2.ok_function(36)
        test_machine2.coin_click(1.0)
        test_machine2.coin_click(1.0)
        test_machine2.coin_click(5.0)
        change = Machine().make_change(fabs(test_machine2.get_current_amount_test()))
        # cena zwrocona w monetach powinna wygladac --> [0.2, 0.2, 2.0, 2.0]
        self.assertEqual(change, [0.2, 0.2, 2.0, 2.0])

    def test_availability(self):
        """4. Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru -
        oczekiwana informacja o braku."""

        test_machine = Machine()
        test_machine.update_availability(30)
        test_machine.update_availability(30)
        test_machine.update_availability(30)
        test_machine.update_availability(30)
        test_machine.update_availability(30)
        state = test_machine.update_availability(30)

        self.assertEqual(state, False)

    def test_check_number_correct(self):
        """5. Sprawdzenie ceny towaru o nieprawidłowym numerze (<30 lub >50) -
        oczekiwana informacja o błędzie"""

        with self.assertRaises(exceptions.InputError):
            check_if_number_exists(25)

    def test_stop_click(self):
        """6. Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet."""
        test_machine2 = Operations(Tk())
        test_machine2.button_click(49)
        test_machine2.coin_click(1.0)
        test_machine2.coin_click(1.0)
        test_machine2.coin_click(2.0)

        self.assertEqual(test_machine2.stop('STOP'), [1.0, 1.0, 2.0])

    def test_buy_product_with_1gr(self):
        """8. Zakup towaru płacąc po 1 gr - suma stu monet ma być równa 1zł (dla floatów
        suma sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0). Płatności można dokonać
        za pomocą pętli for w interpreterze."""

        test_machine2 = Operations(Tk())
        test_machine2.button_click(50)
        test_machine2.ok_function(50)
        for i in range(100):
            test_machine2.coin_click(0.01)
        # resta powinna byc rowna 0:
        change = Machine().make_change(fabs(test_machine2.get_current_amount_test()))
        self.assertEqual(change, [])


if __name__ == '__main__':
    unittest.main()
