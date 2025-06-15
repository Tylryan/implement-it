# ∀x, P(x)
# All S are P
# For every x, x is P.

# A while loop that returns the last evaluated value.
def for_loop(predicate_fn, xs: list[object]) -> object:
    res = None
    for x in xs:
        res, to_break = predicate_fn(x)
        if to_break is True:
            break
    return res

def forall(predicate_fn, xs: list[object]) -> None:
    def fn(x):
        res, to_break = predicate_fn(x)
        assert res == True
        return (None, to_break)

    for_loop(fn, xs)

def identity(x) -> tuple[object, bool]:
    """Just returns what was provided. Useful when you need to provide a lambda
    to delay execution."""
    return (x, False)



def _test():
    S = False or (True and True)
    Q = False
    P = True


    # 3. ¬∀x P(x) ≡ ∃x ¬P(x)
    # Not all x are P == At least one x is not P.
    assert forall_test([S,P]) == True
    assert forall_test([S,Q]) == False
