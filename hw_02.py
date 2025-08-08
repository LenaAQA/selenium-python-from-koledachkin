"""
Самостоятельная работа:
Создать новый проект в любой IDE.
Создать виртуальное окружение и активировать.
Установить необходимые для работы библиотеки.
Создать python-файл с любым названием.
Написать инициализацию любого драйвера.
Запустить, чтобы все работало.
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.quit()
