from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk

class TopFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #建立花的圖
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        canvas = tk.Canvas(self, width=500, height=200)
        canvas.pack()
        canvas.create_image(0, 5, image=self.flowerPhoto1, anchor='nw')
        canvas.create_text(0, 200, text='Flower', fill='yellow',font=('verdana', 36), anchor='sw')
        #建立鑽石圖
        daimondImage1 = Image.open("./images/diamond.png")
        self.daimondPhoto1 = ImageTk.PhotoImage(daimondImage1)
        canvas.create_image(175, 5, image=self.daimondPhoto1, anchor='nw')
        #建立原子圖
        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        canvas.create_image(280, 5, image=self.atomPhoto1, anchor='nw')

