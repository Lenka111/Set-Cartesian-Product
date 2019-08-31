# Elena Voinu
# The Cartesian product of A and B  is the set of all possible ordered pairs
# whose first component comes from A and whose second component comes from B.

import itertools

A = {0, 1, 2}
B = {'a', 'b'}

cart_prod = itertools.product(A, B)

for p in cart_prod:
    print(p)
    



