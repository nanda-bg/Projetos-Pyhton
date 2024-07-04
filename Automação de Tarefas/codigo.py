#Passo a Passo: 
#1: entrar no sistema
import pyautogui #biblioteca de automação
import time 
import pandas #biblioteca para bd

sistema= "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE=1 #pausa após cada comando do pyautogui

#abrir navegador e sistema:
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")
pyautogui.write(sistema)
pyautogui.press("enter")
time.sleep(3) #deixar tempo para a página carregar

#2: Login
pyautogui.click(x=446, y=380)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("Jsbyne8236@$#")
pyautogui.press("enter")
time.sleep(3)

#3: Importar base de dados 
tabela = pandas.read_csv("produtos.csv")

#4: Cadastrar os produtos
for linha in tabela.index:
    pyautogui.click(x=589, y=249)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("enter")
    pyautogui.scroll(5000) #voltar para o começo da pagina

