from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Order_not_auto:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz')
        time.sleep(10)
        search = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-main/app-search-bar/div/div[1]/span/input')
        search.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
        time.sleep(5)
        search_point = self.driver.find_element(By.XPATH,
                                           '/html/body/app-root/div/div/div/div/div/app-main/app-search-bar/div/div[1]/span/span')
        search_point.click()
        time.sleep(5)
        newcards = self.driver.find_element(By.XPATH, "//*[contains(text(), 'ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')]")
        newcards.click()
        time.sleep(5)
        orderpoint = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/div/div[2]/div[2]/div[6]/button[1]')
        orderpoint.click()
        time.sleep(5)
        numbers = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[3]/p-inputmask/input')
        numbers.send_keys('7066930827')
        time.sleep(6)
        name = self.driver.find_element(By.XPATH,
                                   '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[4]/input')
        name.send_keys('Тестовый запросы')
        email = self.driver.find_element(By.XPATH,
                                    '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[5]/input')
        email.send_keys('anton.ialtezza93@gmial.com')
        time.sleep(5)
        company = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[6]/p-dropdown/div/input')
        company.send_keys('Тестовая компания')
        time.sleep(5)
        region = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[7]/p-dropdown')
        region.click()
        ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        region.click()
        time.sleep(5)
        checkbox = self.driver.find_element(By.XPATH, '//*[@id="offer"]')
        action = ActionChains(self.driver)
        action.move_to_element(checkbox)  # Перемещаемся к элементу
        action.click()  # Добавляем действие клика
        action.perform()  # Выполняем цепочку действий

        time.sleep(5)  # Ожидаем 5 секунд
        finishorder = self.driver.find_element(By.XPATH,
                                          '/html/body/app-root/div/div/div/div/div/app-main/app-goods-card/app-callback[2]/div/div/form/div/div[11]/button[1]')
        finishorder.click()
        time.sleep(5)
        self.driver.quit()
