import unittest
from integral_image_tools.integral_image import integral_view, rect_sum


class TestIntegralViewMatrix(unittest.TestCase):
    def setUp(self):
        self.matrices = {
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

        self.coordinates = {
            "good": [
                (1, 1, 3, 2, 1060),
                (2, 3, 3, 3, 238)
            ],
            "bad_not_positive_integer": [
                (None, 0, 0, 0),
                (0, None, 0, 0),
                (0, 0, None, 0),
                (0, 0, 0, None),
                (-1, 0, 0, 0),
                (0, -1, 0, 0),
                (0, 0, -1, 0),
                (0, 0, 0, -1)
            ],
            "bad_outside_boundaries": [
                (4, 0, 0, 0),
                (0, 0, 4, 0),
                (0, 4, 0, 0),
                (0, 0, 0, 4)
            ],
            "bad_top_left_greater_than_bottom_right": [
                (3, 0, 2, 0),
                (0, 3, 0, 2)
            ]
        }

    def test_integral_view_matrix_everything_ok(self):
        self.assertEqual(integral_view(self.matrices["good"]), [
            [244, 275, 306, 511],
            [345, 597, 854, 1255],
            [401, 820, 1166, 1728],
            [502, 959, 1456, 2105]
        ])

    def test_integral_view_matrix_not_list(self):
        with self.assertRaises(ValueError):
            integral_view(self.matrices["bad_not_list"])

    def test_integral_view_matrix_item_not_list(self):
        with self.assertRaises(ValueError):
            integral_view(self.matrices["bad_item_not_list"])

    def test_intergral_view_item_inner_not_integer(self):
        with self.assertRaises(ValueError):
            integral_view(self.matrices["bad_item_inner_not_integer"])

    def test_integral_view_matrix_item_inner_not_within_left_boundary(self):
        with self.assertRaises(ValueError):
            integral_view(
                self.matrices["bad_item_inner_not_within_left_boundary"])

    def test_integral_view_matrix_item_inner_not_within_right_boundary(self):
        with self.assertRaises(ValueError):
            integral_view(
                self.matrices["bad_item_inner_not_within_right_boundary"])

    def test_integral_view_matrix_items_different_length(self):
        with self.assertRaises(ValueError):
            integral_view(self.matrices["bad_item_different_length"])

    def test_rect_sum_matrix_not_list(self):
        with self.assertRaises(ValueError):
            rect_sum(self.matrices["bad_not_list"], 0, 0, 0, 0)

    def test_rect_sum_matrix_item_not_lists(self):
        with self.assertRaises(ValueError):
            rect_sum(self.matrices["bad_item_not_list"], 0, 0, 0, 0)

    def test_rect_sum_matrix_item_inner_not_integer(self):
        with self.assertRaises(ValueError):
            rect_sum(self.matrices["bad_item_inner_not_integer"], 0, 0, 0, 0)

    def test_rect_sum_matrix_items_different_length(self):
        with self.assertRaises(ValueError):
            rect_sum(self.matrices["bad_item_different_length"], 0, 0, 0, 0)

    def test_rect_sum_coordinate_everything_ok(self):
        for coordinate_tuple in self.coordinates["good"]:
            x1, y1, x2, y2, expected = coordinate_tuple
            self.assertEqual(
                rect_sum(self.matrices["good"], x1, y1, x2, y2), expected)

    def test_rect_sum_coordinate_not_positive_integer(self):
        for coordinate_tuple in self.coordinates["bad_not_positive_integer"]:
            x1, y1, x2, y2 = coordinate_tuple
            with self.assertRaises(ValueError):
                rect_sum(self.matrices["good"], x1, y1, x2, y2)

    def test_rect_sum_coordinate_outside_boundaries(self):
        for coordinate_tuple in self.coordinates["bad_outside_boundaries"]:
            x1, y1, x2, y2 = coordinate_tuple
            with self.assertRaises(ValueError):
                rect_sum(self.matrices["good"], x1, y1, x2, y2)

    def test_rect_sum_coordinate_top_left_greater_than_bottom_right(self):
        for coordinate_tuple in self.coordinates["bad_top_left_greater_than_bottom_right"]:
            x1, y1, x2, y2 = coordinate_tuple
            with self.assertRaises(ValueError):
                rect_sum(self.matrices["good"], x1, y1, x2, y2)
