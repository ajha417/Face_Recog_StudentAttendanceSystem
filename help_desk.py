from ast import Not
from cgitb import reset
import imp
from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from PIL import Image,ImageTk
from numpy import imag, pad
from tkinter import messagebox
import mysql.connector
import cv2
from cv2 import VideoCapture


class Help_Desk:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Student Details")

        title_lbl = Label(self.root,text="HELP DESK",font=("times new roman",40,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        img1 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/help_desk.jpg")
        img1 = img1.resize((1520,720),Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        first=Label(self.root,image=self.photo1)
        first.place(x=0,y=47,width=1520,height=720)

        help_lbl = Label(self.root,text="Email: ajha417@rku.ac.in",font=("times new roman",20,"bold"),bg="white",fg="blue")
        help_lbl.place(x=500,y=330,width=500,height=45)
        help_lbl1 = Label(self.root,text="Contact: 8799463393",font=("times new roman",20,"bold"),bg="white",fg="blue")
        help_lbl1.place(x=500,y=375,width=500,height=45)



if __name__=="__main__":  #this is to call main function
    root=Tk()  
    obj = Help_Desk(root)  #here we are creating object of that class
    root.mainloop()  #here we are closing root
