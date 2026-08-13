import pyautogui
import pandas as pd
import time
#1 Ler a tabela de Produtos   
tabela = pd.read_csv("produtos.csv")  
tabela = tabela.head(66)
time.sleep(5)


#Adicionando tempo de espera para cada função

pyautogui.PAUSE = 0.5
#Tempo de espera entre cada comando do pyautogui.

#Clicar no campo Email
pyautogui.click(x=1427, y=533)

#Escreva seu email.
pyautogui.write("ez@gmail.com")
time.sleep(3)
#Clicar no campo de senha ou apertar a tecla "Tab"
pyautogui.click(x=1424, y=610)
#pyautogui.press("tab")

#Escreva sua senha
pyautogui.write("123456")

#Clicar no botão Logar.   
pyautogui.click(x=1526, y=668)

#Adicionar um time sleep, para esperar a pagina carregar.
time.sleep(2)

#Cadastrar os produtos
 # abre o loop
for linha in tabela.index: 

#Formulario de cadastro de produtos
    pyautogui.click(x=1071, y=245)
    time.sleep(3)
    #Escreve o valor
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)    

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")
    time.sleep(3)
    #So escreve se não tiver vazio.
    if not pd.isna(tabela.loc[linha, "obs"] ):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    #Aperta  a tecla "Tab"
    pyautogui.press("tab")

        #Clica no botão enviar,para salvar os produtos.
    pyautogui.click(x=1069, y=711)
    