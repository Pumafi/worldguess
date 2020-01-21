# worldguess
## Summary
This python package guess the country of a subject text, name or list based on places names frequencies.
It works in any languages/alphabet.

## Warning
Originally, this library was made to be used with a list of places extracted with an NER program such as *Spacy*.

*I heavely recommend using it that way.*

It is also possible to use it on a text, but the precision is not very good, as some words in a language correspond to a place in another language.

It is also still a work in progress. I did this in my internship, to quickly identify and classify documents according to  countries.

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
