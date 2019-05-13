
from selenium import webdriver
from loginAutom import login
from subscribeAutom import subscribe
from config import config

accounts = config.accounts
channelURL = config.channelURL
driver = webdriver.Chrome()
SubscribeAutomata = subscribe.SubscribeAutomta(driver)

#Initialization

for account in accounts:
    LoginAutomata = login.LoginAutomata(driver, account, channelURL)
    LoginAutomata.execute()
    SubscribeAutomata.execute()

driver.quit()

