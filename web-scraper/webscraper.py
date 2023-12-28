from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://books.toscrape.com/")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
elem = driver.find_element(
    By.CSS_SELECTOR, "#default > div.container-fluid.page > div > div > div > section > div:nth-child(2) > ol > li:nth-child(1) > article > h3 > a")
elem.click()
# elem.clear()
# elem.send_keys("lolcatz.dk")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
