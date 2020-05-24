n = 5
coinsCount = [n] * 8

"""Klasa zawiera funkcje aktualizujace stan produktow w maszynie"""
class Machine:
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
        self.coinsUsed = [0] * (self.change + 1)

    def product(self):
        for item in self.dic:
            cena = item['price']
            print(cena)

    """funkcja zwracajaca cene nacisnietego produktu z dict."""
    def zwroc_cene(self, number):
        for item in self.dic:
            no = item['code']
            self.price = item['price']
            if no == float(number):
                print(str(self.price))
                print(type(self.price))
                return float(self.price)

    def get_price(self):
        return int(self.price)

    """po wybraniu produktu aktualizujemy stan produktow."""
    def update_availability(self, number):
        for item in self.dic:
            no = item['code']
            quantity = item['quantity']
            if no == float(number):
                if quantity != 0:
                    print("produkt dostepny")
                    item['quantity'] = quantity - 1
                    return True
                else:
                    print("produkt niedostepny")
                    return False


    """Funkcja obliczajaca wydana reszte."""
    def dpMakeChange(self, change):
        global n
        global coinsCount

        coinValueList = [1, 2, 5, 10, 20, 50, 100, 200, 500]
        change = change * 100
        change = int(change)
        coinsUsed = [0] * (change + 1)
        minCoins = [0] * (change + 1)

        for cents in range(change + 1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents - j] + 1 < coinCount:
                    coinCount = minCoins[cents - j] + 1
                    newCoin = j
            minCoins[cents] = coinCount
            coinsUsed[cents] = newCoin

        coin = change
        coinList = []
        while coin > 0:
            thisCoin = coinsUsed[coin]
            index = coinValueList.index(thisCoin)
            if coinsCount[index] > 0:
                coinList.append(thisCoin / 100)
                coin = coin - thisCoin
                coinsCount[index] = coinsCount[index] - 1
            else:
                print("prosze wrzucic odliczona kwote")
                break
        #print("change", change)
        return coinList

