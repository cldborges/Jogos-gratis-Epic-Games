import undetected_chromedriver as uc
from multiprocessing import Process, freeze_support


driver = uc.Chrome()
driver.get('https://nowsecure.nl')
import time

if __name__ == "__main__":
    freeze_support()
    Process(target=f).start()
    url = 'https://store.epicgames.com/pt-BR/free-games'
    driver.get(url)
    time.sleep(90)