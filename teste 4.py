from multiprocessing import Process, freeze_support
import undetected_chromedriver.v2 as uc
import pickle
import time

from funcoes import salvar_cookies

def f():

    url = 'https://store.epicgames.com/pt-BR/free-games'
    driver = uc.Chrome()
    driver.get(url)
    salvar_cookies(driver)

def g():
    url = 'https://store.epicgames.com/pt-BR/free-games'
    driver = uc.Chrome()
    driver.get(url)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(60)

if __name__ == '__main__':
    freeze_support()
    Process(target=g).start()