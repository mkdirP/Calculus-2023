from sympy import *
import typing
from typing import Callable

x = Symbol('x')
y = Symbol('y')
available_systems = [
    tuple([  # x_0 = 0.5, y_0 = -1
        sin(2*x - y) - 1.2*x - 0.4,
        x**2 + y**2 - 1
    ]),
    tuple([  # x_0 = 0.5, y_0 = 0.2
        y - 0.5 * x**2 + x - 0.7,
        2 * x + y - 1/6 * y**3 - 1.6
    ])
]
