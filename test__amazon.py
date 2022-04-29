from page_objects.HomePage import HomePage
from page_objects.BooksPage import BooksPage
from page_objects.ProductPage import ProductPage
from page_objects.ConfirmationPage import ConfirmationtPage
from page_objects.CartPage import CartPage
from selenium import webdriver


def test_amazon1():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.fr/")
    driver.maximize_window()
    driver.quit()

def test_page_object():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.fr/")
    homePage = HomePage(driver)
    quantite = "2"
    homePage.closeCookies()
    homePage.openAllMenu()
    homePage.openBookCategory()
    homePage.openAllBooks()
    booksPage = BooksPage(driver)
    booksPage.selectFirstBookNouveautes()
    productPage = ProductPage(driver)
    productPage.addToCart()
    confirmationPage = ConfirmationtPage(driver)
    confirmationPage.openCart()
    cartPage = CartPage(driver)
    cartPage.changeQuantity()
    cartPage.getQuantity()

    assert quantite == cartPage.getQuantity(), "la quantite_saisie et la quantite  de la selection sont differents"

    driver.quit()




