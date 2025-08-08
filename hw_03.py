"""
Самостоятельная работа:
Инициализировать драйвер (любой, попробуйте Firefox) p.s: не забудьте его установить.
Открыть любую страницу, например: vk.com.
Получить и вывести title в консоль.
Открыть любую другую страницу, например: ya.ru.
Получить и вывести title в консоль.
Вернуться назад и, используя assert, убедиться, что вы точно вернулись.
Сделать рефреш страницы.
Получить и вывести URL-адрес текущей страницы.
Вернуться "вперед" на страницу из пункта 4.
Убедиться, что URL-адрес изменился.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

YANDEX_URL = "https://yandex.ru"
GOOGLE_URL = "https://www.google.com/"

driver.get(YANDEX_URL)
title_yandex = driver.title
print(title_yandex)

driver.get(GOOGLE_URL)
title_google = driver.title
print(title_google)

driver.back()
current_url = driver.current_url
assert current_url == YANDEX_URL, f"Expected Yandex URL, got {current_url}"
assert driver.title == title_yandex, "The Yandex title is not correct"

driver.refresh()
current_url = driver.current_url
print(current_url)

driver.forward()
current_url = driver.current_url
assert current_url == GOOGLE_URL, f"Expected Google URL, got {current_url}"
assert driver.title == title_google, "The Google title is not correct"
