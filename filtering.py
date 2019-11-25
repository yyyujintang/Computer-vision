# coding=gbk
import tkinter as tk
from skimage import io
import numpy as np
from PIL import Image, ImageTk
import cv2
from tkinter.constants import *
from tkinter.simpledialog import askstring, askinteger, askfloat

Img = Image.open('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\2.png')
Img= Img.convert('L')
im = np.array(Img)
r, c = im.shape
im_copy_med = np.zeros((r, c))
im_copy_mea = np.zeros((r, c))
im_copy_gua = np.zeros((r, c))



for i in range(0,r):
    for j in range(0,c):
        im_copy_med[i][j]=im[i][j]
        im_copy_mea[i][j] = im[i][j]
        im_copy_gua[i][j] = im[i][j]


root = tk.Tk()
root.title("fitering")
root.geometry('1200x1200')
var = tk.StringVar()


def get_kernal():
    n = askinteger("Spam", "kernalsize", initialvalue=1*3)
    global step
    step=n

def Open_Img():
    global img_png
    global Img
    var.set('Open Already')
    Img = Image.open('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\2.png')
    Img = Img.convert('L')
    img_png = ImageTk.PhotoImage(Img)

def Show_Img():
    global img_png
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def m_filter(x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]

def Median():
    global img_png
    for i in range(int(step/2),r-int(step/2)):
        for j in range(int(step/2),c-int(step/2)):
            im_copy_med[i][j] = m_filter(i, j, step)


    img_png = Image.fromarray(im_copy_med)
    img_png = img_png.convert('RGB')
    img_png.save('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\Meadian.png')
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def mean_filter(x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s
def Mean():
    global img_png
    for i in range(int(step / 2), r - int(step / 2)):
        for j in range(int(step / 2), c - int(step / 2)):
            im_copy_mea[i][j] = mean_filter(i, j, step)


    img_png = Image.fromarray(im_copy_mea)
    img_png = img_png.convert('RGB')
    img_png.save('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\Mean.jpg')

    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def get_sigma():
    m = askinteger("Spam", "sigma", initialvalue=0*0)
    global sigma
    sigma=m



def Guassian():
    global img_png


    img_png = cv2.GaussianBlur(im_copy_gua, (step, step), sigma)

    cv2.imwrite('F:\\Pycharm Anaconda Python File\\.idea\CV_Project1_517021910275\\Guassain.png',img_png)
    img_png = Image.fromarray(img_png)


    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)


Label_Show = tk.Label(root,
    textvariable=var,
    bg='blue', font=('Arial', 12), width=15, height=2)
Label_Show.pack()

btn_Open = tk.Button(root,
    text='Open Image',
    width=15, height=2,
    command=Open_Img)
btn_Open.pack()


btn_Show = tk.Button(root,
    text='Origin Image',
    width=15, height=2,
    command=Show_Img)
btn_Show.pack()

tk.Button(root, text='Kernel Size', command=get_kernal).pack()



btn_Show = tk.Button(root,
    text='Median Filter',
    width=15, height=2,
    command=Median)
btn_Show.pack()



btn_Show = tk.Button(root,
    text='Mean Filter',
    width=15, height=2,
    command=Mean)
btn_Show.pack()


tk.Button(root, text='sigma', command=get_sigma).pack()


btn_Show = tk.Button(root,
    text='Guassian Filter',
    width=15, height=2,
    command=Guassian)
btn_Show.pack()
root.mainloop()
