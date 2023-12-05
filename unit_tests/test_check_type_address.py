import unittest

from app_view_model.functions.functions import check_type_address


# from functions import check_type_address


class TestCheckTypeAddress(unittest.TestCase):
    def test_case_1(self):
        result = check_type_address(True, False, False, False, False)
        self.assertEqual(result, (True, False, False))

    def test_case_2(self):
        result = check_type_address(True, False, False, True, False)
        self.assertEqual(result, (True, True, False))

    def test_case_3(self):
        result = check_type_address(True, False, False, False, True)
        self.assertEqual(result, (True, False, False))

    def test_case_4(self):
        result = check_type_address(False, True, False, False, False)
        self.assertEqual(result, (False, True, False))

    def test_case_5(self):
        result = check_type_address(False, True, False, True, False)
        self.assertEqual(result, (True, True, False))

    def test_case_6(self):
        result = check_type_address(False, True, False, False, True)
        self.assertEqual(result, (False, True, True))

    def test_case_7(self):
        result = check_type_address(False, False, True, False, False)
        self.assertEqual(result, (False, False, True))

    def test_case_8(self):
        result = check_type_address(False, False, True, False, True)
        self.assertEqual(result, (False, True, True))

    def test_case_9(self):
        result = check_type_address(False, False, True, True, False)
        self.assertEqual(result, (False, False, True))

    def test_case_10(self):
        result = check_type_address(False, False, False, True, True)
        self.assertEqual(result, (False, False, False))

    def test_case_11(self):
        result = check_type_address(True, False, False, True, True)
        self.assertEqual(result, (True, True, True))

    def test_case_12(self):
        result = check_type_address(False, True, False, True, True)
        self.assertEqual(result, (True, True, True))

    def test_case_13(self):
        result = check_type_address(False, False, True, True, True)
        self.assertEqual(result, (True, True, True))

    def test_case_14(self):
        result = check_type_address(False, True, True, True, True)
        self.assertEqual(result, (True, True, True))

    def test_case_15(self):
        result = check_type_address(False, False, False, False, False)
        self.assertEqual(result, (False, False, False))

if __name__ == '__main__':
    unittest.main(verbosity=2)
