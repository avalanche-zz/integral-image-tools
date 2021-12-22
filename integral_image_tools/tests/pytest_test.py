import pytest
from ..integral_image import integral_view

##############################################################################

# Initialization


@pytest.fixture(scope="module")
def env():
    matrices = {
        "good": [
            [244, 31, 31, 205],
            [101, 221, 226, 196],
            [56, 167, 89, 161],
            [101, 38, 151, 87]
        ],
        "bad_not_list": None,
        "bad_item_not_list": [None, None],
        "bad_items_inner__not_integers": [
            [None]
        ],
        "bad_item_inner_not_within_left_boundary": [
            [-1]
        ],
        "bad_item_inner_not_within_right_boundary": [
            [256]
        ],
        "bad_items_different_length": [
            [0],
            [0, 0]
        ]
    }

    return matrices


def test_integral_view_everything_ok(env):
    assert integral_view(env["good"]) == [
        [244, 275, 306, 511],
        [345, 597, 854, 1255],
        [401, 820, 1166, 1728],
        [502, 959, 1456, 2105]
    ]


def test_integral_view_not_list(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_not_list"])


def test_integral_view_item_not_lists(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_items_not_lists"])


def test_integral_view_item_inner_not_within_left_boundary(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_inner_not_within_left_boundary"])


def test_integral_view_item_inner_not_within_right_boundary(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_inner_not_within_right_boundary"])


def test_integral_view_items_different_length(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_items_different_length"])

##############################################################################
