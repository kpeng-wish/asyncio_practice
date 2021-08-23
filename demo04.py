# demo-04, yield usage

def gen():
    for c in 'AB':
        yield c
    for i in range(1, 3):
        yield i

def gen2():
    yield from "AB" # with iterable object
    yield from range(1, 3)

print(list(gen()))

print(list(gen2())) 