def test(*args):
    for arg in args:
        print('hello,' + repr(arg))


my_tuple = (1, 2, 3, 4, 5, 6,)
# use _ to handle variable you don't care
# use * to represent the reset of variables
(num_1, _, *num_rest, num_last,) = my_tuple
print (num_1, num_rest, num_last)

# here I use * before tuple and use this as an paramter
test(*my_tuple)
