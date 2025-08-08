"""
Самостоятельная работа
1. Открыть 3 вкладки
2. Во вкладках перейти на страницы ниже страницы:
Вкладка 1 - https://hyperskill.org/login
Вкладка 2 - https://www.avito.ru/
Вкладка 3 - https://www.ozon.ru/
Так же можете открывать и свои сайты, выше лишь вариант реализации)
3. Вывести в терминал title каждой страницы
4. Кликнуть на любую кнопку или ссылку на каждой странице
Важно:
Сначала нужно открыть все 3 вкладки
Потом получить все title страниц
Потом кликнуть на любой элемент в каждой вкладке
Вариант, когда открыл вкладку и получил title и кликнул, потом открыл новую вкладку и получил title и кликнул,
не подойдет. Важно походить по вкладкам.
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36")


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://hyperskill.org/login")


driver.switch_to.new_window("window")
driver.get("https://demoqa.com/browser-windows")


driver.switch_to.new_window("tab")
driver.get("https://the-internet.herokuapp.com/redirector")


tabs = driver.window_handles
for el in tabs:
    old_window = driver.current_window_handle
    driver.switch_to.window(el)
    print(f"Title: {driver.title}")
    assert driver.current_window_handle != old_window

HYPERSKILL_LOGO = ("xpath", "//div[contains(@class, 'text-logo')]")
DEMO_NEW_TAB = ("xpath", "//button[@id='tabButton']")
HERO_LINK = ("xpath", "//a[@id='redirect']")

old_window = driver.current_window_handle
driver.switch_to.window(tabs[0])
driver.find_element(*HYPERSKILL_LOGO).click()
assert driver.current_window_handle != old_window

old_window = driver.current_window_handle
driver.switch_to.window(tabs[1])
driver.find_element(*DEMO_NEW_TAB).click()
assert driver.current_window_handle != old_window

old_window = driver.current_window_handle
driver.switch_to.window(tabs[2])
driver.find_element(*HERO_LINK).click()
assert driver.current_window_handle != old_window
