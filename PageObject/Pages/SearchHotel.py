from selenium.webdriver.common.by import By
from PageObject import Locator

class SearchHotel:
    def __init__(self,driver):
        self.location=driver.find_element(By.ID, Locator.location)
        self.hotel=driver.find_element(By.ID, Locator.hotel)
        self.room=driver.find_element(By.ID, Locator.room)
        self.no_room=driver.find_element(By.ID, Locator.no_room)
        self.check=driver.find_element(By.ID, Locator.check)
        self.check_out=driver.find_element(By.ID, Locator.check_out)
        self.adult=driver.find_element(By.ID, Locator.adult)
        self.child=driver.find_element(By.ID, Locator.child)
        self.search=driver.find_element(By.ID, Locator.search)

    #getters
    def getLocation(self):
        return self.location
    def getHotel(self):
        return self.hotel
    def getRoom(self):
        return self.room
    def getNo_Room(self):
        return self.no_room
    def getCheck(self):
        return self.check
    def getCheck_Out(self):
        return self.check_out
    def getAdult(self):
        return self.adult
    def getChild(self):
        return self.child
    def getSearch(self):
        return self.search
