from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class review_test:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz/account/purchases')
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password-log"]')
        username.send_keys('anton.ialtezza93@gmail.com')
        password.send_keys('Altezza93!')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()
        time.sleep(10)
        review = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/div/p-table/div/div/table/tbody/tr[1]/td[7]/div')
        action = ActionChains(self.driver)
        action.move_to_element(review)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий
        time.sleep(10)
        finish = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/div/p-table/div/div/table/tbody/tr[1]/td[7]/div/p-menu/div/ul/li/div')
        action = ActionChains(self.driver)
        action.move_to_element(finish)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий
        time.sleep(10)
        review1 = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/p-dialog/div/div/div[2]/div/div[3]/textarea')
        review1.send_keys('Все отлично спасибо ')
        star = self.driver.find_element(By.XPATH,
                                   '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/p-dialog/div/div/div[2]/div/div[2]/p-rating/div/span[6]/img')
        action = ActionChains(self.driver)
        action.move_to_element(star)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий
        time.sleep(10)

        self.driver.quit()