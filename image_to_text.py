import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from math import log
from tkinter import *
from tkinter import filedialog
import os.path
from os import path

def Laplacien(U):
	(I,J,K)=np.shape(U)
	delt=U.copy()
	for k in range(K):
		for i in range(1,I-1):
			for j in range(1,J-1):
				#delt[i,j,k]=(U[i-1,j,k]+U[i+1,j,k]+U[i,j-1,k]+U[i,j+1,k])-4*U[i,j,k]
				delt[i,j,k]=max(((U[i-1,j,k]+U[i+1,j,k]+U[i,j-1,k]+U[i,j+1,k])-4*U[i,j,k]),0)
	return delt

def log_img(U):
	M=np.full(np.shape(U),0.0001, dtype=np.float64)
	(I,J,K)=np.shape(U)
	for k in range(K):
		for i in range(I):
			for j in range(J):
				if(U[i,j,k]!=0) :
					M[i,j,k]=log(U[i,j,k])
	return M

def exp_img(U):
	return np.exp(U,dtype=np.float64)

def eqa_img(U):
	n=U.copy()
	n=log_img(U)
	for i in range(6):
		N=n+(0.5*Laplacien(n))
		n=N
	return log_img(U)-N

def askopen():
	image_name=filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("Image","*.png *.jpg *.jpeg"),("all files","*.*")) )
	textentry.delete(0, 'end')
	textentry.insert(0,image_name)
	def click():
		image = img.imread(image_name)
		plt.imshow(exp_img(eqa_img(image)))
		plt.axis('off')
		plt.show()
	if(path.isfile(image_name)) :
		Button(window,font=button_font,fg='white',bg=button_color,text='OK',width=5,command=click).place(x=550,y=280)
def text_check():
	image_name=textentry.get()
	def click():
		image = img.imread(image_name)
		plt.imshow(exp_img(eqa_img(image)))
		plt.axis('off')
		plt.show()
	ext=image_name.split('.')
	extention=ext[-1].upper()
	if(path.isfile(image_name) and (extention=='PNG' or extention=='JPG' or extention=='JPEG')) :
		Button(window,font=button_font,fg='white',bg=button_color,text='OK',width=5,command=click).place(x=550,y=280)
	else:
		Button(window,font=button_font,fg='white',bg=button_color,text='OK',width=5,state=DISABLED).place(x=550,y=280)


backgrounrd_color="#f58442"
button_color="#576161"
button_font="none 12 bold"
window=Tk()
window.title("Image To text")
window.resizable(0, 0)
window.geometry("653x350")
window.iconbitmap('./.resources/icon.ico')
Button(window,font=button_font,fg='white',bg=button_color,text='browse',width=6,command=askopen).place(x=540,y=45)
Button(window,font=button_font,fg='white',bg=button_color,text='check',width=5,command=text_check).place(x=470,y=45)
Button(window,font=button_font,fg='white',bg=button_color,text='OK',width=5,state=DISABLED).place(x=550,y=280)
textentry=Entry(window,bg="white",width=70,text="test")
textentry.place(x=25,y=50)
window.configure(background=backgrounrd_color)
window.mainloop()