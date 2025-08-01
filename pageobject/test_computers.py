import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ..helpers.test_commonmethods import Helpers

helper = Helpers()


class ComputerPg:
    login_xpath = "//*[text()='Log in']"
    Desktops_xpath = "(//*[contains(text(),'Desktops')])[4]"
    computer_xpath = "(//a[contains(text(),'Computers')])[1]"
    Home_xpath = "//*[@title='Home']"
    product_orderby_xpath = "//*[@id='products-orderby']"
    product_pagesize_xpath = "//*[@id='products-pagesize']"
    product_view_mode_xpath = "//*[@id='products-viewmode']"
    addtocart_xpath = "(//*[@value='Add to cart'])[3]"
    HDD_xpath = "(//*[@type='radio'])[2]"
    OS_xpath = "(//*[@type='radio'])[3]"

    def verify_computer(self, driver):
        try:
            # Clicking Computer link
            link = driver.find_element(By.XPATH, ComputerPg.computer_xpath)
            if link.is_displayed():
                print("Computer is displayed")
                txxt = link.text
                print("txxt =", txxt)
                link.click()
                time.sleep(4)
                # IN Computer fetched Home Title
                txt = driver.find_element(By.XPATH, ComputerPg.Home_xpath)
                tx = txt.text
                print("tx =", tx)

                # Disktop link
                linkk = driver.find_element(By.XPATH, ComputerPg.Desktops_xpath)
                linkk.click()
                time.sleep(2)

                # Using Select Class for DD in Disktop page for sort by
                s = Select(driver.find_element(By.XPATH, ComputerPg.product_orderby_xpath))
                s.select_by_visible_text("Price: Low to High")
                time.sleep(2)

                # Using Select Class for DD in Disktop page for Display
                se = Select(driver.find_element(By.XPATH, ComputerPg.product_pagesize_xpath))
                se.select_by_index(2)
                time.sleep(2)

                # Using Select Class for DD in Disktop page for view-mode
                sel = Select(driver.find_element(By.XPATH, ComputerPg.product_view_mode_xpath))
                sel.select_by_index(1)
                time.sleep(2)

                driver.find_element(By.XPATH, ComputerPg.addtocart_xpath).click()
                time.sleep(5)
                driver.find_element(By.XPATH, ComputerPg.HDD_xpath).click()
                time.sleep(2)
                driver.find_element(By.XPATH, ComputerPg.OS_xpath).click()
                time.sleep(5)
                driver.find_element(By.XPATH, "(//*[@type='radio'])[5]").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//*[@value='22']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//*[@value='23']").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//*[@value='24']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//*[@id='add-to-cart-button-16']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "(//*[text()='Shopping cart'])[1]").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//*[@id='termsofservice']").click()
                time.sleep(2)
                driver.find_element(By.XPATH, "//*[@id='checkout']").click()
                time.sleep(5)
                """driver.find_element(By.XPATH, "//*[@value='Add to compare list']").click()
                time.sleep(5)
                driver.find_element(By.XPATH, "//*[@value='Remove']").click()
                time.sleep(5)"""
                driver.back()
                driver.back()

            else:
                print("Not Displayed")
                assert False
        except Exception as e:
            helper.record_error(driver, e)
