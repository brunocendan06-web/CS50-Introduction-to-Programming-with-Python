import pytest
from um import count

def test_basic():
    assert count("hello, um, world") == 1
    assert count("um") == 1
    assert count("Um") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3
    assert count("Um, I don't know, um...") == 2

def test_substrings():
    assert count("yummy, cucumber, summary") == 0
    assert count("aluminum is a metal") == 0

def test_punctuation():
    assert count("Well, um!") == 1
    assert count("Um... what?") == 1
    assert count("Wait—um, really?") == 1

def test_no_ums():
    assert count("hello world") == 0
    assert count("") == 0
