from typing import List, Optional

import pytest

from pretty_match.attrs import AttrIsNone, FirstNoneAttr


class Query:
    """Object example."""

    def __init__(self, token: Optional[str], start: Optional[int], end: Optional[int]):
        self.token = token
        self.start = start
        self.end = end


@pytest.mark.parametrize(
    "attrs,instance,expected_result",
    [
        [
            ["token", "start", "end"],
            Query(token=None, start=1, end=2),
            AttrIsNone(name="token"),
        ],
        [
            ["token", "start", "end"],
            Query(token="test", start=None, end=2),
            AttrIsNone(name="start"),
        ],
        [
            ["token", "start", "end"],
            Query(token="test", start=1, end=None),
            AttrIsNone(name="end"),
        ],
    ],
)
def test_first_none_attr_match(
    attrs: List[str],
    instance: Query,
    expected_result: AttrIsNone,
):
    assert (
        FirstNoneAttr(
            *attrs,
            instance=instance,
        )
        == expected_result
    )
