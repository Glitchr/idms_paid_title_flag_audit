from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class InventoryPage:

    def __init__(self, driver):
        """Initialize the selenium driver"""
        self.driver = driver

    @property
    def inventory_button(self):
        """Select the homepage's button to go to the inventory"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[4]/ul/li[2]/a")))
    
    @property
    def status_dropdown(self):
        """Select the Status dropdown from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "StatusDisplay")))

    @property
    def open_filters(self):
        """Show the search filters from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "showMoreLessMessageText")))

    @property
    def flags_dropdown(self):
        """Select the Flags dropdown from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "FlagsDisplay")))
    
    @property
    def get_search_input(self):
        """Select the search input field from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[5]/form/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/input")))

    @property
    def search_button(self):
        """Select the search button"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div[4]/div[2]/button")))

    @property
    def waitout_loading_screen(self):
        """Wait for the loading screen to disappear"""
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "spinnerContent")))

    def click_inventory_button(self):
        """Click the selected inventory button to go to the inventory"""
        print('Navigate to the inventory')
        self.inventory_button.click()
    
    def change_status(self):
        """Change the value from Available to None from the status dropdown"""
        print('Changing the status from available to all')
        self.status_dropdown.click()
        status0 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Status0")))
        status0.click()
    
    def click_open_filters(self):
        """Click the button to open show the search filters"""
        print('Adding the search filters')
        self.open_filters.click()
    
    def change_flag_filter(self):
        """Select the PAID TITLE ON TRANSIT flag from the flags dropdown"""
        print('-Select PAID TITLE ON TRANSIT flag')
        self.flags_dropdown.click()
        flags225 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Flags225")))
        flags225.click()
    
    def click_search_button(self):
        """Click the search button to pull the filtered vehicles"""
        print('Searching filtered vehicles...')
        self.search_button.click()
                