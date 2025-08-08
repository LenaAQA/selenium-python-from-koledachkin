""""
Самостоятельная работа
Сайт для выполнения работы: https://omayo.blogspot.com/
Советы:
Выставите явное ожидание на 30 секунд
Для выполнения задания 4, провалитесь в библиотеку EC и поищите метод, погуглите и т.д
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from course_selenium.lesson_11.data import Wait


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)


def scroll_into_view(driver, locator):
    element = driver.find_element(*locator)
    driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"});', element)
    return element


TEXT_DISAPPEAR = ("xpath", "//div[@id='deletesuccess']")
DISAPPEAR_BUTTON = ("xpath", "//input[@id='alert2']")
TEXT_APPEAR = ("xpath", "//div[@id='delayedText']")
ENABLE_BUTTON = ("xpath", "//input[@id='timerButton']")
DISABLE_BUTTON = ("xpath", "//button[@id='myBtn']")
TRY_IT_BUTTON = ("xpath", "//button[@onclick='setTimeout(myFunctionABC,3000)']")


driver.get("https://omayo.blogspot.com/")


# Test_1
scroll_into_view(driver, TEXT_APPEAR)
assert wait.until(EC.text_to_be_present_in_element(TEXT_APPEAR, Wait.TEXT_APPEAR))

# Test_2
scroll_into_view(driver, TEXT_DISAPPEAR)

assert wait.until(EC.invisibility_of_element_located(TEXT_DISAPPEAR))


# Test_3
wait.until(EC.element_to_be_clickable(DISAPPEAR_BUTTON)).click()
alert = wait.until(EC.alert_is_present())

assert alert.text == Wait.ALERT
alert.accept()


# Test_4
scroll_into_view(driver, ENABLE_BUTTON)
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
assert wait.until(EC.alert_is_present())
alert.accept()

# Test_5
scroll_into_view(driver, TRY_IT_BUTTON)
wait.until(EC.element_to_be_clickable(TRY_IT_BUTTON)).click()

assert wait.until(EC.element_attribute_to_include(DISABLE_BUTTON, "disabled"))
