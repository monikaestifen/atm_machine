"""Klasa zawiera funkcje aktualizujace stan produktow w maszynie"""

N = 5
COINS_COUNT = [N] * 8


class Machine:
    """Klasa zawiera informacje dot. produktow. """
    dic = [
        {"code": 30, "price": 2.00, "quantity": 5},
        {"code": 31, "price": 2.50, "quantity": 5},
        {"code": 32, "price": 3.00, "quantity": 3},
        {"code": 33, "price": 4.50, "quantity": 5},
        {"code": 34, "price": 2.20, "quantity": 5},
        {"code": 35, "price": 2.40, "quantity": 5},
        {"code": 36, "price": 2.60, "quantity": 3},
        {"code": 37, "price": 2.70, "quantity": 5},
        {"code": 38, "price": 2.80, "quantity": 5},
        {"code": 39, "price": 2.90, "quantity": 5},
        {"code": 40, "price": 3.10, "quantity": 5},
        {"code": 41, "price": 3.20, "quantity": 5},
        {"code": 42, "price": 3.30, "quantity": 5},
        {"code": 43, "price": 5.00, "quantity": 5},
        {"code": 44, "price": 5.50, "quantity": 5},
        {"code": 45, "price": 2.50, "quantity": 5},
        {"code": 46, "price": 4.60, "quantity": 5},
        {"code": 47, "price": 4.25, "quantity": 5},
        {"code": 48, "price": 3.05, "quantity": 5},
        {"code": 49, "price": 6.10, "quantity": 5},
        {"code": 50, "price": 4.40, "quantity": 5}
    ]

    def __init__(self):
        self.price = 0
        self.change = 0
        self.coins_used = [0] * (self.change + 1)

    def zwroc_cene(self, number):
        """funkcja zwracajaca cene nacisnietego produktu z dict."""
        return_price = 0
        for item in self.dic:
            code_no = item['code']
            self.price = item['price']
            if code_no == float(number):
                print(str(self.price))
                print(type(self.price))
                return_price = float(self.price)

        return return_price

    def get_price(self):
        return int(self.price)

    def update_availability(self, number):
        """po wybraniu produktu aktualizujemy stan produktow."""
        state = False
        for item in self.dic:
            code_no = item['code']
            quantity = item['quantity']
            if code_no == float(number):
                if quantity != 0:
                    item['quantity'] = quantity - 1
                    state = True
                else:
                    state = False
        return state

    def make_change(self, change):
        """Funkcja obliczajaca wydana reszte."""
        global N
        global COINS_COUNT

        coin_value_list = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        change = change * 100
        change = int(change)
        coins_used = [0] * (change + 1)
        min_coins = [0] * (change + 1)

        for cents in range(change + 1):
            coin_count = cents
            new_coin = 1
            for j in [c for c in coin_value_list if c <= cents]:
                if min_coins[cents - j] + 1 < coin_count:
                    coin_count = min_coins[cents - j] + 1
                    new_coin = j
            min_coins[cents] = coin_count
            coins_used[cents] = new_coin

        coin = change
        coin_list = []
        while coin > 0:
            this_coin = coins_used[coin]
            index = coin_value_list.index(this_coin)
            if COINS_COUNT[index] > 0:
                coin_list.append(this_coin / 100)
                coin = coin - this_coin
                COINS_COUNT[index] = COINS_COUNT[index] - 1
            else:
                print("prosze wrzucic odliczona kwote")
                break
        return coin_list
