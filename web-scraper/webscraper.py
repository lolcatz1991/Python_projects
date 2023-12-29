from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()


element_classes = {
    "name": "h3",
    "prize": "price_color"
}


class Book():
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize


books = []

driver.get("https://books.toscrape.com/")

nrOfBooksOnPage = driver.find_elements(By.TAG_NAME, element_classes["name"])


for book in nrOfBooksOnPage:
    book_name = driver.find_element(By.TAG_NAME, element_classes["name"]).text
    book_prize = driver.find_element(
        By.CLASS_NAME, element_classes['prize']).text
    full_book = Book(book_name, book_prize)
    books.append(full_book)
driver.close()

print(
    f"The first book title is {books[0].name} and it costs {books[0].prize}. ")
