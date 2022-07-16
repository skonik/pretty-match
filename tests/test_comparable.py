import pytest

from pretty_match import results
from pretty_match.typing import Result
from pretty_match.comparable import Number


@pytest.mark.parametrize(
    "first_number,second_number,expected_result",
    [[1, 2, results.Less], [2, 2, results.Equal], [3, 2, results.Greater]],
)
def test_number_match(
    first_number: int,
    second_number: int,
    expected_result: Result,
):
    assert (
        Number(first_number).compare(
            second_number,
        )
        == expected_result
    )
