import textwrap


def test():
    text = """
    This is the second line
    This is the third line
    This is the fourth line
    """
    print(repr(text))
    print(repr(textwrap.dedent(text)))


test()
