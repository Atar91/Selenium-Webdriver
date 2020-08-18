import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dress="VERSILLA DRESS - Sukienka koktajlowa"
name = "Anna"
lastname = "Nowak"
email = "anna.nowak@bla.com"
wrong_password= "abcd"
rozmiar_34= "CZ621C0AP-G110006000"


class ZalandoKoszyk(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.zalando.pl/")


    def testZalando(self):
        driver = self.driver
        sleep(10)

        al=driver.find_element_by_id("uc-btn-accept-banner")
        al.click()

        gender= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Kobiety']")))
        gender.click()

        search= driver.find_element_by_xpath('//input[@type="search"]')
        search.send_keys(dress)
        search.submit()

        choose= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cat_brandName-2XZRz cat_ellipsis-MujnT']")))
        choose.click()

        size=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Wybierz rozmiar"]')))
        size.click()

        size_34=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, rozmiar_34)))
        size_34.click()

        add=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Dodaj do koszyka"]')))
        add.click()

        driver.get("https://www.zalando.pl/")
        cart= WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Koszyk"]')))
        cart.click()

        dress_in_cart= WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '//a[text()="VERSILLA DRESS - Sukienka koktajlowa - burgundy"]')))
        if dress_in_cart.is_displayed():
            print()
            print("Sukienka jest w koszyku")

        buy=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="z-1-button z-coast-base-primary-accessible z-coast-base__totals-tile__button-checkout z-1-button--primary z-1-button--button"]')))
        buy.click()

        register=WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="A0umWB XQCmZ9 gM8atJ VcCaWc O82Ha7 UnzkRv P6b3OO febL1w X3ffeU _53iU3L KyqyyN VMeYkv"]')))
        register.click()

        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "register.firstname"))).send_keys(name)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "register.lastname"))).send_keys(lastname)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "register.email"))).send_keys(email)
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, "register.password"))).send_keys(wrong_password)

        preferences=driver.find_element_by_xpath('//label[text()="Moda damska"]')
        preferences.click()

        driver.find_element_by_xpath('//button[@data-testid="register_button"]').click()

        error=driver.find_element_by_xpath('//*[contains(text(), "co najmniej 6 znaków")]')

        if error.is_displayed():
            print("Niepoprawny format hasła")

    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main(verbosity=2)
