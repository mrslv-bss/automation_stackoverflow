from testdata.links import url
from selenium.webdriver.common.by import By

companies_button = (By.ID, "nav-companies")
tags_button = (By.ID, "nav-tags")
users_button = (By.ID, "nav-users")
home_container_button = (By.XPATH, "//a[contains(@class, 's-topbar--menu-btn')]")
home_container_elements_title = (By.XPATH, "//h1[contains(@class, 'fs-headline1')]")


def start(get_driver):
    get_driver.get(url)
    get_driver.maximize_window()
    get_driver.implicitly_wait(15)


def click(get_driver, element):
    get_driver.find_element(*element).click()


def send_keys(get_driver, element, text):
    get_driver.find_element(*element).send_keys(text)


def open_public_page(get_driver, oneofthree):
    if oneofthree == "Companies":
        page_button = companies_button
    elif oneofthree == "Tags":
        page_button = tags_button
    elif oneofthree == "Users":
        page_button = users_button
    else:
        return None
    start(get_driver)
    click(get_driver, home_container_button)
    click(get_driver, page_button)
    page_validation = get_driver.find_element(*home_container_elements_title).text
    assert page_validation == oneofthree
