# A while loop that returns the last evaluated value.
def for_loop(predicate_fn, xs: list[object]) -> object:
    res = None
    for x in xs:
        res, to_break = predicate_fn(x)
        if to_break is True:
            break
    return res

# ∀x, P(x)
def forall(predicate_fn, xs: list[object]) -> None:
    def fn(x):
        res, to_break = predicate_fn(x)
        assert res == True
        return (None, to_break)

    for_loop(fn, xs)

#def forall(xs: list[object], predicate_fn) -> None:
#    for x in xs: assert predicate_fn(x) == True


# ∃x, P(x)
def exists(predicate_fn, xs: list[object]) -> bool:
    def fn(x):
        res, to_break = predicate_fn(x)
        if res is True:
            return (True, True)
        return (False, False)

    return for_loop(fn, xs)


def identity(x) -> tuple[object, bool]:
    """Just returns what was provided. Useful when you need to provide a lambda
    to delay execution."""
    return (x, False)

def lazy_false(x) -> tuple[object, bool]:
    """Returns False"""
    return (False, False)

S = False or (True and True)
Q = False
P = True


# I expect this to fail
try   : forall(identity, [S,Q])
except: 
    print("forall() assertion failed. Found instance where rule was not True.")

assert exists(identity,[S,Q]) == True
assert exists(lazy_false, [S,Q]) == False


# Here we are testing logical equivalence with DeMorgan's Laws.
# ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
# ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
# ¬∀x P(x) ≡ ∃x ¬P(x)
# ¬∃x P(x) ≡ ∀x ¬P(x)

# 1. ¬(P ∧ Q) ≡ ¬P ∨ ¬Q
# If P and Q are True, then return False: Else return True is logically 
# equivalent to If P is not True and Q is not True, then return True.
assert if_and_only_if(not (S and Q), 
                     (not S) or (not Q))

# 2. ¬(P ∨ Q) ≡ ¬P ∧ ¬Q
# If P or Q are True, return False: Else return True is logically
# equivalent to:
# If P is False and Q is False, return True: Else return False.
assert not (S or Q) == (not S) and (not Q)


def forall_test(xs) -> tuple[object, bool]:
    try:
        forall(identity, xs)
        return True
    except:
        return False



# 3. ¬∀x P(x) ≡ ∃x ¬P(x)
# Not all x are P == At least one x is not P.
assert forall_test([S,P]) == True
assert forall_test([S,Q]) == False


# ¬∃x P(x) ≡ ∀x ¬P(x)
# Not a single x is P == Every x is not P.
def not_exists_test(xs):

