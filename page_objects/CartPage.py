from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    select = "select[name='quantity']"

    resultat_quantite_text_selector = "#quantity > option:nth-child(3)"

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def changeQuantity(self, quantity):
        select_Qte = Select(self.driver.find_element(By.CSS_SELECTOR, self.select))
        select_Qte.select_by_value(quantity)

    def getQuantity(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.resultat_quantite_text_selector)))
        return self.driver.find_element(By.CSS_SELECTOR, self.resultat_quantite_text_selector).text



