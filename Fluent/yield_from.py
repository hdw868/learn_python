def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    list(chain(s, t))
