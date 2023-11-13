from lib.greet import *

def test_greet_john():
    expected = 'Hello, John!'
    actual = greet('John')

    assert actual == expected


def test_greet_andrew():
    expected = 'Hello, Andrew!'
    actual = greet('Andrew')

    assert actual == expected

def test_greet_emily():
    expected = 'Hello, Emily!'
    actual = greet('Emily')

    assert actual == expected