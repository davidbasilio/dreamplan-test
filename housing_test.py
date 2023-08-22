# Linear Reggression for Housing Prices
# Author: David Basilio Rodriguez Cortez
# Dreamplan                 22/08/2023

import unittest
from housing import HousePrice

class TestHousing(unittest.TestCase):
    # initialize the test class
    def setUp(self) -> None:
        self.housing = HousePrice()

    # initialize the test class for mean price
    def test_mean_house_price(self):
        mean_price = self.housing.GetMeanHousePrice()
        self.assertIsNotNone(mean_price)
    
    # initialize the test class for predicted price
    def test_predict_price(self):
        price = self.housing.PredictHousePriceFromInput([9960, 3, 2, 2, 1, -1, 1, -1, -1, 2, 1, 1])
        self.assertIsNotNone(price)

if __name__ == '__main__':
    unittest.main()