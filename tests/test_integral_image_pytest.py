import pytest
from integral_image_tools.integral_image import integral_view, rect_sum


##############################################################################

# Fixture with matrices


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
        "bad_item_inner_not_integer": [
            [None]
        ],
        "bad_item_inner_not_within_left_boundary": [
            [-1]
        ],
        "bad_item_inner_not_within_right_boundary": [
            [256]
        ],
        "bad_item_different_length": [
            [0],
            [0, 0]
        ]
    }

    return matrices


# integral_view matrices tests


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


def test_integral_view_item_not_list(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_not_list"])


def test_integral_view_item_inner_not_integer(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_inner_not_integer"])


def test_integral_view_item_inner_not_within_left_boundary(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_inner_not_within_left_boundary"])


def test_integral_view_item_inner_not_within_right_boundary(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_inner_not_within_right_boundary"])


def test_integral_view_items_different_length(env):
    with pytest.raises(ValueError):
        integral_view(env["bad_item_different_length"])


# rect_sum matrices tests


def test_rect_sum_not_list(env):
    with pytest.raises(ValueError):
        rect_sum(env["bad_not_list"], 0, 0, 0, 0)


def test_rect_sum_item_not_lists(env):
    with pytest.raises(ValueError):
        rect_sum(env["bad_item_not_list"], 0, 0, 0, 0)


def test_rect_sum_item_inner_not_integer(env):
    with pytest.raises(ValueError):
        rect_sum(env["bad_item_inner_not_integer"], 0, 0, 0, 0)


def test_rect_sum_items_different_length(env):
    with pytest.raises(ValueError):
        rect_sum(env["bad_item_different_length"], 0, 0, 0, 0)

# rect_sum coordinates tests


@pytest.mark.parametrize(
    "x1, y1, x2, y2, expected",
    [
        (1, 1, 3, 2, 1060),
        (2, 3, 3, 3, 238)
    ]
)
def test_rect_sum_everything_ok(x1, y1, x2, y2, expected, env):
    assert rect_sum(env["good"], x1, y1, x2, y2) == expected


@pytest.mark.parametrize(
    "x1, y1, x2, y2",
    [
        (None, 0, 0, 0),
        (0, None, 0, 0),
        (0, 0, None, 0),
        (0, 0, 0, None),
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1)
    ]
)
def test_rect_sum_coordinate_not_positive_integer(x1, y1, x2, y2, env):
    with pytest.raises(ValueError):
        rect_sum(env["good"], x1, y1, x2, y2)


@pytest.mark.parametrize(
    "x1, y1, x2, y2",
    [
        (4, 0, 0, 0),
        (0, 0, 4, 0),
        (0, 4, 0, 0),
        (0, 0, 0, 4)
    ]
)
def test_rect_sum_coordinate_outside_boundaries(x1, y1, x2, y2, env):
    with pytest.raises(ValueError):
        rect_sum(env["good"], x1, y1, x2, y2)


@pytest.mark.parametrize(
    "x1, y1, x2, y2",
    [
        (3, 0, 2, 0),
        (0, 3, 0, 2)
    ]
)
def test_rect_sum_coordinate_top_left_greater_than_bottom_right(x1, x2, y1, y2, env):
    with pytest.raises(ValueError):
        rect_sum(env["good"], x1, y1, x2, y2)

##############################################################################
