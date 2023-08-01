import undetected_chromedriver as uc
from multiprocessing import Process, freeze_support

def f():
    driver = uc.Chrome(headless=True,use_subprocess=False)
    driver.get('https://nowsecure.nl')
    driver.save_screenshot('nowsecure.png')


if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()