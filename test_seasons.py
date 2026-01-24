from datetime import date, timedelta
from seasons import parse_date, minutes_since, to_words
import pytest

def test_parse_date_valid():
    d = parse_date("2000-01-01")
    assert d.year == 2000
    assert d.month == 1
    assert d.day == 1

def test_parse_date_invalid():
    assert parse_date("2000-13-01") is None
    assert parse_date("2000-00-01") is None
    assert parse_date("abcd-ef-gh") is None
    assert parse_date("2020/01/01") is None

def test_minutes_since_today():
    today = date.today()
    assert minutes_since(today) == 0

def test_minutes_since_yesterday():
    yesterday = date.today() - timedelta(days=1)
    assert minutes_since(yesterday) == 1440

def test_to_words():
    assert to_words(0) + " minutes" == "Zero minutes"
    assert to_words(1) + " minutes" == "One minutes"
    assert to_words(525600) + " minutes" == "Five hundred twenty-five thousand, six hundred minutes"
    assert to_words(1440) + " minutes" == "One thousand, four hundred forty minutes"
