#pyautoguiwww
#passo 1 :abrir o sistema
#    sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#passo 2 :fazer login 
#passo 3 :importar base de dados 
#passo 4 :cadastrar um produto
#passo 5 :repitir cadastro ate acabar 

import time
import pyautogui
pyautogui.PAUSE  = 0.5

pyautogui.press('win')

pyautogui.write('chrome')

pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

pyautogui.press("enter")

time.sleep(3)


pyautogui.click(x=810, y=466)

pyautogui.write("garotodeprogama@yahoo.com")

pyautogui.press("tab")

pyautogui.write("flamareca")

pyautogui.press("tab")

pyautogui.press("enter")

import pandas 

tabela = pandas.read_csv('produtos.csv')


for linha in tabela.index:
    pyautogui.click(x=816, y=327)

    #MOLO000251,Logitech,Mouse,1,25.95,6.50,

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))

    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")

    #preco unitario 
    preco_unitario = tabela.loc[linha, "preco_unitario"]

    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))

    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]

    pyautogui.write(str(obs))

    pyautogui.press("tab")

    pyautogui.press("enter") #envia o formulario 

    pyautogui.scroll(10000)

