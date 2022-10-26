import re
from tkinter import Tk, Text, Label, END, Checkbutton, IntVar, LEFT, Frame, X
import threading
import time
import keyboard
import pyautogui

patrimonio_list = []


def multithreading(funcao):
    threading.Thread(target=funcao).start()


def bot():
    global patrimonio_list

    filtrar = re.sub("[^0-9\n\\s]", "", patrimonios.get("1.0", END)).replace(" ", "\n")

    filtrar = "\n".join([ll.rstrip() for ll in filtrar.splitlines() if ll.strip()])

    patrimonios.delete("1.0", END)

    patrimonios.insert("1.0", filtrar)

    patrimonio_list = patrimonios.get("1.0", END).split("\n")
    patrimonio_list.remove("")

    aviso.config(text="Bot Iniciado.")

    for index in patrimonio_list:

        if len(index) == 10:
            index = index[2:]

        pyautogui.typewrite(index)

        if check.get() == 1:
            pyautogui.press("Enter")
        else:
            pyautogui.press("Tab")

    aviso.config(text="Operação Concluída.")

    patrimonios.delete("1.0", END)


def iniciar_bot(event):
    if keyboard.is_pressed("shift"):
        time.sleep(2)
        multithreading(bot)


root = Tk()

janela_width = 250
janela_height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (janela_width / 2)
y = (screen_height / 2) - (janela_height / 2)

root.geometry("250x270+" + str(int(x)) + "+" + str(int(y)))
root.title("ASIBot")
root.iconbitmap("icones/bot.ico")
root.resizable(False, False)
root.attributes("-topmost", True)

patrimonios = Text(root, height=13)
patrimonios.pack(padx=5, pady=5)

frame = Frame(root)
frame.pack(fill=X)

check = IntVar()
checkbutton = Checkbutton(frame, text="Usar ENTER", variable=check)
checkbutton.pack(side=LEFT, padx=5)

aviso = Label(root, text="...", width=20, height=1)
aviso.pack(pady=5)

root.bind("<FocusOut>", iniciar_bot)
root.mainloop()
