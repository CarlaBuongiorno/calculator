import pytest
from calculator import calculation


@pytest.mark.parametrize("test_input,expected",
    [
        ("4+6.5", 10.5),
        ("5+11", 16),
        ("5-3", 2),
        ("5*3", 15),
        ("9/3", 3),
        ("9+3+1", 13),
        ("9-3-1", 5),
        ("9+3-1", 11),
        ("9-3+1", 7),
    ]
)
def test_sum(test_input, expected):
    result = calculation(test_input)
    assert result == expected
