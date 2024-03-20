from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from vehicle_page import VehiclePage


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
    
    @property
    def vehicle_list(self):
        """Select the html table with the list of vehicles"""
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[5]/form/div[2]/div[4]/div/table/tbody/tr")))

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
                
    def loop_through_vehicle_list(self):
        """Go through each vehicle in the list to find the flag"""
        vehicle_page = VehiclePage(self.driver)
        self.waitout_loading_screen
        print('Checking each vehicle in the list')
        vehicles = []
        rows = self.vehicle_list

        # Initialize a variable to track the current row index
        current_row = 2
        print(f"Number of rows: {len(rows[2:])}") # Skip header and unlock row
        while current_row < len(rows):
            print(f"({current_row - 2}/{len(rows[2:])} Vehicles:)")
            rows[current_row].click()
            
            # Extract information from the new page (e.g., find the flag)
            self.waitout_loading_screen
            vehicle_page.click_note_tab()
            flag_info = vehicle_page.find_note_with_flag()
            vehicles.append(flag_info)
            
            vehicle_page.go_back_page_button.click()
            
            current_row += 1
            # Refresh the rows list (since the page changed)
            rows = self.vehicle_list

        return vehicles
