import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.constants import *
from tkinter.simpledialog import  askinteger
import numpy as np
import imageio
from PIL import Image, ImageTk
import cv2

DEBUG = False
Img = Image.open('1.png')
im_cv=cv2.imread('1.png')
Img= Img.convert('L')
im = np.array(Img)
r, c = im.shape

binary=np.zeros((r, c),dtype=np.int)
for i in range(r):
    for j in range(c):
        if(im[i][j]>100):
            binary[i][j]=255
        else:
            binary[i][j] = 0
im_copy_ero = np.zeros((r, c),dtype=np.int)
im_copy_int = np.zeros((r, c),dtype=np.int)
im_copy_dia = np.zeros((r, c),dtype=np.int)
im_copy_ext = np.zeros((r, c),dtype=np.int)
im_copy_sta = np.zeros((r, c),dtype=np.int)

root = tk.Tk()
root.title("binary edge_detection")
root.geometry('1200x1200')
var = tk.StringVar()

global SE


def show_file():
    global img_png
    img_png = ImageTk.PhotoImage(Img)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)


def get_kernal():
    global SE
    n = askinteger("Spam", "kernalsize", initialvalue=1*3)
    global step
    step=n
    SE=np.ones(shape=(step, step))

def Internal():
    global step
    global img_png
    if (step%2 == 0) or step<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    center_move = int((step-1)/2)
    for i in range(center_move, r-step+1):
        for j in range(center_move, c-step+1):
            im_copy_ero[i, j] = np.min(binary[i-center_move:i+center_move,
                                             j-center_move:j+center_move])
            im_copy_int[i, j]=binary[i, j]-im_copy_ero[i, j]
    img_png = Image.fromarray(im_copy_int)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def External():
    global step
    global img_png
    if (step%2 == 0) or step<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    center_move = int((step-1)/2)
    for i in range(center_move, r-step+1):
        for j in range(center_move, c-step+1):
            im_copy_dia[i, j] = np.max(binary[i-center_move:i+center_move,
                                             j-center_move:j+center_move])
            im_copy_ext[i, j]=im_copy_dia[i, j]-binary[i, j]
    img_png = Image.fromarray(im_copy_ext)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def Standard():
    global step
    global img_png
    if (step%2 == 0) or step<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    center_move = int((step-1)/2)
    for i in range(center_move, r-step+1):
        for j in range(center_move, c-step+1):
            im_copy_ero[i, j] = np.min(binary[i - center_move:i + center_move,
                                       j - center_move:j + center_move])
            im_copy_dia[i, j] = np.max(binary[i-center_move:i+center_move,
                                             j-center_move:j+center_move])

            im_copy_sta[i, j]=im_copy_dia[i, j]-im_copy_ero[i, j]
    img_png = Image.fromarray(im_copy_sta)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)

def D_g(n, f, b, g):
    if n == 0:
        return f
    if n == 1:
        if DEBUG:
            cv2.imshow('g', g)
            cv2.imshow('img', cv2.dilate(f, b, iterations=1))
            cv2.imshow('min', np.min((cv2.dilate(f, b, iterations=1), g), axis=0))
            # cv2.imshow('c',np.min((cv2.dilate(f,b,iterations=1),g),axis=0)-cv2.dilate(f,b,iterations=1))
            cv2.waitKey()
            cv2.destroyAllWindows()
            # from IPython.core.debugger import Tracer; Tracer()()
            # print((cv2.dilate(f,b,iterations=1)<=g).all())
        return np.min((cv2.dilate(f, b, iterations=1), g), axis=0)
    return D_g(1, D_g(n - 1, f, b, g), b, g)


# 膨胀重建
def R_g_D(f, b, g):
    if DEBUG:
        cv2.imshow('origin', f)
        cv2.waitKey()
        # cv2.destroyAllWindows()
    img = f
    while True:
        new = D_g(1, img, b, g)
        cv2.destroyAllWindows()
        if (new == img).all():
            return img
        img = new
# 重建开操作
def O_R(n, f, b, conn):
    erosion = cv2.erode(f, b, iterations=n)
    return R_g_D(erosion, conn, f)

def Conditional_dilation():
    global img_png
    global step
    im_recon = O_R(1, im_cv, np.ones((step, step)), np.ones((step, step)))
    img_png = Image.fromarray(im_recon)
    img_png = ImageTk.PhotoImage(img_png)
    label_Img = tk.Label(root, image=img_png)
    label_Img.pack(side=LEFT)



btn_show_file = tk.Button(root,
    text='open image',
    bg='blue',
    width=15, height=1,
    command=show_file)
btn_show_file.pack(expand=0, fill="none", side="top", anchor="w")


tk.Button(root, text='SE size',  width=15, bg='yellow',height=1, command=get_kernal).pack(expand=0, fill="none", side="top", anchor="w")


btn_Internal = tk.Button(root,
    text='Internal Edge',bg='green',
    width=15, height=1,
    command=Internal)
btn_Internal.pack(expand=0, fill="none", side="top", anchor="w")

btn_External = tk.Button(root,
    text='External Edge',bg='pink',
    width=15, height=1,
    command=External)
btn_External.pack(expand=0, fill="none", side="top", anchor="w")

btn_Standard = tk.Button(root,bg='Orchid',
    text='Standard Edge',
    width=15, height=1,
    command=Standard)
btn_Standard.pack(expand=0, fill="none", side="top", anchor="w")

btn_cd = tk.Button(root,
    text='Conditional dilation',bg='OrangeRed',
    width=15, height=1,
    command=Conditional_dilation)
btn_cd.pack(expand=0, fill="none", side="top", anchor="w")

root.mainloop()


