from app.automata.loginAutom import login
from app.automata.subscribeAutom import subscribe

class Automata():

    def __init__(self, account, channelURL, driver):
        self.driver = driver
        self.account = account
        self.subscribeAutomata = subscribe.SubscribeAutomta(self.driver)
        self.loginAutomata = self.loginAutomata = login.LoginAutomata(self.driver, account, channelURL)

    def execute(self):
        self.loginAutomata.execute()
        response = self.subscribeAutomata.execute()
        if response:
            return {
                'account': self.account['email'],
                'subscribed': response
            }
        else:
            return {
                'account': self.account['email'],
                'subscribed': response,
                'motive': 'Already subscribed'
            }
