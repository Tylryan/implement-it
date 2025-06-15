from __future__ import annotations
from common import for_loop, read_to_string


# LAW
#   ¬∀x P(x) ≡ ∃x ¬P(x)
#
# DESCRIPTION
#   DeMorgan's Laws describe what happens when you negate an entire expression
#   I.e. (not expression).
#
#   This law basically says that the following two sentences are logically equivalent:
#   1. Not all/every x are P.
#   2. At least one x is not P.

#   The following two statements are also logically equivalent:
#       - If P is True, return Falseor Q are True, return False: Else, return True.
#       - If P is False and Q is False, return True: Else return False.

exec(read_to_string("../05-existential-quantifier.py"), globals())
exec(read_to_string("../04-universal-quantifier.py"), globals())
exec(read_to_string("../03-logical-equivalence.py"), globals())

# 3. ¬∀x P(x) ≡ ∃x ¬P(x)
# Not all x are P == At least one x is not P.
def law_three(xs: list[bool]):

    def not_every_x_is_P(xs):
        """¬∀x P(x)"""

        try: # try: return ¬∀x P(x) 
            forall(identity, xs)
            # ∀x P(x): After forall.

            return False

        except: # except: return ∃x P(x)
            return True

    # def law_three(x) -> bool:
    #   return ¬∀x, P(x) ∧ ∃x, ¬P(x)


    # ¬(S ∧ Q) ≡ ¬S ∨ ¬Q.
    # ∃x ¬P(x) -> 

    # ¬∀x, P(x) ≡ ∃x ¬P(x)
    # ¬∀x, P(x)
    # ¬S ∨ ¬Q.
    def at_least_one_x_is_not_P(xs) -> bool:

        def __ident(x) -> tuple[object, bool]:
            res, brek = identity(x)
            if res == False:
                return (True, True)
            return (False, False)
        
        # ∃x, P(x)
        res, brek = exists(__ident, xs)
        return res

    # ¬∀x P(x) ≡ ∃x ¬P(x)
    logically_equivalent = not_every_x_is_P(xs) == at_least_one_x_is_not_P(xs)

    return not_every_x_is_P(xs)


if __name__ == "__main__":
    def test_law(xs: list[bool]):
        res = law_three(xs)
        return res

    
    # ¬∀x, P(x) ≡ ∃x ¬P(x)
    # ¬∀x, P(x)
    # ¬S ∨ ¬Q.
    # ------------- Truth Table
    assert test_law([True, True]) == False
    assert test_law([True, False]) == True
    assert test_law([False, True]) == True
    assert test_law([False, False]) == True
