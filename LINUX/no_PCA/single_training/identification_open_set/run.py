import customtkinter
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from sys import platform
from tkinter import messagebox
import os


def show_popup(title,comment):
    messagebox.showinfo(title,comment)

def on_closing():
    if messagebox.askokcancel("Closure", "Do you really want to close the application?"):
        root.destroy()



def testing():
    os.system("bash start.sh")


def runtime_reid():
    os.system("bash reid_runtime.sh")


width = 589
height = 600

root = customtkinter.CTk()
root.title("Voice Re-identification without PCA")
# Imposta la funzione on_closing come gestore della chiusura della finestra
root.protocol("WM_DELETE_WINDOW", on_closing)

x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.resizable(False, False)

#root.iconbitmap("sport_icon.ico")


# Carica l'immagine da utilizzare come sfondo 
background_image = Image.open("../pic1.png")
enhancer = ImageEnhance.Brightness(background_image)
# Scurisci l'immagine
darkened_background = enhancer.enhance(0.6)  # Modifica il valore per regolare l'intensità del darkening
draw = ImageDraw.Draw(darkened_background)
font = ImageFont.truetype("../Gobold Bold Italic.otf", 50)
draw.text((400, 350), "Voice \n  re-identification", font=font, fill="#93f233")
darkened_background.save("../pic1_darkened.png")


# Carica l'immagine scurita come sfondo
background_image = PhotoImage(file="../pic1_darkened.png")
# Crea una label con l'immagine come sfondo
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Copre l'intera finestra principale


btn1 = customtkinter.CTkButton(master = root, text = "Run", height=40, corner_radius=8, fg_color="transparent",
                hover_color="white", border_color="#93f233", text_color="#93f233", border_width=2, command=testing)
btn1.place(relx=0.3, rely=0.7, anchor="center")


root.mainloop()
