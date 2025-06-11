class Portfolio:
    def __init__(self, stocks, allocation):
        self.stocks = {stock.ticker: stock for stock in stocks}
        self.allocation = allocation

    def update(self):
        # Actualiza el precio para cada acción de la cartera
        for stock in self.stocks.values():
            stock.current_price()

    def total_investment_value(self):
        # Calcula el valor total de la inversión de la cartera
        return sum(stock.investment_value() for stock in self.stocks.values())

    def rebalance(self):
        # Rebalancea la cartera, comprando y vendiendo acciones para alcanzar la distribución asignada
        total_value = self.total_investment_value()
        print(f"\nTotal Portfolio Value: {total_value:.2f}\n")

        for ticker, stock in self.stocks.items():
            current_value = stock.investment_value()
            target_value = self.allocation[ticker] * total_value
            shares_to_trade = target_value - current_value / stock.price

            action = "buy" if shares_to_trade > 0 else "sell"
            print(f"{ticker}: Current = ${current_value:.2f}, Target = ${target_value:.2f}")
            print(f" -> {action} {abs(shares_to_trade):.2f} shares\n")
