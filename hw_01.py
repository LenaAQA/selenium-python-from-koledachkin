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
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
