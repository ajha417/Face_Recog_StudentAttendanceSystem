from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from PIL import Image,ImageTk

from tkinter import messagebox
import mysql.connector
import cv2
from cv2 import VideoCapture
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        # for left image
        img_top = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_detect.png")
        img_top = img_top.resize((700,800),Image.LANCZOS)
        self.photo_top = ImageTk.PhotoImage(img_top)

        first=Label(self.root,image=self.photo_top)
        first.place(x=0,y=52,width=700,height=720)

        # for right image
        img_bottom = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_detect1.jpg")
        img_bottom = img_bottom.resize((820,720),Image.LANCZOS)
        self.photo_bottom = ImageTk.PhotoImage(img_bottom)
        first=Label(self.root,image=self.photo_bottom)
        first.place(x=700,y=52,width=820,height=720)


        b1_1=Button(first,text="FACE RECOGNTION",font=("times new roman",18,"bold"),bg="green",fg="white",cursor="hand2",command=self.face_reco)
        b1_1.place(x=160,y=600,width=500,height=50)


    # ===========attendance========
    def mark_attendance(self,i,r,n,d):
        with open("amit.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")


    def face_reco(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,colors,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coordinates = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict =  clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
                my_cursor = conn.cursor()
                my_cursor.execute("select name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select roll from student where student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select dep from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                
                coordinates = [x,y,w,h]
            return coordinates
        
        def recognize(img,clf,faceCascade):
            coordinates= draw_boundary(img,faceCascade,1.1,10,(255,128,0),"Face",clf)
            return img 
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        
        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
