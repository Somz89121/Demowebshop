import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ..helpers.test_commonmethods import Helpers

helper = Helpers()


class JewelryPg:
    Jewelry_xpath = "Jewelry"
    BWDH_xpath = "Black & White Diamond Heart"
    Jewelry_Addtocart_xpath = "//*[@ID='add-to-cart-button-14']"
    Shopping_xpath = "(//*[text()='Shopping cart'])[1]"

    def verify_Jewelry(self, driver):
        try:
            driver.find_element(By.LINK_TEXT, JewelryPg.Jewelry_xpath).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, JewelryPg.BWDH_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, JewelryPg.Jewelry_Addtocart_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, JewelryPg.Shopping_xpath).click()
            time.sleep(2)
        except Exception as e:
            helper.record_error(driver, e)