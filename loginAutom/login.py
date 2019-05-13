from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginAutomata:

    def __init__(self, driver, account, url):
        self.driver = driver
        self.url = url
        self.account = account
        self.wait = WebDriverWait(self.driver, 10)

    def execute(self):
        # Initialization
        self.driver.get(self.url)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//yt-formatted-string[text() = 'Fazer login']")))
        assert "YouTube" in self.driver.title

        # Click Login Button
        loginButton = self.driver.find_element(By.XPATH, "//yt-formatted-string[text() = 'Fazer login']")
        loginButton.click()
        #self.wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        assert "YouTube" in self.driver.title

        try:
            # Change Account
            self.driver.find_element(By.NAME, "password")
            accSelector = self.driver.find_element(By.ID, "profileIdentifier")
            accSelector.click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Usar outra conta']")))
            changeAcc = self.driver.find_element(By.XPATH, "//div[text() = 'Usar outra conta']")
            changeAcc.click()
            self.wait.until(EC.element_to_be_clickable((By.ID, "identifierId")))
        except:
            print("entrou except")
        # Login in
        emailInput = self.driver.find_element(By.ID, "identifierId")
        #emailInput.clear()
        emailInput.send_keys(self.account['email'])
        emailInput.send_keys(Keys.RETURN)

        self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        assert "Bem-vindo(a)" in self.driver.page_source

        passInput = self.driver.find_element(By.NAME, "password")
        #passInput.clear()
        passInput.send_keys(self.account['password'])
        passInput.send_keys(Keys.RETURN)


        self.wait.until(EC.title_contains("YouTube"))