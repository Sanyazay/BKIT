import unittest
from RK2 import *

class test_RK2(unittest.TestCase):
    def test_sortingB1(self):
        one_to_many = [(m.name, m.freq, c.name) for c in comps for m in micros if m.computer_id == c.id]
        res = sortingB1(one_to_many)
        self.assertEqual(res,[('intel1', 2300, 'RussianButcher'),('intel3', 2950, 'RussianButcher'),('intel9', 4053, 'Evelon'),('pentium1', 5643, 'RussianButcher'),('ryzen1', 2400, 'Evelon'),('ryzen3', 3500, 'Buster'),('ryzen5', 6500, 'Evelon'),('ryzen7', 4200, 'TORONTOTOKYO'),('xenon9', 3456, 'Buster')])
    def test_sortingB2(self):
        one_to_many = [(m.name, m.freq, c.name) for c in comps for m in micros if m.computer_id == c.id]
        res = sortingB2(one_to_many)
        self.assertEqual(res,[('RussianButcher', 3),('Evelon', 3),('Buster', 2),('TORONTOTOKYO', 1)])
    def test_sortingB3(self):
        many_to_many = [
        (m.name, m.freq, c.name)
        for c in comps
        for m in micros
        for r in miccomps
        if c.id == r.comp_id and m.id == r.proc_id
        ]
        res = sortingB3(many_to_many)
        self.assertEqual(res,{"intel1" : ['RussianButcher', 'Buster', 'TORONTOTOKYO'],"ryzen1" : ['RussianButcher', 'Buster', 'Evelon'],"pentium1" : ['RussianButcher', 'TORONTOTOKYO']})




if __name__ == "__name__":
    unittest.main()
    #python -m unittest test_RK2.py