# A while loop that returns the last evaluated value.
def for_loop(predicate_fn, xs: list[object]) -> object:
    res = None
    for x in xs:
        res, to_break = predicate_fn(x)
        if to_break is True:
            break
    return res



def read_to_string(path: str) -> str:
    f = open(path, "r")
    c = f.read()
    f.close()
    return c
