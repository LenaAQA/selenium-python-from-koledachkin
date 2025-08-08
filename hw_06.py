"""
Самостоятельная работа
Задание 1:
Заполнить все текстовые поля данными (почистить поля перед заполнением).
Проверить, что данные действительно введены, используя get_attribute() и assert.
Страница для выполнения задания: https://demoqa.com/text-box
Задание 2:
Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
После каждого клика возвращаться на стартовую страницу.
Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

FULL_NAME = "Elena"
EMAIL = "test@email.com"
CURRENT_ADDRESS = "123 Maple Street, Apt. 4B, Springfield, IL 62704"
PERMANENT_ADDRESS = "TechSolutions Inc. 500 Silicon Avenue, Suite 200, San Francisco, CA 94105"

FULL_NAME_INPUT = (By.ID, "userName")
EMAIL_INPUT = (By.ID, "userEmail")
CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
STATUS_CODE_LINKS = (By.XPATH, "//a[contains(@href, 'status_codes')]")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

full_name = driver.find_element(*FULL_NAME_INPUT)
full_name.clear()
full_name.send_keys(FULL_NAME)
assert full_name.get_attribute("value") == FULL_NAME, "Full Name не совпадает"

email = driver.find_element(*EMAIL_INPUT)
email.clear()
email.send_keys(EMAIL)
assert email.get_attribute("value") == EMAIL, "Email не совпадает"

current_address = driver.find_element(*CURRENT_ADDRESS_INPUT)
current_address.clear()
current_address.send_keys(CURRENT_ADDRESS)
assert current_address.get_attribute("value") == CURRENT_ADDRESS, "Current Address не совпадает"

permanent_address = driver.find_element(*PERMANENT_ADDRESS_INPUT)
permanent_address.clear()
permanent_address.send_keys(PERMANENT_ADDRESS)
assert permanent_address.get_attribute("value") == PERMANENT_ADDRESS, "Permanent Address не совпадает"

driver.get("https://the-internet.herokuapp.com/status_codes")

status_codes = driver.find_elements(*STATUS_CODE_LINKS)
for i in range(len(status_codes)):
    status_codes = driver.find_elements(*STATUS_CODE_LINKS)
    status_codes[i].click()
    driver.back()
