import pymupdf
import json


doc: pymupdf.Document = pymupdf.open("./tfl/station-abbreviations.pdf")
stations = []
networks = {
  "underground": {
    "codes": [],
    "names": []
  },
  "overground": {
    "codes": [],
    "names": []
  },
  "dlr": {
    "codes": [],
    "names": []
  },
  "tramlink": {
    "codes": [],
    "names": []
  }
}
ignore_next: bool = False

for page in doc[:-2]:
  tbl: pymupdf.table.Table = page.find_tables(strategy="lines_strict")[0]
  for row in tbl.extract()[1:]:    
    # Edit station names to match the naming conventions in Google Maps.
    name: str = row[0].replace(
      "\n", " "
    ).replace(
      ".", ""
    ).replace(
      "By", "by"
    ).replace(
      "Heathrow Airport Terminals 1,", "Heathrow Terminals"
    )
    # Ignore repeated entries.
    if ignore_next:
        ignore_next = False
        continue
    elif name[:12] == "Edgware Road":
        name = "Edgware Road"
        ignore_next = True
    elif name[:11] == "Hammersmith":
        name = "Hammersmith"
        ignore_next = True
    elif name[:10] == "Paddington":
        name = "Paddington"
        ignore_next = True
    # Add the station to the networks it is a part of.
    if row[1] != "":
        networks["overground"]["codes"].append(row[1])
        networks["overground"]["names"].append(name)
    if row[2] != "":
        networks["tramlink"]["codes"].append(row[2])
        networks["tramlink"]["names"].append(name)
    if row[3] != "":
        networks["dlr"]["codes"].append(row[3])
        networks["dlr"]["names"].append(name)
    if row[4] != "":
        networks["underground"]["codes"].append(row[4])
        networks["underground"]["names"].append(name)
    # Add the station to stations.
    stations.append({
        "name": name,
        "overground": row[1],
        "tramlink": row[2],
        "dlr": row[3],
        "underground": row[4]
    })

# Save the data.
with open("./tfl/data/networks.json", "w") as file:
  file.write(json.dumps(networks, indent=2))
with open("./tfl/data/stations.json", "w") as file:
  file.write(json.dumps(stations, indent=2))
