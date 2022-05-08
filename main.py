
import imp
from time import strftime
from tkinter import *
from tkinter import ttk
import tkinter  #it is used to style the tkinter widgets just like css
# pillow is library which supports for opening manipulating and saving images
from PIL import Image,ImageTk
import os 
from time import strftime
from datetime import datetime
from student_details import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance_System
from developer import Developer_Details
from help_desk import Help_Desk 

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root  
        self.root.geometry("1520x790+0+0")  #here 0 indicates the starting point of x-axis and y-axis 
        self.root.title("Face Recognition System")  #the title will be displayed on the top of window
        #first image goes here
        Img = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_1.jpg")
        Img = Img.resize((505,135),Image.ANTIALIAS)  #Antialis converts high level image to low level image 

        self.photo = ImageTk.PhotoImage(Img) #here we are storing the image it in  variable

        #now to display image on window
        first = Label(self.root,image=self.photo) #here the first parameter is window and second is image
        first.place(x=0,y=0,width=505,height=135)


        #second image goes here
        Img1 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_2.jpg")
        Img1 = Img1.resize((505,135),Image.ANTIALIAS)  #Antialis converts high level image to low level image 

        self.photo1 = ImageTk.PhotoImage(Img1) #here we are storing the image it in  variable

        #now to display image on window
        first = Label(self.root,image=self.photo1) #here the first parameter is window and second is image
        first.place(x=505,y=0,width=505,height=135)

        #third image goes here
        Img2 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_3.jpg")
        Img2 = Img2.resize((505,135),Image.ANTIALIAS)  #Antialis converts high level image to low level image 

        self.photo2 = ImageTk.PhotoImage(Img2) #here we are storing the image it in  variable

        #now to display image on window
        first = Label(self.root,image=self.photo2) #here the first parameter is window and second is image
        first.place(x=1010,y=0,width=505,height=135)


        #background image goes here
        Img3 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/bg_image.jpg")
        Img3 = Img3.resize((1520,655),Image.ANTIALIAS)  #Antialis converts high level image to low level image 
        self.photo3 = ImageTk.PhotoImage(Img3) #here we are storing the image it in  variable

        #now to display image on window
        bg_image = Label(self.root,image=self.photo3) #here the first parameter is window and second is image
        bg_image.place(x=0,y=130,width=1520,height=655)

        #Now to set title
        title_lbl = Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1520,height=40)

        # this is time function
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl,font=("times new roman",18,"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=130,height=50)
        time()

        #for student details button
        Img4 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/student.jpg")
        Img4 = Img4.resize((220,200),Image.ANTIALIAS)
        self.photo4 = ImageTk.PhotoImage(Img4)
        b1 = Button(bg_image,image=self.photo4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=200)

        b1_1=Button(bg_image,text="STUDENT DETAILS",command=self.student_details,font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b1_1.place(x=100,y=270,width=220,height=45)


        #for face detection button

        Img5 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_4.jpg")
        Img5 = Img5.resize((220,220),Image.ANTIALIAS)
        self.photo5 = ImageTk.PhotoImage(Img5)
        b2 = Button(bg_image,image=self.photo5,cursor="hand2",command=self.face_data) 
        b2.place(x=400,y=70,width=220,height=220)
        b2_1=Button(bg_image,command=self.face_data,text="FACE DETECT",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b2_1.place(x=400,y=270,width=220,height=45)


        #for attendance button
        Img6 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/attendance.jpg")
        Img6 = Img6.resize((220,220),Image.ANTIALIAS)
        self.photo6 = ImageTk.PhotoImage(Img6)
        b3 = Button(bg_image,image=self.photo6,cursor="hand2",command=self.attendance_data) 
        b3.place(x=700,y=70,width=220,height=220)
        b3_1=Button(bg_image,command=self.attendance_data,text="ATTENDANCE",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b3_1.place(x=700,y=270,width=220,height=45)


        #for help desk button

        Img7= Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/help_desk.jpg")
        Img7 = Img7.resize((220,220),Image.ANTIALIAS)
        self.photo7 = ImageTk.PhotoImage(Img7)
        b4=Button(bg_image,image=self.photo7,cursor="hand2",command=self.help_data)
        b4.place(x=1000,y=70,width=220,height=220)
        b4_1 = Button(bg_image,command=self.help_data,text="HELP DESK",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=1000,y=270,width=220,height=45)


        #for train data button
        Img8= Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/train_data.jpg")
        Img8 = Img8.resize((220,220),Image.ANTIALIAS)
        self.photo8 = ImageTk.PhotoImage(Img8)
        b4=Button(bg_image,image=self.photo8,cursor="hand2",command=self.train_data)
        b4.place(x=100,y=370,width=220,height=220)
        b4_1 = Button(bg_image,text="TRAIN DATA",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=100,y=570,width=220,height=45)


        #for photos button
        Img9= Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/Photos.png")
        Img9 = Img9.resize((220,220),Image.ANTIALIAS)
        self.photo9 = ImageTk.PhotoImage(Img9)
        b4=Button(bg_image,image=self.photo9,cursor="hand2",command=self.open_img)
        b4.place(x=400,y=370,width=220,height=220)
        b4_1 = Button(bg_image,command=self.open_img,text="GALLERY",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=400,y=570,width=220,height=45)



        #for developer section
        Img10= Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/face_2.jpg")
        Img10 = Img10.resize((220,220),Image.ANTIALIAS)
        self.photo10 = ImageTk.PhotoImage(Img10)
        b4=Button(bg_image,image=self.photo10,cursor="hand2",command=self.developer_data)
        b4.place(x=700,y=370,width=220,height=220)
        b4_1 = Button(bg_image,command=self.developer_data,text="DEVELOPERS",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=700,y=570,width=220,height=45)

        

        #for exit section
        Img11 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/exit1.jpg")
        Img11 = Img8.resize((220,220),Image.ANTIALIAS)
        self.photo11 = ImageTk.PhotoImage(Img11)
        b4=Button(bg_image,image=self.photo11,cursor="hand2",command=self.iExit)
        b4.place(x=1000,y=370,width=220,height=220)
        b4_1 = Button(bg_image,command=self.iExit,text="EXIT",font=("times new roman",15,"bold"),bg="darkblue",fg="white",cursor="hand2")
        b4_1.place(x=1000,y=570,width=220,height=45)



    def open_img(self):
        os.startfile("data")

    # =========function  buttons=====
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Attendance_System(self.new_window)

    def developer_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Developer_Details(self.new_window)

    def help_data(self):
        self.new_window= Toplevel(self.root)
        self.app = Help_Desk(self.new_window)


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition System","Do you really want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


if __name__=="__main__":  #this is to call main function
    root=Tk()  
    obj = Face_Recognition_System(root)  #here we are creating object of that class
    root.mainloop()  #here we are closing root



