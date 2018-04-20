def test_break(i):
    while True:
        try:
            if i == 0:
                print('break')
                break
            print i
            i -= 1
        except Exception:
            pass
        finally:
            print('finally!')


def test_return(i):
    while True:
        try:
            if i == 0:
                print('return')
                return i
        except Exception:
            pass
        finally:
            print('finally!')


test_break(5)
