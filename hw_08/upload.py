"""
Самостоятельная работа
Задание 1. Загрузить любой файл в 'Choose File'.
Страница для выполнения задания: https://demoqa.com/upload-download
"""

import os
import time
import shutil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from course_selenium.lesson10.data import Demo

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

driver.get("https://demoqa.com/upload-download")
upload_file_field = driver.find_element("xpath", "//input[@id='uploadFile']")
upload_file_field.send_keys(os.path.join(os.getcwd(), "upload//picture.png"))
file_upload = driver.find_element("xpath", "//p[@id='uploadedFilePath']").text

assert Demo.EXPECTED_NAME_UPLOAD_FILE in file_upload

download_file_button = driver.find_element("xpath", "//a[@id='downloadButton']")
download_file_button.click()
time.sleep(2)
downloaded_files = os.listdir(DOWNLOAD_FOLDER)
downloaded_file = downloaded_files[0]

assert downloaded_file == Demo.EXPECTED_NAME_DOWNLOAD_FILE
