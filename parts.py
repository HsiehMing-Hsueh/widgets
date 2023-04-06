from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk

class TopFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #去除線條
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('TLabelframe',borderwidth=0)
        #建立花的圖
        flowerImage1 = Image.open("./images/flower1.png")
        self.flowerPhoto1 = ImageTk.PhotoImage(flowerImage1)
        self.canvas = tk.Canvas(self, width=173, height=200)
        self.canvas.pack()
        self.canvas.create_image(0, 5, image=self.flowerPhoto1, anchor='nw')
        self.canvas.create_text(0, 200, text='Flower', fill='yellow',font=('verdana', 36), anchor='sw')
        #建立鑽石圖
        daimondImage1 = Image.open("./images/diamond.png")
        self.daimondPhoto1 = ImageTk.PhotoImage(daimondImage1)
        self.canvas.create_image(175, 5, image=self.daimondPhoto1, anchor='nw')
        #建立原子圖
        atomImage1 = Image.open("./images/atom.png")
        self.atomPhoto1 = ImageTk.PhotoImage(atomImage1)
        self.canvas.create_image(280, 5, image=self.atomPhoto1, anchor='nw')
        #建立scrollbar捲動軸
        self.scrollbar = ttk.Scrollbar(self,orient='horizontal',command=self.canvas.xview)
        self.scrollbar.pack(side='bottom',fill='x')
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.configure(scrollregion=(0,0,500,200))

class MedianFrame(ttk.LabelFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        #換選項的圖示
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        #去除線條
        ttkStyle.configure('TLabelframe', borderwidth=0)
        #建立一個Frame
        radionFrame = ttk.LabelFrame(self, text='Radio Buttons')
        radionFrame.pack(side=tk.LEFT)
        #設一個字串的Var
        self.radioStringVar = tk.StringVar()
        #設radio的按鈕(多選一選項)
        self.radiobutton1 = ttk.Radiobutton(
            radionFrame, text='Option 1', variable=self.radioStringVar, value='red',command=self.radioEvent)
        self.radiobutton1.pack()
        self.radiobutton2 = ttk.Radiobutton(
            radionFrame, text='Option 2', variable=self.radioStringVar, value='green', command=self.radioEvent)
        self.radiobutton2.pack()
        self.radiobutton3 = ttk.Radiobutton(
            radionFrame, text='Option 3', variable=self.radioStringVar, value='blue', command=self.radioEvent)
        self.radiobutton3.pack()
        self.radiobutton4 = ttk.Radiobutton(
            radionFrame, text='Option 4', variable=self.radioStringVar, value='yellow', command=self.radioEvent)
        self.radiobutton4.pack()
        self.radioStringVar.set('red')
        
    # 建立(多選一選項)的事件
    def radioEvent(self):
        print(self.radioStringVar.get())
    #建立多選
