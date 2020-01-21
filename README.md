# worldguess
## Summary
This python package guess the country of a subject text, name or list based on places names frequencies.
It works in any languages/alphabet.
## Warning
Originally, this library was made to be used with a list of places extracted with an NER program such as *Spacy*.

*I heavely recommend using it that way.*

It is also possible to use it on a text, but the precision is not very good, as some words in a language correspond to a place in another language.

It is also still a work in progress. I did a version of this library in an old internship, to quickly identify and classify documents according to  countries, and thought it was a cool tool to share, so I remade it from scratch at home recently (with permission of my old boss).

It is an easy way to identify the source country of an news article for example, and automatically tag the country.

## Usage

*With a list:*
```python
wg = WorldGuesser()
text = ["London", "Manchester", "UK", "BRISTOL", "Scotland", "Berlin"]
result = wg.from_list(text)
self.assertEqual(result[0], "United Kingdom")
```

*With a name:*
```python
wg = WorldGuesser()
text = "санкт-петербург"
result = wg.from_place(text)
self.assertEqual(result[0], "Russia")
```

If no country is found, the first result in the list will be "Unknown"

## Data Sources
The date sources come from the GeoNames Database: https://www.geonames.org/
