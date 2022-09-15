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
    driver.get(url)    

    #esperando a página de jogos carregar
    WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'css-1myhtyb')))

    #pega os jogos grátis da semana
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
    
    #abre cada link obtido
    for link in links:
        driver.get(link)
        # procura o botão de compras
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/div/aside/div/div/div[5]/div/button')) # FAZER PEDIDO
                )
            print(driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/div/aside/div/div/div[5]/div/button').text)
            driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/div[2]/div/aside/div/div/div[5]/div/button').click()
            time.sleep(10)
            driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="webPurchaseContainer"]/iframe'))
            print(driver.find_element(By.XPATH, '//*[@id="purchase-app"]/div/div/div/div[2]/div[2]/button').text) 
            driver.find_element(By.XPATH, '//*[@id="purchase-app"]/div/div/div/div[2]/div[2]/button').click()
            time.sleep(10)
            print('achou o popup')
        except:
            print('Não achou o botão FAZER PEDIDO')
            # verifica se o jogo está indisponível
            try:
                WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'css-8en90x')) # INDISPONÍVEL ou NA BIBLIOTECA
                )
                print(driver.find_element(By.CLASS_NAME, 'css-8en90x').text)
            except:
                print('Não achou os botões INDISPONÍVEL ou NA BIBLIOTECA')
                #driver.quit()

    print(links)

if __name__ == '__main__':
    freeze_support()
    Process(target=f).start()