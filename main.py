from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config

from login_page import LoginPage
from inventory_page import InventoryPage


if __name__ == '__main__':
    password = config('PASSWORD')
    url = config('URL_LINK')

    options = Options()
    # options.add_argument("--headless=new")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get(url)

    login_page = LoginPage(driver)
    login_page.login(password)

    inventory_page = InventoryPage(driver)
    inventory_page.click_inventory_button()
    inventory_page.change_status()
    inventory_page.click_open_filters()
    inventory_page.change_flag_filter()
    inventory_page.click_search_button()

    vehicle_list = inventory_page.loop_through_vehicle_list()

    print('Vehicles with more than 10 days past since PAID flag was set')
    for vehicle in vehicle_list:
        print(vehicle)

    print('Script finished')
    driver.quit()
