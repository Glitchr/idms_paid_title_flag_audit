from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class VehiclePage:

    def __init__(self, driver):
        """Initialize the selenium driver"""
        self.driver = driver

    @property
    def go_back_page_button(self):
        """Select the back-page button to return to the inventory list"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pageLevelNavigationBackButton")))
    
    @property
    def get_vin(self):
        """Get the vehicle's VIN from the details section"""
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[8]/div[1]/div/div[1]/div/div/div/div/div[1]/div[7]/div[1]/span[2]")))

    @property
    def get_stock_number(self):
        """Get the vehicle's stock number from the details section"""
        return WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[8]/div[1]/div/div[1]/div/div/div/div/div[1]/div[3]/span[2]")))

    @property
    def open_more_details(self):
        """Opens the details section"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "showMoreAnchor")))

    @property
    def notes_tab(self):
        """Select the Notes tab button"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "Notes")))

    @property
    def notes_list(self):
        """Select the html table with the list of notes"""
        return WebDriverWait(self.driver, 60).until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[8]/div[2]/div[14]/div/div[4]/div[2]/div")))
        
    @property
    def next_note_page(self):
        """Select the next page button on the note element"""
        return WebDriverWait(self.driver, 60).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "goForwardOnePage")))

    @property
    def waitout_loading_screen(self):
        """Wait for the loading screen to disappear"""
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "spinnerContent")))  
    
    def get_current_note_page(self):
        """Get the current notes page number"""
        page_number = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "curpagenumber")))
        
        return int(page_number)

    def get_total_note_pages(self):
        """Get the total number of pages from the paging wrapper"""
        paging_wrapper = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pagingWrapper")))
        
        return int(paging_wrapper.get_attribute('data-totalpages'))

    def click_note_tab(self):
        self.notes_tab.click()

    def navigate_to_next_note_page(self):
        """Click the next page button on the notes element"""
        self.next_note_page.click()

    def find_note_with_flag(self):
        """Find the note with the flag name in its description"""
        self.waitout_loading_screen
        rows = self.notes_list

        current_row = 1
        while current_row < len(rows):
            if "PAID TITLE ON TRANSIT" in rows[current_row].find_element(By.CLASS_NAME, "descriptionText").text:
                vin = self.get_vin
                date = rows[current_row].find_element(By.CLASS_NAME, "noteDate")
                date_text = date.text
                extracted_date = datetime.strptime(date_text, "%Y-%m-%d")
                days_difference = (datetime.now() - extracted_date).days

                if days_difference > 10:
                    print(f"- {vin} / PAID flag was set more than 10 days ago.")
                else:
                    print(f"- {vin} / PAID flag set within 10 days.")

            current_row += 1  # Increment the row count in every iteration

            # Check if there's a next page
            total_pages = self.get_total_note_pages()
            current_page = self.get_current_note_page()
            if current_page < total_pages and current_row == len(rows):
                self.navigate_to_next_note_page()
                rows = self.notes_list.find_elements(By.CLASS_NAME, "oneChild")  # Refresh rows
                current_row = 1  # Reset the row count for the new page

        return vin
     