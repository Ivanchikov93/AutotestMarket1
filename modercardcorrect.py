from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Modercardcorrect:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz')
        time.sleep(10)
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
        time.sleep(5)
        cabinetmoderation = self.driver.find_element(By.XPATH,
                                                '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/button')
        cabinetmoderation.click()
        time.sleep(5)
        newcards = self.driver.find_element(By.XPATH, "//*[contains(text(), 'ТЕСТОВАЯ КАРТОЧКА НА КОРРЕКТИРОВКУ')]")
        newcards.click()
        time.sleep(5)
        adjustment = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/div/div/div/div/app-check-edit/form/div/div/div[1]/button')
        adjustment.click()
        time.sleep(5)
        adjustment_text = self.driver.find_element(By.XPATH,
                                              '/html/body/app-root/div/div/div/div/div/app-check-edit/p-dialog[1]/div/div/div[3]/div[2]/textarea')
        adjustment_text.send_keys('ТЕСТ ПРОЙДЕН')
        time.sleep(5)
        adjustment_text_send = self.driver.find_element(By.XPATH,
                                                   '/html/body/app-root/div/div/div/div/div/app-check-edit/p-dialog[1]/div/div/div[3]/div[3]/button[1]')
        adjustment_text_send.click()
        time.sleep(5)
        # Закрытие драйвера в конце теста
        self.driver.quit()

