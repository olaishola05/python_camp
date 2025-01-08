travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 5,
    },
]

country = input("Which country do you want to add to travel logs\n: ").lower()
cities_visited = input(
    "List of cities visited seperated by space. E.g Lisbon Berling\n: "
).split(" ")
total_visits = int(input(f"How many times have you visited {country}: "))


def add_new_country(name, number_of_visits, cities):
    new_country = {}

    new_country["country"] = name
    new_country["cities_visited"] = cities
    new_country["total visit"] = number_of_visits

    travel_log.append(new_country)

    print(f"You've  visited {name} {number_of_visits} times")
    print(f"{", ".join(cities)}")


add_new_country(name=country, number_of_visits=total_visits, cities=cities_visited)
print(travel_log)
