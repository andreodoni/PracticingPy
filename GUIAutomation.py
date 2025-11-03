# Project step-by-step
# Step 1: Log into the company's system
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> write text
# pyautogui.press -> press a key
# pyautogui.click -> click somewhere on the screen
# pyautogui.hotkey -> key combination
pyautogui.PAUSE = 0.3

# open the browser (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# go to the link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Step 2: Log in
# select the email field
pyautogui.click(x=685, y=451)
# type your email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # move to the next field
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # click the login button
time.sleep(3)

# Step 3: Import the products database to register
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Step 4: Register a product
for linha in tabela.index:
    # click the code field
    pyautogui.click(x=653, y=294)
    # get from the table the value of the field we want to fill
    codigo = tabela.loc[linha, "codigo"]
    # fill the field
    pyautogui.write(str(codigo))
    # move to the next field
    pyautogui.press("tab")
    # fill the field
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # submit the product (send button)
    # scroll everything up
    pyautogui.scroll(5000)
    # Step 5: Repeat the registration process until the end
