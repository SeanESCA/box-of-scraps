import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


# Initialise the webdriver and open the Wikipedia page.
driver: WebDriver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_London_Underground_stations")
# List the names of underground stations in the data table.
names: list[str] = [name.text for name in driver.find_elements(
  By.CSS_SELECTOR,
  ".wikitable tbody tr th:first-child > a"
)]
# List the area each station is located in.
areas: list[str] = [area.text for area in driver.find_elements(
  By.CSS_SELECTOR,
  ".wikitable tbody tr td:last-child > a"
)]
# List the lines each station is on.
list_lines = lambda elem: re.sub(r"\[.\]", "", elem.text).split("\n")
lines: list[list[str]] = [list_lines(elem) for elem in driver.find_elements(
  By.CSS_SELECTOR,
  ".wikitable tbody tr td:nth-child(3)"
)]
# Ensure that all lists have the same length.
assert len(names) == len(lines)
assert len(names) == len(areas)
# Combine the data for repeated stations.
i = 0
while i < len(names) - 1:
  if names[i] == names[i+1]:
    names.pop(i)
    lines[i] = lines[i] + lines[i+1]
    areas.pop(i)
  i += 1
# Save the station data to a JSON file.
with open("data/stations1.json", "w") as file:
  file.write(json.dumps({
    "names": names,
    "lines": lines,
    "areas": areas
  }, indent=4))
