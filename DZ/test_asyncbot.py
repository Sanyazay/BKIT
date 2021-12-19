import unittest
from asyncbot3 import summary,average_price,first_course,first_course_price,main_course,main_course_price,dessert,dessert_price




class Bot_test(unittest.TestCase):
    def test_summary(self):
        ans1 = 1
        ans2 = 2
        ans3 = 3
        res = summary(first_course,first_course_price,main_course,main_course_price,dessert,dessert_price,ans1,ans2,ans3)
        self.assertEqual("Итоговая сумма = 324\n",res)
    def test_average_price(self):
        ans1 = 1
        ans2 = 2
        ans3 = 3
        res = average_price(first_course,first_course_price,main_course,main_course_price,dessert,dessert_price,ans1,ans2,ans3)
        self.assertEqual("Средняя стоимость одной позиции = 108",res)




if __name__ == "__name__":
    unittest.main()
    
    #python -m unittest test_asyncbot.py