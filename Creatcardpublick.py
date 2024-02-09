from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Сreatecardpublick:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)

    def test_site(self):
        self.driver.get('https://business.ismet.kz')
        time.sleep(10)
        # Закрыть браузер после задержки
        time.sleep(10)
        button = self.driver.find_element(By.XPATH, '/html/body/app-root/div/app-header/div/div/div/div/div[2]/button')
        button.click()
        username = self.driver.find_element(By.XPATH, '//*[@id="username"]')
        password = self.driver.find_element(By.XPATH, '//*[@id="password-log"]')
        username.send_keys('anton.ialtezza@gmail.com')
        password.send_keys('Altezza93!')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="kc-login"]')
        login_button.click()
        time.sleep(10)
        element_to_hover_over = self.driver.find_element(By.XPATH,
                                                    '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[1]/div[1]')
        action = ActionChains(self.driver)
        action.move_to_element(element_to_hover_over).perform()
        time.sleep(10)
        cabinemain = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/app-header/div/div/div/div/div[2]/div[4]/div[2]/div[2]/div/div[2]/button')
        cabinemain.click()
        time.sleep(5)
        myprodact = self.driver.find_element(By.XPATH, '//*[@id="pn_id_106_header_action"]/span')
        myprodact.click()
        time.sleep(5)
        addcard = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-account/app-my-products-and-services/div/div[1]/button')
        addcard.click()
        time.sleep(5)
        # Найдите элемент загрузки файла
        file_input = self.driver.find_element(By.CSS_SELECTOR,
                                         "body > app-root > div > div > div > div > div > app-create-card > form > div > div:nth-child(2) > div:nth-child(2) > div.card.relative.my-2.file-err > p-fileupload:nth-child(1) > div > div.p-fileupload-buttonbar > span > input[type=file]")  # Измените селектор в соответствии с вашим случаем
        # Отправьте абсолютный путь к файлу
        file_path = "C:\\Users\\Антон\\PycharmProjects\\AutotestMarket\\Использованные\\img\\2.jpg"  # Укажите корректный путь к файлу
        file_input.send_keys(file_path)
        time.sleep(5)
        nameru = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[3]/input')
        descriptionru = self.driver.find_element(By.XPATH,
                                            '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[5]/p-editor/div/div[2]/div[1]')
        namekz = self.driver.find_element(By.XPATH,
                                     '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[7]/input')
        descriptionkz = self.driver.find_element(By.XPATH,
                                            '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div[9]/p-editor/div/div[2]/div[1]')
        nameru.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
        descriptionru.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
        namekz.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
        descriptionkz.send_keys('ТЕСТОВАЯ КАРТОЧКА НА ПУБЛИКАЦИЮ')
        time.sleep(5)
        nextstep = self.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[2]/button')
        nextstep.click()
        time.sleep(2)
        element_to_hover_over1 = self.driver.find_element(By.XPATH,
                                                     '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/p-dropdown/div/div[2]/chevrondownicon')
        element_to_hover_over1.click()
        time.sleep(2)
        cat = self.driver.find_element(By.XPATH,
                                  '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div[2]/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input')
        cat.send_keys(Keys.ARROW_DOWN)
        cat.send_keys(Keys.ENTER)
        time.sleep(2)
        element_to_hover_over2 = self.driver.find_element(By.XPATH,
                                                     '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/p-dropdown/div/div[2]/chevrondownicon')
        element_to_hover_over2.click()
        time.sleep(2)
        cat = self.driver.find_element(By.XPATH,
                                  '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div[2]/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input')
        cat.send_keys(Keys.ARROW_DOWN)
        cat.send_keys(Keys.ENTER)
        time.sleep(2)
        price = self.driver.find_element(By.ID, 'price')
        price.send_keys('12990')
        min_order_count = self.driver.find_element(By.ID, 'min_order_count')
        min_order_count.send_keys('100')
        time.sleep(2)
        tipecoast = self.driver.find_element(By.XPATH,
                                        '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div[5]/div/div[3]/div/p-dropdown')
        tipecoast.click()
        time.sleep(2)
        tipecoast.click()
        ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        time.sleep(5)
        nextstep1 = self.driver.find_element(By.XPATH,
                                        '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[3]/button')
        nextstep1.click()
        time.sleep(5)
        regionid = self.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/div[2]/div')
        regionid.click()
        time.sleep(5)
        pointreionid = self.driver.find_element(By.XPATH,
                                           '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/p-overlay/div/div/div/div[1]/div[1]/div[2]')
        pointreionid.click()
        time.sleep(5)
        regionid = self.driver.find_element(By.XPATH,
                                       '/html/body/app-root/div/div/div/div/div/app-create-card/form/div/div[2]/div[2]/div/p-multiselect/div/div[2]/div')
        regionid.click()
        publick = self.driver.find_element(By.XPATH,
                                      '/html/body/app-root/div/div/div/div/div/app-create-card/div[2]/div/div[4]/p-button/button/span')
        publick.click()
        time.sleep(5)
        # Продолжение кода с использованием self.driver...

        # Закрытие драйвера в конце теста
        self.driver.quit()

