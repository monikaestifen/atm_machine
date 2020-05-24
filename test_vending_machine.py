import unittest
from Vending_Machine import Machine


class MyTestCase(unittest.TestCase):

    def test_get_price(self):
        print("test funkcja zwroc_cene()")
        self.assertEqual(Machine().zwroc_cene(32), 3.00)

    def test_update_availability(self):
        print("test update_availability()")
        self.assertEqual(Machine().update_availability(32), True)

    def make_change_test(self):
        print("test making change()")
        self.expectedChange = [2, 1, 0.5]
        self.expectedChange2 = [2, 1, 0.5]

        self.assertListEqual(Machine().dpMakeChange(3.5), self.expectedChange)

if __name__ == '__main__':
    unittest.main()
