# P -> Q
def implies(p, q) -> bool:
    # Here we can clearly see that P
    if p: return q

    # If anything but True is returned, then this would no
    # longer acurately represent "imply".
    return True

# Implication Truth Table
assert implies(True, True) == True
assert implies(True, False) == False
assert implies(False, False) == True
assert implies(False, True) == True
