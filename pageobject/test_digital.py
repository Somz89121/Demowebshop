import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ..helpers.test_commonmethods import Helpers

helper = Helpers()


class DigitalPg:
    digital_xpath = "Digital downloads"
    Review_xpath = "//div[@class='product-review-links']/a[1]"
    Music2_xpath = "(//*[@title='Show details for Music 2'])[2]"
    wishlist_xpath = "//*[@id='add-to-wishlist-button-51']"
    Add_to_cart_xpath = "//*[@id='add-to-cart-button-51']"
    Shopping_cart_xpath = "Shopping cart"
    FirstName_xpath = "//*[@id='BillingNewAddress_FirstName']"
    LastName_xpath = "//*[@id='BillingNewAddress_LastName']"
    Email_xpath = "//*[@id='BillingNewAddress_Email']"
    Company_xpath = "//*[@id='BillingNewAddress_Company']"
    CountryId_xpath = "//*[@id='BillingNewAddress_CountryId']"
    City_xpath = "//*[@id='BillingNewAddress_City']"
    Address1_xpath = "//*[@id='BillingNewAddress_Address1']"
    Address2_xpTH = "//*[@id='BillingNewAddress_Address2']"
    Pincode_xpath = "//*[@id='BillingNewAddress_ZipPostalCode']"
    PhoneNumber_xpath = "//*[@id='BillingNewAddress_PhoneNumber']"
    FaxNumber_xpath = "//*[@id='BillingNewAddress_FaxNumber']"
    Continue_xpath = "(//*[@value='Continue'])[1]"
    continue1_xpath = "(//*[@value='Continue'])[2]"
    continue2_xpath = "(//*[@value='Continue'])[3]"
    Confirm_xpath = "//*[@value='Confirm']"
    continue_xpath = "//*[@class='buttons']/input"
    Check_out_guest = "//*[@value='Checkout as Guest']"

    def verify_digital_downloads(self, driver):
        try:
            digital_link = driver.find_element(By.LINK_TEXT, DigitalPg.digital_xpath)
            if digital_link.is_displayed():
                txxt = digital_link.text
                print("txxt =", txxt)
                digital_link.click()
                time.sleep(4)

            # Click on Music 2 link and do end-to-end test case

            driver.find_element(By.XPATH, DigitalPg.Music2_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.Review_xpath).click()
            time.sleep(2)
            driver.back()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.wishlist_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.Add_to_cart_xpath).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, DigitalPg.Shopping_cart_xpath).click()
            time.sleep(2)
            driver.find_element(By.ID, "termsofservice").click()
            time.sleep(2)
            driver.find_element(By.ID, "checkout").click()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.Check_out_guest).click()
            driver.find_element(By.XPATH, DigitalPg.FirstName_xpath).send_keys("Gnaesh")
            driver.find_element(By.XPATH, DigitalPg.LastName_xpath).send_keys("Kumar")
            driver.find_element(By.XPATH, DigitalPg.Email_xpath).send_keys("ganesh@gmail.com")
            driver.find_element(By.XPATH, DigitalPg.Company_xpath).send_keys("Tech Matrix")
            s = Select(driver.find_element(By.XPATH, DigitalPg.CountryId_xpath))
            s.select_by_visible_text("India")
            driver.find_element(By.XPATH, DigitalPg.City_xpath).send_keys("Hyderabad")
            driver.find_element(By.XPATH, DigitalPg.Address1_xpath).send_keys("Chintal")
            driver.find_element(By.XPATH, DigitalPg.Address2_xpTH).send_keys("kphb")
            driver.find_element(By.XPATH,DigitalPg.Pincode_xpath).send_keys("500054")
            driver.find_element(By.XPATH, DigitalPg.PhoneNumber_xpath).send_keys("9765649749")
            driver.find_element(By.XPATH, DigitalPg.FaxNumber_xpath).send_keys("655665")
            driver.find_element(By.XPATH, DigitalPg.Continue_xpath).click()
            time.sleep(5)
            driver.find_element(By.XPATH, DigitalPg.continue1_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.continue2_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, DigitalPg.Confirm_xpath).click()
            time.sleep(5)
            driver.find_element(By.XPATH, DigitalPg.continue_xpath).click()
        except Exception as e:
            helper.record_error(driver, e)
