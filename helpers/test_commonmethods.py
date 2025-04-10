import csv
import datetime
from TDD.config.test_config import Test_Config
class Helpers:

    def open_browser(self,driver):
        driver.maximize_window()
        driver.get(Test_Config.base_url)

    def close_browser(self,driver):
        driver.quit()

    def user_list(self):
        file = open("../testdata/userlist.csv","r")
        userlist =csv.reader(file)
        return userlist

    def record_error(self,driver,e):
        print("error occured", str(e))
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        driver.save_screenshot(f"../reports/screenshots/error_{now}.png")
