from __future__ import annotations
from common import for_loop, read_to_string

# TODO(tyler): Eventually stop relying on these
S = False or (True and True)
Q = False
P = True

# DeMorgan's Laws describe what happens when you negate an entire expression
# I.e. (not expression).
#
# Here we are testing logical equivalence with DeMorgan's Laws.
# ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
# ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
# ¬∀x P(x) ≡ ∃x ¬P(x)
# ¬∃x P(x) ≡ ∀x ¬P(x)

exec(read_to_string("../05-existential-quantifier.py"), globals())
exec(read_to_string("../04-universal-quantifier.py"), globals())
exec(read_to_string("../03-logical-equivalence.py"), globals())



# 1. ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
# If P and Q are True, then return False: Else return True is logically 
# equivalent to If P is not True and Q is not True, then return True.
def law_one():
    assert if_and_only_if(not (S and Q), 
                         (not S) or (not Q))

# 2. ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
# If P or Q are True, return False: Else return True is logically
# equivalent to:
# If P is False and Q is False, return True: Else return False.
def law_two():
    assert not (S or Q) == (not S) and (not Q)


def forall_test(fn, xs) -> tuple[object, bool]:
    try:
        forall(fn, xs)
        return True
    except:
        return False

# 3. ¬∀x P(x) ≡ ∃x ¬P(x)
# Not all x are P == At least one x is not P.
def law_three():
    assert forall_test([S,P]) == True
    assert forall_test([S,Q]) == False


# ¬∃x P(x) ≡ ∀x ¬P(x)
# Not a single x is P == Every x is not P.
class LawFour():
    @staticmethod
    def run(xs) -> bool:
        """Given a list of booleans where True means "x_is_P" and False means
        "x_is_not_P", this method will determine if not (at least one element in
        the list is P)."""
        # Logical Equivalence Test
        print("law_four() -- input: ", xs)
        print("law_four() -- ¬∃x P(x): ", LawFour.no_x_is_P(xs))
        print("law_four() -- ∀x ¬P(x):", LawFour.every_x_is_not_P(xs))
        logically_equivalent = LawFour.no_x_is_P(xs) == LawFour.every_x_is_not_P(xs)
        msg = "'¬∃x P(x)' is logically equivalent to '∀x ¬P(x)': "
        print(f"law_four() -- {msg}", logically_equivalent)
        assert logically_equivalent

        return LawFour.no_x_is_P(xs)

    # ¬∃x P(x): ~(At least one x is P).
    @staticmethod
    def no_x_is_P(xs):
        def is_p(x):
            if x is True:
                return (x, True)
            return (x, False)

        return not exists(is_p, xs)[0]

    # ∀x ¬P(x): Every x is not P.
    @staticmethod
    def every_x_is_not_P(xs):
        def fn(x):
            if x != P:
                return (True, False)
            return (False, True)

        return forall_test(fn, xs)



if __name__ == "__main__":
    is_P  = True
    not_P = not is_P

    assert LawFour.run([is_P, is_P, is_P]) == False
    assert LawFour.run([is_P, is_P, not_P]) == False
    assert LawFour.run([not_P, not_P, not_P]) == True
