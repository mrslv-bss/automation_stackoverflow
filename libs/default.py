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


def open_page_companies(get_driver):
    start(get_driver)
    click(get_driver, home_container_button)
    click(get_driver, companies_button)
    has_the_page_opened = get_driver.find_element(*home_container_elements_title).text
    assert has_the_page_opened == "Companies"  # opened


def open_page_tags(get_driver):
    start(get_driver)
    click(get_driver, home_container_button)
    click(get_driver, tags_button)
    has_the_page_opened = get_driver.find_element(*home_container_elements_title).text
    assert has_the_page_opened == "Tags"  # opened


def open_page_users(get_driver):
    start(get_driver)
    click(get_driver, home_container_button)
    click(get_driver, users_button)
    has_the_page_opened = get_driver.find_element(*home_container_elements_title).text
    assert has_the_page_opened == "Users"  # opened
