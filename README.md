# Rebalance Portfolio

Este proyecto implementa un sistema simple para gestionar y rebalancear una cartera de acciones en Python. (Fue creado por un usuario nuevo en lo que es uso de github, intentar ser comprensivos)
El uso de LLM se encuentra registrado en chatgpt.txt

## Descripción

- La clase `Stock` almacena información de cada acción (ticker, precio, cantidad).
- La clase `Portfolio` maneja múltiples acciones y permite actualizar precios y rebalancear la cartera según una distribución objetivo.

## Estructura
rebalance-portfolio/
├── src/
│   ├── __init__.py
│   ├── stock.py
│   └── portfolio.py
├── notebook/
│   └── rebalance_demo.ipynb
├── main.py
├── chatgpt.txt
└── README.md


## Uso

1. Clona el repositorio.
2. Ejecuta el ejemplo para ver cómo crear una cartera y rebalancearla:

```bash
python rebalance_example.py
