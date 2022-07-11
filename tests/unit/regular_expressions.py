import re

import unittest


class TestRegularExpression(unittest.TestCase):
    def test_match(self):
        results = re.finditer(
            # "^(?P<street>[\\w\\s]+)(\\s+)(\\d+\\w?)$",
            # "^(?P<street>[\\w\\s]+)(?:\\s+)(?P<house_number>\\d+\\w?)$",
            "^"
                + "(?P<street>[\\D\\s]+\\d+)"
                + "(?:[\\s]+)"
                # +  "(?P<house_number>No\\s+\\d+\\s?\\D?)"
                +  "(?P<house_number>No 1540)"
                + "$"
            ,
            'Calle 39 No 1540'
        )
        print('test')
        # print(len(list(results)))
        # self.asserstEqual('list', type(result))
        for result in results:
            print('test')
            print(result)
            # self.assertEqual(None, result)