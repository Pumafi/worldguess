import read_data
import re

COUNTRY_WEIGH = 3.0
NEIGHBOURS_WEIGH = 0.75


class WorldGuesser:

    def __init__(self):
        self.iso_to_country_dict, self.places_to_iso_dict = read_data.read_country_data()

    def create_proba_dict(self) -> dict:
        proba_dict = {}
        for key, value in self.iso_to_country_dict.items():
            proba_dict[value['country']] = 0.0
        return proba_dict

    @staticmethod
    def find_all_probables_country(proba_dict: dict) -> list:
        probables_countries = []
        for key, value in proba_dict.items():
            if value > 2.0:
                probables_countries.append(key)
        if len(probables_countries) == 0:
            probables_countries.append("Unknown")
        return probables_countries

    @staticmethod
    def find_n_most_probables_country(proba_dict: dict, n: int = 3) -> list:
        probables_countries = []
        for i in range(n):
            max_key = max(proba_dict, key=lambda key: proba_dict[key])
            if proba_dict[max_key] != 0:
                probables_countries.append(max_key)
                proba_dict.pop(max_key)
            else:
                break
        if len(probables_countries) == 0:
            probables_countries.append("Unknown")
        return probables_countries

    def iso_from_place(self, place: str) -> list:
        if not place:
            return []
        place_lower = place.casefold()
        if place_lower in self.places_to_iso_dict:
            return self.places_to_iso_dict[place_lower]['ISO']
        return []

    @staticmethod
    def augment_proba_from_lists(proba_dict: dict, countries: list, neighbours: list) -> None:
        for country in countries:
            if country in proba_dict:
                proba_dict[country] += 1.0 * COUNTRY_WEIGH
        for country in neighbours:
            if country in proba_dict:
                proba_dict[country] += 1.0 * NEIGHBOURS_WEIGH

    def countries_from_iso(self, iso_list: list) -> tuple:
        countries = []
        neighbours = []
        for iso in iso_list:
            if iso in self.iso_to_country_dict:
                countries.append(self.iso_to_country_dict[iso]["country"])
                neighbours += self.iso_to_country_dict[iso]["neighbours"]
        return countries, neighbours

    def augment_proba_from_place(self, place: str, proba_dict: dict) -> None:
        iso_list = self.iso_from_place(place)
        countries, neighbours = self.countries_from_iso(iso_list)
        self.augment_proba_from_lists(proba_dict, countries, neighbours)

    def from_list(self, places_list: list) -> list:
        if not places_list:
            return ["Unknown", ]
        proba_dict = self.create_proba_dict()
        for place in places_list:
            self.augment_proba_from_place(place, proba_dict)
        probables_countries = self.find_n_most_probables_country(proba_dict)
        return probables_countries

    def from_place(self, place: str) -> list:
        if not place:
            return ["Unknown", ]
        proba_dict = self.create_proba_dict()
        self.augment_proba_from_place(place, proba_dict)
        probables_countries = self.find_n_most_probables_country(proba_dict)
        return probables_countries

    def from_text(self, text: str) -> list:
        if not text:
            return ["Unknown", ]
        text_new = re.findall(r"\w+", text)
        return self.from_list(text_new)
