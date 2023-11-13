from lib.report_length import * 

def test_report_length_glide():
    actual = report_length('glide')

    assert actual == "This string was 5 characters long."

def test_report_length_adorable():
    actual = report_length('adorable')

    assert actual == "This string was 8 characters long."

def test_report_length_fight():
    actual = report_length("fight")

    assert actual == "This string was 5 characters long."

def test_report_length_thisisastring():
    actual = report_length("This is a string")

    assert actual == "This string was 16 characters long."