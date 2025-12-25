import pymupdf
import json


doc: pymupdf.Document = pymupdf.open("station-abbreviations.pdf")
stations = []
ignore_next: bool = False

for page in doc[:-2]:
  tbl: pymupdf.table.Table = page.find_tables(strategy="lines_strict")[0]
  for row in tbl.extract()[1:]:    
    # Edit station names.
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
    stations.append({
        "name": name,
        "overground": row[1],
        "tramlink": row[2],
        "dlr": row[3],
        "underground": row[4]
    })
      
with open("data/codes.json", "w") as file:
  file.write(json.dumps(stations, indent=4))
