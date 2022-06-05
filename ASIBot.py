from tkinter import Tk, Button, Text, Label, END
import threading
import time
import pyautogui

patrimonio_list = []


def multithreading(funcao):
    threading.Thread(target=funcao).start()


def iniciar_bot():
    global patrimonio_list

    contador = 3

    iniciar["state"] = "disabled"

    patrimonio_list = patrimonios.get("1.0", END).split("\n")
    patrimonio_list.remove("")

    while contador >= 0:
        contagem_regressiva["text"] = contador
        contador = contador - 1
        time.sleep(1)

    contagem_regressiva["text"] = "Bot Iniciado."

    for index in patrimonio_list:
        pyautogui.typewrite(index)
        pyautogui.press("Tab")

    iniciar["state"] = "normal"
    contagem_regressiva["text"] = "Operação Concluída."


root = Tk()
root.geometry("250x250")
root.title("ASIBot")
root.iconbitmap("icones/bot.ico")
root.resizable(False, False)
root.attributes("-topmost", True)

patrimonios = Text(root, height=10)
patrimonios.pack(padx=5, pady=5)

iniciar = Button(root, text="Iniciar", width=10, height=1, command=lambda: multithreading(iniciar_bot))
iniciar.pack(pady=5)

contagem_regressiva = Label(root, text="Contagem Regressiva...", width=20, height=1)
contagem_regressiva.pack(pady=5)

root.mainloop()
