def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise ValueError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise ValueError("b must be an integer")
    if isinstance(a, float):
        a = int(b)
    if isinstance(b, float):
        b  = float(b)
    return a + b
