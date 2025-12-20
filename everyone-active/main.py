import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import TypedDict


URL = "https://book.everyoneactive.com/Connect/memberHomePage.aspx"

class Centre(TypedDict):
  name: str
  badminton: int

# Unused function for searching by date.
def search_date(driver: WebDriver) -> None:
  # Prompt for a date.
  date: str = ""
  while len(date) != 10:
    date: str = input("Enter date to check availability (YYYY-MM-DD): ")
  # Enter the date into search box.
  driver.find_element(
    By.ID,
    "ctl00_MainContent__advanceSearchUserControl_specificDate"
  ).send_keys(f"{date[0:4]}\t{date[4:]}") # The year field has a length of 6.

  # Click the search button.
  driver.find_element(
    By.ID,
    "ctl00_MainContent__advanceSearchUserControl__lnkBtnSpecifyDateSearch"
  ).click()

  # Wait for the search to finish.
  WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element(
      (
        By.ID, 
        "ctl00_MainContent__advanceSearchUserControl__lnkBtnSpecifyDateSearch"
      ), "Search"
    )
  )

# Unusued function for listing spaces in activities.
def list_spaces(driver: WebDriver) -> list[bool]:
  spaces: list[WebElement] = driver.find_elements(
    By.CSS_SELECTOR,
    '#collapseActivities .col-sm-3'
  )
  return [int(space.text.lower().find('space') > -1 for space in spaces)]

if __name__ == "__main__":
  # Setup driver.
  options = Options()
  options.add_argument("--log-level=3") # Suppress deprecated endpoint warnings.
  driver: WebDriver = webdriver.Chrome(options=options)
  driver.set_window_size(1000, 250)
  driver.get(URL)

  # While still on the login page.
  at_login: bool = True
  while at_login:
    # Prompt for username and password.
    username: str = input("Enter your username for Everyone Active: ")
    password: str = input("Enter your password for Everyone Active: ")
    # Enter the username into the login page.
    user_field: WebElement = driver.find_element(
      By.ID,
      "ctl00_MainContent_InputLogin"
    )
    user_field.clear() # The field must always be cleared on additional attempts.
    user_field.send_keys(username)
    # Enter the password into the login page.
    driver.find_element(
      By.ID,
      "ctl00_MainContent_InputPassword"
    ).send_keys(password)
    # Click the submit button.
    driver.find_element(By.ID, "ctl00_MainContent_btnLogin").click()
    try:
      # Wait for the page to process the login details.
      WebDriverWait(driver, 3).until(EC.url_to_be(URL))
    except TimeoutException:
      print("Login failed, please try again.")
    else:
      at_login = False

  print("Login successful!")
  
  # List the centres on the booking page.
  centres: dict[str, Centre] = {}
  for centre in driver.find_elements(By.CSS_SELECTOR, '#searchPanel option'):
    centre_id: str = centre.get_attribute('value')
    if centre_id == "" or int(centre_id) < 0:
      continue
    centres[centre_id] = {
      "name": centre.text,
      "badminton": 0
    }

  # Check whether each centre has badminton courts.
  for centre_id in centres.keys(): 
    # Select the centre.
    driver.find_element(By.CSS_SELECTOR, '#searchPanel select').click()
    driver.find_element(
      By.CSS_SELECTOR,
      f'#searchPanel option[value="{centre_id}"]'
    ).click()
    # Wait until the page has loaded.
    WebDriverWait(driver, 5).until(
      EC.text_to_be_present_in_element((
        By.ID, 
        "ctl00_MainContent__advanceSearchUserControl__lnkBtnToday"
      ), "Today")
    )
    # List the activities at the centre.
    activities: list[WebElement] = driver.find_elements(
      By.CSS_SELECTOR,
      '#collapseActivities .col-sm-9'
    )
    # Note if badminton is provided at the centre.
    for activity in activities:
      if activity.text.lower().find('badminton') > -1:
        centres[centre_id]["badminton"] = 1
        break
    
    print(f"Checked centre: {centres[centre_id]["name"]}")

  # Save the centres to a CSV.
  pd.DataFrame.from_dict(
    centres,
    orient="index"
  ).to_csv("./everyone-active/EveryoneActive.csv", index_label="id")
  print("Saved data to EveryoneActive.csv!")
