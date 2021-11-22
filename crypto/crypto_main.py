from crypto.binance_session import connect_API


class CryptoInfo:

    def __init__(self):
        self.connection = connect_API()

    def get_current_price(self, symbol: str = 'BTCUSDT'):
        """
        Get latest price from any symbol
        :param symbol:
        :return: dict
        """
        def search(s, tickers):
            return [element for element in tickers if element['symbol'] == s]
        return search(symbol, self.connection.get_all_tickers())


if __name__ == '__main__':

    crypto_info = CryptoInfo()
    print("Connecting to binance API")
    if crypto_info.connection:
        print("Connection succesful")

    while True:
        symbol = input("Introduce moneda y te doy el precio actual: ").upper()
        print(crypto_info.get_current_price(symbol))
        if symbol == 'FIN':
            break
