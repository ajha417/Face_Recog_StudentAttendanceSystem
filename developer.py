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


class Developer_Details:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Student Details")

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",40,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        img1 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/developer.jpg")
        img1 = img1.resize((1520,720),Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        first=Label(self.root,image=self.photo1)
        first.place(x=0,y=47,width=1520,height=720)

        main_frame = Frame(first,bd=2,bg="white") #here bd represents border and frame will be made and bg means background color
        main_frame.place(x=1000,y=0,width=500,height=610)


        img2 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/mypic.jpeg")
        img2 = img2.resize((200,200),Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        first=Label(main_frame,image=self.photo2)
        first.place(x=300,y=0,width=200,height=200)


        # developer info
        dev_lbl = Label(main_frame,text="Hi, I am Amit",font=("times new roman",18,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=5,y=10,width=180,height=40)

        dev_lbl = Label(main_frame,text="I am B.tech Student",font=("times new roman",18,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=5,y=50,width=240,height=40)

        dev_lbl = Label(main_frame,text="I am learning python and",font=("times new roman",18,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=5,y=90,width=260,height=40)

        dev_lbl = Label(main_frame,text="Android Development",font=("times new roman",18,"bold"),bg="white",fg="darkblue")
        dev_lbl.place(x=5,y=130,width=230,height=40)

        img3 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/laptop.jpg")
        img3 = img3.resize((500,400),Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        first=Label(main_frame,image=self.photo3)
        first.place(x=0,y=205,width=500,height=400)






if __name__=="__main__":
    root = Tk()
    obj = Developer_Details(root)
    root.mainloop()
