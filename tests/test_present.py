import pytest
from lib.present import *

def test_wrap_then_unwrap():
    presents = Present()
    presents.wrap('toys')
    assert presents.unwrap() == 'toys'

def test_contents_not_none():
    presents = Present()
    presents.wrap('cars')
    with pytest.raises(Exception) as e:
        presents.wrap('toys')
    error_message = str(e.value)    
    assert error_message == "A contents has already been wrapped."

def test_unwrap():
    presents = Present()
    with pytest.raises(Exception) as e:
        presents.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_unwrap_preserve_wrap():
    presents = Present()
    presents.wrap('cars')
    with pytest.raises(Exception) as e:
        presents.wrap('toys')
    assert presents.unwrap() == 'cars'
