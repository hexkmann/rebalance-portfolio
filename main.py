from src import Stock, Portfolio
import random

def main():
    # Genera valores aleatorios para las condiciones iniciales META y AAPL
    meta_stock = Stock('META', price=random.uniform(250, 350), quantity=random.randint(5, 20))
    aapl_stock = Stock('AAPL', price=random.uniform(100, 200), quantity=random.randint(5, 20))
    aim = {'META': 0.4, 'AAPL': 0.6}                            # Define la distribución objetivo
    
    # Ejecuta la simulación
    portfolio = Portfolio([meta_stock, aapl_stock], aim)        # Crea el portafolio
    portfolio.update()                                          # Actualiza precios
    portfolio.rebalance()                                       # Realiza el rebalanceo


if __name__ == "__main__":
    main()
    input('Presiona Enter para finalizar')
