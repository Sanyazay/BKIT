import unittest
import unittest.mock
from Logistic_company import Truck


class TruckTest(unittest.TestCase):

    def test_weight(self):
        a=Truck(0,0,57)
        self.assertEqual(a.weight,57)
    def test_delivertype(self):
        a=Truck("1",0,0)
        self.assertEqual(a.deliverytype,"1")    
    def test_boxtype(self):
        a=Truck(0,"1",0)
        self.assertEqual(a.boxtype,"1")
    def test_weight_mock(self):
        a=Truck(0,0,57)
        m=unittest.mock.Mock()
        m.weight = 57
        self.assertEqual(m.weight,a.weight)
if __name__ == "__name__":
    unittest.main()
    
    #python -m unittest test_Truck.py