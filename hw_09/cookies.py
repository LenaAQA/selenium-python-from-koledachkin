"""
Самостоятельная работа
Задание 1 (Установка и чтение куки)
  - Откройте любой сайт и добавьте куки с именем "username" и значением "user123".
  - Затем обновите страницу и убедитесь, что кука "username" была успешно установлена.
  - Получите и провалидируйте значение куки "username" и выведете его на экран.
Задание 2 (Удаление куков)
  - Откройте любой сайт и через Devtools выберете куку.
  - Удалите выбранную куку.
  - После удаления куки, обновите страницу и проверьте, что она отсутствует.
Задание 3 (Автоматизация корзины покупок)
  - Напишите сценарий, который использует Selenium WebDriver для автоматического добавления товаров в корзину,
в интернет-магазине, например Amazon.
  - После добавления товаров, сохраните состояние корзины, записав куки в переменную или файл.
  - Затем удалите все товары из корзины, очистив все куки и перезагрузив страницу.
  - Восстановите сессию путем подставления ранее сохраненных куков и перезагрузкой странцы после.
Заметки:
Используйте режим отключения WebDriver и User-agent
"""

import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/134.0.0.0 Safari/537.36")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

EXPECTED_COOKIE = {
    'domain': 'demoqa.com',
    'httpOnly': False,
    'name': 'username',
    'path': '/',
    'sameSite': 'Lax',
    'secure': True,
    'value': 'user123'
}


def scroll_into_view(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"});', element)
    return element


driver.get("https://demoqa.com/login")

# Test_1
driver.add_cookie({"name": "username", "value": "user123"})
driver.refresh()
my_cookie = driver.get_cookie("username")
assert my_cookie == EXPECTED_COOKIE
print(my_cookie)

# Test_2
print(driver.get_cookie("cto_bundle"))
driver.delete_cookie("cto_bundle")
driver.refresh()
delete_cookie = driver.get_cookie("cto_bundle")
print(delete_cookie)
assert delete_cookie is None

# Test_3
driver.get("https://www.citilink.ru/catalog/noutbuki/?ref=mainpage_popular")
ADD_PRODUCT = ("xpath", "//button[@data-meta-name='Snippet__cart-button']")
CART = ("xpath", "//a[@href='/order/']")
CART_ITEM = ("css selector", "[data-meta-name='CartProductCard']")

scroll_into_view(driver, ADD_PRODUCT)
wait.until(EC.visibility_of_element_located(ADD_PRODUCT)).click()
wait.until(EC.visibility_of_element_located(CART)).click()

os.makedirs(os.getcwd() + "/cookies", exist_ok=True)
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

driver.delete_all_cookies()
driver.refresh()

cookies = pickle.load(open(os.getcwd() + "/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
items = wait.until(EC.presence_of_all_elements_located(CART_ITEM))
assert len(items) > 0
