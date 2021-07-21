from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import  Select


class Base:
    def launch_browser(self):
        self.driver=webdriver.Chrome(executable_path=r"C:\Users\ARUL KUMARAN\PycharmProjects\pythonProjectselenium10.00 PM\seleniumtest\test\driver\chromedriver.exe")
        return self.driver
    def window_maximize(self):
        self.driver.maximize_window()
    def load_url(self,url):
        self.driver.get(url)
    def set_text(self,element,data):
        element.send_keys(data)
    def btn_click(self,e):
        e.click()
    def page_url(self):
        url=self.driver.current_url
        return url
    def page_title(self):
        t=self.driver.title
        return t
    def mouse_over(self,e):
        a=ActionChains(self.driver)
        a.move_to_element(e).perform()
    def dd_by_index(self,dd_element,index):
        s=Select(dd_element)
        s.select_by_index(index)
    def switching_frame_by_id(self,id):
        self.driver.switch_to.frame(id)
    def script_load(self,element,value):
        self.driver.execute_script(element,value)
    def screen_load(self,data):
        self.driver.save_screenshot(data)
    def page_refresh(self):
        self.driver.refresh()
    def page_forward(self):
        self.driver.forward()
    def page_back(self):
        self.driver.back()
    def window_load(self):
        url=self.driver.current_window_handle
        return url
    def windows_load(self):
        url=self.driver.window_handles
        return url
