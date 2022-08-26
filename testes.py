from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pickle
import time


chrome_options = Options()
#chrome_options.add_argument("user-data-dir=G:\Meu Drive\Python\Projetos\Jogos gratis Epic Games\selenium") 
chrome_options.add_argument("user-data-dir=C:\PortableApps\PortableApps\GoogleChromePortable\Data\profile 2")
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
driver.get("https://store.epicgames.com/pt-BR/free-games")

time.sleep(30)

#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))