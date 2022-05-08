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


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1520x790+0+0")
        self.root.title("Student Details")

        # ========variables=========
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name  = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        img1 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/at1.jpg")
        img1 = img1.resize((505,135),Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        first=Label(self.root,image=self.photo1)
        first.place(x=0,y=0,width=505,height=135)


        #for second image
        img2 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/at2.jpeg")
        img2 = img2.resize((505,135),Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        first=Label(self.root,image=self.photo2)
        first.place(x=505,y=0,width=505,height=135)


        img3 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/at3.jpg")
        img3 = img3.resize((505,135),Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        first=Label(self.root,image=self.photo3)
        first.place(x=1010,y=0,width=505,height=135)


        #for background image
        img4 = Image.open("C:/Users/Amit jha/Desktop/AI_Project/Images/bg_image.jpg")
        img4 = img4.resize((1520,655),Image.LANCZOS)
        self.photo4 = ImageTk.PhotoImage(img4)
        bg_image= Label(self.root,image=self.photo4)
        bg_image.place(x=0,y=135,width=1520,height=655)

        #to set title
        title_lbl = Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1520,height=45)

        main_frame = Frame(bg_image,bd=2,bg="white") #here bd represents border and frame will be made and bg means background color
        main_frame.place(x=0,y=50,width=1500,height=610)

        #for left side frame
        l_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        l_frame.place(x=10,y=10,width=720,height=580)

        #for image in left_frame
        l_img=Image.open(r"C:\Users\Amit jha\Desktop\AI_Project\Images\at4.jpg")
        l_img = l_img.resize((710,130),Image.ANTIALIAS)
        self.photoleft = ImageTk.PhotoImage(l_img)
        l_lbl = Label(l_frame,image=self.photoleft)
        l_lbl.place(x=5,y=0,width=710,height=130)


        #for current frame
        c_frame = LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"),fg="black")
        c_frame.place(x=5,y=120,width=705,height=120)
        

        #for department label in current course frame
        department = Label(c_frame,text="Department",font=("times new roman",12,"bold"),bg="white",fg="black")
        department.grid(row=0,column=0,padx=2)
        department_combo=ttk.Combobox(c_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        department_combo["values"]=("Select Department","CSE/CE","IT","Mechanical","Civil","ECE") #here we passed the values in indexing pos
        department_combo.current(0) #current method is used to get the selected value
        department_combo.grid(row=0,column=1,padx=5,pady=7)


        #for course label in current form
        course = Label(c_frame,text="Course",font=("times new roman",12,"bold"),bg="white",fg="black")
        course.grid(row=0,column=2,padx=5,sticky=W) #here sticky protects if cells are larger than widgets
        course_combo=ttk.Combobox(c_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=7,sticky=W)


        #for year label in current form
        year = Label(c_frame,text="Year",font=("times new roman",12,"bold"),bg="white",fg="black")
        year.grid(row=1,column=0,padx=2)
        year_combo = ttk.Combobox(c_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("select year","2020-21","2021-22","2022-2023","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=7,sticky=W)


        #for semester label in current form
        sem = Label(c_frame,text="Semester",font=("times new roman",12,"bold"),bg="white",fg="black")
        sem.grid(row=1,column=2,padx=5,sticky=W)
        sem_combo = ttk.Combobox(c_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("select your semester","semester-I","semester-II")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #now create frame for student class information
        student_frame = LabelFrame(l_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"),fg="black")
        student_frame.place(x=5,y=240,width=705,height=310)

        #now create label for student id
        studentId_lbl = Label(student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white",fg="black")
        studentId_lbl.grid(row=0,column=0,padx=10,sticky=W)
        studentId_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,pady=8,sticky=W)

        #for student name
        studentName_lbl = Label(student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white",fg="black")
        studentName_lbl.grid(row=0,column=2,padx=10,sticky=W)
        studentName_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=2,pady=8,sticky=W)

        #for division 
        division_lbl = Label(student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white",fg="black")
        division_lbl.grid(row=1,column=0,padx=10,sticky=W)
        division_combo = ttk.Combobox(student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly")
        division_combo["values"] = ("A","B","C","D")
        division_combo.current(0)
        division_combo.grid(row=1,column=1)

        #for roll number
        rollNo_lbl = Label(student_frame,text="Roll No.:",font=("times new roman",12,"bold"),bg="white",fg="black")
        rollNo_lbl.grid(row=1,column=2,padx=10,sticky=W)
        rollNo_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=2,pady=8,sticky=W)

        #for gender
        gender_lbl = Label(student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white",fg="black")
        gender_lbl.grid(row=2,column=0,padx=10,sticky=W)
        # gender_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=2,pady=8,sticky=W)
        gender_combo = ttk.Combobox(student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"] = ("Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1)

        # for date of birth 
        dob_lbl = Label(student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white",fg="black")
        dob_lbl.grid(row=2,column=2,padx=10,sticky=W)
        dob_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=8,sticky=W)

        #for email
        email_lbl = Label(student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white",fg="black")
        email_lbl.grid(row=3,column=0,padx=10,sticky=W)
        email_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=8,sticky=W)

        # for phone number
        phone_lbl = Label(student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white",fg="black")
        phone_lbl.grid(row=3,column=2,padx=10,sticky=W)
        phone_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=8,sticky=W)

        # for address
        address_lbl = Label(student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white",fg="black")
        address_lbl.grid(row=4,column=0,padx=10,sticky=W)
        address_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=8,sticky=W)

        # for teacher name
        teacher_lbl = Label(student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white",fg="black")
        teacher_lbl.grid(row=4,column=2,padx=10,sticky=W)
        teacher_entry = ttk.Entry(student_frame,width=18,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=8,sticky=W)


        # for radio buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
        radio1.grid(row=6,column=0,padx=2,pady=7,sticky=W)

        
        radio2 = ttk.Radiobutton(student_frame,variable=self.var_radio1,text="No photo Sample",value="no")
        radio2.grid(row=6,column=2,padx=2,pady=7,sticky=W)

        # now we have to create frame for button
        button_frame = Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=235,width=700,height=27)

        #for save button
        save_btn = Button(button_frame,width=18,command=self.add_data,text="Save",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)

        # for update button
        update_btn = Button(button_frame,width=18,command=self.update_data,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)

        # for delete button
        delete_btn = Button(button_frame,width=18,command=self.delete_data,text="Delete",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)

        # for reset button
        reset_btn = Button(button_frame,width=19,command=self.reset_data,text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        button_frame1 = Frame(student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame1.place(x=0,y=262,width=700,height=50)

        take_photo_btn = Button(button_frame1,width=40,command=self.generate_data,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        take_photo_btn.grid(row=0,column=0,padx=4)

        update_photo_btn = Button(button_frame1,width=40,text="Update photo sample",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=0,column=1,padx=4)


        #for right side frame
        r_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="red")
        r_frame.place(x=740,y=20,width=720,height=580)

        

        r_img=Image.open(r"C:\Users\Amit jha\Desktop\AI_Project\Images\student1.jpg")
        r_img = r_img.resize((710,130),Image.ANTIALIAS)
        self.photoright = ImageTk.PhotoImage(r_img)
        r_lbl = Label(r_frame,image=self.photoright)
        r_lbl.place(x=5,y=0,width=710,height=130)

        # for search frame
        
        search_frame = LabelFrame(r_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),fg="black")
        search_frame.place(x=5,y=135,width=700,height=70)


        search_lbl = Label(search_frame,width=10,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_lbl.grid(row=0,column=0,padx=10,sticky=W)
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("select","Name","phone","semester","rollno")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        # now for entry field
        search_entry = ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=8,sticky=W)

        # now for buttons 
        search_btn = Button(search_frame,width=15,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        search_btn.grid(row=0,column=3)

        showAll_btn = Button(search_frame,width=15,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        showAll_btn.grid(row=0,column=4)

        # ==========for table frame========
        table_frame = Frame(r_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=205,width=700,height=300)


        # now for scroll bars in table frame
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","rollno","gender","dob","email","phone","address","teacher","pstatus"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # self.student_table.heading("mar",text="Marks")
        self.student_table.heading("dep",text="department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("id",text="ID No.")
        # self.student_table.heading("id",text="ID No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rollno",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("pstatus",text="PhotoSample Status")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name == "" or self.var_std_id == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("error",f"due to: {str(e)}",parent=self.root) 


    # =============fetch function============
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    # ============= get cursor=========
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    
    # =======update function======
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name == "" or self.var_std_id == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                update = messagebox.askyesno("update","Do you want to update this student details",parent = self.root)
                # we use parent = self.root to display the message on the same window not on different
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_id.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                        
                    ))
                else:
                    if not update:
                        return 
                messagebox.showinfo("success","Student details updated successfully!!!",parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as e:
                messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student detail must be selected",parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete?",parent= self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details deleted successfully!!!",parent = self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent = self.root)
    

    #===========reset function======
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("select course")
        self.var_year.set("Select year"),
        self.var_semester.set("Select your semester"),
        self.var_std_name.set(""),
        self.var_std_id.set(""),
        self.var_div.set("select division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        self.var_std_id.set("")


    # ========Generate data set take photo samples===========
    def generate_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name == "" or self.var_std_id == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                # we use parent = self.root to display the message on the same window not on different
                conn = mysql.connector.connect(host="localhost",username="root",password="",database="face_ai")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id = id+1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,student_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_std_id.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                           ))
                conn.commit() #commit helps to update connection
                self.fetch_data()
                self.reset_data() #it clears the data
                conn.close()  #it closes the connection
                    # there is haar cascade algorithm in python which identifies an faces in image
                    # ==========Load predefined data from frontal face from open cv2

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


                def face_cropped(img):
                        # we have to convert colored images into grey color
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                        # scaling factor = 1.3
                        # minimum neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped 
                        
                cap = cv2.VideoCapture(0)  #if we pass then by default it will open web camera
                img_id = 0

                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id = img_id+1
                        face = cv2.resize(face_cropped(my_frame),(450,450))  #this helps to crop the image and 450 is the size
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            # now we have to write all the image
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) #2 is scale and thickness respectively
                        cv2.imshow("face cropped",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed!!!")

            except Exception as e:
                messagebox.showerror("Error",f"Due to :{str(e)}",parent = self.root)

    
                    


if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()





