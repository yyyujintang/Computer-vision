

from PIL import Image, ImageTk
from tkinter.constants import *
import tkinter as tk
import numpy as np
import cv2


window = tk.Tk()
window.title('edge_detector')
window.geometry('1200x1200')
global img_png
var = tk.StringVar()


def Open_Img():
    global img_png
    global Img
    var.set('Open Already')
    Img = Image.open('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\2.png')
    Img = Img.convert('L')
    img_png = ImageTk.PhotoImage(Img)

def Show_Img():
    global img_png

    label_Img = tk.Label(window, image=img_png)
    label_Img.pack(side=LEFT)

def Roberts():
    global img_png
    global Img

    im_array = np.array(Img)
    r, c = im_array.shape
    res = np.zeros((r, c))
    r_sunnzi = [[-1, -1], [1, 1]]
    for x in range(r):
        for y in range(c):
            if (y + 2 <= c) and (x + 2 <= r):
                imgChild = im_array[x:x + 2, y:y + 2]
                list_robert = r_sunnzi * imgChild
                res[x, y] = abs(list_robert.sum())
    img_png = Image.fromarray(res)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack(side=LEFT)

def Prewitt():
    global img_png
    global Img

    im_array = np.array(Img)
    r, c = im_array.shape
    res = np.zeros((r, c))
    resx = np.zeros((r, c))
    resy = np.zeros((r, c))
    p_suanziX = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    p_suanziY = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    for i in range(r - 2):
        for j in range(c - 2):
            resx[i + 1, j + 1] = abs(np.sum(im_array[i:i + 3, j:j + 3] * p_suanziX))
            resy[i + 1, j + 1] = abs(np.sum(im_array[i:i + 3, j:j + 3] * p_suanziY))
            res[i + 1, j + 1] = (resx[i + 1, j + 1] * resx[i + 1, j + 1] + resy[i + 1, j + 1] *
                                 resy[i + 1, j + 1]) ** 0.5
    img_png = Image.fromarray(res)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack(side=LEFT)
def Sobel():
    global img_png
    global Img

    im_array = np.array(Img)
    r, c = im_array.shape
    res = np.zeros((r, c))
    resx = np.zeros((r, c))
    resy = np.zeros((r, c))
    s_suanziX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    s_suanziY = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    for i in range(r - 2):
        for j in range(c - 2):
            resx[i + 1, j + 1] = abs(np.sum(im_array[i:i + 3, j:j + 3] * s_suanziX))
            resy[i + 1, j + 1] = abs(np.sum(im_array[i:i + 3, j:j + 3] * s_suanziY))
            res[i + 1, j + 1] = (resx[i + 1, j + 1] * resx[i + 1, j + 1] + resy[i + 1, j + 1] *
                                       resy[i + 1, j + 1]) ** 0.5
    img_png = Image.fromarray(res)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(window, image=img_png)
    label_Img.pack(side=LEFT)


Label_Show = tk.Label(window,
    textvariable=var,
    bg='blue', font=('Arial', 12), width=15, height=2)
Label_Show.pack()

btn_Open = tk.Button(window,
    text='Open Image',
    width=15, height=2,
    command=Open_Img)
btn_Open.pack()
# 创建显示原图按钮
btn_Show = tk.Button(window,
    text='Origin Image',
    width=15, height=2,
    command=Show_Img)
btn_Show.pack()

btn_Show = tk.Button(window,
    text='Roberts',
    width=15, height=2,
    command=Roberts)
btn_Show.pack()

btn_Show = tk.Button(window,
    text='Prewitt',
    width=15, height=2,
    command=Prewitt)
btn_Show.pack()

btn_Show = tk.Button(window,
    text='Sobel',
    width=15, height=2,
    command=Sobel)
btn_Show.pack()


# 运行整体窗口
window.mainloop()

