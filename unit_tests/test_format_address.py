import unittest

from app_view_model.functions.format_address import format_address


class TestFormatAddress(unittest.TestCase):

    def test_format_address(self):
        test_cases = [
            (['197375', 'Санкт-Петербург', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20/3', '',
              'А', '', '300'], "197375, Санкт-Петербург, Санкт-Петербург г., Вербная ул., д. 20/3, лит. А, кв. 300"),
            (['197375', '', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20/3', '',
              'А', '', '300'], "197375, Санкт-Петербург г., Вербная ул., д. 20/3, лит. А, кв. 300"),
            ([None, 'Санкт-Петербург', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20/3', '',
              'А', '', '300'], "Санкт-Петербург, Санкт-Петербург г., Вербная ул., д. 20/3, лит. А, кв. 300"),
            ([None, '', None, '', 'Санкт-Петербург', 'г.', '', None, 'Вербная', 'ул.', '20', '6',
              None, '', '300'], "Санкт-Петербург г., Вербная ул., д. 20, корп. 6, кв. 300")

        ]

        for input_data, expected_output in test_cases:
            with self.subTest(input_data=(input_data), expected_output=expected_output):
                result = format_address(input_data)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
