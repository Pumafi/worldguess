import pandas as pd


def get_and_clean_csv(path: str) -> dict:
    df = pd.read_csv(path, sep=';', keep_default_na=False)

    df.fillna("NOVALUE")

    if "neighbours" in df:
        df.set_index('ISO', inplace=True)
        df["neighbours"] = df["neighbours"].str.split(",")

    elif "ISO" in df:
        df.set_index('name', inplace=True)
        df["ISO"] = df["ISO"].str.split(",")

    else:
        raise ValueError

    return df.to_dict(orient="index")


def read_country_data() -> tuple:
    path_iso_to_country = "../data/iso_to_country.csv"
    path_places_to_iso = "../data/places_to_iso.csv"
    dict_iso_to_country = get_and_clean_csv(path_iso_to_country)
    dict_place_to_iso = get_and_clean_csv(path_places_to_iso)
    return dict_iso_to_country, dict_place_to_iso
