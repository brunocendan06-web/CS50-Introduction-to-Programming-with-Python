#import the program
from plates import is_valid

def test_min_max_length():
    assert is_valid("C") == False
    assert is_valid("DB") == True
    assert is_valid("AHCTER") == True
    assert is_valid("APCWEXG") == False

def test_starts_with_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("5C50") == False
    assert is_valid("!CS50") == False

def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS123") == True

def test_no_symbols():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CSFIVE") == True