import time
from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''Создание класса'''
class Login():
    def test(self):
        a = 'C:\\Users\\Rail\\PycharmProjects\\RESTAURANT_GURU'
        s = Service(a)
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Firefox(service=s, options=options)

        url = ['https://restaurantguru.ru',
               'https://restaurantguru.it', 'https://restaurantguru.com.br',
               'https://restaurant-guru.in', 'https://restaurantguru.com']  # список url с разными доменами
        un = 'cegelir278@jucatyo.com' # email
        pw = '1231234'  # пароль
        problem_domen = [] #список проблемных доменов

        #Locators
        head_l = '//div[@id="content"]'  # шапка сайта
        authorization_l = '//div[@class="user_button"]' #локатор авторизации
        logout_l = '//a[@class="logout"]'
        email_field_l = '//input[@name="email"]' # локатор поля email
        password_field_l = '//input[@name="password"]' # локатор поля пароль
        login_button_field_l = '//input[@name="doLogin"]' # локатор кнопки войти
        for f in url:
            print(f'Тест URL {f}')
            driver.get(f)  # вход на сайт по url
            driver.maximize_window()  # открытие окна на максимальный размер
            print('Вход на сайт')
            time.sleep(5)
            head = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, head_l)))
            head.click()#клик по шапке сайта
            print('click')
            authorization = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, authorization_l)))
            authorization.click()# клик на локатор авторизации
            print(f'Нажали на User_button')
            time.sleep(3)
            try:
                logout = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, logout_l)))
                logout.click()
                print('Разлогинились')
                authorization = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, authorization_l)))
                authorization.click()  # клик на локатор авторизации
                email_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, email_field_l)))
                email_field.send_keys(un)  # заполнение поля email
                print(f'Ввели email')
                password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, password_field_l)))
                password_field.send_keys(pw)  # заполнение поля пароль
                print(f'Ввели пароль')
                login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, login_button_field_l)))
                login_button.click()  # нажать на кнопку войти
                time.sleep(10)
                current_url = driver.current_url  # выдать текущий URL
                print(current_url)
                if current_url != f:
                    print(f'Авторизация прошла успешно!\n'
                          f'URL: {f}')
                else:
                    problem_domen.append(f)  # добавить URL в список проблемных
                    print(f'Проблемный URL: {f}!!!')
            except TimeoutException:
                email_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, email_field_l)))
                email_field.send_keys(un)  # заполнение поля email
                print(f'Ввели email')
                password_field = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, password_field_l)))
                password_field.send_keys(pw)  # заполнение поля пароль
                print(f'Ввели пароль')
                login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, login_button_field_l)))  # локатор кнопки войти
                login_button.click()  # нажать на кнопку войти
                time.sleep(10)
                current_url = driver.current_url #выдать текущий URL
                print(current_url)
                if current_url != f:
                    print(f'Авторизация прошла успешно!\n'
                          f'URL: {f}')
                else:
                    problem_domen.append(f) #добавить URL в список проблемных
                    print(f'Проблемный URL: {f}!!!')
        print(f'Список проблемных доменов:'
              f'{problem_domen}')
        print('Тест завершен')
        driver.quit()

client = Login()
client.test()