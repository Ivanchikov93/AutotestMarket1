from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Sales_test:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz/account/sales')
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password-log"]')
        username.send_keys('anton.ialtezza@gmail.com')
        password.send_keys('Altezza93!')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()
        time.sleep(10)
        status = self.driver.find_element(By.XPATH, '//*[@id="pn_id_14-table"]/tbody/tr[1]/td[8]/div')
        action = ActionChains(self.driver)
        action.move_to_element(status)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий
        time.sleep(10)
        view = self.driver.find_element(By.XPATH, '//*[@id="pn_id_15_0"]/div')
        action = ActionChains(self.driver)
        action.move_to_element(view)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий
        time.sleep(10)
        towork = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[1]/div/div/div[3]/div[3]/div[1]/p-button/button')
        towork.click()
        time.sleep(5)
        execute = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[2]/div/div/div[3]/div[3]/div[3]/p-button/button')
        execute.click()
        time.sleep(5)
        yes = self.driver.find_element(By.XPATH,
                                  '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[6]/div/div/div[3]/div[3]/div[1]/p-button/button')
        yes.click()
        time.sleep(5)
        self.driver.quit()