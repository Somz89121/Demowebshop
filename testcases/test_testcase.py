import pytest
from ..helpers.test_commonmethods import Helpers
from ..pageobject.test_login import DemoPOM
from ..pageobject.test_book import Book
from ..pageobject.test_computers import ComputerPg
from ..pageobject.test_digital import DigitalPg
from ..pageobject.test_jewelry import JewelryPg
from ..pageobject.test_giftcards import GiftcardsPg
from ..pageobject.test_Apparel import ApparelPg
App = ApparelPg()
gift = GiftcardsPg()
jewelry  = JewelryPg()
book  = Book()
helper = Helpers()
demo=DemoPOM()
com = ComputerPg()
digital=DigitalPg()
class Test_Case:

    @pytest.mark.m1
    @pytest.mark.parametrize("creds",helper.user_list())
    def test_login(self,driver,creds):
        helper.open_browser(driver)
        demo.verify_login(driver,creds)
        helper.close_browser(driver)
    @pytest.mark.m1
    @pytest.mark.parametrize("creds",helper.user_list())
    def test_book(self,driver,creds):
        helper.open_browser(driver)
        demo.verify_login(driver,creds)
        book.verify_book(driver)
        helper.close_browser(driver)
    @pytest.mark.parametrize("creds",helper.user_list())
    def test_boook(self,driver,creds):
        helper.open_browser(driver)
        demo.verify_login(driver,creds)
        book.verify_book(driver)
        helper.close_browser(driver)

    @pytest.mark.parametrize("creds", helper.user_list())
    def test_computer(self, driver, creds):
        helper.open_browser(driver)
        demo.verify_login(driver, creds)
        com.verify_computer(driver)
        helper.close_browser(driver)


    @pytest.mark.parametrize("creds", helper.user_list())
    def test_digital(self, driver, creds):
        helper.open_browser(driver)
        demo.verify_login(driver, creds)
        digital.verify_digital_downloads(driver)
        helper.close_browser(driver)

    @pytest.mark.parametrize("creds", helper.user_list())
    def test_jewelry(self, driver, creds):
        helper.open_browser(driver)
        demo.verify_login(driver, creds)
        jewelry.verify_Jewelry(driver)
        helper.close_browser(driver)

    @pytest.mark.parametrize("creds", helper.user_list())
    def test_giftcards(self, driver, creds):
        helper.open_browser(driver)
        demo.verify_login(driver, creds)
        gift.verify_gift(driver)
        helper.close_browser(driver)

    @pytest.mark.parametrize("creds", helper.user_list())
    def test_Apparel(self, driver, creds):
        helper.open_browser(driver)
        demo.verify_login(driver, creds)
        App.verify_Apparel(driver)
        helper.close_browser(driver)


