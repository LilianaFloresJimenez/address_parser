import re
import json


# noinspection PyMethodMayBeStatic
class AddressParser:
    def parse_street_to_json(self, raw: str) -> str:
        return self.to_json(
            self.parse_street(raw)
        )

    def parse_street(self, raw: str) -> dict:
        street = None
        house_number = None

        patterns = [
            # Spanish format
            "^(?P<street>[\\D\\s]+\\d*)(?:[,\\s]+)(?P<house_number>No\\s+\\d+\\s?\\w?)$",
            # German format
            "^(?:\\s*)(?P<street>[\\w\\s\\.]+)(?:[,\\s]+)(?P<house_number>(-?\\d+\\s?\\w?)+)(?:\\s*)$",
            # French / us format
            "^(?P<house_number>\\d+)\\s*,?\\s*(?P<street>[\\w\\s]+)"
        ]
        for pattern in patterns:
            match = re.match(pattern, raw)
            if match is not None:
                street, house_number = self.get_street_and_house_number(match)
            if street is not None and house_number is not None:
                return self.to_dict(street.strip(), house_number.strip())
        # No street name or house number could be found
        return self.to_dict(None, None)

    def to_dict(self, street, house_number):
        return {
            "street": street,
            "housenumber": house_number
        }

    def get_street_and_house_number(self, match) -> "tuple[str,str]":
        match_dict = match.groupdict()
        street = None
        house_number = None
        if 'street' in match_dict:
            street = match_dict.get('street') or None
        if 'house_number' in match_dict:
            house_number = match_dict.get('house_number', None)
        return street, house_number

    def to_json(self, result: dict) -> str:
        return json.dumps(result, indent=None, sort_keys=False)
