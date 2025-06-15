# Logical Equivalence is when two logical expressions mean exactly the same thing.
# Logical Equivalence is tested with the "If And Only If" construct ("↔") and it is
# the same as "==" in programming.

# P -> Q
def implies(p, q) -> bool:
    # An implication can only be false if p is True and Q is False.
    if p: return q

    # If anything but True is returned, then this would no
    # longer acurately represent "imply".
    # Imagine what could be ...
    return True

# Implication Truth Table
assert implies(True, True) == True
assert implies(True, False) == False
assert implies(False, False) == True
assert implies(False, True) == True

# If And Only If: P <-> Q
def if_and_only_if(p, q) -> bool:
    # This is the same thing as writing "p == q". The version below just makes
    # it painfully obvious how it relates to what has been learned so far.
    return implies(p, q) and implies(q, p)

# IFF Truth Table
assert if_and_only_if(True, True) == True
assert if_and_only_if(True, False) == False
assert if_and_only_if(False, True) == False
assert if_and_only_if(False, False) == True
