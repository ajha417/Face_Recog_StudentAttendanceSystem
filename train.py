from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from PIL import Image,ImageTk

from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Train Data")


        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        img_top = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/train.jpeg")
        img_top = img_top.resize((1530,310),Image.LANCZOS)
        self.photo_top = ImageTk.PhotoImage(img_top)
        first=Label(self.root,image=self.photo_top)
        first.place(x=0,y=55,width=1530,height=310)

        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,font=("times new roman",28,"bold"),bg="red",fg="white",cursor="hand2")
        b1_1.place(x=0,y=350,width=1530,height=59)

        img_bottom = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/train_data.jpg")
        img_bottom = img_bottom.resize((1530,310),Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(img_bottom)
        first=Label(self.root,image=self.photo_bottom)
        first.place(x=0,y=410,width=1530,height=280)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file)  for file in os.listdir(data_dir)] 

        faces = []
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #converts to gray scale image
            imageNp = np.array(img,'uint8') #unint8 is data type in python
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp) 
            cv2.waitKey(1)==13

        ids = np.array(ids)
        # ========== Train classifier and save===========
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)    
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!!!")


if __name__=="__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
