"""
Самостоятельная работа
1. Создать файл hw_05.py
2. Записать все xpath-локаторы, для всех элементов на странице https://hyperskill.org/tracks
в формате кортежей
3. Обязательно проверить, что все локаторы валидные, т.е элемент по ним находится.
"""

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://hyperskill.org/courses")
time.sleep(5)
# Header
TEXT_LOGO = driver.find_element("xpath", "//div[contains(@class,'text-logo')]")
SVG_LOGO = driver.find_element("xpath", "(//div[@class='!relative'])[1]")
CATALOG = driver.find_element("xpath", "//li[contains(@class,'!relative')]")
PRICING = driver.find_element("xpath", "//li[@click-event-target='pricing']")
FOR_BUSINESS = driver.find_element("xpath", "//li[@click-event-target='join_as_organization']")
SIGN_IN = driver.find_element("xpath", "//button[contains(@class, 'btn-outline-light')]")
START_FOR_FREE = driver.find_element("xpath", "//button[contains(@class, 'btn-primary')]")
# Body
HEADER = driver.find_element("xpath", "//h1")
DESCRIPTION = driver.find_element("xpath", "//p[@class='!mb-6']")
ALL_COURSES = driver.find_element("xpath", "(//a[@click-event-target='category'])[1]")
print(TEXT_LOGO, SVG_LOGO, CATALOG, PRICING, FOR_BUSINESS,
      SIGN_IN, START_FOR_FREE, HEADER, DESCRIPTION, ALL_COURSES)
