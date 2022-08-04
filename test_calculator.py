import pytest
from calculator import calculation


@pytest.mark.parametrize("test_input,expected",
    [
        ("4+6", 10),
    ]
)
def test_sum(test_input, expected):
    result = calculation(test_input)
    assert result == expected
