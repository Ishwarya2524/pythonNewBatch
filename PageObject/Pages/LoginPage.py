from selenium.webdriver.common.by import By
from PageObject import Locator

class LoginPage:
    def __init__(self,driver):
        self.txt_username=driver.find_element(By.ID, Locator.username_id)
        self.txt_password=driver.find_element(By.ID, Locator.password_id)
        self.btn_login=driver.find_element(By.XPATH, Locator.btn_login)
        self.btn_new_user=driver.find_element(By.XPATH, Locator.btn_new_user_xpath)

    #getters
    def getTxtUserName(self):
        return self.txt_username
    def getTxtPassword(self):
        return self.txt_password
    def getBtnLogin(self):
        return self.btn_login
    def getBtnNew(self):
        return self.btn_new_user

