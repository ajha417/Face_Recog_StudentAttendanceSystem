from cgitb import text
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
import os
import csv
from tkinter import filedialog



mydata = []
class Attendance_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Attendance System")

        # ============text variables====
        self.var_atten_id = StringVar()
        self.var_roll_no = StringVar()
        self.var_std_name = StringVar()
        self.var_std_dep = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_status = StringVar()

        #first image goes here
        Img = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/attendance.jpg")
        Img = Img.resize((760,170),Image.ANTIALIAS)  #Antialis converts high level image to low level image 

        self.photo = ImageTk.PhotoImage(Img) #here we are storing the image it in  variable

        #now to display image on window
        first = Label(self.root,image=self.photo) #here the first parameter is window and second is image
        first.place(x=0,y=0,width=760,height=170)


        #second image goes here
        Img1 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/at1.jpg")
        Img1 = Img1.resize((760,170),Image.ANTIALIAS)  #Antialis converts high level image to low level image 

        self.photo1 = ImageTk.PhotoImage(Img1) #here we are storing the image it in  variable

        #now to display image on window
        first = Label(self.root,image=self.photo1) #here the first parameter is window and second is image
        first.place(x=760,y=0,width=760,height=170)

        # now for background image
        Img3 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/bg_image.jpg")
        Img3 = Img3.resize((1520,655),Image.ANTIALIAS)  #Antialis converts high level image to low level image 
        self.photo3 = ImageTk.PhotoImage(Img3) #here we are storing the image it in  variable

        #now to display image on window
        bg_image = Label(self.root,image=self.photo3) #here the first parameter is window and second is image
        bg_image.place(x=0,y=170,width=1520,height=655)

        title_lbl = Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=170,width=1520,height=45)

        # for main frame
        main_frame = Frame(bg_image,bd=2,bg="white") #here bd represents border and frame will be made and bg means background color
        main_frame.place(x=0,y=50,width=1500,height=610)

        # for left frame
        l_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"),fg="red")
        l_frame.place(x=10,y=10,width=720,height=580)
        #for image in left_frame
        l_img=Image.open(r"C:\Users\Amit jha\Desktop\AI_Project\Images\at4.jpg")
        l_img = l_img.resize((710,130),Image.ANTIALIAS)
        self.photoleft = ImageTk.PhotoImage(l_img)
        l_lbl = Label(l_frame,image=self.photoleft)
        l_lbl.place(x=5,y=0,width=710,height=130)

        left_insideframe = Frame(l_frame,bd=2,relief=RIDGE,bg="white") #here bd represents border and frame will be made and bg means background color
        left_insideframe.place(x=0,y=135,width=710,height=400)

        # label and entry
        # attendance id
        attendanceId_lbl = Label(left_insideframe,text="Attendace ID:",font=("times new roman",12,"bold"),bg="white",fg="black")
        attendanceId_lbl.grid(row=0,column=0,padx=10,sticky=W)
        attendanceId_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        # for roll number
        
        rollno_lbl = Label(left_insideframe,text="Roll:",font=("times new roman",12,"bold"),bg="white",fg="black")
        rollno_lbl.grid(row=0,column=2,padx=10,sticky=W)
        rollno_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_roll_no,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        # for name
        name_lbl = Label(left_insideframe,text="Name:",font=("times new roman",12,"bold"),bg="white",fg="black")
        name_lbl.grid(row=1,column=0,padx=10,sticky=W)
        name_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=2,pady=8,sticky=W)

        # for department
        department_lbl = Label(left_insideframe,text="Department:",font=("times new roman",12,"bold"),bg="white",fg="black")
        department_lbl.grid(row=1,column=2,padx=10,sticky=W)
        department_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_std_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        # for time
        time_lbl = Label(left_insideframe,text="Time:",font=("times new roman",12,"bold"),bg="white",fg="black")
        time_lbl.grid(row=2,column=0,padx=10,sticky=W)
        time_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_attendance_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=2,pady=8,sticky=W)

        # for date
        date_lbl = Label(left_insideframe,text="Date:",font=("times new roman",12,"bold"),bg="white",fg="black")
        date_lbl.grid(row=2,column=2,padx=10,sticky=W)
        date_entry = ttk.Entry(left_insideframe,width=18,textvariable=self.var_attendance_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=8,sticky=W)

        # for attendance status
        attendancestatus_lbl = Label(left_insideframe,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white",fg="black")
        attendancestatus_lbl.grid(row=3,column=0,padx=10,sticky=W)
        attendancestatus_combo = ttk.Combobox(left_insideframe,textvariable=self.var_attendance_status,font=("times new roman",12,"bold"),state="readonly")
        attendancestatus_combo["values"] = ("Status","Present","Absent")
        attendancestatus_combo.current(0)
        attendancestatus_combo.grid(row=3,column=1)


        button_frame = Frame(left_insideframe,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=345,width=700,height=33)

        #for export button
        save_btn = Button(button_frame,width=18,command=self.exportCSV,text="Export CSV",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        # for import csv button
        import_btn = Button(button_frame,width=18,command=self.importCSV,text="Import CSV",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        import_btn.grid(row=0,column=1)

        # for update button
        update_btn = Button(button_frame,width=18,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=2)

        # for delete button
        reset_btn = Button(button_frame,width=19,command=self.reset_data,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        # for right frame
        r_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),fg="red")
        r_frame.place(x=740,y=10,width=720,height=580)

        table_frame = Frame(r_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=500)


        # creating scrollbar
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Student Department")
        self.AttendanceReportTable.heading("time",text="Attendance Time")
        self.AttendanceReportTable.heading("date",text="Attendance Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=120)
        self.AttendanceReportTable.column("roll",width=120)
        self.AttendanceReportTable.column("name",width=120)
        self.AttendanceReportTable.column("department",width=120)
        self.AttendanceReportTable.column("time",width=120)
        self.AttendanceReportTable.column("date",width=120)
        self.AttendanceReportTable.column("attendance",width=120)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    # ===========fetch data function========
    def fetch_data(self,row):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in row:
            self.AttendanceReportTable.insert("",END,values=i)

    def importCSV(self):
        global mydata
        mydata.clear()  #it doesn't let the duplicate value to be shown as it clears the previous values 
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("export csv","Your data exported to "+os.path.basename(fln)+" successfully!!!")
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    # ============get cursor function=======
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_roll_no.set(rows[1])
        self.var_std_name.set(rows[2])
        self.var_std_dep.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_status.set(rows[6])

    
    # =======for reseting data=====
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_roll_no.set("")
        self.var_std_name.set("")
        self.var_std_dep.set("")
        self.var_attendance_time.set("")
        self.var_attendance_date.set("")
        self.var_attendance_status.set("Status")


if __name__=="__main__":
    root = Tk()
    obj = Attendance_System(root)
    root.mainloop()