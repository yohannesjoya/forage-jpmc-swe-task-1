import unittest
from client3 import getDataPoint,getPriceBidGreaterThanAsk

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i,quote in enumerate(quotes):
        stock, bid_price, ask_price, price = getDataPoint(quote)
        correct_price = (bid_price + ask_price)/2
        assert price == correct_price,f'Calculate Price Test {i} : Failed'
    print('All Tests of Calculate Price : Passed')
  
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for i,quote in enumerate(quotes):
      
        success,data = getPriceBidGreaterThanAsk(quote)
        if not success: continue

        stock, bid_price, ask_price, price = data
        assert bid_price > ask_price,f'Calculate Price Bid Greater Than Ask Test {i} : Failed'
        
    print('All Tests of Calculate Price Bid Greater Than Ask : Passed')


  """ ------------ Add more unit tests ------------ """


if __name__ == '__main__':
    unittest.main()
