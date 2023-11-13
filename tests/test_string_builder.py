from lib.string_builder import *

def test_string_add():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""


def test_string_add():
    stringbuilder = StringBuilder()
    stringbuilder.add("this is a string")
    assert stringbuilder.output() == 'this is a string'

def test_string_length():
    stringbuilder = StringBuilder()
    stringbuilder.add('glide')
    assert stringbuilder.size() == 5

def test_another_string_length():
    stringbuilder = StringBuilder()
    stringbuilder.add('I am tired')
    assert stringbuilder.size() == 10
