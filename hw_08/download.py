"""
Самостоятельная работа
Задание 2. С помощью цикла for скачать все файлы в папку lesson_6/downloads.
Страница для выполнения задания: http://the-internet.herokuapp.com/download
"""

import os
import time
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from course_selenium.lesson10.data import Downloads


DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")

shutil.rmtree(DOWNLOAD_FOLDER, ignore_errors=True)
os.makedirs(DOWNLOAD_FOLDER)

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
preferences = {
    "download.default_directory": DOWNLOAD_FOLDER,
    "safebrowsing.enabled": True,
    "safebrowsing.disable_download_protection": True
}
options.add_experimental_option("prefs", preferences)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")
elements = driver.find_elements("xpath", "//div[contains(@class, 'example')]//a")

for el in elements:
    el.click()

time.sleep(10)
downloaded_files = sorted(os.listdir(DOWNLOAD_FOLDER))
expected_files = sorted(Downloads.EXPECTED_NAMES)

assert len(downloaded_files) == len(expected_files)
assert downloaded_files == expected_files
