##############################
########## ARACHNE ###########
##############################


from selenium import webdriver
import numpy as np
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

### Função cadastra
def cadastra():
    ativos = input("Insira o código de negociação dos fundos, separados por espaço:\n")
    ativos_lista = ativos.split()
    return(ativos_lista)
    #clear()

### Função minera
def minera(ativos_lista = ["XPML11", "XPIN11", "IRDM11"]):
    driver = webdriver.Firefox()
    for i in ativos_lista:
        #Site 1
        urlpage1 = "https://www.clubefii.com.br/fiis/" + i
        driver.get(urlpage1)
        title1 = driver.title
        window1 = driver.current_window_handle
        results = driver.find_element_by_xpath\
            ("/html/body/div[6]/div[1]/ul[1]/li[*]/div[2]/div[2]/span")
        info1 = title1, i.upper(), results.get_attribute("innerHTML")
    driver.quit()

    return(info1, window1)
### Função furtiva (Use com responsabilidade! Uso didático)    
def furtiva(url='https://www.brandcrowd.com/maker/logo/ce07c4ab-a95a-4efc-8872-6267683f4c50/draft/4c65c7c7-076b-4505-a790-900e7f546c14'):
    driver = webdriver.Firefox()
    driver.get(url)
    results = driver.find_elements_by_class_name('maker-canvas-container')
    imagem = results.get_attribute("value")
    driver.quit()

menu = input("Função Minera ou Furtiva.(M ou F):\n")
if menu.capitalize == 'M':
    ativos_lista = cadastra()

    if ativos_lista:
        info_ativos = minera(ativos_lista)
    else:
        info_ativos = minera()
else:
    furtiva()