import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(1, 21):
            cart.add_dvd(DigitalVideoDisc(f"Movie {i}", "Category", 10.0))

        result = cart.add_dvd(DigitalVideoDisc("Movie 21", "Category", 10.0))
        self.assertFalse(result, "Giỏ hàng phải từ chối đĩa thứ 21")

    def test_discount_valid(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Movie 1", "Category", 100.0))
        discount_percent = 20
        discounted_cost = cart.total_cost_with_discount(discount_percent)

        self.assertEqual(discounted_cost, 80.0, places=2, msg="Chi phí sau khi áp dụng giảm giá 20% phải là 20.0")

    def test_discount_error_above_100(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Movie 1", "Category", 100.0))

        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)