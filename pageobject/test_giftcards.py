import time
from selenium.webdriver.common.by import By
from TDD.helpers.test_commonmethods import Helpers

helper = Helpers()


class GiftcardsPg:
    Giftcards_xpath = "Gift Cards"
    Giftcard4 = "$100 Physical Gift Card"
    Recipient_name = "giftcard_4_RecipientName"
    Your_name = "giftcard_4_SenderName"
    Message = "giftcard_4_Message"
    Addtocart = "add-to-cart-button-4"
    Shoppingcart = "(//*[text()='Shopping cart'])[1]"
    Checkbox = "(//*[@type='checkbox'])[1]"
    Checkbox1 = "(//*[@type='checkbox'])[2]"
    Checkout = "checkout"

    def verify_gift(self, driver):
        try:
            driver.find_element(By.LINK_TEXT, GiftcardsPg.Giftcards_xpath).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, GiftcardsPg.Giftcard4).click()
            time.sleep(2)
            driver.find_element(By.ID, GiftcardsPg.Recipient_name).send_keys("Ganesh")
            time.sleep(2)
            driver.find_element(By.ID, GiftcardsPg.Your_name).send_keys("Shiva")
            driver.find_element(By.ID, GiftcardsPg.Message).send_keys("Hi Team")
            driver.find_element(By.ID,GiftcardsPg.Addtocart).click()
            driver.find_element(By.XPATH, GiftcardsPg.Shoppingcart).click()
            driver.find_element(By.XPATH, GiftcardsPg.Checkbox).click()
            driver.find_element(By.XPATH, GiftcardsPg.Checkbox1).click()
            driver.find_element(By.ID, GiftcardsPg.Checkout).click()




            time.sleep(2)
        except Exception as e:
            helper.record_error(driver, e)