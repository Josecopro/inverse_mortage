import unittest

from check_process import is_old_enough, required_stratum, is_value_enough, is_property_valid, hope_of_life

normal_testcase_1 = (65, 4, 655e5, 25, True, True)
extraordinary_testcase_1 = (85, 4, 655e5, 18, False, True)


class inverse_mortage(unittest.TestCase):

    

    def normal_testcase_1(self, age: int, stratum: int, commercial_value: float, antiqueness: int, is_women: bool, is_legal: bool):

        if is_old_enough(age) and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women) and is_legal:
            return True
        return False
    
    def normal_testcase_value1():
        pass

    #Verifica si puede acceder a la hipoteca inversa
    def test_normal_testcase_1(self):
        age, stratum, commercial_value, antiqueness, is_women, is_legal = normal_testcase_1
        result = self.normal_testcase_1(age, stratum, commercial_value, antiqueness, is_women, is_legal)
        self.assertTrue(result)

    
    def extraordinary_testcase_1(self, age: int):

        if is_old_enough(age): #and required_stratum(stratum) and is_value_enough(commercial_value) and is_property_valid(antiqueness) and hope_of_life(age, is_women)== 0 and is_legal:
            return True
        return False

    def test_extraordinary_testcase_1(self):
        age= 85
        result = self.extraordinary_testcase_1(age)
        self.assertTrue(result)

