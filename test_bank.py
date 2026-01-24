#import the program
from bank import value

#assert all methods
def test_hello():
    assert value("hello") == 0
    assert value("Hello, friend") == 0
    assert value("HELLO there") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("Hi there") == 20
    assert value("how are you") == 20

def test_other():
    assert value("good morning") == 100
    assert value("What's up?") == 100

if __name__ == "__main__":
    main()
