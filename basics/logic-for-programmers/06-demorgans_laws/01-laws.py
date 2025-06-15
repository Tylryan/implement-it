from __future__ import annotations
from common import for_loop, read_to_string

S = False or (True and True)
Q = False
P = True

# LAW
#   ¬(S ∧ Q) ≡ ¬S ∨ ¬Q.
#
# DESCRIPTION
#   DeMorgan's Laws describe what happens when you negate an entire expression
#   I.e. (not expression).
#
#   This law basically says that the following two sentences are logically equivalent:
#       1. If both S and Q are True, return False. Else, return True.
#       2. If S is False or Q is False, return True. Else Return False.


exec(read_to_string("../05-existential-quantifier.py"), globals())
exec(read_to_string("../04-universal-quantifier.py"), globals())
exec(read_to_string("../03-logical-equivalence.py"), globals())


def law_one(s, q) -> bool:
    # ¬(S ∧ Q) 
    not_both_s_and_q = not (s and q)
    # ¬S ∨ ¬Q.
    neither_s_nor_q  = (not s) or (not q)

    # ¬(S ∧ Q) ≡ ¬S ∨ ¬Q.
    assert if_and_only_if(not_both_s_and_q, neither_s_nor_q) == True

    return not_both_s_and_q

if __name__ == "__main__":

    # ------------- Truth Table
    # !(True and True)
    # = !(True)
    # = False
    # !True or !True
    # = False or False
    # = False
    assert law_one(s = True , q = True ) == False
    # !(True and False)
    # = !(False)
    # = True
    # !True or !False
    # = False or True
    # = True
    assert law_one(True , False) == True
    assert law_one(False, True ) == True
    assert law_one(False, False) == True
