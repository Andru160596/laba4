# -*- coding: utf-8 -*-
"""
Created on Wed May 17 18:23:42 2017

@author: annan
"""

import sympy

def solve(*equalities):
    if len(equalities) == 1:
        return sympy.solve(equalities[0])
    return sympy.solve_poly_system(equalities)

x = sympy.Symbol("x")
print('\nПроизводная: ')
#expr = x ** 2 + sympy.log(x)
expr = x ** 2 * sympy.sin(1)
sympy.pprint(expr)
sympy.plot(expr)
print('\nПроизводная: ')
diff = sympy.diff(expr)
sympy.pprint(diff)
sympy.plot(diff)
print('\nПервообразная: ')
integr = sympy.integrate(expr)
sympy.pprint(integr)
sympy.plot(integr)


y = sympy.Symbol("y")
eq1 = sympy.Equality(3 , x ** 2 - x * y)

eq2 = sympy.Equality(-2, y ** 2 - x * y)

eq3 = sympy.Equality(x**2, -2)

sympy.pprint(solve(eq1, eq2))
sympy.pprint(solve(eq3))