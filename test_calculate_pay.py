from unittest import TestCase

from calculate_pay import calculate_pay


class Test(TestCase):

    def test_negative_wages(self):
        self.assertEqual(0, calculate_pay(10, -10))

    def test_negative_hours(self):
        self.assertEqual(0, calculate_pay(-10, 10))

    def test_negative_both(self):
        self.assertEqual(0, calculate_pay(-10, -10))

    def test_zero_hours(self):
        self.assertEqual(0, calculate_pay(0, 10))

    def test_zero_wages(self):
        self.assertEqual(0, calculate_pay(10, 0))

    def test_zero_both(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_under_40_hours(self):
        self.assertEqual(200, calculate_pay(20, 10))

    def test_40_hours(self):
        self.assertEqual(400, calculate_pay(40, 10))

    def test_over_40_hours(self):
        self.assertEqual(800, calculate_pay(60, 10))
