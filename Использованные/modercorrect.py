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
url = 'https://business.ismet.kz'

# Открыть страницу
driver.get(url)

# Закрыть браузер после задержки
time.sleep(5)
button = driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/button')
button.click()
username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password-log"]')
username.send_keys('company.legion@mail.ru')
password.send_keys('MarketModer2023$')
login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
login_button.click()
time.sleep(10)
element_to_hover_over = driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[1]/div[1]')
action = ActionChains(driver)
action.move_to_element(element_to_hover_over).perform()
time.sleep(5)
cabinetmoderation = driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/button')
cabinetmoderation.click()
time.sleep(5)
newcards = driver.find_element(By.XPATH, "//*[contains(text(), 'ТЕСТОВАЯ КАРТОЧКА НА КОРРЕКТИРОВКУ')]")
newcards.click()
time.sleep(5)
adjustment = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-check-edit/form/div/div/div[1]/button')
adjustment.click()
time.sleep(5)
adjustment_text = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div/app-check-edit/p-dialog[1]/div/div/div[3]/div[2]/textarea')
adjustment_text.send_keys('ТЕСТ ПРОЙДЕН')
time.sleep(5)
adjustment_text_send = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-check-edit/p-dialog[1]/div/div/div[3]/div[3]/button[1]')
adjustment_text_send.click()
time.sleep(5)