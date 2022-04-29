
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class ProductPage:

    ajout_panier = "input#add-to-cart-button"



    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def addToCart(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.ajout_panier)))
        self.driver.find_element(By.CSS_SELECTOR, self.ajout_panier).click()


