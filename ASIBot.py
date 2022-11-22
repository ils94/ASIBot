import re
from tkinter import Tk, Text, Label, END, Checkbutton, IntVar, LEFT, Frame, X
import threading
import time
import keyboard
import pyautogui

patrimonio_list = []


def multithreading(funcao):
    t = threading.Thread(target=funcao)
    t.setDaemon(True)
    t.start()


def bot():
    global patrimonio_list

    if check_tab11.get() == 0:
        filtrar = re.sub("[^0-9\n\\s]", "", patrimonios.get("1.0", END)).replace(" ", "\n")

        filtrar = "\n".join([ll.rstrip() for ll in filtrar.splitlines() if ll.strip()])

        patrimonios.delete("1.0", END)

        patrimonios.insert("1.0", filtrar)

    patrimonios.insert("1.0", patrimonios.get("1.0", END).replace(" ", ""))
    patrimonio_list = patrimonios.get("1.0", END).split("\n")
    patrimonio_list.remove("")

    aviso.config(text="Bot Iniciado.")

    for index in patrimonio_list:

        if len(index) == 10:
            index = index[2:]

        pyautogui.typewrite(index)

        if check_enter.get() == 1:
            pyautogui.press("Enter")
        elif check_tab11.get() == 1:
            for key in range(11):
                pyautogui.press("Tab")
        else:
            pyautogui.press("Tab")

    aviso.config(text="Operação Concluída.")


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

check_enter = IntVar()
check_button_enter = Checkbutton(frame, text="Usar ENTER", variable=check_enter)
check_button_enter.pack(side=LEFT, padx=5)

check_tab11 = IntVar()
check_button_tab11 = Checkbutton(frame, text="Usar TAB11", variable=check_tab11)
check_button_tab11.pack(side=LEFT, padx=5)

aviso = Label(root, text="...", width=20, height=1)
aviso.pack(pady=5)

root.bind("<FocusOut>", iniciar_bot)
root.mainloop()
