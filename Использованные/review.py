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
url = 'https://business.ismet.kz/account/purchases'
time.sleep(10)

# Открыть страницу
driver.get(url)
username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password-log"]')
username.send_keys('anton.ialtezza93@gmail.com')
password.send_keys('Altezza93!')
login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
login_button.click()
time.sleep(10)
review = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/div/p-table/div/div/table/tbody/tr[1]/td[7]/div')
action = ActionChains(driver)
action.move_to_element(review) # Перемещаемся к элементу
action.click() # Добавляем действие клика
action.perform() # Выполняем цепочку действий
time.sleep(10)
finish = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/div/p-table/div/div/table/tbody/tr[1]/td[7]/div/p-menu/div/ul/li/div')
action = ActionChains(driver)
action.move_to_element(finish) # Перемещаемся к элементу
action.click() # Добавляем действие клика
action.perform() # Выполняем цепочку действий
time.sleep(10)
review1 = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/p-dialog/div/div/div[2]/div/div[3]/textarea')
review1.send_keys('Все отлично спасибо ')
star = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-purchases/p-dialog/div/div/div[2]/div/div[2]/p-rating/div/span[6]/img')
action = ActionChains(driver)
action.move_to_element(star) # Перемещаемся к элементу
action.click() # Добавляем действие клика
action.perform() # Выполняем цепочку действий
time.sleep(10)