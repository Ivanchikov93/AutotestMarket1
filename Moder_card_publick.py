from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Moder_card_publick:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz')
        time.sleep(10)
        # Закрыть браузер после задержки
        time.sleep(5)
        button = self.driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/button')
        button.click()
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password-log"]')
        username.send_keys('company.legion@mail.ru')
        password.send_keys('MarketModer2023$')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()
        time.sleep(10)
        element_to_hover_over = self.driver.find_element(By.XPATH,
                                                    '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[1]/div[1]')
        action = ActionChains(self.driver)
        action.move_to_element(element_to_hover_over).perform()
        time.sleep(10)
        cabinetmoderation = self.driver.find_element(By.XPATH,
                                                '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/button')
        cabinetmoderation.click()
        time.sleep(10)
        newblock = self.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/div/div/div/div/app-moderator/div/p-tabview/div/div[1]/div/ul/li[2]/a/div')
        newblock.click()
        time.sleep(10)
        newcards = self.driver.find_element(By.XPATH, "//*[contains(text(), 'ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')]")
        newcards.click()
        time.sleep(10)
        publickcard = self.driver.find_element(By.XPATH,
                                          '/html/body/app-root/div/div/div/div/div/app-check-edit/form/div/div/div[2]/button')
        publickcard.click()
        time.sleep(10)
        self.driver.quit()