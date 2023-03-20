from bank import value

def test_value():
    assert value("Hello") == 0
    assert value("Hey there") == 20
    assert value("Other thing") == 100
