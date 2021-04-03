import random


def truth(s):
    b = s.lower()
    return b


def test_in():
    colors = ['khaki', 'black', 'white', 'brown', 'pink']
    return random.choice(colors)


def greater(a, b):
    c = a + b
    return c


def less():
    words = ['cat', 'home', 'cat', 'mom', 'dad', 'I', 'you', 'road', 'mime', 'pig']
    return random.choice(words)


def equal():
    monty_python = {'Terry Jones', 'John Cleese', 'Michel Palin', 'Graham Chapman'}
    return monty_python
