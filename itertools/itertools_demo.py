import itertools

# map applies a function to all the items in an input_list
# type(m) = map
m = map(str, range(1,10))

for i in itertools.product(m, repeat = 3):
    # type(i) = tuple
    print("".join(i))

"""
111
112
113
...
997
998
999
"""