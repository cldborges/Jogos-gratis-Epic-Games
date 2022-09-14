from multiprocessing import Process, freeze_support
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

from funcoes import login_with_epic, salvar_cookies

def f():

    url = 'https://store.epicgames.com/pt-BR/free-games'
    driver = uc.Chrome()
    #driver.get('https://nowsecure.nl')  # known url using cloudflare's "under attack mode"
    #cookies = pickle.load(open("cookies.pkl", "rb"))


    #salvar_cookies(driver)
    #for cookie in cookies:
    #    driver.add_cookie(cookie)

    #login   
    login_with_epic(driver)

    time.sleep(20)

    #driver.maximize_window()
    #driver.implicitly_wait(30)

    driver.get(url)    

    WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1myhtyb')))

    jogos_gratis = driver.find_element(By.CLASS_NAME, 'css-1myhtyb')
    jogos_gratis_da_semana = jogos_gratis.find_elements(By.CLASS_NAME, 'css-5auk98')
    print(len(jogos_gratis_da_semana))

    #pegar links
    links = []
    for jogo_gratis in jogos_gratis_da_semana:
        jogo_gratis_semana = None
        try:
            jogo_gratis_semana = jogo_gratis.find_element(By.CLASS_NAME, 'css-11xvn05') #verifica se tem a DIV "GRÁTIS" no jogo
            link = jogo_gratis.find_element(By.CSS_SELECTOR, 'a').get_attribute("href")
            links.append(link)
            print(links)
        except:
            pass

    for link in links:
        driver.get(link)
        try:
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'css-187rod9'))
                )
        except:
            print('Não funcionou aqui')
            driver.quit()
        print(driver.find_element(By.CLASS_NAME, 'css-187rod9').text)
        driver.find_element(By.CLASS_NAME, 'css-187rod9').click()
        time.sleep(15)
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="webPurchaseContainer"]/iframe'))
        time.sleep(15)
        botoes = driver.find_elements(By.TAG_NAME, 'button')
        for botao in botoes:
            print(botao.text)
        #frames = driver.find_elements(By.XPATH, '//*[@id="webPurchaseContainer"]/iframe')
        #for frame in frames:
        #print(len(frames))


if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()