from lib2to3.pgen2 import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PageObject.Pages.LoginPage import LoginPage
from PageObject.Pages.SearchHotel import SearchHotel
from seleniumtest.test.LibGlobal.LibGlobal import Base


class Sample:
    def login(self):
        b=Base()
        driver=b.launch_browser()
        b.window_maximize()
        b.load_url("http://adactinhotelapp.com/")
        txt_username=driver.find_element(By.ID,"username")
        b.set_text(txt_username,"SHALWARUl")
        txt_password = driver.find_element(By.ID, "password")
        b.set_text(txt_password,"JMMsT3gyt22u3@A")
        btn_login=driver.find_element(By.ID,"login")
        b.btn_click(btn_login)
    def search(self):
        b=Base()
        driver=b.launch_browser()
        b.window_maximize()
        b.load_url("http://adactinhotelapp.com/")
        acc=ActionChains(driver)
        location=driver.find_element(By.ID,"location")
        acc.move_to_element(location).perform()
        hotel = driver.find_element(By.ID, "hotels")
        acc.move_to_element(hotel).perform()
        room = driver.find_element(By.ID, "room_type")
        acc.move_to_element(room).perform()
        no_room = driver.find_element(By.ID, "room_nos")
        acc.move_to_element(no_room).perform()
        check = driver.find_element(By.ID, "datepick_in")
        b.set_text(check, "06-06-2021")
        check_out = driver.find_element(By.ID, "datepick_out")
        b.set_text(check_out, "07-06-2021")
        adult = driver.find_element(By.ID, "adult_room")
        acc.move_to_element(adult).perform()
        child = driver.find_element(By.ID, "child_room")
        acc.move_to_element(child).perform()
        search = driver.find_element(By.ID, "Submit")
        b.btn_click(search)



S=Sample()
S.login()
S.search()
