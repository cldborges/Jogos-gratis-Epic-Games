from multiprocessing import Process, freeze_support
import undetected_chromedriver.v2 as uc
import time

def f():
    print ('hello world!')

    url = 'https://store.epicgames.com/pt-BR/free-games'
    driver = uc.Chrome()
    #driver.get('https://nowsecure.nl')  # known url using cloudflare's "under attack mode"
    driver.get(url)
    time.sleep(30)

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()