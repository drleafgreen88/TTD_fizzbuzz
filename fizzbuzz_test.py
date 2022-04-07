from fizzbuzz import *
import unittest

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.number_div_by_three = 9
        self.number_div_by_five = 10
        self.number_div_by_three_and_five = 15
        self.number_not_div_by_three_or_five = 11
        

    # @unittest.skip("delete this line to run the test")
    def test_div_by_three(self):
        self.assertEqual("fizz", fizzbuzz(self.number_div_by_three))

    # @unittest.skip("delete this line to run the test")
    def test_div_by_five(self):
        self.assertEqual("buzz", fizzbuzz(self.number_div_by_five))

    # @unittest.skip("delete this line to run the test")
    def test_div_by_three_and_five(self):
        self.assertEqual("fizzbuzz", fizzbuzz(self.number_div_by_three_and_five))

    # @unittest.skip("delete this line to run the test")
    def test_not_div_by_three_or_five(self):
        self.assertEqual(11, fizzbuzz(self.number_not_div_by_three_or_five))



    # def test_pet_shop_name(self):
    #     name = get_pet_shop_name(self.cc_pet_shop)
    #     self.assertEqual("Camelot of Pets", name)

    # @unittest.skip("delete this line to run the test")
    # def test_total_cash(self):
    #     sum = get_total_cash(self.cc_pet_shop)
    #     self.assertEqual(1000, sum)

    # @unittest.skip("delete this line to run the test")
    # def test_add_or_remove_cash__add(self):
    #     add_or_remove_cash(self.cc_pet_shop,10)
    #     cash = get_total_cash(self.cc_pet_shop)
    #     self.assertEqual(1010, cash)