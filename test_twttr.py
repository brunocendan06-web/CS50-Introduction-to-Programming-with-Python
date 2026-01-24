#create a program that outputs the same text but with all vowels ommitted.
#but now we need to test its with assert
from twttr import shorten


def test_basic():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed():
    assert shorten("Hi tO AlL of YoU") == "H t lL f Y"

def test_only_vowels():
    assert shorten("aeiouAEIOU") == ""

def test_numbers():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("%!!!") == "%!!!"




if __name__ == "__main__":
    main()