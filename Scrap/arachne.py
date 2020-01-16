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
    urlpage1 = "https://www.clubefii.com.br/fiis/" + i
    driver = webdriver.Firefox()
    cotacao = []
    for i in ativos_lista:
        #Site 1
        driver.get(urlpage1)
        time.sleep(5)
        title1 = driver.title
        window1 = driver.current_window_handle
        results = driver.find_element_by_xpath\
            ("/html/body/div[6]/div[1]/ul[1]/li[*]/div[2]/div[2]/span")
        info1 = title1, i.upper(), results.get_attribute("innerHTML")
    driver.quit()

    return(info1, window1)

ativos_lista = cadastra()

if ativos_lista:
    info_ativos = minera(ativos_lista)
else:
    info_ativos = minera()

print(info_ativos[0])