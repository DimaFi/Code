import csv
import json
from collections import defaultdict

data = [
    {
        "name": "Orion",
        "latin_name": "Orion",
        "abbreviation": "Ori",
        "area": 594,
        "brightest_stars": [
            {"name": "Betelgeuse", "magnitude": 0.5},
            {"name": "Rigel", "magnitude": 0.12},
            {"name": "Bellatrix", "magnitude": 1.64}
        ],
        "neighboring_constellations": ["Gemini", "Taurus", "Lepus"]
    },
    {
        "name": "Ursa Major",
        "latin_name": "Ursa Major",
        "abbreviation": "UMa",
        "area": 1280,
        "brightest_stars": [
            {"name": "Alioth", "magnitude": 1.76},
            {"name": "Dubhe", "magnitude": 1.79},
            {"name": "Merak", "magnitude": 2.34}
        ],
        "neighboring_constellations": ["Lynx", "Draco", "Ursa Minor"]
    }
]

with open('constellations.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

with open('constellations.json', 'r') as json_file:
    constellations = json.load(json_file)

# переход в csv
stars_data = []
for constellation in constellations:
    for star in constellation["brightest_stars"]:
        stars_data.append({
            "star_name": star["name"],
            "magnitude": star["magnitude"],
            "constellation_name": constellation["name"],
            "latin_name": constellation["latin_name"],
            "abbreviation": constellation["abbreviation"],
            "area": constellation["area"]
        })


for constellation in data:
    constellation["brightest_stars"].sort(key=lambda x: x["magnitude"])


with open('sorted_constellations.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


with open('stars.csv', 'w', newline='') as csv_file:
    fieldnames = ["star_name", "magnitude", "constellation_name", "latin_name", "abbreviation", "area"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    stars_data.sort(key=lambda x: x["magnitude"])  # по яркости
    for row in stars_data:
        writer.writerow(row)

with open('stars.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    reconstructed_data = defaultdict(lambda: {
        "brightest_stars": [],
        "neighboring_constellations": []
    })

    for row in reader:
        constellation_name = row["constellation_name"]
        reconstructed_data[constellation_name]["latin_name"] = row["latin_name"]
        reconstructed_data[constellation_name]["abbreviation"] = row["abbreviation"]
        reconstructed_data[constellation_name]["area"] = int(row["area"])
        reconstructed_data[constellation_name]["brightest_stars"].append({
            "name": row["star_name"],
            "magnitude": float(row["magnitude"])
        })

reconstructed_list = [{"name": name, **data} for name, data in reconstructed_data.items()]

with open('reconstructed_constellations.json', 'w') as json_file:
    json.dump(reconstructed_list, json_file, indent=4)
