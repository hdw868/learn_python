from .stack import Stack


def par_checker(s):
    par_stack = Stack()
    for c in s:
        if c in "([{":
            par_stack.push(c)
        else:
            if not par_stack.isEmpty():
                top = par_stack.pop()
                if match_symbol(c, top):
                    continue
                else:
                    return False
            else:
                return False
    return par_stack.isEmpty()


def match_symbol(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


def test_par():
    assert par_checker("(((()))") is False
    assert par_checker("())") is False
    assert par_checker("(((())))") is True


def test_decimal2binary():
    assert decimal2binary(16) == "10000"
    assert decimal2binary(19) == "10011"


def decimal2binary(num):
    st = Stack()
    while num != 0:
        st.push(num % 2)
        num = num // 2
    result = []
    while not st.isEmpty():
        result.append(str(st.pop()))
    return "".join(result)


def base_convert(num, base):
    digits = "0123456789ABCDEF"
    st = Stack()
    while num != 0:
        st.push(num % base)
        num = num // base
    result = []
    while not st.isEmpty():
        result.append(digits[st.pop()])
    return "".join(result)


def test_base_convert():
    assert base_convert(16, 2) == "10000"
    assert base_convert(19, 2) == "10011"
    assert base_convert(19, 8) == "23"
    assert base_convert(19, 16) == "13"
    assert base_convert(31, 16) == "1F"
