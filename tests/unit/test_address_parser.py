import unittest

from parameterized import parameterized

from address_parser.address_parser import AddressParser


class Examples:
    # noinspection PyMethodMayBeStatic
    def get_data(self):
        return [
            (
                'Winterallee 3',
                {
                    "street": "Winterallee",
                    "housenumber": "3"
                }
            ),
            (
                'Musterstrasse 45',
                {
                    "street": "Musterstrasse",
                    "housenumber": "45"
                }
            ),
            (
                'Blaufeldweg 123B',
                {
                    "street": "Blaufeldweg",
                    "housenumber": "123B"
                }
            ),
            (
                'Am Bächle 23',
                {
                    "street": "Am Bächle",
                    "housenumber": "23"
                }
            ),
            (
                'Auf der Vogelwiese 23 b',
                {
                    "street": "Auf der Vogelwiese",
                    "housenumber": "23 b"
                }
            ),
            (
                '4, rue de la revolution',
                {
                    "street": "rue de la revolution",
                    "housenumber": "4"
                }
            ),
            (
                '200 Broadway Av',
                {
                    "street": "Broadway Av",
                    "housenumber": "200"
                }
            ),
            (
                'Calle Aduana, 29',
                {
                    "street": "Calle Aduana",
                    "housenumber": "29"
                }
            ),
            (
                'Calle 39 No 1540',
                {
                    "street": "Calle 39",
                    "housenumber": "No 1540"
                }
            ),
            (
                '   Altenhofer Straße    13  ',
                {
                    "street": "Altenhofer Straße",
                    "housenumber": "13"
                }
            ),
            (
                'Altenhofer Str. 13',
                {
                    "street": "Altenhofer Str.",
                    "housenumber": "13"
                }
            ),
            (
                'Hauptplatz 101-103',
                {
                    "street": "Hauptplatz",
                    "housenumber": "101-103"
                }
            ),
            (
                'Löbauerstrasse 1a-4b',
                {
                    "street": "Löbauerstrasse",
                    "housenumber": "1a-4b"
                }
            ),
        ]


class TestAddressParser(unittest.TestCase):

    @parameterized.expand(Examples().get_data())
    def test_parse_address(self, raw, expected_parsed_street):
        result = AddressParser().parse_street(raw)
        self.assertEqual(
            expected_parsed_street,
            result
        )

    def test_parse_address_to_json(self):
        result = AddressParser().parse_street_to_json('Winterallee 3')
        self.assertEqual(
            '{"street": "Winterallee", "housenumber": "3"}',
            result
        )
