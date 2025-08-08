"""
Самостоятельная работа
На странице https://testautomationpractice.blogspot.com/:
Найти иконку Wikipedia по имени класса.
Найти поле ввода Wikipedia по id.
Найти кнопку поиска Wikipedia по классу.
Найти любой другой элемент на странице по тегу.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://testautomationpractice.blogspot.com/")

wait = WebDriverWait(driver, 10)

WIKIPEDIA_ICON = (By.CLASS_NAME, "wikipedia-icon")
WIKIPEDIA_INPUT = (By.ID, "Wikipedia1_wikipedia-search-input")
WIKIPEDIA_BUTTON = (By.CLASS_NAME, "wikipedia-search-button")
ANY_ELEMENT = (By.TAG_NAME, "h1")

wikipedia_icon = wait.until(EC.visibility_of_element_located(WIKIPEDIA_ICON))
assert wikipedia_icon.is_displayed()

wikipedia_search = wait.until(EC.visibility_of_element_located(WIKIPEDIA_INPUT))
assert wikipedia_search.is_displayed()

wikipedia_search_button = wait.until(EC.visibility_of_element_located(WIKIPEDIA_BUTTON))
assert wikipedia_search_button.is_displayed()

h1 = wait.until(EC.visibility_of_element_located(ANY_ELEMENT))
assert h1.is_displayed()
