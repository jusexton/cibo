import random
from dataclasses import dataclass


@dataclass
class Cuisine:
    name: str
    websites: dict[str, str]


CUISINES = [
    Cuisine(
        name="Mexican",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican/"
        },
    ),
    Cuisine(
        name="Italian",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/723/world-cuisine/european/italian/"
        },
    ),
    Cuisine(
        name="Chinese",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese/"
        },
    ),
    Cuisine(
        name="Indian",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/233/world-cuisine/asian/indian/"
        },
    ),
    Cuisine(
        name="German",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/722/world-cuisine/european/german/"
        },
    ),
    Cuisine(
        name="Japanese",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/699/world-cuisine/asian/japanese/"
        },
    ),
    Cuisine(
        name="Thai",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/702/world-cuisine/asian/thai/"
        },
    ),
    Cuisine(
        name="Vietnamese",
        websites={
            "allrecipes.com": "https://www.allrecipes.com/recipes/703/world-cuisine/asian/vietnamese/"
        },
    ),
]


def print_cuisine(cuisine: Cuisine):
    locations = "\n".join(
        f"{name} :: {url}" for (name, url) in cuisine.websites.items()
    )
    print(f"Cuisine: {cuisine.name}\n" + locations)


def random_cuisine() -> Cuisine:
    return random.choice(CUISINES)
