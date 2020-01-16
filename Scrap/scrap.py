from selenium import webdriver
import time

### Função limpar tela
from os import system, name
def clear():
    #Windows
    if name == 'nt':
        _ = system('cls')

    #Demais SO's
    else:
        _ = system('clear')
clear()



### Web Scrap by Luiz Gatão
print("Sistema para coleta de informações de FII's\n")
ativos = input("Insira o código de negociação dos fundos, separados por espaço:\n")
ativos_lista = ativos.split()
clear()

for i in ativos_lista:
    urlpage1 = "https://www.clubefii.com.br/fiis/" + i
    urlpage2 = "https://fiis.com.br/" + i
    urlpage3 = "https://www.fundsexplorer.com.br/funds/" + i
    driver = webdriver.Firefox()

    #Site 1
    driver.get(urlpage1)
    time.sleep(5)
    results = driver.find_element_by_xpath("/html/body/div[6]/div[1]/ul[1]/li[*]/div[2]/div[2]/span")
    print("Site 1: ", i.upper(), results.get_attribute("innerHTML"))

    #Site 2
    driver.get(urlpage2)
    time.sleep(5)
    results = driver.find_element_by_xpath("/html/body/div[2]/section[3]/div/div/div[3]/div/div[1]/span[2]")
    print("Site 2: ", i.upper(), "R$", results.get_attribute("innerHTML"))

    #Site 3
    driver.get(urlpage3)
    time.sleep(5)
    results = driver.find_element_by_xpath("/html/body/section/section/div/div/div/div[2]/div/span[1]")
    #results = driver.find_element_by_xpath("//*[@class='value']")
    print("Site 3: ", i.upper(), "R$", results.get_attribute("innerHTML"))
