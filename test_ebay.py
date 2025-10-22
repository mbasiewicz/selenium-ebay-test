import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def test_search(selenium):
    selenium.get("https://www.ebay.com/")
    search = WebDriverWait(selenium, 60).until(
        lambda s: s.find_element(By.NAME, "_nkw")
    )
    search.send_keys("laptop" + Keys.ENTER)
    time.sleep(3)
    computers_element = selenium.find_element(
        By.LINK_TEXT, "Computers/Tablets & Networking"
    )
    laptop_element = selenium.find_element(By.LINK_TEXT, "Laptops & Netbooks")

    computers_position = computers_element.location["y"]
    laptop_position = laptop_element.location["y"]
    assert computers_position < laptop_position

    time.sleep(3)
    selenium.quit()
