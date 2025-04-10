import time
from TDD.helpers.test_commonmethods import Helpers
from selenium.webdriver.common.by import By
helper = Helpers()

class Book:
    login_xpath = "//*[text()='Log in']"
    Books_xpath = "Books"
    Addtocart1_xpath = "(//*[@value='Add to cart'])[1]"
    Addtocart2_xpath = "(//*[@value='Add to cart'])[2]"
    Addtocart3_xpath = "(//*[@value='Add to cart'])[3]"
    CartTable_xpath = "//*[@class='cart']"

    def verify_book(self,driver):
        try:
            driver.find_element(By.LINK_TEXT, Book.Books_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, Book.Addtocart1_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, Book.Addtocart2_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH, Book.Addtocart3_xpath).click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, "Shopping cart").click()
            time.sleep(2)
            a = driver.find_element(By.XPATH, "//*[@class='cart']")
            b = a.find_elements(By.XPATH, "//*[@class='cart-item-row']")
            count = len(b)
            print(count)
            c = driver.find_element(By.XPATH, "//*[@class='cart-qty']").text
            d = f"({count})"
            print(f"Value of d: {d}")
            if d == c:
                print("same")
            else:
                print("not")


        except Exception as e:
            helper.record_error(driver, e)
            assert False, f"Test failed due to: {str(e)}"
