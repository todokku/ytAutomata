from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubscribeAutomta:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def execute(self):
        # Initialization
        response = False
        self.wait.until(EC.presence_of_element_located((By.ID, "channel-header")))
        assert "YouTube" in self.driver.title

        # Subscribe
        header = self.driver.find_element(By.ID, "channel-header")
        subButton = header.find_element(By.ID, "buttons")
        if "INSCREVER-SE" in subButton.text:
            subButton.click()
            response = True

        print(subButton.text)
        # Menu Dropdown
        menuDropdown = self.driver.find_element(By.ID, "avatar-btn")
        menuDropdown.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href = '/logout']")))

        sairButton = self.driver.find_element(By.XPATH, "//a[@href = '/logout']")
        sairButton.click()

        return response
