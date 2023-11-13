from lib.check_codeword import *

def test_check_correct():
    actual = check_codeword('horse')

    assert actual == "Correct! Come in."

def test_check_close():
    actual = check_codeword('hive')

    assert actual == "Close, but nope."

def test_check_wrong():
    actual = check_codeword('masquerade')
    
    assert actual == "WRONG!"