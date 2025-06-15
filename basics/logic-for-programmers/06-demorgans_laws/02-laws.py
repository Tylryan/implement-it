from __future__ import annotations
from common import for_loop, read_to_string


# LAW
#   ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
#
# DESCRIPTION
#   DeMorgan's Laws describe what happens when you negate an entire expression
#   I.e. (not expression).
#
#   This law basically says that the following two sentences are logically equivalent:
#   1. Not a single element is a P.
#   2. Every element is not a P.

#   The following two statements are also logically equivalent:
#       - If P or Q are True, return False: Else, return True.
#       - If P is False and Q is False, return True: Else return False.

exec(read_to_string("../05-existential-quantifier.py"), globals())
exec(read_to_string("../04-universal-quantifier.py"), globals())
exec(read_to_string("../03-logical-equivalence.py"), globals())

#   The statements "If P or Q are True, return False: Else return True" and
#   "If P is False and Q is False, return True: Else return False." are logically
#   equivalent as shown by the tests.
def law_two(s, q):
    not_s_or_q      =  not (s or q)       # ¬(P ∨ Q)
    not_s_and_not_q = (not s) and (not q) # ¬P ∧ ¬Q

    # ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
    logically_equivalent = not_s_or_q == not_s_and_not_q
    assert logically_equivalent

    return not_s_or_q

if __name__ == "__main__":
    # P, Q
    def test_law(s, q):
        res = law_two(s, q)
        print(f"not( {s} or {q} ) = ", res)

    test_law(True, True)
    test_law(True, False)
    # not(False or True)
    # not(True)
    # False
    test_law(False, True)
    # not(False or False)
    # not(False)
    # True
    test_law(False, False)
