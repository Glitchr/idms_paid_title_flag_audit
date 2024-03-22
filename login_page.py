from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        """Initialize the selenium driver"""
        self.driver = driver

    @property
    def password_field(self):
        """Select the input element from the page"""
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password")))

    @property
    def next_button(self):
        """Select the button from the page"""
        return self.driver.find_element(By.ID, "next")

    @property
    def send_2fa_button(self):
        """Select the send code button from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_send_code")))

    @property
    def verification_code_field(self):
        """Select the input element from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "verificationCode")))

    @property
    def verify_2fa_button(self):
        """Select the verify 2FA button from the page"""
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.ID, "phoneVerificationControl-readOnly_but_verify_code")))

    def enter_password(self, password):
        """Send the password to the input field"""
        self.password_field.send_keys(password)

    def click_next(self):
        """Click the next button"""
        self.next_button.click()

    def send_2fa_code(self):
        """Click the send 2FA button"""
        self.send_2fa_button.click()

    def enter_verification_code(self, code):
        """Send the 2FA code to the input field"""
        self.verification_code_field.clear()
        self.verification_code_field.send_keys(code)

    def verify_2fa_code(self):
        """Click the verify 2FA button"""
        self.verify_2fa_button.click()


    def login(self, password):
        """Function to log into IDMS"""
        print('Logging into IDMS...')
        self.enter_password(password)
        self.click_next()
        self.send_2fa_code()
        
        # Allow up to 3 attempts for entering the 2FA code
        for attempt in range(2):
            auth_code = input('Please enter the 2FA code: ')
            self.enter_verification_code(auth_code)
            self.verify_2fa_code()
            
            # Check for error message indicating wrong 2FA code
            try:
                error_present = WebDriverWait(self.driver, 2).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "#phoneVerificationControl-readOnly_error_message[aria-hidden='false']")
                    )
                )
            except:
                error_present = False
            
            if error_present:
                print('You have entered the wrong code, please try again:')
            else:
                print('2FA code verified')
                break  # Exit the loop if verification is successful
            
            if attempt == 2:
                print('Maximum retries allowed, restart the script in 30 minutes')
