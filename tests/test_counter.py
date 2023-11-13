from lib.counter import *

def test_counted_to_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_twenty():
    counter = Counter()
    counter.add(20)
    assert counter.report() == "Counted to 20 so far."

def test_counter_add_multiple_numbers():
    counter = Counter()
    counter.add(10)
    counter.add(5)
    assert counter.report() == "Counted to 15 so far."