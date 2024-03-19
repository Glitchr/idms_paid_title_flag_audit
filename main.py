from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config

from login_page import LoginPage


if __name__ == '__main__':
    password = config('PASSWORD')
    url = config('URL')

    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    login_page = LoginPage(driver)
    login_page.login(password)
