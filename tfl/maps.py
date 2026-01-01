from datetime import datetime
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


WEIGHT = 0.5

# Load existing data.
with open("./tfl/data/maps.json", "r") as f:
  data = json.load(f)

# Ask the user which network the line to be updated belongs to.
for i, network in enumerate(data.keys()):
  print(f"{i+1}: {network.title()}")
network = list(data.keys())[
  int(input(f"Please pick 1-{len(data)}: ")) - 1
]

# Ask the user which line to update.
for i, line in enumerate(data[network].keys()):
  print(f"{i+1}: {line.title()}")
line = list(data[network].keys())[
  int(input(f"Please pick 1-{len(data[network])}: ")) - 1
]

# Initialise the webdriver.
options = Options()
options.add_argument("--log-level=3") # Suppress deprecated endpoint warnings.
driver: WebDriver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/maps")
driver.find_element(
  By.CSS_SELECTOR,
  'button[aria-label="Reject all"]'
).click()
time.sleep(1)

for path, path_data in data[network][line]["paths"].items():
  is_new_path = False
  driver.get(path_data["url"])
  if not (
    "times" in path_data.keys() and
    isinstance(path_data["times"], list)
  ):
    data[network][line]["paths"][path]["times"] = []
    is_new_path = True
  else:
    print(f"Updating data for the {line.title()} line from" \
          f" {path_data["names"][0]} to {path_data["names"][-1]}...")
    input("Please check that the journey is correct" \
          "Please enter any key to continue: ")
    data[network][line]["paths"][path]["url"] = driver.current_url
  
  # Open all journey details.
  for element in driver.find_elements(
    By.CSS_SELECTOR,
    'button[aria-label="Toggle details"]'
  ):
    if element.is_displayed():
      element.click()
  time.sleep(1)

  # List the stations on the path.
  names = []
  for entry in driver.find_elements(
    By.CSS_SELECTOR,
    'span[id^=transit_group] h2'
  ):
    # Remove '.' from the name.
    station: str = re.sub(r"\.", "", entry.text)
    # Remove 'Station' from the name.
    station = re.sub(r" Station", r"", station)
    if len(station) > 0:
      names.append(station)

  # List the timestamps of each station.
  timestamps = []
  for entry in driver.find_elements(
    By.CSS_SELECTOR,
    'span[id^=transit_group] div:has(~ h2), span[id^=transit_group] > div > div:first-child'
  ):
    timestamp_str: str = re.sub(r"\u202f", "", entry.text)
    if len(timestamp_str) > 0:
      timestamp = datetime.strptime(timestamp_str, "%I:%M%p")
      timestamps.append(timestamp)
  
  assert len(names) == len(timestamps)
  assert len(names) > 0, "No stops found. Check that the url is correct."
  if is_new_path:
    data[network][line]["paths"][path]["names"] = names
  else:
    assert len(path_data["names"]) == len(names), "There are more stations than expected."

  # Calculate the travel time between neighbouring stations.
  for i in range(len(timestamps) - 1):
    travel_time: int = max((timestamps[i+1] - timestamps[i]).seconds//60, 1)
    if is_new_path:
      data[network][line]["paths"][path]["times"].append(travel_time)
    else:
      data[network][line]["paths"][path]["times"][i] = round(
        WEIGHT * travel_time + (1 - WEIGHT) * path_data["times"][i],
        3
      )

# List all the stations on the line.
if not (
  "names" in data[network][line].keys() and
  isinstance(data[network][line]["names"], list)
):
  data[network][line]["names"] = sorted(list(set(
    sum([path["names"] for path in data[network][line]["paths"].values()], [])
  )))

# Save the data.
with open("./tfl/data/maps.json", "w") as f:
  json.dump(data, f, indent=2)
print("The data has been saved!")
