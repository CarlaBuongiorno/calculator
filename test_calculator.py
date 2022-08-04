import pytest
from calculator import calculation


@pytest.mark.parametrize("test_input,expected",
    [
        ("4+6", 10),
        ("5+11", 16),
        ("5-3", 2),
    ]
)
def test_sum(test_input, expected):
    result = calculation(test_input)
    assert result == expected
