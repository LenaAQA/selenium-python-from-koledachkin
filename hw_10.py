"""
Самостоятельная работа
Сайт для выполнения задания: https://demoqa.com/selectable
Открыть вкладку Grid
Кликнуть на пару любых элементов
Убедиться, что они выбраны
Кликнуть еще раз и убедиться, что теперь они не выбраны
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)


def scroll_into_view(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"});', element)
    return element


driver.get("https://demoqa.com/selectable")
GRID = ("xpath", "//a[@id='demo-tab-grid']")
ELEMENTS = ("xpath", "//div[@id='gridContainer']/div/li")

wait.until(EC.visibility_of_element_located(GRID)).click()
scroll_into_view(driver, ELEMENTS)
elements = wait.until(EC.visibility_of_all_elements_located(ELEMENTS))

for el in elements:
    el.click()
    attribute_class = el.get_attribute("class")
    assert "active" in attribute_class
    el.click()
    attribute_class = el.get_attribute("class")
    assert "active" not in attribute_class
