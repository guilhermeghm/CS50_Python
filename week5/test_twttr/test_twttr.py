from twttr import shorten

def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("t3ste") == "t3st"
    assert shorten("my test!") == "my tst!"
    assert shorten("TESTEUPPER") == "TSTPPR"
