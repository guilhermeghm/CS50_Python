import pytest
from seasons import format_output

def test_seasons():
    assert format_output("525600") == "Five hundred twenty-five thousand, six hundred minutes"
    assert format_output("1051200") == "One million, fifty-one thousand, two hundred minutes"