from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Создаем экземпляр драйвера
# Убедитесь, что chromedriver доступен в PATH
driver = webdriver.Chrome()

driver.set_window_size(1920, 1080)

# URL-адрес, который нужно открыть
url = 'https://business.ismet.kz/account/sales'

# Открыть страницу
driver.get(url)
username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password-log"]')
username.send_keys('anton.ialtezza@gmail.com')
password.send_keys('Altezza93!')
login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
login_button.click()
time.sleep(10)
status = driver.find_element(By.XPATH, '//*[@id="pn_id_14-table"]/tbody/tr[1]/td[8]/div')
action = ActionChains(driver)
action.move_to_element(status) # Перемещаемся к элементу
action.click() # Добавляем действие клика
action.perform() # Выполняем цепочку действий
time.sleep(10)
view = driver.find_element(By.XPATH, '//*[@id="pn_id_15_0"]/div')
action = ActionChains(driver)
action.move_to_element(view) # Перемещаемся к элементу
action.click() # Добавляем действие клика
action.perform() # Выполняем цепочку действий
time.sleep(10)
towork = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[1]/div/div/div[3]/div[3]/div[1]/p-button/button')
towork.click()
time.sleep(5)
execute = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[2]/div/div/div[3]/div[3]/div[3]/p-button/button')
execute.click()
time.sleep(5)
yes = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-sales/p-dialog[6]/div/div/div[3]/div[3]/div[1]/p-button/button')
yes.click()
time.sleep(5)