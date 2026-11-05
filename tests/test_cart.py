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