import time
from ..helpers.test_commonmethods import Helpers
from selenium.webdriver.common.by import By
helper = Helpers()

class DemoPOM:
    login_xpath = "//*[text()='Log in']"
    Books_xpath = "Books"
    Addtocart1_xpath = "(//*[@value='Add to cart'])[1]"
    Addtocart2_xpath = "(//*[@value='Add to cart'])[2]"
    Addtocart3_xpath = "(//*[@value='Add to cart'])[3]"
    CartTable_xpath = "//*[@class='cart']"

    def verify_login(self,driver,creds):
        try:
            link = driver.find_element(By.XPATH, DemoPOM.login_xpath).click()
            driver.find_element(By.ID, "Email").send_keys(creds[0])
            driver.find_element(By.ID, "Password").send_keys(creds[1])
            driver.find_element(By.XPATH, "//*[@value='Log in']").click()
            time.sleep(3)
        except Exception as e:
            helper.record_error(driver, e)
            assert False, f"Test failed due to: {str(e)}"

