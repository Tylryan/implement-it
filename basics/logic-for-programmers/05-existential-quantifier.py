# ∃x, P(x)
# Some x are P.
# There exists at least one x that is a P.

# A while loop that returns the last evaluated value.
def for_loop(predicate_fn, xs: list[object]) -> object:
    res = None
    for x in xs:
        res, to_break = predicate_fn(x)
        if to_break is True:
            break
    return res

# ∃x, P(x)
def exists(predicate_fn, xs: list[object]) -> tuple[object, bool]:
    def fn(x) -> tuple[object, bool]:
        res, to_break = predicate_fn(x)
        if res is True:
            return (True, True)
        return (False, False)

    return (for_loop(fn, xs), True)


def identity(x) -> tuple[object, bool]:
    """Just returns what was provided. Useful when you need to provide a lambda
    to delay execution."""
    return (x, False)

def invert(fn, x) -> tuple[object, bool]:
    """A logical not."""
    res, to_break = fn(x)
    return (not res, to_break)

def lazy_false(x) -> tuple[object, bool]:
    """Returns False"""
    return (False, False)


def _test():
    S = False or (True and True)
    Q = False
    P = True


    assert exists(identity,[S,Q]) == True
    assert exists(lazy_false, [S,Q]) == False
