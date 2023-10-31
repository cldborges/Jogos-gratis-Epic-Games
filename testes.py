import undetected_chromedriver as uc
from undetected_chromedriver import Chrome, ChromeOptions
from multiprocessing import Process, freeze_support

class Options(ChromeOptions):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.headless: bool = False


def f():

    driver = uc.Chrome(headless=True,use_subprocess=False,options=Options())
    driver.get('https://nowsecure.nl')
    driver.save_screenshot('nowsecure.png')


if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()