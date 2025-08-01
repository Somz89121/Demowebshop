import time
from selenium.webdriver.common.by import By
from ..helpers.test_commonmethods import Helpers

helper = Helpers()


class ApparelPg:

    ApparelShoes = "Apparel & Shoes"
    GreenShoe = "Green and blue Sneaker"
    Compare = "//input[@value='Add to compare list']"
    Clear = "Clear list"
    Compare_Product = "//div[@class='page-body']"


    def verify_Apparel(self, driver):
        try:
            driver.find_element(By.LINK_TEXT, ApparelPg.ApparelShoes).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, ApparelPg.GreenShoe).click()
            time.sleep(2)
            driver.find_element(By.XPATH, ApparelPg.Compare).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT,ApparelPg.Clear).click()
            Text = driver.find_element(By.XPATH,"//div[@class='page-body']").text
            assert Text == "You have no items to compare."
            time.sleep(2)
        except Exception as e:
            helper.record_error(driver, e)