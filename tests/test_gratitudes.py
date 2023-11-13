from lib.gratitudes import *

def test_gratitude_add():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    assert gratitudes.format() == "Be grateful for: family"

def test_multiple_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add('family')
    gratitudes.add('friends')
    gratitudes.add('sunshine')
    assert gratitudes.format() == "Be grateful for: family, friends, sunshine"