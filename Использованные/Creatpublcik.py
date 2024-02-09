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
username.send_keys('anton.ialtezza@gmail.com')
password.send_keys('Altezza93!')
login_button = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
login_button.click()
time.sleep(10)
element_to_hover_over = driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[1]/div[1]')
action = ActionChains(driver)
action.move_to_element(element_to_hover_over).perform()
time.sleep(5)
cabinemain = driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/button')
cabinemain.click()
time.sleep(5)
myprodact = driver.find_element(By.XPATH, '//*[@id="pn_id_106_header_action"]/span')
myprodact.click()
time.sleep(5)
addcard = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-account/app-my-products-and-services/div/div[1]/button')
addcard.click()
time.sleep(5)
# Найдите элемент загрузки файла
file_input = driver.find_element(By.CSS_SELECTOR, "body > app-root > div > div > div > div > div > app-create-card > form > div > div:nth-child(2) > div:nth-child(2) > div.card.relative.my-2.file-err > p-fileupload:nth-child(1) > div > div.p-fileupload-buttonbar > span > input[type=file]")  # Измените селектор в соответствии с вашим случаем
# Отправьте абсолютный путь к файлу
file_path = "/Использованные/img\\1.png"  # Укажите корректный путь к файлу
file_input.send_keys(file_path)
time.sleep(5)
nameru = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[3]/input')
descriptionru = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[5]/p-editor/div/div[2]/div[1]')
namekz = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[7]/input')
descriptionkz = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[9]/p-editor/div/div[2]/div[1]')
nameru.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
descriptionru.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
namekz.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
descriptionkz.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
time.sleep(5)
nextstep = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[2]/button')
nextstep.click()
time.sleep(2)
element_to_hover_over1 = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/p-dropdown/div/div[2]/chevrondownicon')
element_to_hover_over1.click()
time.sleep(2)
cat = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input')
cat.send_keys(Keys.ARROW_DOWN)
cat.send_keys(Keys.ENTER)
time.sleep(2)
element_to_hover_over2 = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/p-dropdown/div/div[2]/chevrondownicon')
element_to_hover_over2.click()
time.sleep(2)
cat = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input')
cat.send_keys(Keys.ARROW_DOWN)
cat.send_keys(Keys.ENTER)
time.sleep(2)
price = driver.find_element(By.ID, 'price')
price.send_keys('12990')
min_order_count = driver.find_element(By.ID, 'min_order_count')
min_order_count.send_keys('100')
time.sleep(2)
tipecoast = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[5]/div/div[3]/div/p-dropdown')
tipecoast.click()
time.sleep(2)
tipecoast.click()
ActionChains(driver).send_keys(Keys.DOWN).perform()
time.sleep(5)
nextstep1 = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[3]/button')
nextstep1.click()
time.sleep(5)
regionid = driver.find_element(By.XPATH ,'/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/div[2]/div')
regionid.click()
time.sleep(5)
pointreionid = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/p-overlay/div/div/div/div[1]/div[1]/div[2]')
pointreionid.click()
time.sleep(5)
regionid = driver.find_element(By.XPATH ,'/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/div[2]/div')
regionid.click()
publick = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[4]/p-button/button/span')
publick.click()
time.sleep(5)




