from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

url = 'https://store.epicgames.com/pt-BR/free-games'

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get(url)
time.sleep(60)