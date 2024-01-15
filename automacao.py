import pyautogui
import time

#pyautogui.write - escreve um texto
#pyautogui.press - aperta uma tecla
#pyautogui.click - clica em algum lugar da tela.
#pyautogui.hotkey - combinação de teclas.

pyautogui.PAUSE = 0.3

#abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("enter")

#passo 2: Fazer login
#selecionar o campo de email
pyautogui.click(x=742, y=512)
#escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

#passo 3: Importar a base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

#passo 4: Cadastrar um produto
for linha in tabela.index:
    print(linha)
    pyautogui.click(x=762, y=375)
    #pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo
    pyautogui.write(str(codigo))
    #passar para o proximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha,"obs"]):
        pyautogui.write(str(tabela.loc[linha,"obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    #dar scroll para subir a tela e cadastrar novo produto(pra cima é positivo, pra baixo é negativo)
    pyautogui.scroll(3000)
#passo 5: Repetir o processo de cadastro até o fim
#index é o numero de linhas