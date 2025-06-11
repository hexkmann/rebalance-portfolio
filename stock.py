import random


class Stock:
    def __init__(self, ticker, price, quantity):
        self.ticker = ticker
        self.price = price
        self.quantity = quantity

    def current_price(self):
        # Actualiza el precio con la última información disponible 
        change = random.uniform(-0.05, 0.05)                # Simula un cambio de +/-5%
        self.price *= (1 + change)

    def investment_value(self):
        # Calcula el valor de inversión de la acción
        return self.price * self.quantity
