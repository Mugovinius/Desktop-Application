from tkinter import *
import customtkinter
import datetime
from datetime import date
from datetime import datetime,timedelta
import sqlite3
from tkinter import ttk
import calendar
from tkcalendar import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tksheet import Sheet
from PIL import ImageTk, Image
import os, sys
import win32print
import win32api
import tempfile
import itertools
import requests
import socket
from twilio.rest import Client
import json

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
spacer=" "#empty space to position title at the center
root.title(200*spacer+"SAMARIA MILK GROUP")
root.geometry("1360x800")
root.iconbitmap("logo1.ico")
root.state('zoomed')
class Login:
    def __init__(self, master) -> None:
        #create label widget containing logo
        self.title_frame=Frame(master)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1=" LOGIN"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Mega Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,fg_color="maroon",text_color="white", text_font=("Consollas 10", -30, "italic"),width=200,height=35)
        self.my_sub_text.grid(row=1, column=1,padx=10,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1, fg_color="orange",text_color="white", text_font=("Consollas 10", -35, "bold","underline"),width=300,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4, padx=10)
        #signup frame
        self.signup_frame=customtkinter.CTkFrame(master,corner_radius=8)
        self.signup_frame.pack(anchor="e",pady=5)
        self.signup_button=customtkinter.CTkButton(self.signup_frame, text="Sign Up",fg_color="purple",text_color="white",text_font=("Consollas 10", -20,"bold"),width=200, height=30,command=self.sign_up)
        self.signup_button.pack(padx=30)
        #right frame
        self.right_frame=customtkinter.CTkFrame(master,border_color="green",border_width=5,corner_radius=8,width=800,height=600)
        self.right_frame.pack(fill=BOTH, expand=YES)
        
        #leftframe
        self.left_frame=customtkinter.CTkFrame(self.right_frame,corner_radius=10,width=400,height=450)
        self.left_frame.pack(anchor="center",pady=10)
        #login
        #variable
        self.c_v1=IntVar(value=0)
        self.login_label=customtkinter.CTkLabel(self.left_frame, text=" USER LOGIN", fg_color="darkblue",text_color="white", text_font=("Consollas 10", -40, "underline", "bold"),width=300,height=50)
        self.login_label.grid(row=0, column=0, columnspan=15, rowspan=2, pady=10,padx=30,sticky=EW)
        self.img1= ImageTk.PhotoImage(Image.open('user.png'))
        self.image_label1=customtkinter.CTkLabel(self.left_frame, image=self.img1)
        self.image_label1.grid(row=2, column=0, columnspan=15,padx=30)
        self.username_label=customtkinter.CTkLabel(self.left_frame, text="UserName:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -25, "bold"),width=200,height=35)
        self.username_label.grid(row=3, column=0,columnspan=8, rowspan=2,pady=20, padx=30)
        self.username_entry=customtkinter.CTkEntry(self.left_frame, width=300,height=40,corner_radius=8,placeholder_text="Enter Username",placeholder_text_color="purple",border_color="blue")
        self.username_entry.grid(row=3, column=8,rowspan=2,pady=20,padx=20,columnspan=7)
        self.password_label=customtkinter.CTkLabel(self.left_frame, text="Password:",fg_color="maroon",text_color="white",text_font=("Consollas 10", -25 ,"bold"),width=200,height=35)
        self.password_label.grid(row=5, column=0,columnspan=8,padx=30)
        self.password_entry=customtkinter.CTkEntry(self.left_frame,show="*", width=300,height=40,corner_radius=8,placeholder_text="Enter Password",placeholder_text_color="purple",border_color="blue")
        self.password_entry.grid(row=5, column=8,columnspan=7)
        self.showpassword_ck=customtkinter.CTkCheckBox(self.left_frame,text="Show Password",text_font=("Consollas 10", -20, "bold"),text_color="green",variable=self.c_v1,command=self.my_show)
        self.showpassword_ck.grid(row=6,column=0,padx=20,pady=10,columnspan=10)
        self.forgot_password_button=customtkinter.CTkButton(self.left_frame,text="Forgot Password ?",fg_color="purple",text_color="white",text_font=("Consollas 10", -15,"bold"),width=200,height=30,command=self.forgot_password)
        self.forgot_password_button.grid(row=6,column=10,columnspan=5,padx=10)
        self.login_button=customtkinter.CTkButton(self.left_frame, text="LOGIN", fg_color="maroon",text_color="white",text_font=("Consollas 10", -25,"bold"),width=250, height=50, command=self.user_login)
        self.login_button.grid(row=7, column=0, columnspan=15,pady=10,padx=30,sticky=EW)
        
        #show password
    def my_show(self):
        if(self.c_v1.get()==0):
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    #forgot password    
    def update_table(self):
        if self.enter_new_pass_entry.get()!=self.confirm_new_pass_entry.get():
            messagebox.showerror("ERROR", "Password does not match")
            self.enter_new_pass_entry.delete(0, END)
            self.confirm_new_pass_entry.delete(0, END)
            self.jibu_entry.delete(0, END)
            self.enter_username_entry.delete(0, END)
            self.top3.destroy()
            self.top2.destroy()
        else:
            #update table
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
            results=c.fetchall()
            for record in results:
                c.execute("""UPDATE User_Data SET
                            UserName=:u_name,
                            Password=:pwd,
                            Security_Question=:s_quiz,
                            Security_Answer=:s_ans,
                            User_Mode=:u_mode

                            WHERE UserName=:u_name""",
                            {
                                'u_name' : record[0],
                                'pwd': self.enter_new_pass_entry.get(),
                                's_quiz': record[2],
                                's_ans' :record[3],
                                'u_mode': record[4]
                                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations", "Succesfully modified password")
                #clear entries
                self.enter_new_pass_entry.delete(0, END)
                self.confirm_new_pass_entry.delete(0, END)
                self.jibu_entry.delete(0, END)
                self.enter_username_entry.delete(0, END)
                self.top3.destroy()
                self.top2.destroy()
                            
    def new_password(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Security_Answer FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
        jibu=c.fetchone()
        if jibu!=self.jibu_entry.get():
            messagebox.showerror("ERROR", "Wrong Answer TRY AGAIN")
            self.jibu_entry.delete(0, END)
            self.enter_username_entry.delete(0, END)
            self.top2.destroy()
        else:
            self.top3=Toplevel()
            self.top3.title("SAMARIA MILK GROUP")
            self.top3.iconbitmap("logo1.ico")
            new_pass_frame=Frame(self.top3)
            new_pass_frame.pack(anchor="w")
            self.change_pass_label=Label(new_pass_frame, text="CHANGE PASSWORD",fg="purple",bg="white",font=("Consollas 10", 20,"underline", "bold"))
            self.change_pass_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
            self.enter_new_pass_label=Label(new_pass_frame, text="Enter New Password:", fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.enter_new_pass_label.grid(row=1, column=0, padx=10, pady=10)
            self.enter_new_pass_entry=customtkinter.CTkEntry(new_pass_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="New Password",placeholder_text_color="purple")
            self.enter_new_pass_entry.grid(row=1, column=1, padx=10, pady=10)
            self.confirm_new_pass_label=Label(new_pass_frame, text="Confirm New Password:",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.confirm_new_pass_label.grid(row=2, column=0, padx=10, pady=10)
            self.confirm_new_pass_entry=customtkinter.CTkEntry(new_pass_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Confirm Password",placeholder_text_color="purple")
            self.confirm_new_pass_entry.grid(row=2, column=1, padx=10, pady=10)
            self.change_new_pass_button=customtkinter.CTkButton(new_pass_frame, text="CHANGE PASSWORD",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40, command=self.update_table)
            self.change_new_pass_button.grid(row=3, column=0, columnspan=5, padx=10, pady=10,)
    def retreive_password(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Security_Question FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
        swali=c.fetchone()
        conn.commit()
        conn.close()
        if swali==None:
            messagebox.showerror("ERROR", "Enter Correct USERNAME")
            self.enter_username_entry.delete(0, END)
            self.top2.destroy()
        else:
            self.request_label=Label(self.forgot_frame, text="Answer this question with correct answer provided during registration!")
            self.request_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
            self.question_label=Label(self.forgot_frame, text="QUESTION",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.question_label.grid(row=4, column=0, padx=10, pady=10)
            self.answer_label=Label(self.forgot_frame, text="ANSWER",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.answer_label.grid(row=4, column=1, padx=10, pady=10)
            self.swali_label=Label(self.forgot_frame, text=swali)
            self.swali_label.grid(row=5, column=0, padx=10, pady=10)
            self.jibu_entry=customtkinter.CTkEntry(self.forgot_frame, width=150, height=40,border_color="blue",placeholder_text="Answer",placeholder_text_color="purple")
            self.jibu_entry.grid(row=5, column=1, padx=10, pady=10)
            self.change_password_button=customtkinter.CTkButton(self.forgot_frame, text="CHANGE PASSWORD",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40,command=self.new_password)
            self.change_password_button.grid(row=6, column=0,columnspan=4, padx=10, pady=10)
            
    def forgot_password(self):
        self.top2=Toplevel()
        self.top2.title("SAMARIA MILK GROUP")
        self.top2.iconbitmap("logo1.ico")
        self.forgot_frame=Frame(self.top2)
        self.forgot_frame.pack(anchor="w")
        self.retreive_password_label=Label(self.forgot_frame, text="RETREIVE PASSWORD",fg="purple",bg="white",font=("Consollas 10", 20,"underline", "bold"))
        self.retreive_password_label.grid(row=0, column=0,columnspan=8, padx=10, pady=10)
        self.enter_username_label=Label(self.forgot_frame, text="ENTER USERNAME:",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
        self.enter_username_label.grid(row=1, column=0, padx=10, pady=10)
        self.enter_username_entry=customtkinter.CTkEntry(self.forgot_frame, width=150, height=40,border_color="blue",placeholder_text="Username",placeholder_text_color="purple")
        self.enter_username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.submit_button=customtkinter.CTkButton(self.forgot_frame, text="SUBMIT",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40, command=self.retreive_password)
        self.submit_button.grid(row=2, column=0,columnspan=6, padx=20, pady=10)
 
    def user_login(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE UserName=?", (self.username_entry.get(),))
        login_pass=c.fetchone()
        conn.commit()
        conn.close()
        if login_pass==None:
            messagebox.showerror("ERROR","Unknown Username, Check Username And Try Again")
        else:
            if login_pass!=self.password_entry.get():
                messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again")
            else:
                global server
                server=self.username_entry.get()
                messagebox.showinfo("Login Succesful", "Welcome"+"\t"+ f'{self.username_entry.get()}')
                self.username_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.load_home_window()
    #signup
    def add_user(self):
        if self.pass_word_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("ERROR","Password Does Not Match",parent=self.top)
        else:
            if self.clicked.get()=="User":
                self.top1=Toplevel()
                self.top1.title("SAMARIA MILK GROUP")
                self.top1.iconbitmap("logo1.ico")
                top_frame=Frame(self.top1)
                top_frame.pack(anchor="w")
                self.administrator_label=Label(top_frame, text="Enter Administrator Password:",fg="darkblue", bg="white", font=("Consollas 10", 10, "bold"))
                self.administrator_label.grid(row=0,column=0, padx=10, pady=10)
                self.administrator_entry=customtkinter.CTkEntry(top_frame,show="*", width=150,height=40,text_color="purple",placeholder_text="Enter Admin Password", placeholder_text_color="purple",border_color="blue")
                self.administrator_entry.grid(row=0, column=1, padx=10, pady=10)
                self.ok_button=customtkinter.CTkButton(top_frame, text="VERIFY",fg_color="maroon", text_color="white", text_font=("Consollas 10", -20,"bold"),width=200, height=50,command=self.verify_admin)
                self.ok_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            else:
                #insert data into our table
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT * FROM User_Data WHERE User_Mode='Administrator'")
                results=c.fetchall()
                wakuu=len(results)
                conn.commit()
                conn.close()
                if (wakuu >= 1):
                    messagebox.showerror("Error", "There can only be one Administrator",parent=self.top)
                else:
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO User_Data VALUES(:UserName, :Password, :Security_Question, :Security_Answer, :User_Mode)",
                                {
                                    "UserName":self.user_name_entry.get(),
                                    "Password":self.pass_word_entry.get(),
                                    "Security_Question":self.selected.get(),
                                    "Security_Answer": self.answer_entry.get(),
                                    "User_Mode": self.clicked.get()
                                    })
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Congratulations", "New Administrator User Succesfully Added")
                self.user_name_entry.delete(0, END)
                self.pass_word_entry.delete(0, END)
                self.answer_entry.delete(0, END)
                #self.top.destroy()
    def verify_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin=c.fetchone()
        conn.commit()
        conn.close()
        if self.administrator_entry.get()!=admin:
            messagebox.showerror("ERROR", "Administrator Password is incorrect,Check password and try again",parent=self.top)
            self.top1.destroy()
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("INSERT INTO User_Data VALUES(:UserName, :Password, :Security_Question, :Security_Answer, :User_Mode)",
                        {
                            "UserName":self.user_name_entry.get(),
                            "Password":self.pass_word_entry.get(),
                            "Security_Question":self.selected.get(),
                            "Security_Answer": self.answer_entry.get(),
                            "User_Mode": self.clicked.get()
                            })
            conn.commit()
            conn.close()
            messagebox.showinfo("Congratulations", "New User Succesfully Added")
            self.administrator_entry.delete(0, END)
            self.user_name_entry.delete(0, END)
            self.pass_word_entry.delete(0, END)
            self.answer_entry.delete(0, END)
            self.top1.destroy()
            self.top.destroy()
    def sign_up(self):
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top)
        my_frame.pack(anchor="w")
        self.sign_up_label=customtkinter.CTkLabel(my_frame, text="SIGN UP", fg_color="purple", text_color="white", text_font=("Consollas 10", 30, "underline", "bold"),width=200,height=30)
        self.sign_up_label.grid(row=0, column=0, columnspan=10,padx=10, pady=10)
        self.instruction_label=customtkinter.CTkLabel(my_frame, text="*** Please fill each detail", fg_color="red", text_color="white", text_font=("Consollas 10", -15, "underline"),width=300,height=25)
        self.instruction_label.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        self.user_name_label=customtkinter.CTkLabel(my_frame, text="Enter UserName:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.user_name_label.grid(row=2, column=0, padx=10, rowspan=2, pady=10)
        self.user_name_entry=customtkinter.CTkEntry(my_frame,width=200, height=40,border_color="blue",placeholder_text="Enter Username",placeholder_text_color="purple")
        self.user_name_entry.grid(row=2, column=1, rowspan=2, padx=10, pady=10)
        self.pass_word_label=customtkinter.CTkLabel(my_frame, text="Enter Password:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.pass_word_label.grid(row=4, column=0, rowspan=2, padx=10, pady=10)
        self.pass_word_entry=customtkinter.CTkEntry(my_frame, show="*", width=200, height=40,border_color="blue",placeholder_text="Enter Password",placeholder_text_color="purple")
        self.pass_word_entry.grid(row=4, column=1, rowspan=2, padx=10, pady=10)
        self.confirm_pass_word_label=customtkinter.CTkLabel(my_frame, text="Confirm Password:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.confirm_pass_word_label.grid(row=6, column=0, rowspan=2, padx=10, pady=10)
        self.confirm_pass_entry=customtkinter.CTkEntry(my_frame,width=200,height=40,border_color="blue",placeholder_text="Confirm Password",placeholder_text_color="purple",show="*")
        self.confirm_pass_entry.grid(row=6,column=1,rowspan=2,padx=10,pady=10)
        self.security_questions_label=customtkinter.CTkLabel(my_frame, text="SECURITY QUESTIONS", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=250,height=30)
        self.security_questions_label.grid(row=8, column=0, padx=10,pady=10)
        self.answer_label=customtkinter.CTkLabel(my_frame, text="ANSWER", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=200,height=30)
        self.answer_label.grid(row=8, column=1,padx=10, pady=10)
        #menu
        self.selected=StringVar()
        self.security_menubar=customtkinter.CTkOptionMenu(my_frame, variable=self.selected,values=["What's your Pet Name?","What's your Mother Maiden's Name?","What's your Favorite place?"],width=250, height=50,fg_color="red",dropdown_text_color="purple", text_color="black")
        self.security_menubar.grid(row=9, column=0, padx=10, pady=10)
        self.answer_entry=customtkinter.CTkEntry(my_frame, width=200,height=40,border_color="blue",placeholder_text="Answer",placeholder_text_color="violet",text_color="purple")
        self.answer_entry.grid(row=9, column=1, padx=10, pady=10)
        #option menu
        self.user_mode_label=customtkinter.CTkLabel(my_frame, text="Set User AS:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=200,height=30)
        self.user_mode_label.grid(row=10, column=0, padx=10, pady=10)
        self.clicked=StringVar()
        self.user_mode_menu=customtkinter.CTkOptionMenu(my_frame, variable=self.clicked,values=["Administrator", "User"],width=150, height=50,fg_color="red",dropdown_text_color="purple", text_color="black")
        self.user_mode_menu.grid(row=10, column=1,padx=10, pady=10)
        #signup button
        self.sign_up_button=customtkinter.CTkButton(my_frame, text="SIGN UP",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=250, height=60,command=self.add_user)
        self.sign_up_button.grid(row=11, column=0, columnspan=8, padx=10, pady=10)


    def load_home_window(self):
        home=Landing_Page(root)
        root.mainloop()
class Landing_Page:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x800")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
        #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)       
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        report_menu=Menu(my_menu,tearoff=0)
        farmer_menu=Menu(report_menu,tearoff=0)
        farmer_menu.add_command(label="Daily Report",command=self.farmers_daily_report)
        farmer_menu.add_separator()
        farmer_menu.add_command(label="Monthly Report", command=self.farmers_monthly_report)
        my_menu.add_cascade(label="Report", menu=report_menu)
        report_menu.add_cascade(label="Farmer's Report",menu=farmer_menu)
        report_menu.add_separator()
        report_menu.add_command(label="Daily Report", command=self.verify_daily_report)
        report_menu.add_separator()
        report_menu.add_command(label="Monthly Report",command=self.verify_monthly_report)
        

        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Stuck?..get help",command=self.help_menu)

        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

        notifications_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Notifications", menu=notifications_menu)
        notifications_menu.add_command(label="Notify Farmers",command=self.notifications)
        
        #dates
        self.currentDateTime=date.today()
        self.today=self.currentDateTime.strftime("%A - %B %d, %Y")
        self.count=0
        self.mwezi=datetime.now().month
        self.mwaka=datetime.now().year
        self.monthm=datetime.now().month
        self.time=datetime.now()
        self.today1=self.time.strftime("%m/%d/%Y")
        self.today2=self.time.strftime("%d/%m/%Y")
        self.Time=self.time.strftime("%I:%M:%S %p")
        #variable
        self.mode=StringVar()
        self.start=1
        self.clicked1=StringVar()
        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1=" WELCOME"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Mega Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,fg_color="maroon",text_color="white", text_font=("Consollas 10", -30, "italic"),width=200,height=35)
        self.my_sub_text.grid(row=1, column=1,padx=10,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1, fg_color="orange",text_color="white", text_font=("Consollas 10", -35, "bold","underline"),width=300,height=35)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4, padx=10)
        #container frame
        self.log_frame=customtkinter.CTkFrame(self.top0)
        self.log_frame.pack(anchor="e",padx=10,pady=2)
        self.logout_button=customtkinter.CTkButton(self.log_frame, text="LOG OUT",fg_color="maroon", text_color="white", text_font=("Consollas 10", -20, "bold"),width=300,height=30,command=self.user_logout)
        self.logout_button.pack()
        #container frame
        self.container_frame=customtkinter.CTkFrame(self.top0, border_color="green", border_width=7,corner_radius=10,width=400,height=450)
        self.container_frame.pack(side=LEFT,fill=BOTH,expand=YES)
        #rightframe
        self.right_frame=customtkinter.CTkFrame(self.container_frame,corner_radius=10,width=400,height=450)
        self.right_frame.pack(side=LEFT,anchor="w",padx=50)
        #data
        self.menu_title_label=customtkinter.CTkLabel(self.right_frame, text="MENU", fg_color="green", text_color="white", text_font=("Consollas 10", -30, "underline","bold"),width=200,height=40)
        self.menu_title_label.grid(row=0, column=0,columnspan=12, padx=20, pady=10,sticky=EW)
        #images
        records_image=ImageTk.PhotoImage(Image.open("customer.png").resize((30,20),Image.ANTIALIAS))
        sales_image=ImageTk.PhotoImage(Image.open("sale.png").resize((30,20),Image.ANTIALIAS))
        loans_image=ImageTk.PhotoImage(Image.open("loan.png").resize((30,20),Image.ANTIALIAS))
        feeds_image=ImageTk.PhotoImage(Image.open("feed.png").resize((30,20),Image.ANTIALIAS))
        payments_image=ImageTk.PhotoImage(Image.open("pay.png").resize((30,20),Image.ANTIALIAS))
        #buttons
        self.customer_records_button=customtkinter.CTkButton(self.right_frame, text="RECORDS", image=records_image,compound="right",width=240, height=60,corner_radius=8,text_font=("Consollas 10", -20,"bold"),fg_color="blue",text_color="white", command=self.load_customer_records_window)
        self.customer_records_button.grid(row=1, column=0, columnspan=6, padx=25, pady=30)
        self.customer_sales_button=customtkinter.CTkButton(self.right_frame, text="FARMER'S SALES", image=sales_image,compound="right",width=240, height=60,corner_radius=8, fg_color="maroon", text_color="white", text_font=("Consollas 10", -20, "bold"), command=self.load_customer_sales_window)
        self.customer_sales_button.grid(row=2, column=0, columnspan=6, padx=20, pady=30)
        self.customer_local__sales_button=customtkinter.CTkButton(self.right_frame, text="LOCAL SALES", image=sales_image, compound="right",width=240, height=60,corner_radius=8,fg_color="blue", text_color="white", text_font=("Consollas 10", -20, "bold"),command=self.load_local_sales_window)
        self.customer_local__sales_button.grid(row=1, column=6, columnspan=6, padx=35, pady=30)
        self.customer_loans_button=customtkinter.CTkButton(self.right_frame, text="ADVANCE", image=loans_image,compound="right",width=240,height=60, corner_radius=8,fg_color="maroon", text_color="white", text_font=("Consollas 10", -20, "bold"),command=self.load_loan_window)
        self.customer_loans_button.grid(row=2, column=6, columnspan=6, padx=35, pady=30)
        self.customer_feeds_button=customtkinter.CTkButton(self.right_frame, text="FEEDS",image=feeds_image, compound="right",width=240, height=60,corner_radius=8, fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"), command=self.select_feeds)
        self.customer_feeds_button.grid(row=3, column=0, columnspan=6, padx=25, pady=30)
        self.customer_payment_button=customtkinter.CTkButton(self.right_frame, text="PAYMENTS",image=payments_image,width=240, height=60,corner_radius=8, fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"), command=self.load_customer_payments_window)
        self.customer_payment_button.grid(row=3, column=6, columnspan=6, padx=25, pady=30)
        
        #leftframe
        self.left_frame=customtkinter.CTkFrame(self.container_frame,corner_radius=10, width=400,height=450)
        self.left_frame.pack(side=RIGHT,anchor="e",padx=50)
        #create login table
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE User_Data")
        print("table dropped sucessfully")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS User_Data(
                    UserName TEXT PRIMARY KEY,
                    Password Text,
                    Security_Question TEXT,
                    Security_Answer TEXT,
                    User_Mode TEXT
                    )""")
        conn.commit()
        conn.close()
        #variable
        self.c_v1=IntVar(value=0)
        self.login_label=customtkinter.CTkLabel(self.left_frame, text=" MANAGE ACCOUNT", fg_color="darkblue",text_color="white", text_font=("Consollas 10", -35, "underline", "bold"),width=250,height=40)
        self.login_label.grid(row=0, column=0, columnspan=40, rowspan=2, pady=20,padx=50,sticky=EW)
        self.signup_button=customtkinter.CTkButton(self.left_frame, text="Add New User",fg_color="blue",text_color="white",text_font=("Consollas 10", -20,"bold"),width=300, height=50,command=self.sign_up)
        self.signup_button.grid(row=2, column=0,columnspan=20,rowspan=2,padx=50,pady=20,ipadx=50,ipady=10)
        self.change_password_button=customtkinter.CTkButton(self.left_frame, text="Change Password", fg_color="darkblue", text_color="white", text_font=("Consollas 10", -20,"bold"),width=300,height=50,command=self.change_password)
        self.change_password_button.grid(row=4, column=0,columnspan=20,rowspan=2,padx=50, pady=20,ipadx=50,ipady=10)
        self.remove_user_button=customtkinter.CTkButton(self.left_frame, text="Remove User",fg_color="purple",text_color="white",text_font=("Consollas 10", -20,"bold"),width=300,height=50,command=self.remove_user)
        self.remove_user_button.grid(row=8, column=0,columnspan=20,rowspan=2,padx=50,pady=20,ipadx=50,ipady=10)
        
    #show password
    def my_show(self):
        if(self.c_v1.get()==0):
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')
    #choose mode
    def choose_mode(self,event):
        if self.mode.get()=="Farmer Feeds":
            self.top98.destroy()
            c_feeds=Customer_Feeds(root)
            root.mainloop()
        else:
            self.top98.destroy()
            l_feeds=Local_Feeds(root)
            root.mainloop()
    def user_logout(self):
        self.top0.destroy()
    #select feeds
    def select_feeds(self):
        self.top98=Toplevel()
        self.top98.title("SAMARIA MILK GROUP")
        self.top98.iconbitmap("logo1.ico")
        top_frame=Frame(self.top98)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT MODE:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.mode,command=self.choose_mode,values=["Farmer Feeds","Local Feeds"],width=160,height=25,fg_color="red",text_color="white")
        mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    #help menu
    def help_menu(self):
        self.top101=Toplevel()
        self.top101.title("                                                                                                                                                                                SAMARIA MILK GROUP")
        self.top101.iconbitmap("logo1.ico")
        self.top101.state("zoomed")
        self.title_frame=Frame(self.top101)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1=" HELP CENTER"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Mega Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,fg_color="maroon",text_color="white", text_font=("Consollas 10", -30, "italic"),width=200,height=35)
        self.my_sub_text.grid(row=1, column=1,padx=10,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1, fg_color="orange",text_color="white", text_font=("Consollas 10", -35, "bold","underline"),width=300,height=35)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4, padx=10)
        self.my_text_block=ScrolledText(self.top101,height=34,width=800,bg="lightgrey")
        self.my_text_block.pack()
        #enter information
        self.my_text_block.delete(1.0,END)
        self.my_text_block.tag_configure('headings',justify='center',foreground="green",font=("Consollas 10",30,"bold","underline"))
        self.my_text_block.tag_configure('norm',font=("Consollas 10",12))
        self.my_text_block.configure(state='normal')
        #about
        self.my_text_block.insert(END, '\n ABOUT SAMARIA APP\n','headings')
        about_quote="""
            Samaria Milk APP is an intergrated,user friendly desktop application that helps an individual or a group of people to maintain key records in a Dairy Firm Context.
            It entails key modules like:   RECORDS,               SALES,              FEEDS,               ADVANCES         AND             PAYMENTS.
            These Modules helps the firm to manage every aspect of their customers and also maintain updated records regarding the firm.
                                                                                       ALL DETAILS AT YOUR TIPS!!!!
            """
        self.my_text_block.insert(END, about_quote, 'norm')
        #Access
        self.my_text_block.insert(END, '\n ACCESS SAMARIA APP\n','headings')
        access_quote="""
            For anyone to access and use Samaria App and It's accessories, they need to register first with a valid Username and a Password that is only known to them to ensure
            security and accountability in every detail captured by the application database. Usernames and Passwords used are case-sensitive therefore, every user must keep mind
            of their login credentials for timely access to the app. Passwords can revolve under any combinations of Alphabetic letters, numbers and special symbols.
            Administrator Passwords are encouraged to be a combination of letters,numbers and symbols for optimal security.
            
            There are two types of accounts in this application: Administrator and User Accounts.
            Adinistrator Account which can only be one has super priviledges where the Admin can perform tasks like: Adding new users, Removing Existing Users, Accessing Daily and
            Monthly reports,Adding new Products and Feeds,Granting Advances and Paying the Farmers among others. Therefore, Administrator is urged to always ensure secrecy of their
            passwords to prevent mass degredation and destruction of information concerning the firm.
            User accounts have limited access and priviledges upon which undertake given tasks  under supervision of the Administrator.

            After opening the app, The Login Page is displayed for the user to enter credentials to proceed using the app. If an individual, does not have an account, click the
            'SIGN UP' Button on the furthest right hand side. A Sign Up Page will be displayed, where the user will be prompted to enter their prefered username and password.
            The individual will also repeat the password for a match. They will also be prompted to choose a security question and provide an answer upon which the  user will be
            needed to retreive answer if they forget the password to their respective username. To ensure security,they are urged to choose a question whose answer will not be easily
            guessed. Lastly, one has to choose the type of account they want either administrator or user accounts. If it's administrator account, the system will check if there exists
            another administrator account. If it exists, an error message will be prompted to inform them that there can only be one administrator. If it's user account, then the system
            will prompt the admin to enter his/her password inorder to add the new user. If succesful, a congratulatory message will be prompted to the user to show that the account was
            succesfully created. The user can therefore use the above credentials to login to the system.

            If a user forget's his/her password, they should click on the purple button 'Forgot password?'. The user will then be prompted to enter their username to proceed.They will
            then be required to answer the security question that they answered during registration and they will be given a chance to enter a new password to proceed with login in to
            the system.
            The 'show password' checkbox is there to prompt the user to check if the password they entered is the one they intended to enter.
            With that, the user should click the login button and a welcome message will be prompted to the user. Incase of any errors in the login credentials, one will be blocked from
            accessing the system.
            """
        self.my_text_block.insert(END, access_quote, 'norm')
        #welcome page
        self.my_text_block.insert(END,'\n WELCOME PAGE\n','headings')
        welcome_quote="""
            WELCOME TO SAMARIA APP HOME PAGE. This is the heart of our heart where you can access every aspect of our app. On the top, we have a menu where it contains all needed aspects
            of system. We have the records, sales, advances, payments, reports, help and about menu where they are gateways to the specified entity. On the upper right side, we have a
            'Logout Button' which takes you back to the login page. Hence when the user is not using the system ,they should logout first to prevent any chance that an intruder may use the
            system with their credentials.
            The Report menu is dividend into 3 categories namely: Farmer Report, Daily Report and Monthly Report. Farmer report is further dividend into 2:Daily Report and Monthly Report.
            
            Farmer's Daily Report entails a window where user is required to  enter the Farmer's ID and then choose the particular Date in which they want to know what transpired  in the
            said date. Then the user should click the 'Generate Report' Button and the Farmer's Report for the said date will be retreived in the text box below. The report entails morning
            afternoon and evening sales that the user depicted on the said date, the time they conducted the sales and the server whom performed the said sales. It then has the accumulated
            quantity that the server made on that specific date.
            If the farmer received an advance amount, the report will show the advance amount received and the status of the loan if paid or not paid.
            If the farmer received advanced feeds, the report will showcase the feeds name, quantity and amount partaining the feeds amount. Then the accumulated amount will be recorded below.
            Then the server who has retreived the said report will be recorded for followup purposes.
            The report is printable and can be printed using a receipt printer if availably connected to the computer or laptop partaining the Samaria App system.

            Farmer's Monthly Report entails details of a farmer dividend  by the period's of a month.The user is required to provide the farmer's id and then choose the desired month.
            When you chose the month from the dropdown, a prompt to choose the period as 'From 1-15' and 'From 16-'Last day of the selected month''. To retreive the report, please click the
            'Generate Report' Button. If the farmer is not paid for the selected month, an error message will be prompted that the farmer is not paid. If the farmer is paid, then an explicit
            report partaining the accumulated quantity for the selected period,the total advance amount they received, the total feeds amount and transport received by the farmer and the balance
            remaining for the particular period. The report is also printable and can be printed by clicking on the print button below.

            The Daily Report contains an explicit report of all the activities that happens in a particular date. This information is priviledged to be accessed only by the admin and hence a prompt
            to enter the administrator password is presented and the admin should enter their password to access the information. Here one should first choose the date and then choose the specific
            module that  they want to deduce the report from. The modules include:Farmer's Sales, Product Sales,Loans,Farmer Feeds,Local Feeds and Payments.
            The Farmer's Sales contains information of that particular date of total morning quantity sales, total eveinig sales and the daily accumulated quantity.The creditors report is also
            present where each creditor and the amount they received from the firm. The amount remaining from the daily quantity is left for local sale.
            The product Sales module entails the Products sold per that day and their respective quantity and hence the total amount of money received from the product sales sector.
            The Loans module contains the respective people who have received advance amount in the particular date and the respective amount  per individual and total advance amount per that day.
            The Farmer feeds contains the details of Farmer's who've taken feeds credit from Feeds depot in a particular date. The report contains the Farmer's Name, ID,Feeds' Name, Feeds'Quantity
            and the amount as per the price of the feeds. Then the accumulated amount of money partaining the feeds granted as credit as per that day.
            The Local Feeds module contains the details of feeds sold from the feeds depot to local customers on that specific date. The feeds are grouped by the Feeds name and the quantity sold
            in that day.The total amount of money received from the day is also registered below.
            The credit given to local customers is also registered by the creditor name, feeds name and quantity granted and lastly the amount worth the feeds granted. The total amount of money
            correspondent to those feeds is registered below too.
            The payment module entails the amount of money paid to farmers in a particular day. The report contains the farmer's name and id and then the month and period paid and lastly the
            amount of money paid to each farmer. The total amount paid to customers in that day is also registered below for better management.

            The Monthly Report also contains an explicit monthly report of all the summaries of monthly activities partaining the system's usage. This information is also priviledged only by
            the admin and hence a prompt to enter the administrator password is presented. Once entered, the Monthly report page is presented. The admin is required to choose the specific month
            that he/she wants to retreive the report. They are also required to choose the module in which they want to get information about.The Monthly report has the following modules:
            Farmer's Sales,Advance, Feeds and Payment modules.
            The Farmer Sales module contains the total amount of litres registered in that particular month. It also entails the total amount of litres credited to respectively shown
            creditors and the amount not paid by those creditors.
            The Advance module contains the total amount of pending money granted to farmers for advances.It entails the farmer's name and ID and the total amount of advances they have not cleared.
            The total amount of advance for that particular month is also registered below.
            The Feeds module contains the explicit report of Feeds intake,sold out and remaining feeds quantity in a particular month. It therefore provides a clear output of how feeds have been
            utilized in the depot. It gives the admin a clear indication of which feeds have more demand in the depot than others and therefore helps in making progresively decisions regarding new
            stock needed in the depot.
            The Payment Module contains information of farmers who have been successfuly paid in a particular month. It also contains the period paid and the amount paid to each farmer and lastly
            the total amount of cash paid accumulatively to every farmer in the particular month.
            The Notifications menu on top gives a platform for the user to pass relevant message to the farmers. The user can compose a message of any length and then click on the send message
            button about the relevant information.Examples of these topics may include: Notifying farmers of change in the monthly payent rate of milk and notifying them of a meeting scheduled for
            all farmers.
            If the computer or laptop partaining the system is not connected to internet,an error message will be prompted for the user to check their internet connectivity and try again. The messages
            cost's 0.35 Kenyan shillings per 160 characters hence the more the characters, the more the rate of sending per message. The user should therefore make sure that their wallet of Mobitech
            Technologies,the company that provides bulk sms for this system has enough credit to send messages to each farmer registered in the system. The technology sends message to each farmer via
            the phone number taken on the registration date.If a farmer has not provided their phone number then they would not receive the message.The process is progressive from the first farmer to
            the last, therefore the user is urged to keep all the neccesary conditions ie. Enough Credit to send messages and good internet connectivity.
            
            On the left side we have the menu which contains Records, Farmer Sales, Feeds, Local Sales, Advances and Payments Buttons. They are clear gateways to the said entities.
            On the right side, we have Manage Accounts Menu which contains options to manage accounts.
            The 'Add New User' Button is used to add a new user into the system. It's the same as the signup button on the login page. One should follow the same procedure and a new user would be
            added to the system.
            The 'Change Password' Button is used by any user to change their  passwords incase they are weak passwords or they have been revieled to other peole. First, the user will be prompted to
            enter their initial passwords and then enter the new paswords and confirm them.
            The 'Remove User' Button is specifically reserved for the Admin to remove any user if they are not using the system anymore. The Admin should check the
            desired user by checking the desired checkbox and then entering their password on the Entry box provided and clicking the Remove button.
            
            """
        self.my_text_block.insert(END, welcome_quote, 'norm')
        #records page
        self.my_text_block.insert(END, '\n RECORDS PAGE\n','headings')
        records_quote="""
            WELCOME TO SAMARIA APP RECORDS PAGE!!
            Here we keep all the details of our beloved farmers which include all the three official names, national id number, phone number and their addresses. This information is vital in
            identification of an individual farmer.Each farmer also has a unique farmer id which is given by the system when a farmer is registered. This farmer id is very essential since it
            stores all the farmers details in the system. Hence this farmer id should and must be unique for every farmer. If a farmer does not have this number, he/she cannot access any
            services in this system.
            To be registered in this system, a farmer has to provide all the neccesary details ie. First Name, Last Name, Surname, Address, National ID Number, a valid Phone Number
            and the method in which the farmer would wish to be paid. It can either be in CASH, MPESA or via Bank Transfer.With this information, the system would then produce a unique
            identification number that the farmer will be using to do all the said functions of the system.
            This information is to be entered in designated entry boxes below in the Records Page. For the Payment mode, the user is required to choose from the dropdown box designated
            in the payment mode area.
            To register a farmer, please click on the 'Add New Record' Button on the left.
            The Tabular-like object (Treeview) above contains information of all farmers registered in the system in an ascending order using the farmer id criteria.Once a farmer id has been
            issued, it can not be given to any other person neither can it be deleted for better followup purposes and effecient records keeping.Incase of any changes in the information of a
            registered farmer, we can change their information.
            This can be done by clicking or selecting the said record in the tabular like object and the information of the selected farmer will be reflected in the designated entry boxes below.
            Now this information can be changed or modified and later updated by clicking on the 'Update Existing Record' Button.
            Incase the farmer has selected 'Bank Account' as the mode of Payment, the system will then provide a window for the user to enter their bank records appropriately.
        """
        self.my_text_block.insert(END, records_quote, 'norm')
    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
        
    #signup
    def add_user(self):
        if self.pass_word_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("ERROR","Password Does Not Match",parent=self.top)
        else:
            if self.clicked.get()=="User":
                self.top1=Toplevel()
                self.top1.title("SAMARIA MILK GROUP")
                self.top1.iconbitmap("logo1.ico")
                top_frame=Frame(self.top1)
                top_frame.pack(anchor="w")
                self.administrator_label=Label(top_frame, text="Enter Administrator Password:",fg="darkblue", bg="white", font=("Consollas 10", 10, "bold"))
                self.administrator_label.grid(row=0,column=0, padx=10, pady=10)
                self.administrator_entry=customtkinter.CTkEntry(top_frame,show="*", width=150,height=40,text_color="purple",placeholder_text="Enter Admin Password", placeholder_text_color="purple",border_color="blue")
                self.administrator_entry.grid(row=0, column=1, padx=10, pady=10)
                self.ok_button=customtkinter.CTkButton(top_frame, text="VERIFY",fg_color="maroon", text_color="white", text_font=("Consollas 10", -20,"bold"),width=200, height=50,command=self.verify_admin)
                self.ok_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            else:
                #insert data into our table
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT * FROM User_Data WHERE User_Mode='Administrator'")
                results=c.fetchall()
                wakuu=len(results)
                conn.commit()
                conn.close()
                if (wakuu >= 1):
                    messagebox.showerror("Error", "There can only be one Administrator",parent=self.top)
                else:
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO User_Data VALUES(:UserName, :Password, :Security_Question, :Security_Answer, :User_Mode)",
                                {
                                    "UserName":self.user_name_entry.get(),
                                    "Password":self.pass_word_entry.get(),
                                    "Security_Question":self.selected.get(),
                                    "Security_Answer": self.answer_entry.get(),
                                    "User_Mode": self.clicked.get()
                                    })
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Congratulations", "New Administrator User Succesfully Added")
                self.user_name_entry.delete(0, END)
                self.pass_word_entry.delete(0, END)
                self.answer_entry.delete(0, END)
                #self.top.destroy()
    def verify_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin=c.fetchone()
        conn.commit()
        conn.close()
        if self.administrator_entry.get()!=admin:
            messagebox.showerror("ERROR", "Administrator Password is incorrect,Check password and try again",parent=self.top)
            self.top1.destroy()
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("INSERT INTO User_Data VALUES(:UserName, :Password, :Security_Question, :Security_Answer, :User_Mode)",
                        {
                            "UserName":self.user_name_entry.get(),
                            "Password":self.pass_word_entry.get(),
                            "Security_Question":self.selected.get(),
                            "Security_Answer": self.answer_entry.get(),
                            "User_Mode": self.clicked.get()
                            })
            conn.commit()
            conn.close()
            messagebox.showinfo("Congratulations", "New User Succesfully Added")
            self.administrator_entry.delete(0, END)
            self.user_name_entry.delete(0, END)
            self.pass_word_entry.delete(0, END)
            self.answer_entry.delete(0, END)
            self.top1.destroy()
            self.top.destroy()
    def sign_up(self):
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top)
        my_frame.pack(anchor="w")
        self.sign_up_label=customtkinter.CTkLabel(my_frame, text="SIGN UP", fg_color="purple", text_color="white", text_font=("Consollas 10", 30, "underline", "bold"),width=200,height=30)
        self.sign_up_label.grid(row=0, column=0, columnspan=10,padx=10, pady=10)
        self.instruction_label=customtkinter.CTkLabel(my_frame, text="*** Please fill each detail", fg_color="red", text_color="white", text_font=("Consollas 10", -15, "underline"),width=300,height=25)
        self.instruction_label.grid(row=1, column=0, columnspan=5, padx=10, pady=10)
        self.user_name_label=customtkinter.CTkLabel(my_frame, text="Enter UserName:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.user_name_label.grid(row=2, column=0, padx=10, rowspan=2, pady=10)
        self.user_name_entry=customtkinter.CTkEntry(my_frame,width=200, height=40,border_color="blue",placeholder_text="Enter Username",placeholder_text_color="purple")
        self.user_name_entry.grid(row=2, column=1, rowspan=2, padx=10, pady=10)
        self.pass_word_label=customtkinter.CTkLabel(my_frame, text="Enter Password:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.pass_word_label.grid(row=4, column=0, rowspan=2, padx=10, pady=10)
        self.pass_word_entry=customtkinter.CTkEntry(my_frame, show="*", width=200, height=40,border_color="blue",placeholder_text="Enter Password",placeholder_text_color="purple")
        self.pass_word_entry.grid(row=4, column=1, rowspan=2, padx=10, pady=10)
        self.confirm_pass_word_label=customtkinter.CTkLabel(my_frame, text="Confirm Password:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=200,height=40)
        self.confirm_pass_word_label.grid(row=6, column=0, rowspan=2, padx=10, pady=10)
        self.confirm_pass_entry=customtkinter.CTkEntry(my_frame,width=200,height=40,border_color="blue",placeholder_text="Confirm Password",placeholder_text_color="purple",show="*")
        self.confirm_pass_entry.grid(row=6,column=1,rowspan=2,padx=10,pady=10)
        self.security_questions_label=customtkinter.CTkLabel(my_frame, text="SECURITY QUESTIONS", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=250,height=30)
        self.security_questions_label.grid(row=8, column=0, padx=10,pady=10)
        self.answer_label=customtkinter.CTkLabel(my_frame, text="ANSWER", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=200,height=30)
        self.answer_label.grid(row=8, column=1,padx=10, pady=10)
        #menu
        self.selected=StringVar()
        self.security_menubar=customtkinter.CTkOptionMenu(my_frame, variable=self.selected,values=["What's your Pet Name?","What's your Mother Maiden's Name?","What's your Favorite place?"],width=250, height=50,fg_color="red",dropdown_text_color="purple", text_color="black")
        self.security_menubar.grid(row=9, column=0, padx=10, pady=10)
        self.answer_entry=customtkinter.CTkEntry(my_frame, width=200,height=40,border_color="blue",placeholder_text="Answer",placeholder_text_color="violet",text_color="purple")
        self.answer_entry.grid(row=9, column=1, padx=10, pady=10)
        #option menu
        self.user_mode_label=customtkinter.CTkLabel(my_frame, text="Set User AS:", fg_color="maroon",text_color="white",text_font=("Consollas 10", -15, "bold"),width=200,height=30)
        self.user_mode_label.grid(row=10, column=0, padx=10, pady=10)
        self.clicked=StringVar()
        self.user_mode_menu=customtkinter.CTkOptionMenu(my_frame, variable=self.clicked,values=["Administrator", "User"],width=150, height=50,fg_color="red",dropdown_text_color="purple", text_color="black")
        self.user_mode_menu.grid(row=10, column=1,padx=10, pady=10)
        #signup button
        self.sign_up_button=customtkinter.CTkButton(my_frame, text="SIGN UP",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=250, height=60,command=self.add_user)
        self.sign_up_button.grid(row=11, column=0, columnspan=8, padx=10, pady=10)

    #forgot password    
    def update_table(self):
        if self.enter_new_pass_entry.get()!=self.confirm_new_pass_entry.get():
            messagebox.showerror("ERROR", "Password does not match")
            self.enter_new_pass_entry.delete(0, END)
            self.confirm_new_pass_entry.delete(0, END)
            self.jibu_entry.delete(0, END)
            self.enter_username_entry.delete(0, END)
            self.top3.destroy()
            self.top2.destroy()
        else:
            #update table
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
            results=c.fetchall()
            for record in results:
                c.execute("""UPDATE User_Data SET
                            UserName=:u_name,
                            Password=:pwd,
                            Security_Question=:s_quiz,
                            Security_Answer=:s_ans,
                            User_Mode=:u_mode

                            WHERE UserName=:u_name""",
                            {
                                'u_name' : record[0],
                                'pwd': self.enter_new_pass_entry.get(),
                                's_quiz': record[2],
                                's_ans' :record[3],
                                'u_mode': record[4]
                                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations", "Succesfully modified password")
                #clear entries
                self.enter_new_pass_entry.delete(0, END)
                self.confirm_new_pass_entry.delete(0, END)
                self.jibu_entry.delete(0, END)
                self.enter_username_entry.delete(0, END)
                self.top3.destroy()
                self.top2.destroy()
                            
    def new_password(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Security_Answer FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
        jibu=c.fetchone()
        if jibu!=self.jibu_entry.get():
            messagebox.showerror("ERROR", "Wrong Answer TRY AGAIN")
            self.jibu_entry.delete(0, END)
            self.enter_username_entry.delete(0, END)
            self.top2.destroy()
        else:
            self.top3=Toplevel()
            self.top3.title("SAMARIA MILK GROUP")
            self.top3.iconbitmap("logo1.ico")
            new_pass_frame=Frame(self.top3)
            new_pass_frame.pack(anchor="w")
            self.change_pass_label=Label(new_pass_frame, text="CHANGE PASSWORD",fg="purple",bg="white",font=("Consollas 10", 20,"underline", "bold"))
            self.change_pass_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)
            self.enter_new_pass_label=Label(new_pass_frame, text="Enter New Password:", fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.enter_new_pass_label.grid(row=1, column=0, padx=10, pady=10)
            self.enter_new_pass_entry=customtkinter.CTkEntry(new_pass_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="New Password",placeholder_text_color="purple")
            self.enter_new_pass_entry.grid(row=1, column=1, padx=10, pady=10)
            self.confirm_new_pass_label=Label(new_pass_frame, text="Confirm New Password:",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.confirm_new_pass_label.grid(row=2, column=0, padx=10, pady=10)
            self.confirm_new_pass_entry=customtkinter.CTkEntry(new_pass_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Confirm Password",placeholder_text_color="purple")
            self.confirm_new_pass_entry.grid(row=2, column=1, padx=10, pady=10)
            self.change_new_pass_button=customtkinter.CTkButton(new_pass_frame, text="CHANGE PASSWORD",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40, command=self.update_table)
            self.change_new_pass_button.grid(row=3, column=0, columnspan=5, padx=10, pady=10,)
    def retreive_password(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Security_Question FROM User_Data WHERE UserName=?",(self.enter_username_entry.get(),))
        swali=c.fetchone()
        conn.commit()
        conn.close()
        if swali==None:
            messagebox.showerror("ERROR", "Enter Correct USERNAME")
            self.enter_username_entry.delete(0, END)
            self.top2.destroy()
        else:
            self.request_label=Label(self.forgot_frame, text="Answer this question with correct answer provided during registration!")
            self.request_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
            self.question_label=Label(self.forgot_frame, text="QUESTION",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.question_label.grid(row=4, column=0, padx=10, pady=10)
            self.answer_label=Label(self.forgot_frame, text="ANSWER",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
            self.answer_label.grid(row=4, column=1, padx=10, pady=10)
            self.swali_label=Label(self.forgot_frame, text=swali)
            self.swali_label.grid(row=5, column=0, padx=10, pady=10)
            self.jibu_entry=customtkinter.CTkEntry(self.forgot_frame, width=150, height=40,border_color="blue",placeholder_text="Answer",placeholder_text_color="purple")
            self.jibu_entry.grid(row=5, column=1, padx=10, pady=10)
            self.change_password_button=customtkinter.CTkButton(self.forgot_frame, text="CHANGE PASSWORD",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40,command=self.new_password)
            self.change_password_button.grid(row=6, column=0,columnspan=4, padx=10, pady=10)
            
    def forgot_password(self):
        self.top2=Toplevel()
        self.top2.title("SAMARIA MILK GROUP")
        self.top2.iconbitmap("logo1.ico")
        self.forgot_frame=Frame(self.top2)
        self.forgot_frame.pack(anchor="w")
        self.retreive_password_label=Label(self.forgot_frame, text="RETREIVE PASSWORD",fg="purple",bg="white",font=("Consollas 10", 20,"underline", "bold"))
        self.retreive_password_label.grid(row=0, column=0,columnspan=8, padx=10, pady=10)
        self.enter_username_label=Label(self.forgot_frame, text="ENTER USERNAME:",fg="purple",bg="white",font=("Consollas 10", 10, "bold"))
        self.enter_username_label.grid(row=1, column=0, padx=10, pady=10)
        self.enter_username_entry=customtkinter.CTkEntry(self.forgot_frame, width=150, height=40,border_color="blue",placeholder_text="Username",placeholder_text_color="purple")
        self.enter_username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.submit_button=customtkinter.CTkButton(self.forgot_frame, text="SUBMIT",fg_color="maroon",text_color="white",text_font=("Consollas 10", -20, "bold"),width=150, height=40, command=self.retreive_password)
        self.submit_button.grid(row=2, column=0,columnspan=6, padx=20, pady=10)
        
    #remove user
    def delete_user(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        passcode=c.fetchone()
        conn.commit()
        conn.close()
        if passcode!=self.enter_administrator_entry.get():
            messagebox.showerror("ERROR", "Administrator Password is incorrect, Check password and try again",parent=self.top0)
            self.ch.deselect()
            self.enter_administrator_entry.delete(0, END)
            self.top4.destroy()
        else:
            for p in self.varIables:
                for x in range(len(self.users)):
                    if p.get()==self.users[x]:
                        user_name=self.users[x]
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("DELETE FROM User_Data WHERE UserName=?",(user_name,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", "User Deleted Succesfully",parent=self.top0)
            self.ch.deselect()
            self.enter_administrator_entry.delete(0, END)
            self.top4.destroy()
    def remove_user(self):            
        self.top4=Toplevel()
        self.top4.title("SAMARIA MILK GROUP")
        self.top4.iconbitmap("logo1.ico")
        remove_frame=Frame(self.top4)
        remove_frame.pack(anchor="w")
        self.select_user_label=Label(remove_frame, text="Select User You want to Remove:", fg="purple", bg="white", font=("Consollas 10", 15, "bold"))
        self.select_user_label.grid(row=0, column=0,columnspan=4, padx=10, pady=10)
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT UserName FROM User_Data")
        self.users=c.fetchall()
        conn.commit()
        conn.close()
        self.varIables=[]
        for x in range(len(self.users)):
            self.varIables.append(StringVar())
            self.ch=customtkinter.CTkCheckBox(remove_frame, text=self.users[x], variable=self.varIables[-1], onvalue=self.users[x], offvalue="")
            self.ch.grid(row=self.start, column=0,sticky=W,padx=10, pady=10)
            self.start+=1
        self.enter_administrator_label=Label(remove_frame, text="Enter Administrator Password:" ,fg="purple",bg="white", font=("Consollas 10", 10, "bold"))
        self.enter_administrator_label.grid(row=self.start, column=0, padx=10, pady=10)
        self.enter_administrator_entry=customtkinter.CTkEntry(remove_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="purple")
        self.enter_administrator_entry.grid(row=self.start, column=1, padx=10, pady=10)
        self.delete_user_button=customtkinter.CTkButton(remove_frame, text="DELETE USER",fg_color="maroon",text_color="white", text_font=("Consollas 10", -20, "bold"),width=150, height=40, command=self.delete_user)
        self.delete_user_button.grid(row=self.start+1, column=0, columnspan=4, padx=10, pady=10)
    #change password
    def change_passcode(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE UserName=?",(self.change_username_entry.get(),))
        code=c.fetchone()
        conn.commit()
        conn.close()
        if code!=self.current_passcode_entry.get():
            messagebox.showerror("ERROR", "Current Password is Incorrect,Check Password And Try Again",parent=self.top0)
            self.change_username_entry.delete(0, END)
            self.current_passcode_entry.delete(0, END)
            self.new_passcode_entry.delete(0, END)
            self.confirm_new_passcode_entry.delete(0, END)
            self.top5.destroy()          
        else:
            if self.new_passcode_entry.get()!=self.confirm_new_passcode_entry.get():
                messagebox.showerror("ERROR","New Password Does Not Match",parent=self.top0)
                self.change_username_entry.delete(0, END)
                self.current_passcode_entry.delete(0, END)
                self.new_passcode_entry.delete(0, END)
                self.confirm_new_passcode_entry.delete(0, END)
                self.top5.destroy()          
            else:
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM User_Data WHERE UserName=?",(self.change_username_entry.get(),))
                result=c.fetchall()
                for record in result:
                    c.execute("""UPDATE User_Data SET
                                UserName=:u_name,
                                Password=:pwd,
                                Security_Question=:s_quiz,
                                Security_Answer=:s_ans,
                                User_Mode=:u_mode
                                
                                WHERE UserName=:u_name""",
                                {
                                    'u_name' : record[0],
                                    'pwd': self.confirm_new_passcode_entry.get(),
                                    's_quiz': record[2],
                                    's_ans' :record[3],
                                    'u_mode': record[4]
                                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Congratulations","Password changed succesfully",parent=self.top0)
                self.change_username_entry.delete(0, END)
                self.current_passcode_entry.delete(0, END)
                self.new_passcode_entry.delete(0, END)
                self.confirm_new_passcode_entry.delete(0, END)
                self.top5.destroy()                            
    def change_password(self):
        self.top5=Toplevel()
        self.top5.title("SAMARIA MILK GROUP")
        self.top5.iconbitmap("logo1.ico")
        change_frame=Frame(self.top5)
        change_frame.pack(anchor="w")
        self.change_passcode_label=Label(change_frame, text="CHANGE PASSWORD", fg="purple", bg="white", font=("Consollas 10", 20, "underline", "bold"))
        self.change_passcode_label.grid(row=0, column=0, columnspan=6,padx=10, pady=10)
        self.change_username_label=Label(change_frame, text="Enter Username:",fg="purple", bg="white", font=("Consollas 10", 10, "bold"))
        self.change_username_label.grid(row=1, column=0, padx=10, pady=10)
        self.change_username_entry=customtkinter.CTkEntry(change_frame, width=150, height=40,border_color="blue",placeholder_text="Username",placeholder_text_color="purple")
        self.change_username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.current_passcode_label=Label(change_frame, text="Enter Current Password:",fg="purple", bg="white", font=("Consollas 10", 10, "bold"))
        self.current_passcode_label.grid(row=2, column=0, padx=10, pady=10)
        self.current_passcode_entry=customtkinter.CTkEntry(change_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Current Password",placeholder_text_color="purple")
        self.current_passcode_entry.grid(row=2, column=1, padx=10, pady=10)
        self.new_passcode_label=Label(change_frame, text="Enter New Password:",fg="purple", bg="white", font=("Consollas 10", 10, "bold"))
        self.new_passcode_label.grid(row=3, column=0, padx=10, pady=10)
        self.new_passcode_entry=customtkinter.CTkEntry(change_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="New Password",placeholder_text_color="purple")
        self.new_passcode_entry.grid(row=3, column=1, padx=10, pady=10)
        self.confirm_new_passcode_label=Label(change_frame, text="Confirm New Password:",fg="purple", bg="white", font=("Consollas 10", 10, "bold"))
        self.confirm_new_passcode_label.grid(row=4, column=0, padx=10, pady=10)
        self.confirm_new_passcode_entry=customtkinter.CTkEntry(change_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Confirm New Password",placeholder_text_color="purple")
        self.confirm_new_passcode_entry.grid(row=4, column=1, padx=10, pady=10)
        self.change_passcode_button=customtkinter.CTkButton(change_frame, text="CHANGE PASSWORD",fg_color="maroon", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150, height=40,command=self.change_passcode)
        self.change_passcode_button.grid(row=5, column=0, columnspan=6, padx=10, pady=10)
    def admin_daily_report(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top6.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top6.destroy()
            #
            #print function
            def print_receipt87():
                printText=self.my_receipt87.get("1.0", 'end')
                filename=tempfile.mktemp(".txt")
                open(filename, "w").write(printText)
                #print out as hardcopy
                win32api.ShellExecute(0,
                                    "printto",
                                    filename,
                                    '"%s"' % win32print.GetDefaultPrinter(),
                                    ".",
                                    0
                                    )
                self.my_receipt87.delete('1.0', 'end')
            #variables    
            self.module_chooser=StringVar()
            self.chosen_date86=self.today1
            #self.chosen_date85=(self.chosen_date86[3:5])
            #print(self.chosen_date85)
            def grab_date86():
                self.top86=Toplevel()
                self.top86.title("SAMARIA MILK GROUP")
                self.top86.iconbitmap("logo1.ico")
                self.my_label1=customtkinter.CTkLabel(self.top86, text="Choose Date",text_color="white",fg_color="maroon",width=200,height=25).pack(anchor="center",pady=5)
                self.cal86=Calendar(self.top86, selectmode="day", cursor="hand1",date_pattern="mm/dd/yyyy",year=self.currentDateTime.year,month=self.currentDateTime.month,day=self.currentDateTime.day)
                self.cal86.pack(padx=10,pady=12, anchor="w")
                self.cal86.bind("<<CalendarSelected>>",clicker86)
            def clicker86(e):
                self.chosen_date86=self.cal86.get_date()
                self.top86.destroy()
            def generate_admin_daily_report():
                if self.module_chooser.get()=="FARMER SALES":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Morning Sales:"
                    heading4="Total Afternoon Sales:"
                    heading5="Total Evening Sales:"
                    heading6="DAILY TOTAL SALES:"
                    heading7="CREDITORS"
                    heading8="Remaining Quantity For Local Sale:"
                    heading9="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    #morning sales
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(MORNING_QUANTITY) FROM Morning_Sales WHERE DATE=?",(self.chosen_date86,))
                    morning_q=c.fetchone()
                    conn.commit()
                    conn.close()
                    if morning_q==None:
                        morning_q=0.0
                    self.my_receipt87.insert('end', "\n" +heading3 +"\t"+f'{morning_q} Litres'+"\n")
                    #afternoon_sales
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(AFTERNOON_QUANTITY) FROM Afternoon_Sales WHERE DATE=?",(self.chosen_date86,))
                    after_q=c.fetchone()
                    conn.commit()
                    conn.close()
                    if after_q==None:
                        after_q=0.0
                    self.my_receipt87.insert('end', "\n" +heading4 +"\t"+f'{after_q} Litres'+"\n")
                    #evening sales
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(EVENING_QUANTITY) FROM Evening_Sales WHERE DATE=?",(self.chosen_date86,))
                    even_q=c.fetchone()
                    conn.commit()
                    conn.close()
                    if even_q==None:
                        even_q=0.0
                    self.my_receipt87.insert('end', "\n" +heading5 +"\t"+f'{even_q} Litres'+"\n")
                    #daily totals
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Daily_Accumulated) FROM DAILY_TOTALS WHERE DATE=?",(self.chosen_date86,))
                    daily_q=c.fetchone()
                    conn.commit()
                    conn.close()
                    if daily_q==None:
                        daily_q=0.0
                    self.my_receipt87.insert('end', "\n" +heading6+"\t"+f'{daily_q} Litres'+"\n")
                    #tenders
                    sumtenders=0.0
                    self.my_receipt87.insert('end', "\n" +"\t"+heading7+"\n")
                    self.my_receipt87.insert('end', "\n"+"NAME"+"\t"+"\t"+"QUANTITY"+"\t"+"STATUS"+"\n")
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Tenders WHERE DATE=(?)", (self.chosen_date86,))
                    records=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in records:
                        self.my_receipt87.insert('end', "\n"+str(record[0])+"\t"+str(record[1])+"\t"+str(record[5])+"\n")
                        sumtenders+=float(record[1])
                    self.my_receipt87.insert('end', "\n"+"Total Creditors Quantity:"+f'{sumtenders} Litres'+"\n")
                    #remaining quantity
                    remaining_q=(daily_q - sumtenders)
                    self.my_receipt87.insert('end', "\n"+heading8+f'{remaining_q} Litres'+"\n")
                    #server
                    self.my_receipt87.insert('end', "\n"+heading9+"\t"+server+"\n")
                    #self.my_receipt87.configure(state="disabled")
                if self.module_chooser.get()=="PRODUCT SALES":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Product Sales:"
                    heading4="Products Inventory"
                    heading5="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today +','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    #product sales
                    sumproducts=0.0
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT DISTINCT Product_Name, SUM(Quantity) FROM Local_Sales WHERE Date=(?) GROUP BY Product_Name", (self.chosen_date86,))
                    results=c.fetchall()
                    conn.commit()
                    conn.close()
                    self.my_receipt87.insert('end', "\n"+"Product Name"+"\t"+"Quantity"+" Price"+" Total"+"\n")
                    for record in results:
                        conn=sqlite3.connect('samaria database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Local_Sales WHERE Product_Name=?",(str(record[0]),))
                        money=c.fetchone()
                        conn.commit()
                        conn.close()
                        total=(float(money) * float(record[1]))
                        self.my_receipt87.insert('end', "\n"+str(record[0])+"\t"+str(record[1])+"\t"+str(money)+"\t"+str(total)+"\n")
                        sumproducts+=total
                    self.my_receipt87.insert('end', "\n"+heading3+"\t"+f'Kshs {sumproducts}'+"\n")
                    self.my_receipt87.insert('end', "\n"+heading5+"\t"+server+"\n")
                #loans
                if self.module_chooser.get()=="LOANS":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Advance Granted:"
                    heading4="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt87.insert('end', "\n" +"NAME"+"\t"+"\t"+"ID"+"\t"+"Amount"+"\n")
                    #queries
                    sumloan=0.0
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE DATE=?",(self.chosen_date86,))
                    result=c.fetchall()
                    conn.commit()
                    conn.close()
                    for x in result:
                        self.my_receipt87.insert('end', "\n" +str(x[1])+"\t"+str(x[2])+"\t"+str(x[0])+"\t"+str(x[5])+"\n")
                        sumloan+=float(x[5])
                    self.my_receipt87.insert('end', "\n" +heading3+"\t"+f'Kshs {sumloan}'+"\n")
                    self.my_receipt87.insert('end', "\n" +heading4+"\t"+server+"\n")
                #local feeds
                if self.module_chooser.get()=="LOCAL FEEDS":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Feeds Amount:"
                    heading4="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt87.insert('end', "\n" +"FEED NAME"+"\t"+"\t"+"Quantity"+"\t"+"Price"+"\t"+"Total"+"\n")
                    #queries
                    sumlocal=0.0
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT DISTINCT Feed_Names, SUM(Feed_Quantity) FROM Local_Feeds WHERE DATE=? GROUP BY Feed_Names",(self.chosen_date86,))
                    group=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in group:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        conn.row_factory=lambda cursor, row:row[0]
                        c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(str(record[0]),))
                        mapesa=c.fetchone()
                        conn.commit()
                        conn.close()
                        total=(record[1] * int(mapesa[0]))
                        self.my_receipt87.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(mapesa[0])+"\t"+str(total)+"\n")
                        sumlocal+=total
                    self.my_receipt87.insert('end', "\n" +heading3+"\t"+f'Kshs {sumlocal}'+"\n")
                    self.my_receipt87.insert('end', "\n" +heading4+"\t"+server+"\n")
                    
                #customer feeds
                if self.module_chooser.get()=="FARMER FEEDS":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Feeds Amount:"
                    heading4="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today +','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt87.insert('end', "\n" +"NAME"+"\t"+"\t"+"Farmer_ID"+"\t"+"FEED_NAME"+"\t"+"Quantity"+"\t"+"Price"+"\t"+"Total"+"\n")
                    sumfeeds=0.0
                    #queries
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM FEEDS WHERE DATE=?", (self.chosen_date86,))
                    group1=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in group1:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        conn.row_factory=lambda cursor, row:row[0]
                        c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(str(record[3]),))
                        mapesa=c.fetchone()
                        conn.commit()
                        conn.close()
                        total=(int(mapesa[0]) * record[4])
                        self.my_receipt87.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[3])+"\t"+str(record[4])+"\t"+str(mapesa[0])+"\t"+str(total)+"\n")
                        sumfeeds+=total
                    self.my_receipt87.insert('end', "\n" +heading3+"\t"+f'Kshs {sumfeeds}'+"\n")
                    self.my_receipt87.insert('end', "\n" +heading4+"\t"+server+"\n")
                if self.module_chooser.get()=="PAYMENTS":
                    sum_paid=0.0
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.chosen_date86}'
                    heading2="MODULE:"
                    heading3="Total Paid Amount:"
                    heading4="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt87.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt87.insert('end', "\n" +title + "\n")
                    self.my_receipt87.insert('end', "\n" +sub + "\n")
                    self.my_receipt87.insert('end', "\n" +heading1+"\n")
                    self.my_receipt87.insert('end', "\n" +self.today +','+self.Time+"\n")
                    self.my_receipt87.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt87.insert('end', "\n" +"NAME"+"\t"+"\t"+"Farmer_ID"+"\t"+"Month"+"\t"+"Period"+"\t"+"Amount"+"\n")
                    #query
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Payments WHERE DATE=?",(self.chosen_date86,))
                    all_paid=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in all_paid:
                        self.my_receipt87.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[12])+"\t"+str(record[3])+"\t"+str(record[11])+"\n")
                        sum_paid+=float(record[11])
                    self.my_receipt87.insert('end', "\n" +heading3+"\t"+f'Kshs {sum_paid}'+"\n")
                    self.my_receipt87.insert('end', "\n" +heading4+"\t"+server+"\n")
            #toplevel
            self.top87=Toplevel()
            self.top87.iconbitmap("logo1.ico")
            self.top87.state('zoomed')
            self.title_frame=Frame(self.top87)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="DAILY REPORT"
            self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
            self.my_img_label=Label(self.title_frame, image=self.img1)
            self.my_img_label.grid(row=0, column=0, rowspan=3)
            self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
            self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
            self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
            self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
            self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
            self.my_sub1_text.grid(row=2, column=1, columnspan=4)
            #left frame
            self.left_frame=customtkinter.CTkFrame(self.top87,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
            self.left_frame.pack(anchor="center")
            self.choose_date_button=customtkinter.CTkButton(self.left_frame,text="Choose Date",text_color="white",fg_color="red",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=grab_date86)
            self.choose_date_button.grid(row=0,column=0,columnspan=5,pady=20,padx=20)
            self.choose_module_label=customtkinter.CTkLabel(self.left_frame,text="Choose Module:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
            self.choose_module_label.grid(row=0,column=5,columnspan=2)
            self.choose_module_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.module_chooser,values=["FARMER SALES","PRODUCT SALES","LOANS","FARMER FEEDS","LOCAL FEEDS","PAYMENTS"],width=200,height=25,fg_color="red",text_color="white")
            self.choose_module_menu.grid(row=0, column=7,columnspan=3)
            self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_admin_daily_report)
            self.generate_button.grid(row=0,column=10,padx=20,pady=20,columnspan=5,sticky=E)
            self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
            self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
            self.my_receipt87=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
            self.my_receipt87.grid(row=2,column=0,columnspan=15,padx=20)
            self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt87)
            self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    def verify_daily_report(self):
        self.top6=Toplevel()
        self.top6.title("SAMARIA MILK GROUP")
        self.top6.iconbitmap("logo1.ico")
        my_frame=Frame(self.top6)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.admin_daily_report)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    def admin_monthly_report(self):
        #print function
        def print_receipt85():
            printText=self.my_receipt85.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt85.delete('1.0', 'end')
        def generate_monthly_report():
            if self.module_chooser.get()=="":
                messagebox.showerror("ERROR","Please Choose Module",parent=self.top85)
            elif self.month_chooser.get()=="":
                messagebox.showerror("ERROR","Please Choose Month",parent=self.top85)
            elif self.year_chooser.get()=="":
                messagebox.showerror("ERROR","Please Choose Year",parent=self.top85)
            else:
                #sales & creditors
                #print(self.year_chooser.get())
                if self.module_chooser.get()=="SALES":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'MONTHLY REPORT FOR {self.month_chooser.get()} {self.year_chooser.get()}'
                    heading2="MODULE:"
                    heading3="Total Monthly Sales:"
                    heading4="PENDING CREDITS"
                    heading5="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +heading1+"\n")
                    self.my_receipt85.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    #queries
                    conn=sqlite3.connect("samaria database.db")
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=?",(self.choosed,self.year_chooser.get(),))
                    monthly_total=c.fetchone()
                    if monthly_total == None:
                        monthly_total=0.0
                    c.execute("SELECT SUM(Quantity) FROM Tenders WHERE MONTH=? AND YEAR=? AND STATUS=?",(self.choosed,self.year_chooser.get(),"NOT PAID",))
                    unpaid_q=c.fetchone()
                    if unpaid_q==None:
                        unpaid_q=0.0
                    conn.commit()
                    conn.close()
                    self.my_receipt85.insert('end', "\n" +heading3+"\t"+f'{monthly_total} Litres'+"\n")
                    self.my_receipt85.insert('end', "\n" +"\t"+heading4+"\n")
                    self.my_receipt85.insert('end', "\n" +"NAME"+"\t"+"\t"+"QUANTITY"+"\t"+"DATE"+"\n")
                    #queries
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT * FROM Tenders WHERE MONTH=? AND YEAR=? AND STATUS=?",(self.choosed,self.year_chooser.get(),"NOT PAID",))
                    unpaid_t=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in unpaid_t:
                        self.my_receipt85.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\n")
                    self.my_receipt85.insert('end', "\n" +"Total Unpaid Credits:"+"\t"+f'{unpaid_q} Litres'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading5+"\t"+server+"\n")
                #feeds
                if self.module_chooser.get()=="FEEDS":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'MONTHLY REPORT FOR {self.month_chooser.get()} {self.year_chooser.get()}'
                    heading2="MODULE:"
                    heading3="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +heading1+"\n")
                    self.my_receipt85.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt85.insert('end', "\n" +"FEED NAME"+"\t"+"\t"+"Carry IN"+"\t"+"Added"+" Sold Out"+" Price"+" Total"+"\t"+"Carry OUT"+"\n")
                    #queries
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Feeds_Name FROM Feeds_Records")
                    all_feeds=c.fetchall()
                    conn.commit()
                    conn.close()
                    self.monthmn = self.choosed-1
                    if self.monthm==1:
                        self.monthmn=12
                    totalfeeds=0.0
                    for record in all_feeds:
                        #carry in from last month
                        #remainder from last month
                        #added last month
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feeds_Quantity FROM Feeds_Records WHERE Feeds_Name=? AND Month=? AND Year=?",(record,self.monthmn,self.year_chooser.get(),))
                        p_added=c.fetchone()
                        if p_added==None:
                            p_added=0
                        conn.commit()
                        conn.close()
                        #sold out last month
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(record,self.monthmn,self.year_chooser.get(),))
                        p_customer_given_out=c.fetchone()
                        if p_customer_given_out==None:
                            p_customer_given_out=0
                        c.execute("SELECT SUM(Feed_Quantity) FROM Local_Feeds WHERE Feed_Names=? AND Month=? AND Year=? GROUP BY Feed_Names",(record,self.monthmn,self.year_chooser.get(),))
                        p_local_sold_out=c.fetchone()
                        if p_local_sold_out==None:
                            p_local_sold_out=0
                        p_sold_out=(p_customer_given_out+p_local_sold_out)
                        conn.commit()
                        conn.close()
                        #carry in from last month/remainder
                        p_remainder =(p_added - p_sold_out)
                        #added this month
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feeds_Quantity FROM Feeds_Records WHERE Feeds_Name=? AND Month=? AND Year=?",(record,self.choosed,self.year_chooser.get(),))
                        added=c.fetchone()
                        if added==None:
                            added=0
                        conn.commit()
                        conn.close()
                        #sold out this month
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(record,self.choosed,self.year_chooser.get(),))
                        customer_given_out=c.fetchone()
                        if customer_given_out==None:
                            customer_given_out=0
                        c.execute("SELECT SUM(Feed_Quantity) FROM Local_Feeds WHERE Feed_Names=? AND Month=? AND Year=? GROUP BY Feed_Names",(record,self.choosed,self.year_chooser.get(),))
                        local_sold_out=c.fetchone()
                        if local_sold_out==None:
                            local_sold_out=0
                        sold_out=(customer_given_out+local_sold_out)
                        #price
                        c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(record,))
                        price=c.fetchone()
                        if price==None:
                            price=0
                        conn.commit()
                        conn.close()
                        total=(sold_out * price)
                        #carry to next month/remainder
                        remainder =((added +p_remainder)- sold_out)
                        #input
                        self.my_receipt85.insert('end', "\n" +str(record)+"\t"+f'{p_remainder} bags'+"\t"+f'{added} bags'+"\t"+f'{sold_out} bags'+"\t"+str(price)+"\t"+str(total)+"\t"+f'{remainder} bags'+"\n")
                        totalfeeds+=total
                    self.my_receipt85.insert('end', "\n" +"Total Feeds Amount:"+"\t"+f'Kshs {totalfeeds}'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading3+"\t"+server+"\n")
                #loans
                if self.module_chooser.get()=="ADVANCE":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'MONTHLY REPORT FOR {self.month_chooser.get()} {self.year_chooser.get()}'
                    heading2="MODULE:"
                    heading3="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +heading1+"\n")
                    self.my_receipt85.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt85.insert('end', "\n" +"\t"+"UNPAID MONTHLY ADVANCE"+"\n")
                    #queries
                    totalloans=0.0
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE MONTH=? AND YEAR=? AND STATUS=?",(self.choosed,self.year_chooser.get(),"NOT PAID",))
                    unpaid_loans=c.fetchall()
                    conn.commit()
                    conn.close()
                    self.my_receipt85.insert('end', "\n" +"NAME"+"\t"+"ID"+"\t"+"Advance_Amount"+"\n")
                    for record in unpaid_loans:
                        self.my_receipt85.insert('end', "\n" +str(record[1])+"\t"+str(record[0])+"\t"+str(record[5])+"\n")
                        totalloans+=float(record[5])
                    self.my_receipt85.insert('end', "\n" +"Total Unpaid Advance:"+"\t"+f'Kshs {totalloans}'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading3+"\t"+server+"\n")
                #payments
                if self.module_chooser.get()=="PAYMENTS":
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'MONTHLY REPORT FOR {self.month_chooser.get()} {self.year_chooser.get()}'
                    heading2="MODULE:"
                    heading3="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +heading1+"\n")
                    self.my_receipt85.insert('end', "\n" +self.today+','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +heading2 +"\t" +self.module_chooser.get()+"\n")
                    self.my_receipt85.insert('end', "\n" +"\t"+"PAID FARMERS"+"\n")
                    #queries
                    totalbal=0.0
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Payments WHERE MONTH=? AND YEAR=? ORDER BY Customer_ID ASC",(self.choosed,self.year_chooser.get(),))
                    all_paid=c.fetchall()
                    conn.commit()
                    conn.close()
                    self.my_receipt85.insert('end', "\n" +"\t"+"Name"+"\t"+"ID"+"\t"+"Period"+"\t"+"Sales"+" Rate(Kshs)"+" Total_Amount"+" Advance"+" Feeds"+" Transport"+" Balance"+"\n")
                    for record in all_paid:
                        self.my_receipt85.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(record[2])+"\t"+str(record[3])+"\t"+str(record[4])+"\t"+str(record[5])+"\t"+str(record[7])+"\t"+str(record[8])+"\t"+str(record[9])+"\t"+str(record[10])+"\t"+str(record[11])+"\n")
                        totalbal+=float(record[11])
                    self.my_receipt85.insert('end', "\n" +"Total Amount:"+"\t"+f'Kshs {totalbal}'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading3+"\t"+server+"\n")
        def choose_month(event):
            if self.month_chooser.get()=="January":
                self.choosed=1
            if self.month_chooser.get()=="February":
                self.choosed=2
            if self.month_chooser.get()=="March":
                self.choosed=3
            if self.month_chooser.get()=="April":
                self.choosed=4
            if self.month_chooser.get()=="May":
                self.monthm=5
            if self.month_chooser.get()=="June":
                self.choosed=6
            if self.month_chooser.get()=="July":
                self.choosed=7
            if self.month_chooser.get()=="August":
                self.choosed=8
            if self.month_chooser.get()=="September":
                self.choosed=9
            if self.month_chooser.get()=="October":
                self.choosed=10
            if self.month_chooser.get()=="November":
                self.choosed=11
            if self.month_chooser.get()=="December":
                self.choosed=12
        #verify admin
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry1.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry1.delete(0, END)
            self.top13.destroy()
        else:
            self.admin_passode_entry1.delete(0, END)
            self.top13.destroy()
            #variables
            months=["January","February","March","April","May","June","July","August","September","October","November","December"]
            years=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}']
            self.month_chooser=StringVar()
            self.year_chooser=StringVar()
            self.module_chooser=StringVar()
            #toplevel
            self.top85=Toplevel()
            self.top85.iconbitmap("logo1.ico")
            self.top85.state('zoomed')
            self.title_frame=Frame(self.top85)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="MONTHLY REPORT"
            self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
            self.my_img_label=Label(self.title_frame, image=self.img1)
            self.my_img_label.grid(row=0, column=0, rowspan=3)
            self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
            self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
            self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
            self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
            self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
            self.my_sub1_text.grid(row=2, column=1, columnspan=4)
            #left frame
            self.left_frame=customtkinter.CTkFrame(self.top85,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
            self.left_frame.pack(anchor="center")
            self.choose_month_label=customtkinter.CTkLabel(self.left_frame,text="Choose Month",text_color="white",fg_color="brown",text_font=("Consollas 10",-20,"bold"),width=200,height=25)
            self.choose_month_label.grid(row=0,column=0,columnspan=2,pady=20,padx=10)
            self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,fg_color="red",text_color="white",variable=self.month_chooser,values=months,width=150,height=25,command=choose_month)
            self.choose_month_menu.grid(row=0,column=2,columnspan=2)
            self.choose_year_menu=customtkinter.CTkOptionMenu(self.left_frame,fg_color="red",text_color="white",variable=self.year_chooser,values=years,width=120,height=25)
            self.choose_year_menu.grid(row=0,column=4,columnspan=2,padx=10)
            self.choose_module_label=customtkinter.CTkLabel(self.left_frame,text="Choose Module:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
            self.choose_module_label.grid(row=0,column=6,columnspan=2,padx=10,pady=20)
            self.choose_module_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.module_chooser,values=["SALES","ADVANCE","FEEDS","PAYMENTS"],width=200,height=25,fg_color="red",text_color="white")
            self.choose_module_menu.grid(row=0, column=8,columnspan=2)
            self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_monthly_report)
            self.generate_button.grid(row=0,column=10,padx=20,pady=20,columnspan=5,sticky=E)
            self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
            self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
            self.my_receipt85=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
            self.my_receipt85.grid(row=2,column=0,columnspan=15,padx=20)
            self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt85)
            self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    def verify_monthly_report(self):
        self.top13=Toplevel()
        self.top13.title("SAMARIA MILK GROUP")
        self.top13.iconbitmap("logo1.ico")
        my_frame=Frame(self.top13)
        my_frame.pack(anchor="w")
        self.admin_passcode_label1=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label1.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry1=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry1.grid(row=0, column=1, padx=5)
        self.admin_button1=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.admin_monthly_report)
        self.admin_button1.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #farmers daily report
    def farmers_daily_report(self):
        #print function
        def print_receipt89():
            printText=self.my_receipt88.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt88.delete('1.0', 'end')
            self.top89.destroy()
        #Daily report
        def generate_daily_report():
            try:
                if self.farmers_cid_entry.get()=="":
                    messagebox.showerror("ERROR","Please Enter Customer ID",parent=self.top89)
                elif self.selection88=="":
                    messagebox.showerror("ERROR","Please Choose Date",parent=self.top89)
                else:
                    #id
                    c_id=self.farmers_cid_entry.get()
                    #names
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT First_Name, Last_Name, Surname FROM Customers WHERE Customer_ID=?",(self.farmers_cid_entry.get(),))
                    names=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in names:
                        f_name=record[0]
                        l_name=record[1]
                        s_name=record[2]
                    #morning sales
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT * FROM Morning_Sales WHERE Customer_ID=? AND DATE=?",(self.farmers_cid_entry.get(),self.selection88,))
                    results_m=c.fetchall()
                    conn.commit()
                    conn.close()
                    #afternoon sales
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT * FROM Afternoon_Sales WHERE Customer_ID=? AND DATE=?",(self.farmers_cid_entry.get(),self.selection88,))
                    results_a=c.fetchall()
                    conn.commit()
                    conn.close()
                    #evening sales
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("SELECT * FROM Evening_Sales WHERE Customer_ID=? AND DATE=?",(self.farmers_cid_entry.get(),self.selection88,))
                    results_e=c.fetchall()
                    conn.commit()
                    conn.close()
                    #loans
                    conn=sqlite3.connect("samaria database.db")
                    #conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE DATE=? AND Customer_ID=?",(self.selection88,self.farmers_cid_entry.get(),))
                    all_loans=c.fetchall()
                    conn.commit()
                    conn.close()
                    #feeds
                    conn=sqlite3.connect("samaria feeds database.db")
                    #conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT * FROM FEEDS WHERE DATE=? AND Customer_ID=?",(self.selection88,self.farmers_cid_entry.get(),))
                    all_feeds=c.fetchall()
                    conn.commit()
                    conn.close()
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1=f'DAILY REPORT FOR {self.selection88}'
                    heading2="NAME:"
                    heading3="CUSTOMER ID:"
                    heading4="MORNING SALES"
                    heading5="AFTERNOON SALES"
                    heading6="EVENING SALES"
                    heading7="DAILY TOTAL SALES:"
                    heading8="LOAN"
                    heading9="FEEDS"
                    heading10="Served By:"
                    #first delete the scrolledtext  contents
                    self.my_receipt88.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt88.insert('end', "\n" +title + "\n")
                    self.my_receipt88.insert('end', "\n" +sub + "\n")
                    self.my_receipt88.insert('end', "\n" +heading1+"\n")
                    self.my_receipt88.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
                    self.my_receipt88.insert('end', "\n" +heading2 +"\t" + f_name +"\t" +l_name +"\t"+s_name+"\n")
                    self.my_receipt88.insert('end', "\n" +heading3 +"\t" +c_id + "\n")
                    sum_morn=0.0
                    sum_after=0.0
                    sum_even=0.0
                    sum_feeds=0.0
                    #morning sales
                    if results_m==[]:
                        self.my_receipt88.insert('end', "\n" +"Total Morning Quantity:"+"\t"+str(0.0)+"\n")
                    else:
                        self.my_receipt88.insert('end', "\n" +heading4 +"\n")
                        self.my_receipt88.insert('end', "\n" +"Quantity" +"\t"+"Time"+"\t"+"Server"+"\n")
                        for x in results_m:
                            self.my_receipt88.insert('end', "\n" +f'{x[1]} Litres'+"\t"+str(x[3])+"\t"+str(x[2])+"\n")
                            sum_morn+=float(x[1])
                        self.my_receipt88.insert('end', "\n" +"Total Morning Quantity:"+"\t"+f'{sum_morn} Litres'+"\n")
                    #afternoon sales
                    if results_a==[]:
                        self.my_receipt88.insert('end', "\n" +"Total AfterNoon Quantity:"+"\t"+str(0.0)+"\n")
                    else:
                        self.my_receipt88.insert('end', "\n" +heading5 +"\n")
                        self.my_receipt88.insert('end', "\n" +"Quantity" +"\t"+"Time"+"\t"+"Server"+"\n")
                        for p in results_a:
                            self.my_receipt88.insert('end', "\n" +f'{p[1]} Litres'+"\t"+str(p[3])+"\t"+str(p[2])+"\n")
                            sum_after+=float(p[1])
                        self.my_receipt88.insert('end', "\n" +"Total AfterNoon Quantity:"+"\t"+f'{sum_after} Litres'+"\n")
                    #evening sales
                    if results_e==[]:
                        self.my_receipt88.insert('end', "\n" +"Total Evening Quantity:"+"\t"+str(0.0)+"\n")
                    else:
                        self.my_receipt88.insert('end', "\n" +heading6 +"\n")
                        self.my_receipt88.insert('end', "\n" +"Quantity" +"\t"+"Time"+"\t"+"Server"+"\n")
                        for v in results_e:
                            self.my_receipt88.insert('end', "\n" +f'{v[1]} Litres'+"\t"+str(v[3])+"\t"+str(v[2])+"\n")
                            sum_even+=float(v[1])
                        self.my_receipt88.insert('end', "\n" +"Total Evening Quantity:"+"\t"+f'{sum_even} Litres'+"\n")
                    #daily total
                    sum_daily=(sum_morn+sum_after+sum_even)
                    self.my_receipt88.insert('end', "\n" +heading7+"\t"+f'{sum_daily} Litres'+"\n")
                    #loan
                    if all_loans!=[]:
                        self.my_receipt88.insert('end', "\n" +heading8+"\n")
                        for u in all_loans:
                            self.my_receipt88.insert('end', "\n" +"Advance_Amount"+"\t"+"STATUS"+"\n")
                            self.my_receipt88.insert('end',"\n" +f'Kshs {u[5]}'+"\t"+str(u[6])+"\n")
                    #feeds
                    if all_feeds!=[]:
                        self.my_receipt88.insert('end', "\n" +heading9+"\n")
                        self.my_receipt88.insert('end', "\n" +"FEEDS NAME" +"\t"+"\t"+"PRICE"+"\t"+"\t"+"STATUS"+"\n")
                        for y in all_feeds:
                            self.my_receipt88.insert('end', "\n"+str(y[3])+"\t"+str(y[5])+"\t"+str(y[7])+"\n")
                            sum_feeds+=float(y[5])
                        self.my_receipt88.insert('end', "\n" +"Total Feeds Amount:"+"\t"+f'Kshs {sum_feeds}'+"\n")
                    #server
                    self.my_receipt88.insert('end', "\n" +heading10+"\t"+f'{server}'+"\n")
            except AttributeError:
                messagebox.showerror("ERROR","Please Choose Date",parent=self.top89)
            
        def grab_date88():
            self.top88=Toplevel()
            self.top88.title("SAMARIA MILK GROUP")
            self.top88.iconbitmap("logo1.ico")
            my_label=customtkinter.CTkLabel(self.top88, text="Choose Date",text_color="white",fg_color="maroon",width=200,height=25).pack(anchor="center",pady=5)
            self.cal88=Calendar(self.top88, selectmode="day", cursor="hand1",date_pattern="mm/dd/yyyy",year=self.currentDateTime.year,month=self.currentDateTime.month,day=self.currentDateTime.day)
            self.cal88.pack(pady=20)
            self.cal88.bind("<<CalendarSelected>>",clicker88) 
        def clicker88(e):
            self.selection88=self.cal88.get_date()
            self.top88.destroy()
        
        #toplevel
        self.top89=Toplevel()
        self.top89.iconbitmap("logo1.ico")
        self.title_frame=Frame(self.top89)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="FARMER'S DAILY REPORT"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top89,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.farmers_id_label=customtkinter.CTkLabel(self.left_frame,text="Enter Farmer's ID",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.farmers_id_label.grid(row=0,column=0,columnspan=3,padx=20,pady=5,sticky=E)
        self.farmers_cid_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.farmers_cid_entry.grid(row=0,column=3,columnspan=3,sticky=E)
        self.choose_date_button=customtkinter.CTkButton(self.left_frame,text="Choose Date",text_color="white",fg_color="red",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=grab_date88)
        self.choose_date_button.grid(row=0,column=6,columnspan=4,sticky=E,pady=10,padx=10)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_daily_report)
        self.generate_button.grid(row=0,column=10,padx=20,pady=10,columnspan=5,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt88=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=20)
        self.my_receipt88.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt89)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    #select period
    def select_period(self):
        self.top98=Toplevel()
        self.top98.title("SAMARIA MILK GROUP")
        self.top98.iconbitmap("logo1.ico")
        top_frame=Frame(self.top98)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT Period:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.clicked1,command=self.close_period,values=[f'From 1-15',f'From 16-{self.last_day}',"Entire Month"],width=160,height=25,fg_color="red",text_color="white")
        mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def close_period(self,e):
        get_period=self.clicked1.get()
        #print(get_period)
        self.top98.destroy()
    #farmers monthly report
    def farmers_monthly_report(self):
        #print function
        def print_receipt():
            printText=self.my_receipt.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt.delete('1.0', 'end')
            self.top90.destroy()
        #variables
        self.choser=StringVar()
        self.year_choser=StringVar()
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        years=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}']
        def choose_month(event):
            if self.choser.get()=="January":
                self.choosed=1
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="February":
                self.choosed=2
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="March":
                self.choosed=3
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="April":
                self.choosed=4
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="May":
                self.monthm=5
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="June":
                self.choosed=6
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="July":
                self.choosed=7
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="August":
                self.choosed=8
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="September":
                self.choosed=9
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="October":
                self.choosed=10
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="November":
                self.choosed=11
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
            if self.choser.get()=="December":
                self.choosed=12
                m_details=calendar.monthrange(self.mwaka,self.choosed)
                self.last_day=m_details[1]
                self.select_period()
        def generate_report():
            if self.farmers_id_entry.get()=="":
                messagebox.showerror("ERROR","Please Enter Farmer's ID",parent=self.top90)
            elif self.choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Month",parent=self.top90)
            elif self.year_choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Year",parent=self.top90)
            else:
                if self.clicked1.get()=="From 1-15":
                    #monthly payment rate
                    conn=sqlite3.connect("samaria database.db")
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT MONTHLY_RATE FROM Payments WHERE MONTH=? AND YEAR=? AND PERIOD=? AND CUSTOMER_ID=?",(self.choosed,self.year_choser.get(),self.clicked1.get(),self.farmers_id_entry.get(),))
                    rate=c.fetchone()
                    conn.commit()
                    conn.close()
                    if rate==None:
                        self.my_receipt.delete('1.0','end')
                        messagebox.showerror("ERROR",f'Report Not Compiled,Farmer Not Paid {self.clicked1.get()}{self.choser.get()} {self.year_choser.get()}',parent=self.top90)
                    else:
                        #get data
                        #names
                        conn=sqlite3.connect("samaria database.db")
                        c=conn.cursor()
                        c.execute("SELECT First_Name, Last_Name, Surname FROM Customers WHERE Customer_ID=?",(self.farmers_id_entry.get(),))
                        names=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in names:
                            f_name=record[0]
                            l_name=record[1]
                            s_name=record[2]
                        #id
                        c_id=self.farmers_id_entry.get()
                        #
                        conn=sqlite3.connect("samaria database.db")
                        #conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND PERIOD=? AND MONTH=? AND YEAR=?",(self.farmers_id_entry.get(),self.clicked1.get(),self.choosed,self.year_choser.get(),))
                        all_data=c.fetchone()
                        conn.commit()
                        conn.close()
                        bal=float(all_data[7]) - float(all_data[9] + all_data[8] + all_data[10])
                        #receipt
                        #define headings
                        title="SAMARIA MILK GROUP"
                        sub="Quality Milk, Healthy Life"
                        heading1=f'MONTHLY REPORT FOR {self.choser.get()} {self.year_choser.get()}'
                        heading11=f'PERIOD: {self.clicked1.get()}'
                        heading2="NAME:"
                        heading3="Farmer ID:"
                        heading4="ACCUMULATED SALES:"
                        heading5="PAYMENT RATE:"
                        heading6="TOTAL WAGES:"
                        heading7="Total Feeds Deducted:"
                        heading8="Total Advance Deducted:"
                        heading9="BALANCE:"
                        heading10="Served By:"
                        heading12="Feeds Transport Deducted:"
                        #first delete the scrolledtext  contents
                        self.my_receipt.delete('1.0', 'end')
                        #add stuff into our scrolled text
                        self.my_receipt.insert('end', "\n" +title + "\n")
                        self.my_receipt.insert('end', "\n" +sub + "\n")
                        self.my_receipt.insert('end', "\n" +heading1+"\n")
                        self.my_receipt.insert('end', "\n" +heading11+"\n")
                        self.my_receipt.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
                        self.my_receipt.insert('end', "\n" +heading2 +"\t" + f_name +"\t" +l_name +"\t"+s_name+"\n")
                        self.my_receipt.insert('end', "\n" +heading3 +"\t" +c_id + "\n")
                        self.my_receipt.insert('end', "\n" +heading4 +"\t" +f'{all_data[4]} Litres'+"\n")
                        self.my_receipt.insert('end', "\n" +heading5 +"\t" +f'Kshs {all_data[5]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading6 +"\t" +f'Kshs {all_data[7]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading7 +"\t" +f'Kshs {all_data[9]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading8 +"\t" +f'Kshs {all_data[8]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading12 +"\t" +f'Kshs {all_data[10]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading9+"\t"+f'Kshs {bal}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading10+"\t"+f'{server}'+"\n")
                        self.my_receipt.configure(state='disabled')
                if self.clicked1.get()==f'From 16-{self.last_day}':
                    #monthly payment rate
                    conn=sqlite3.connect("samaria database.db")
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT MONTHLY_RATE FROM Payments WHERE MONTH=? AND YEAR=? AND PERIOD=? AND CUSTOMER_ID=?",(self.choosed,self.year_choser.get(),self.clicked1.get(),self.farmers_id_entry.get(),))
                    rate=c.fetchone()
                    conn.commit()
                    conn.close()
                    if rate==None:
                        self.my_receipt.delete('1.0','end')
                        messagebox.showerror("ERROR",f'Report Not Compiled,Farmer Not Paid {self.clicked1.get()}{self.choser.get()} {self.year_choser.get()}',parent=self.top90)
                    else:
                        #get data
                        #names
                        conn=sqlite3.connect("samaria database.db")
                        c=conn.cursor()
                        c.execute("SELECT First_Name, Last_Name, Surname FROM Customers WHERE Customer_ID=?",(self.farmers_id_entry.get(),))
                        names=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in names:
                            f_name=record[0]
                            l_name=record[1]
                            s_name=record[2]
                        #id
                        c_id=self.farmers_id_entry.get()
                        #
                        conn=sqlite3.connect("samaria database.db")
                        #conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND PERIOD=? AND MONTH=? AND YEAR=?",(self.farmers_id_entry.get(),self.clicked1.get(),self.choosed,self.year_choser.get(),))
                        all_data=c.fetchone()
                        conn.commit()
                        conn.close()
                        bal=float(all_data[7]) - float(all_data[9] + all_data[8] + all_data[10])
                        #receipt
                        #define headings
                        title="SAMARIA MILK GROUP"
                        sub="Quality Milk, Healthy Life"
                        heading1=f'MONTHLY REPORT FOR {self.choser.get()} {self.year_choser.get()}'
                        heading11=f'PERIOD: {self.clicked1.get()}'
                        heading2="NAME:"
                        heading3="Farmer ID:"
                        heading4="ACCUMULATED SALES:"
                        heading5="PAYMENT RATE:"
                        heading6="TOTAL WAGES:"
                        heading7="Total Feeds Deducted:"
                        heading8="Total Advance Deducted:"
                        heading9="BALANCE:"
                        heading10="Served By:"
                        heading12="Feeds Transport Deducted:"
                        #first delete the scrolledtext  contents
                        self.my_receipt.delete('1.0', 'end')
                        #add stuff into our scrolled text
                        self.my_receipt.insert('end', "\n" +title + "\n")
                        self.my_receipt.insert('end', "\n" +sub + "\n")
                        self.my_receipt.insert('end', "\n" +heading1+"\n")
                        self.my_receipt.insert('end', "\n" +heading11+"\n")
                        self.my_receipt.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
                        self.my_receipt.insert('end', "\n" +heading2 +"\t" + f_name +"\t" +l_name +"\t"+s_name+"\n")
                        self.my_receipt.insert('end', "\n" +heading3 +"\t" +c_id + "\n")
                        self.my_receipt.insert('end', "\n" +heading4 +"\t" +f'{all_data[4]} Litres'+"\n")
                        self.my_receipt.insert('end', "\n" +heading5 +"\t" +f'Kshs {all_data[5]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading6 +"\t" +f'Kshs {all_data[7]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading7 +"\t" +f'Kshs {all_data[9]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading8 +"\t" +f'Kshs {all_data[8]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading12 +"\t" +f'Kshs {all_data[10]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading9+"\t"+f'Kshs {bal}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading10+"\t"+f'{server}'+"\n")
                else:
                    #monthly payment rate
                    conn=sqlite3.connect("samaria database.db")
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT MONTHLY_RATE FROM Payments WHERE MONTH=? AND YEAR=? AND PERIOD=? AND CUSTOMER_ID=?",(self.choosed,self.year_choser.get(),self.clicked1.get(),self.farmers_id_entry.get(),))
                    rate=c.fetchone()
                    conn.commit()
                    conn.close()
                    if rate==None:
                        self.my_receipt.delete('1.0','end')
                        messagebox.showerror("ERROR",f'Report Not Compiled,Farmer Not Paid {self.clicked1.get()}{self.choser.get()} {self.year_choser.get()}',parent=self.top90)
                    else:
                        #get data
                        #names
                        conn=sqlite3.connect("samaria database.db")
                        c=conn.cursor()
                        c.execute("SELECT First_Name, Last_Name, Surname FROM Customers WHERE Customer_ID=?",(self.farmers_id_entry.get(),))
                        names=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in names:
                            f_name=record[0]
                            l_name=record[1]
                            s_name=record[2]
                        #id
                        c_id=self.farmers_id_entry.get()
                        #
                        conn=sqlite3.connect("samaria database.db")
                        #conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND PERIOD=? AND MONTH=? AND YEAR=?",(self.farmers_id_entry.get(),self.clicked1.get(),self.choosed,self.year_choser.get(),))
                        all_data=c.fetchone()
                        conn.commit()
                        conn.close()
                        bal=float(all_data[7]) - float(all_data[9] + all_data[8] + all_data[10])
                        #receipt
                        #define headings
                        title="SAMARIA MILK GROUP"
                        sub="Quality Milk, Healthy Life"
                        heading1=f'MONTHLY REPORT FOR {self.choser.get()} {self.year_choser.get()}'
                        heading11=f'PERIOD: {self.clicked1.get()}'
                        heading2="NAME:"
                        heading3="Farmer ID:"
                        heading4="MONTHLY ACCUMULATED SALES:"
                        heading5="MONTHLY PAYMENT RATE:"
                        heading6="TOTAL WAGES:"
                        heading7="Total Feeds Deducted:"
                        heading8="Total Advance Deducted:"
                        heading9="BALANCE:"
                        heading10="Served By:"
                        heading12="Feeds Transport Deducted:"
                        #first delete the scrolledtext  contents
                        self.my_receipt.delete('1.0', 'end')
                        #add stuff into our scrolled text
                        self.my_receipt.insert('end', "\n" +title + "\n")
                        self.my_receipt.insert('end', "\n" +sub + "\n")
                        self.my_receipt.insert('end', "\n" +heading1+"\n")
                        self.my_receipt.insert('end', "\n" +heading11+"\n")
                        self.my_receipt.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
                        self.my_receipt.insert('end', "\n" +heading2 +"\t" + f_name +"\t" +l_name +"\t"+s_name+"\n")
                        self.my_receipt.insert('end', "\n" +heading3 +"\t" +c_id + "\n")
                        self.my_receipt.insert('end', "\n" +heading4 +"\t" +f'{all_data[4]} Litres'+"\n")
                        self.my_receipt.insert('end', "\n" +heading5 +"\t" +f'Kshs {all_data[5]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading6 +"\t" +f'Kshs {all_data[7]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading7 +"\t" +f'Kshs {all_data[9]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading8 +"\t" +f'Kshs {all_data[8]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading12 +"\t" +f'Kshs {all_data[10]}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading9+"\t"+f'Kshs {bal}'+"\n")
                        self.my_receipt.insert('end', "\n" +heading10+"\t"+f'{server}'+"\n")
        #toplevel
        self.top90=Toplevel()
        self.top90.iconbitmap("logo1.ico")
        self.title_frame=Frame(self.top90)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="FARMER'S MONTHLY REPORT"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top90,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.farmers_id_label=customtkinter.CTkLabel(self.left_frame,text="Enter Farmer's ID",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.farmers_id_label.grid(row=0,column=0,columnspan=3,padx=20,pady=5,sticky=E)
        self.farmers_id_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.farmers_id_entry.grid(row=0,column=3,columnspan=2,sticky=E)
        self.choose_month_label=customtkinter.CTkLabel(self.left_frame,text="Choose Month",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.choose_month_label.grid(row=0,column=5,columnspan=2,padx=20,pady=5,sticky=E)
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.choser,values=months,fg_color="red",text_color="white",width=150,height=25,command=choose_month)
        self.choose_month_menu.grid(row=0,column=7,columnspan=2)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.year_choser,values=years,fg_color="red",text_color="white",width=150,height=25)
        self.choose_year_menu.grid(row=0,column=9,columnspan=2,padx=10)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_report)
        self.generate_button.grid(row=0,column=11,padx=20,pady=10,columnspan=4,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=20)
        self.my_receipt.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    #notifications
    def notifications(self):
        #toplevel
        self.top40=Toplevel()
        self.top40.iconbitmap("logo1.ico")
        self.top40.title("SAMARIA MILK GROUP")
        self.top40.state('zoomed')
        self.title_frame=Frame(self.top40)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="Notifications"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top40,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.notify_title_label=customtkinter.CTkLabel(self.left_frame,text="Compose Message",fg_color="brown",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30)
        self.notify_title_label.grid(row=0,column=0,columnspan=10,padx=20,pady=15,sticky=EW)
        self.my_receipt=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=20)
        self.my_receipt.grid(row=1,column=0,columnspan=10,padx=20)
        self.send_button=customtkinter.CTkButton(self.left_frame,text="Send Messages",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=self.send_bulk_messages)
        self.send_button.grid(row=2,column=0,columnspan=15,padx=10,pady=10)
        
    #send bulk messages
    def send_bulk_messages(self):
        #variable
        start=0
        #query
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Phone_Number FROM Customers")
        all_phones=c.fetchall()
        c.execute("SELECT COUNT(Phone_Number) FROM Customers")
        all_no=c.fetchone()
        conn.commit()
        conn.close()
        for record in all_phones:
            if record =='':
                print('no number')
            else:
                try:
                    #requests mobitechtechnologies
                    url = "https://api.mobitechtechnologies.com/sms/sendsms"

                    payload = json.dumps({
                        "mobile": f'+254{record}',
                        "response_type": "json",
                        "sender_name": 23107,
                        "service_id": 0,
                        "message": self.my_receipt.get("1.0", 'end')
                    })
                    headers = {
                        'h_api_key': 'ead62d3ed9c918bb366cba5ec6692224d8926bd8b0c339c0a58cc137075b3e4a',
                        'Content-Type': 'application/json'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)
                    print(response.text)
                    x=response.text[20]
                    if x != '0':
                        print(x)
                        messagebox.showerror("ERROR",f'{start} Out of {all_no} SMS Sent,Please Recharge your Account And Try Again',parent=self.top40)
                        break
                    else:
                        messagebox.showinfo("BRAVO",f'{start} Out of {all_no} SMS Sent Succesfully',parent=self.top40)
            
                except:
                    messagebox.showerror("ERROR","SMS Not Sent,Please Check Your Internet Connectivity And Try Again",parent=self.top40)
                    break
            start+=1
    #loading functions
    def load_home_window(self):
        home=Landing_Page(root)
        root.mainloop()

    def load_customer_records_window(self):
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
         sales=Customer_Sales(root)
         root.mainloop()
    def load_customer_feeds_window(self):
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        l_feeds=Local_Feeds(root)
        root.mainloop()    
class Customer_Records:
    def __init__(self,master)-> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x800")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
        #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        records_menu.add_separator()
        records_menu.add_command(label="Bank Details",command=self.selected)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        report_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Report", menu=report_menu)
        report_menu.add_command(label="Records Report", command=self.records_report)
        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)

        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

        #variables
        global payment_mode
        self.currentDateTime= date.today()
        self.yesterday=date.today() - timedelta(7)
        self.today1=self.currentDateTime
        self.today=self.currentDateTime.strftime("%A - %B %d, %Y")
        self.time=datetime.now()
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.today2=self.time.strftime("%d/%m/%Y")
        #treeview
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="violet",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="violet"
                        )
        #change selected color
        style.map('Treeview',
                  background=[('selected', 'green')])
        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="Farmer RECORDS"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4, pady=5)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #create a frame so that we can add a scrollbar
        self.tree_frame=Frame(self.top0,highlightbackground="green", highlightthickness=5,bd=0)
        self.tree_frame.pack(pady=10, anchor="w", padx=10)
        #treeview scrollbar
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        #create our treeview
        self.my_tree=ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=14)
        self.my_tree.pack()
        #configure the scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)
        #define our columns
        self.my_tree['columns']=("First Name", "Last Name","Surname", "Address","Customer_ID","National_ID","Phone Number","Payment Mode","DATE")
        #Format our columns
        self.my_tree.column("#0", width=0,stretch=NO)
        self.my_tree.column("First Name" ,anchor="w", width=150)
        self.my_tree.column("Last Name" ,anchor="w", width=150)
        self.my_tree.column("Surname" ,anchor="w", width=100)
        self.my_tree.column("Address" ,anchor="w", width=150)
        self.my_tree.column("Customer_ID" ,anchor="w", width=150)
        self.my_tree.column("National_ID", anchor="w", width=150)
        self.my_tree.column("Phone Number" ,anchor="w", width=200)
        self.my_tree.column("Payment Mode" ,anchor="w", width=150)
        self.my_tree.column("DATE" ,anchor="w", width=220)
        #create headings
        self.my_tree.heading("#0", text="")
        self.my_tree.heading("First Name", text="First Name", anchor="w")
        self.my_tree.heading("Last Name", text="Last Name", anchor="w")
        self.my_tree.heading("Surname", text="Surname", anchor="w")
        self.my_tree.heading("Address", text="Address", anchor="w")
        self.my_tree.heading("Customer_ID", text="Farmer_ID", anchor="w")
        self.my_tree.heading("National_ID", text="National_ID", anchor="w")
        self.my_tree.heading("Phone Number", text="Phone Number", anchor="w")
        self.my_tree.heading("Payment Mode", text="Payment Mode", anchor="w")
        self.my_tree.heading("DATE", text="Date", anchor="w")
        #create striped row tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")
        #binding
        self.my_tree.bind("<ButtonRelease-1>",self.clicker)
        #create frame
        self.my_frame=Frame(self.top0)
        self.my_frame.pack(pady=5, padx=10,anchor="w")

        #create textboxes labels
        self.first_name_label=customtkinter.CTkLabel(self.my_frame, text="FIRST NAME:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.first_name_label.grid(row=0, column=0, padx=10, pady=5,sticky=W)
        self.last_name_label=customtkinter.CTkLabel(self.my_frame, text="LAST NAME:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.last_name_label.grid(row=0, column=2, padx=10, pady=5,sticky=W)
        self.surname_label=customtkinter.CTkLabel(self.my_frame, text="SURNAME:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.surname_label.grid(row=0, column=4, padx=10, pady=5,sticky=W)
        self.address_label=customtkinter.CTkLabel(self.my_frame, text="ADDRESS:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.address_label.grid(row=0, column=6, padx=10, pady=5,sticky=W)
        self.customer_id_label=customtkinter.CTkLabel(self.my_frame, text="FARMER ID:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.customer_id_label.grid(row=1, column=0, padx=10, pady=5,sticky=W)
        self.national_ID_label=customtkinter.CTkLabel(self.my_frame, text="National_ID:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.national_ID_label.grid(row=1,column=2, padx=10, pady=5,sticky=W)
        self.phone_number_label=customtkinter.CTkLabel(self.my_frame, text="PHONE NUMBER:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.phone_number_label.grid(row=1, column=4, padx=10, pady=5,sticky=W)
        self.payment_mode_label=customtkinter.CTkLabel(self.my_frame, text="PAYMENT MODE:",width=100, height=25,fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"))
        self.payment_mode_label.grid(row=1, column=6, padx=10, pady=5,sticky=W)
        #create text boxes
        self.first_name_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.first_name_box.grid(row=0, column=1)
        self.last_name_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.last_name_box.grid(row=0, column=3)
        self.surname_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.surname_box.grid(row=0, column=5)    
        self.address_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.address_box.grid(row=0, column=7)                                                                                                                                          
        self.customer_id_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.customer_id_box.grid(row=1, column=1)
        self.national_id_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue")
        self.national_id_box.grid(row=1,column=3)
        self.phone_number_box=customtkinter.CTkEntry(self.my_frame,width=120, height=30,border_color="blue",placeholder_text="Enter 9 digits 12-345-678",placeholder_text_color="purple")
        self.phone_number_box.grid(row=1, column=5)
         #dropdown menu
        self.clicked=StringVar()
        self.payment_mode_box=customtkinter.CTkOptionMenu(self.my_frame,variable=self.clicked,values=["Bank Account", "MPESA","CASH"],dropdown_color="white",fg_color="red",text_color="white")
        self.payment_mode_box.grid(row=1, column=7)
        #add record button
        self.add_record_btn=customtkinter.CTkButton(self.my_frame, text="Add New Record", fg_color="purple", text_color="white", text_font=("Consollas 10", -17, "bold"),width=200, height=40,command=self.add_record)
        self.add_record_btn.grid(row=2, column=0,columnspan=5,ipadx=50,padx=10,pady=10)
        #update button
        self.update_btn=customtkinter.CTkButton(self.my_frame, text="Update Existing Record", fg_color="purple", text_color="white", text_font=("Consollas 10", -17, "bold"),width=200, height=40,command=self.update_record)
        self.update_btn.grid( row=2, column=5,columnspan=5,padx=10,ipadx=50,pady=10)
        
        #create a database or connect to one
        conn = sqlite3.connect('samaria database.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        # create a cursor
        c = conn.cursor()
        '''
        #drop table
        c.execute("DROP TABLE Customers")
        '''
        # create a table
        c.execute(""" CREATE TABLE IF NOT EXISTS Customers(
                    First_name TEXT NOT NULL,
                    Last_name TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    Address TEXT NOT NULL,
                    Customer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    National_ID INT NOT NULL UNIQUE,
                    Phone_number INT NOT NULL,
                    Payment_mode TEXT NOT NULL,
                    DATE TEXT NOT NULL
                    )""")            
        conn.commit()
        conn.close()
        # create bank account holder table
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE BANK_ACCOUNTS")
        c.execute("DROP TABLE BANK_NAMES")
        print("table dropped successfully")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS BANK_ACCOUNTS(
                    FIRST_NAME   TEXT NOT NULL,
                    LAST_NAME TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    Customer_ID INTEGER PRIMARY KEY,
                    BANK_ACCOUNT_NUMBER INT NOT NULL UNIQUE,
                    BANK_NAME TEXT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS BANK_NAMES(
                    BANK_NAME TEXT PRIMARY KEY NOT NULL
                    )""")
        conn.commit()
        conn.close()
        print("table created succesfully")
        self.query_database()

    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    # clear the textboxes
    def clear_entries(self):
            self.first_name_box.delete(0, END)
            self.last_name_box.delete(0, END)
            self.surname_box.delete(0,END)
            self.address_box.delete(0, END)
            self.customer_id_box.delete(0, END)
            self.national_id_box.delete(0, END)
            self.phone_number_box.delete(0, END)
            
    #create binding function
    def clicker(self,event):
        #self.select_record()
        #clear entry boxes
        self.clear_entries()
         #grab record number
        selected=self.my_tree.focus()
        #grab record values
        values=self.my_tree.item(selected,'values')
        #output to entry boxes
        self.first_name_box.insert(0, values[0])
        self.last_name_box.insert(0, values[1])
        self.surname_box.insert(0,values[2])
        self.address_box.insert(0, values[3])
        self.customer_id_box.insert(0, values[4])
        self.national_id_box.insert(0, values[5])
        self.phone_number_box.insert(0, values[6])
        #double click
        #my_tree.bind("<Double-1>", clicker)
        #single click(button release)
        #self.my_tree.bind("<ButtonRelease-1>",self.clicker)

    # create query function
    def query_database(self):
            conn=sqlite3.connect('samaria database.db')
            c= conn.cursor()
            #query the database
            c.execute("SELECT * FROM Customers ORDER BY Customer_ID ASC")
            records=c.fetchall()
            #add our data to the treeview
            self.count=0
            for record in records:
                if self.count%2==0:
                    self.my_tree.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],f'0{record[6]}',record[7],record[8]), tags=("evenrow",))
                else:
                    self.my_tree.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5],f'0{record[6]}',record[7],record[8]), tags=("oddrow",))

                self.count+=1
                      
            conn.commit()
            conn.close()
    
    #update records
    def update_record(self):
        if self.customer_id_box.get()=="":
            messagebox.showerror("ERROR", "PLEASE ENTER Farmer ID",parent =self.top0)
        #elif len(self.national_id_box.get()) !=8:
            #messagebox.showerror("ERROR","Please Enter Valid National ID Number",parent=self.top0)
        #elif len(self.phone_number_box.get()) !=10:
            #messagebox.showerror("ERROR","Please Enter Valid Phone Number",parent=self.top0)
        elif self.clicked.get()=="":
            messagebox.showerror("ERROR","Please Specify Payment Mode",parent=self.top0)
        else:
            #update the database
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Customers")
            results=c.fetchall()
            for record in results:
                initial_date=record[8]
            c.execute(""" UPDATE Customers SET
                        First_Name=:f_name,
                        Last_Name=:l_name,
                        Surname=:s_name,
                        Address=:address,
                        Customer_ID=:c_id,
                        National_ID=:n_id,
                        Phone_number=:p_no,
                        Payment_mode=:p_mode,
                        DATE=:date

                        WHERE Customer_ID=:c_id""",
                        {
                            'f_name':self.first_name_box.get(),
                            'l_name':self.last_name_box.get(),
                            's_name':self.surname_box.get(),
                            'address':self.address_box.get(),
                            'c_id':self.customer_id_box.get(),
                            'n_id':self.national_id_box.get(),
                            'p_no':self.phone_number_box.get(),
                            'p_mode':self.clicked.get(),
                            'date':initial_date
                            })
            conn.commit()
            conn.close()
            #clear entry boxes
            self.clear_entries()
            #refresh the treeview
            self.my_tree.delete(* self.my_tree.get_children())
            #run to pull data again from database
            self.query_database()
            messagebox.showinfo("Bravo","Record Updated Succesfully",parent=self.top0)
            if  self.clicked.get() =="Bank Account":
                    self.selected()
    #add new record
    def add_record(self):
        #if len(self.national_id_box.get()) !=8:
            #messagebox.showerror("ERROR","Please Enter Valid National ID Number",parent=self.top0)
        if len(self.phone_number_box.get()) !=9:
            messagebox.showerror("ERROR","Please Enter 9 digits phone number, ommit the first 0",parent=self.top0)
        if self.clicked.get()=="":
            messagebox.showerror("ERROR","Please Specify Payment Mode",parent=self.top0)
        else:
            #message
            try:
                #requests mobitechtechnologies
                url = "https://api.mobitechtechnologies.com/sms/sendsms"

                payload = json.dumps({
                    "mobile": f'+254{self.phone_number_box.get()}',
                    "response_type": "json",
                    "sender_name": 23107,
                    "service_id": 0,
                    "message": "Welcome At Samaria Milk Group:Quality Milk, Healthy Life. For any Queries,Contact:0724507816 or 0719440945"
                })
                headers = {
                    'h_api_key': 'ead62d3ed9c918bb366cba5ec6692224d8926bd8b0c339c0a58cc137075b3e4a',
                    'Content-Type': 'application/json'
                }

                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                x=response.text[20]
                if x != '0':
                    print(x)
                    messagebox.showerror("ERROR","SMS Not Sent,Please Recharge your Account And Try Again",parent=self.top0)
                else:
                    messagebox.showinfo("BRAVO","SMS Sent Succesfully",parent=self.top0)
                    try:
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Customers VALUES(:First_name, :Last_name, :Surname, :Address,:Customer_ID,:National_ID,:Phone_number, :Payment_mode,:DATE)",
                                    {
                                        'First_name': self.first_name_box.get(),
                                        'Last_name' :self.last_name_box.get(),
                                        'Surname': self.surname_box.get(),
                                        'Address': self.address_box.get(),
                                        'Customer_ID': None,
                                        'National_ID': self.national_id_box.get(),
                                        'Phone_number': self.phone_number_box.get(),
                                        'Payment_mode': self.clicked.get(),
                                        'DATE': self.today1
                                        })
                        conn.commit()
                        conn.close()
                        #clear entry boxes
                        self.clear_entries()
                        #refresh the treeview
                        self.my_tree.delete(* self.my_tree.get_children())
                        #run to pull data again from database
                        self.query_database()
                        #bankers
                        if  self.clicked.get() =="Bank Account":
                            self.selected()
                        #messagebox
                        messagebox.showinfo("Information", "New record has been added successfully",parent =self.top0)
                    except:
                        messagebox.showerror("ERROR","Record Already Exist,Check National ID No And Try Again",parent=self.top0)
            except:
                messagebox.showerror("ERROR","SMS Not Sent,Please Check Your Internet Connectivity And Try Again",parent=self.top0)
            #clear entry boxes
            self.clear_entries()
                
    #delete one record
    def remove_one(self):
        if self.customer_id_box.get()=="":
            messagebox.showerror("ERROR", "PLEASE ENTER CUSTOMER ID",parent =self.top0)
        else:
            #messagebox
            response=messagebox.askyesno("Confirm", "Selected Record will be deleted",parent =self.top0)
            if response==1:
                x=self.my_tree.selection()[0]
                self.my_tree.delete(x)
                #delete from database
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Customers WHERE Customer_ID=" +self.customer_id_box.get())
                conn.commit()
                conn.close()
                #clear entry boxes
                self.clear_entries()
                #messagebox
                messagebox.showinfo("Information", "Record deleted succesfully",parent =self.top0)

    def selected(self,arg=None):
            self.top=Toplevel()
            #self.top.geometry("400x200")
            self.top.title("SAMARIA MILK GROUP")
            self.top.iconbitmap("logo1.ico")
            #menu
            my_menu1 = Menu(self.top)
            self.top.config(menu=my_menu1)
            #create menu item
            bank_menu= Menu(my_menu1,tearoff=0)
            my_menu1.add_cascade(label="Bank Names", menu=bank_menu)
            bank_menu.add_command(label="Add Bank Name", command=self.add_bank_name)
            #variable
            self.chooser=StringVar()
            #database
            conn=sqlite3.connect("samaria database.db")
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT BANK_NAME FROM BANK_NAMES")
            banks=c.fetchall()
            if banks==None:
                banks=[""]
            conn.commit()
            conn.close()
            my_frame1=Frame(self.top)
            my_frame1.pack(anchor="w")
            self.bank_label=customtkinter.CTkLabel(my_frame1, text="BANK DETAILS", fg_color="brown", text_color="white", text_font=("Consollas 10",-25,"underline", "bold"),width=250, height=35)
            self.bank_label.grid(row=0, column=0, columnspan=6, pady=10)
            #treeview
            self.tree_frame1=Frame(my_frame1,highlightbackground="green", highlightthickness=5,bd=0)
            self.tree_frame1.grid(row=1,column=0,columnspan=6,pady=10,padx=10)
            #treeview scrollbar
            self.tree_scroll1=Scrollbar(self.tree_frame1)
            self.tree_scroll1.pack(side=RIGHT, fill=Y)

            #create our treeview
            self.my_tree1=ttk.Treeview(self.tree_frame1, yscrollcommand=self.tree_scroll1.set)
            self.my_tree1.pack()
            #configure the scrollbar
            self.tree_scroll1.config(command=self.my_tree1.yview)
            #define our columns
            self.my_tree1['columns']=("First Name", "Last Name","Surname","Customer_ID","Bank Account Number","Bank Name")
            #Format our columns
            self.my_tree1.column("#0", width=0,stretch=NO)
            self.my_tree1.column("First Name" ,anchor="w", width=150)
            self.my_tree1.column("Last Name" ,anchor="w", width=150)
            self.my_tree1.column("Surname" ,anchor="w", width=100)
            self.my_tree1.column("Customer_ID" ,anchor="w", width=150)
            self.my_tree1.column("Bank Account Number" ,anchor="w", width=200)
            self.my_tree1.column("Bank Name", anchor="w", width=150)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("First Name", text="First Name", anchor="w")
            self.my_tree1.heading("Last Name", text="Last Name", anchor="w")
            self.my_tree1.heading("Surname", text="Surname", anchor="w")
            self.my_tree1.heading("Customer_ID", text="Farmer_ID", anchor="w")
            self.my_tree1.heading("Bank Account Number", text="Account Number", anchor="w")
            self.my_tree1.heading("Bank Name", text="Bank Name", anchor="w")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="lightblue")
            self.my_tree1.bind("<ButtonRelease-1>",self.clicker1)
            self.first_name_label=customtkinter.CTkLabel(my_frame1, text="First Name:", fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.first_name_label.grid(row=2, column=0,sticky=W, padx=10, pady=5)
            self.first_name_entry=customtkinter.CTkEntry(my_frame1,width=150,height=25,border_color="blue")
            self.first_name_entry.grid(row=2,column=1)
            self.last_name_label=customtkinter.CTkLabel(my_frame1, text="Last Name:", fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.last_name_label.grid(row=2, column=2,sticky=W, padx=10, pady=5)
            self.last_name_entry=customtkinter.CTkEntry(my_frame1,width=150,height=25,border_color="blue")
            self.last_name_entry.grid(row=2,column=3)
            self.surname_label=customtkinter.CTkLabel(my_frame1, text="Surname:", fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.surname_label.grid(row=2, column=4,sticky=W, padx=10, pady=5)
            self.surname_entry=customtkinter.CTkEntry(my_frame1,width=150,height=25,border_color="blue")
            self.surname_entry.grid(row=2,column=5)
            self.customer_id_label=customtkinter.CTkLabel(my_frame1, text="Farmer ID:", fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.customer_id_label.grid(row=3, column=0,sticky=W, padx=10, pady=5)
            self.customer_id_entry=customtkinter.CTkEntry(my_frame1,width=150,height=25,border_color="blue")
            self.customer_id_entry.grid(row=3,column=1)
            self.bank_account_label=customtkinter.CTkLabel(my_frame1, text="Bank Account Number:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.bank_account_label.grid(row=3, column=2,sticky=W, padx=10, pady=5)
            self.bank_account_entry=customtkinter.CTkEntry(my_frame1,width=150,height=25,border_color="blue")
            self.bank_account_entry.grid(row=3,column=3)
            self.bank_name_label=customtkinter.CTkLabel(my_frame1, text="Bank Name:", fg_color="brown", text_color="white", text_font=("Consollas 10",-15, "bold"),width=150, height=25)
            self.bank_name_label.grid(row=3, column=4,sticky=W, padx=10, pady=5)
            self.bank_name_menu=customtkinter.CTkOptionMenu(my_frame1,width=150,height=25,text_color="white",fg_color="red",variable=self.chooser,values=banks)
            self.bank_name_menu.grid(row=3,column=5)
            self.my_update_button=customtkinter.CTkButton(my_frame1, text="Update Record",fg_color="purple", text_color="white", text_font=("Consollas 10",-18, "bold"),width=200, height=40, command=self.update_bank)
            self.my_update_button.grid(row=4, column=3, columnspan=3,ipadx=10,pady=10)
            self.my_add_button=customtkinter.CTkButton(my_frame1, text="Add Record",fg_color="purple", text_color="white", text_font=("Consollas 10",-18, "bold"),width=200, height=40, command=self.save_bank)
            self.my_add_button.grid(row=4, column=0, columnspan=3,ipadx=20,pady=10)
            self.query_database1()
    #clear entries
    def clear_entries1(self):
        self.first_name_entry.delete(0,END)
        self.last_name_entry.delete(0,END)
        self.surname_entry.delete(0,END)
        self.customer_id_entry.delete(0,END)
        self.bank_account_entry.delete(0,END)
    #create binding function
    def clicker1(self,event):
        #self.select_record()
        #clear entry boxes
        self.clear_entries1()
        #grab record number
        selected=self.my_tree1.focus()
        #grab record values
        values=self.my_tree1.item(selected,'values')
        #output to entry boxes
        self.first_name_entry.insert(0, values[0])
        self.last_name_entry.insert(0, values[1])
        self.surname_entry.insert(0, values[2])
        self.customer_id_entry.insert(0, values[3])
        self.bank_account_entry.insert(0, values[4])
        #double click
        #my_tree1.bind("<Double-1>", clicker)
        #single click(button release)
        #self.my_tree1.bind("<ButtonRelease-1>",self.clicker1)
    def query_database1(self):
            conn=sqlite3.connect('samaria database.db')
            c= conn.cursor()
            #query the database
            c.execute("SELECT * FROM BANK_ACCOUNTS ORDER BY Customer_ID ASC")
            records=c.fetchall()
            conn.commit()
            conn.close()
            #add our data to the treeview
            self.count=0
            for record in records:
                if self.count%2==0:
                    self.my_tree1.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=("evenrow",))
                else:
                    self.my_tree1.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]), tags=("oddrow",))

                self.count+=1
    def add_bank_name(self):
        self.top55=Toplevel()
        self.top55.iconbitmap("logo1.ico")
        self.top55.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top55)
        my_frame.pack()
        self.title_label=customtkinter.CTkLabel(my_frame,text="ADD BANK",fg_color="maroon",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.bank_name_label=customtkinter.CTkLabel(my_frame,text="Enter Bank Name:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.bank_name_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
        self.bank_name_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
        self.bank_name_entry.grid(row=1,column=2,columnspan=2)
        self.save_button=customtkinter.CTkButton(my_frame,text="ADD BANK NAME",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=self.save_bank_name)
        self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20,ipady=10)
    def save_bank_name(self):
        self.top.destroy()
        if self.bank_name_entry.get()=="":
            messagebox.showerror("ERROR","Please Enter Bank Name",parent=self.top55)
        else:
            try:
                conn=sqlite3.connect("samaria database.db")
                c=conn.cursor()
                c.execute("INSERT INTO BANK_NAMES VALUES(:BANK_NAME)",
                          {
                              'BANK_NAME':self.bank_name_entry.get()
                          })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo","Bank Name Added Succesfully",parent=self.top55)
            except:
                messagebox.showerror("ERROR","BANK NAME ALREADY EXISTS",parent=self.top55)
            self.bank_name_entry.delete(0,END)
            self.top55.destroy()
            self.selected()
    def save_bank(self):
        #insert into our bank account table
        if ((self.chooser.get()=="") and (self.bank_account_entry.get()=="")):
            messagebox.showerror("ERROR","Please Enter Bank Details",parent=self.top0)
            self.top.destroy()
        bk_no=len(self.bank_account_entry.get())
        if int(bk_no)<8:
            messagebox.showerror("ERROR","Please Enter a Valid Bank Account Number",parent=self.top)
        elif int(bk_no)>20:
            messagebox.showerror("ERROR","Please Enter a Valid Bank Account Number",parent=self.top)
        elif self.chooser.get()=="":
            messagebox.showerror("ERROR","Please Choose Bank Name",parent=self.top)
        else:
            try:
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()    
                c.execute("INSERT INTO BANK_ACCOUNTS VALUES(:FIRST_NAME, :LAST_NAME, :Surname,:Customer_ID,:BANK_ACCOUNT_NUMBER, :BANK_NAME)",
                            {
                                'FIRST_NAME': self.first_name_entry.get(),
                                'LAST_NAME': self.last_name_entry.get(),
                                'Surname':self.surname_entry.get(),
                                'Customer_ID': self.customer_id_entry.get(),
                                'BANK_ACCOUNT_NUMBER': self.bank_account_entry.get(),
                                'BANK_NAME': self.chooser.get()
                                    })
                conn.commit()
                conn.close()
                #clear entries
                self.clear_entries1()
                #refresh the treeview
                self.my_tree1.delete(* self.my_tree1.get_children())
                #run to pull data again from database
                self.query_database1()
                messagebox.showinfo("Bravo","Records Saved Succesfully",parent =self.top)
            except:
                messagebox.showerror("ERROR","Record Already Exist",parent=self.top)
                #clear entries
                self.clear_entries1()
    def update_bank(self):
        #messagebox
        response=messagebox.askyesno("Confirm", "Selected Record will be deleted",parent =self.top)
        if response==1:
            bk_no=len(self.bank_account_entry.get())
            if int(bk_no)<8:
                messagebox.showerror("ERROR","Please Enter a Valid Bank Account Number",parent=self.top)
            elif int(bk_no)>20:
                messagebox.showerror("ERROR","Please Enter a Valid Bank Account Number",parent=self.top)
            elif self.chooser.get()=="":
                messagebox.showerror("ERROR","Please Choose Bank Name",parent=self.top)
            else:
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("""UPDATE BANK_ACCOUNTS SET
                          FIRST_NAME=:F_name,
                          LAST_NAME=:L_name,
                          Surname=:S_name,
                          Customer_ID=:C_id,
                          BANK_ACCOUNT_NUMBER=:b_a_n,
                          BANK_NAME=:B_name

                          WHERE Customer_ID=:C_id""",
                          {
                              'F_name':self.first_name_entry.get(),
                              'L_name':self.last_name_entry.get(),
                              'S_name':self.surname_entry.get(),
                              'C_id':self.customer_id_entry.get(),
                              'b_a_n':self.bank_account_entry.get(),
                              'B_name':self.chooser.get()
                              })
                conn.commit()
                conn.close()
                #clear entries
                self.clear_entries1()
                #refresh the treeview
                self.my_tree1.delete(* self.my_tree1.get_children())
                #run to pull data again from database
                self.query_database1()
                messagebox.showinfo("Bravo","Record Updated Succesfully",parent=self.top)
    def remove_bank(self):
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "PLEASE ENTER Farmer ID",parent =self.top)
        else:
            #messagebox
            response=messagebox.askyesno("Confirm", "Selected Record will be deleted",parent =self.top)
            if response==1:
                x=self.my_tree1.selection()[0]
                self.my_tree1.delete(x)
                #delete from database
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("DELETE FROM BANK_ACCOUNTS WHERE Customer_ID=" +self.customer_id_entry.get())
                conn.commit()
                conn.close()
                #clear entry boxes
                self.clear_entries1()
                #messagebox
                messagebox.showinfo("Information", "Record deleted succesfully",parent =self.top)
    def records_report(self):
        #variables
        self.module_chooser=StringVar()
        #print function
        def print_receipt85():
            printText=self.my_receipt85.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt85.delete('1.0', 'end')
        def generate_records_report():
            if self.module_chooser.get()=="ALL":
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1="Served By:"
                #first delete the scrolledtext  contents
                self.my_receipt85.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt85.insert('end', "\n" +title + "\n")
                self.my_receipt85.insert('end', "\n" +sub + "\n")
                self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                self.my_receipt85.insert('end', "\n" +f'{self.module_chooser.get()} FARMERS'+"\n")
                self.my_receipt85.insert('end', "\n" +"Name"+"\t"+"\t"+"\t"+"Address"+"\t"+"Farmer_ID"+"\t"+" Phone Number"+"\n")
                #query
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM Customers")
                all_farmers=c.fetchall()
                conn.commit()
                conn.close()
                for x in all_farmers:
                    self.my_receipt85.insert('end', "\n" +str(x[0])+"\t"+str(x[1])+"\t"+str(x[2])+"\t"+str(x[3])+"\t"+str(x[4])+"\t"+f'0{x[6]}'+"\n")
                self.my_receipt85.insert('end', "\n" +heading1+"\t"+server+"\n")
            if self.module_chooser.get()=="M~PESA PAY MODE":
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1="Served By:"
                #first delete the scrolledtext  contents
                self.my_receipt85.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt85.insert('end', "\n" +title + "\n")
                self.my_receipt85.insert('end', "\n" +sub + "\n")
                self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                self.my_receipt85.insert('end', "\n" +f'{self.module_chooser.get()} FARMERS'+"\n")
                self.my_receipt85.insert('end', "\n" +"Name"+"\t"+"\t"+"\t"+"Address"+"\t"+"Farmer_ID"+" National_ID"+" Phone Number"+"\n")
                #query
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM Customers WHERE Payment_Mode=?",("MPESA",))
                all_farmers=c.fetchall()
                conn.commit()
                conn.close()
                for x in all_farmers:
                    self.my_receipt85.insert('end', "\n" +str(x[0])+"\t"+str(x[1])+"\t"+str(x[2])+"\t"+str(x[3])+"\t"+str(x[4])+"\t"+str(x[5])+"\t"+f'0{x[6]}'+"\n")
                self.my_receipt85.insert('end', "\n" +heading1+"\t"+server+"\n")
            if self.module_chooser.get()=="BANK PAY MODE":
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1="Served By:"
                #first delete the scrolledtext  contents
                self.my_receipt85.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt85.insert('end', "\n" +title + "\n")
                self.my_receipt85.insert('end', "\n" +sub + "\n")
                self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                self.my_receipt85.insert('end', "\n" +f'{self.module_chooser.get()} FARMERS'+"\n")
                self.my_receipt85.insert('end', "\n" +"Name"+"\t"+"\t"+"\t"+"Address"+"\t"+"Farmer_ID"+" National_ID"+" Phone Number"+"\t"+"Bank_Name"+"\t"+"Bank_Account_No"+"\n")
                #query
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM Customers WHERE Payment_Mode=?",("Bank Account",))
                all_farmers=c.fetchall()
                conn.commit()
                conn.close()
                for x in all_farmers:
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM BANK_ACCOUNTS WHERE Customer_ID=?",(x[4],))
                    all_bankers=c.fetchall()
                    conn.commit()
                    conn.close()
                    for v in all_bankers:
                        self.my_receipt85.insert('end', "\n" +str(x[0])+"\t"+str(x[1])+"\t"+str(x[2])+"\t"+str(x[3])+"\t"+str(x[4])+"\t"+str(x[5])+"\t"+f'0{x[6]}'+"\t"+str(v[5])+"\t"+str(v[4])+"\n")
                self.my_receipt85.insert('end', "\n" +heading1+"\t"+server+"\n")
        #toplevel
        self.top85=Toplevel()
        self.top85.iconbitmap("logo1.ico")
        self.top85.state('zoomed')
        self.title_frame=Frame(self.top85)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="RECORDS REPORT"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top85,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.choose_module_label=customtkinter.CTkLabel(self.left_frame,text="Choose Module:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.choose_module_label.grid(row=0,column=0,columnspan=5,padx=10,pady=20)
        self.choose_module_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.module_chooser,values=["ALL","M~PESA PAY MODE","BANK PAY MODE"],width=250,height=25,fg_color="red",text_color="white")
        self.choose_module_menu.grid(row=0, column=5,columnspan=5)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_records_report)
        self.generate_button.grid(row=0,column=10,padx=20,pady=20,columnspan=5,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt85=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
        self.my_receipt85.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt85)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)

    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()    
class Customer_Sales:
    def __init__(self,master)-> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x800")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')            
        #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)

        notifications_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Notifications", menu=notifications_menu)
        notifications_menu.add_command(label="Send Bulk SMS",command=self.notifications)

        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

        #variables
        self.currentDateTime= date.today()
        self.sday=datetime.now().day
        self.mwezi=datetime.now().month
        self.mwaka=datetime.now().year
        self.today=self.currentDateTime.strftime("%A - %B %d, %Y")
        self.time=datetime.now()
        #today=yesterday.strftime("%A - %B %d, %Y")
        self.currentdatetime=self.time.strftime("%Y,%A-%B %d, %H:%M:%S")
        self.now_day=datetime.now().day
        self.yesterday=datetime.now() - timedelta(1)
        self.yesterday1=self.yesterday.strftime("%m/%d/%Y")
        self.today1=self.time.strftime("%m/%d/%Y")
        self.today2=self.time.strftime("%d/%m/%Y")
        self.today_month=self.time.strftime("%B")
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.selection=self.today1
        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="FARMER'S SALES"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=45, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=20, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=25, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #create tree frame
        self.tree_frame=Frame(self.top0)
        self.tree_frame.pack(side=BOTTOM, expand=YES, padx=10)
        #add frame
        self.left_frame=customtkinter.CTkFrame(self.top0, border_color="green", border_width=5, width=450, height=800)
        self.left_frame.pack(pady=5,side=LEFT,fill=BOTH, expand=YES)
        #text labels
        morning_title="MORNING SALES"
        self.morning_title_label=customtkinter.CTkLabel(self.left_frame, text=morning_title, fg_color="orange",text_color="white", text_font=("Consollas 10",-20, "underline","bold"),width=150,height=30)
        self.morning_title_label.grid(row=0, column=0,columnspan=3, pady=5)
        self.day_label=customtkinter.CTkLabel(self.left_frame, text="Today:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.day_label.grid(row=1, column=0, padx=10, pady=3, sticky=W)
        self.today_label=customtkinter.CTkLabel(self.left_frame, text=self.today)
        self.today_label.grid(row=1, column=1, padx=10, pady=3, sticky=W)
        self.customer_id_label=customtkinter.CTkLabel(self.left_frame, text="Enter Farmer's ID:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.customer_id_label.grid(row=2, column=0, padx=8, pady=3, sticky=W)
        self.first_name_label=customtkinter.CTkLabel(self.left_frame, text="First Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.first_name_label.grid(row=3, column=0, padx=10, pady=3, sticky=W)
        self.last_name_label=customtkinter.CTkLabel(self.left_frame, text="Last Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.last_name_label.grid(row=4, column=0, padx=10, pady=3, sticky=W)
        self.morning_label=customtkinter.CTkLabel(self.left_frame, text="Morning-Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.morning_label.grid(row=5, column=0, padx=10, pady=3, sticky=W)
        #entry boxes
        self.customer_id_entry=customtkinter.CTkEntry(self.left_frame,width=120, height=25,border_color="blue", placeholder_text="Farmer ID", placeholder_text_color="blue")
        self.customer_id_entry.grid(row=2, column=1)
        self.first_name_entry=customtkinter.CTkEntry(self.left_frame,width=120, height=25,border_color="blue")
        self.first_name_entry.grid(row=3, column=1)
        self.last_name_entry=customtkinter.CTkEntry(self.left_frame,width=120, height=25,border_color="blue")
        self.last_name_entry.grid(row=4, column=1)
        self.morning_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=120, height=25,border_color="blue",placeholder_text="0.0", placeholder_text_color="blue")
        self.morning_quantity_entry.grid(row=5, column=1)
        
        #retrieve button
        self.retrieve_button=customtkinter.CTkButton(self.left_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=80,height=20,command=self.retrieve)
        self.retrieve_button.grid(row=2, column=2, pady=5,padx=5)
        #submit button
        self.submit_button=customtkinter.CTkButton(self.left_frame, text="SAVE RECORD",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100,height=20,command=self.submit)
        self.submit_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10, ipadx=70)
        #****************************************************************************************************************************************************
        #center frame
        self.center_frame=customtkinter.CTkFrame(self.top0,border_color="purple",border_width=5,width=450,height=800)
        self.center_frame.pack(pady=5,side=LEFT,fill=BOTH, expand=YES)
        #sub-title
        afternoon_title="AFTERNOON SALES"
        self.afternoon_title_label=customtkinter.CTkLabel(self.center_frame, text=afternoon_title, fg_color="orange",text_color="white", text_font=("Consollas 10",-20, "underline","bold"),width=150,height=30)
        self.afternoon_title_label.grid(row=0, column=0,columnspan=3, pady=5)
        #text labels    
        self.day_label1=customtkinter.CTkLabel(self.center_frame, text="Today:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.day_label1.grid(row=1, column=0, padx=10, pady=3, sticky=W)
        self.today_label1=customtkinter.CTkLabel(self.center_frame, text=self.today)
        self.today_label1.grid(row=1, column=1)
        self.customer_id_label1=customtkinter.CTkLabel(self.center_frame, text="Enter Farmer's ID:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.customer_id_label1.grid(row=2, column=0, padx=8, pady=3, sticky=W)
        self.first_name_label1=customtkinter.CTkLabel(self.center_frame, text="First Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.first_name_label1.grid(row=3, column=0, padx=10, pady=3, sticky=W)
        self.last_name_label1=customtkinter.CTkLabel(self.center_frame, text="Last Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.last_name_label1.grid(row=4, column=0, padx=10, pady=3, sticky=W)
        self.afternoon_label=customtkinter.CTkLabel(self.center_frame, text="Afternoon-Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.afternoon_label.grid(row=5, column=0, padx=10, pady=3, sticky=W)
        #entry boxes
        self.customer_id_entry1=customtkinter.CTkEntry(self.center_frame,width=120, height=25,border_color="blue", placeholder_text="Farmer ID", placeholder_text_color="blue")
        self.customer_id_entry1.grid(row=2, column=1)
        self.first_name_entry1=customtkinter.CTkEntry(self.center_frame,width=120, height=25,border_color="blue")
        self.first_name_entry1.grid(row=3, column=1)
        self.last_name_entry1=customtkinter.CTkEntry(self.center_frame,width=120, height=25,border_color="blue")
        self.last_name_entry1.grid(row=4, column=1)
        self.afternoon_quantity_entry=customtkinter.CTkEntry(self.center_frame,width=120, height=25,border_color="blue",placeholder_text="0.0", placeholder_text_color="blue")
        self.afternoon_quantity_entry.grid(row=5, column=1)        
        #retrieve button
        self.retrieve_button1=customtkinter.CTkButton(self.center_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=80,height=20,command=self.retrieve1)
        self.retrieve_button1.grid(row=2, column=2, pady=5,padx=5)
        #submit button
        self.submit_button1=customtkinter.CTkButton(self.center_frame, text="SAVE RECORD",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100,height=20,command=self.submit1)
        self.submit_button1.grid(row=6, column=0, columnspan=4, padx=10, pady=10, ipadx=70)

        #*************************************************************************************************************************************************************
        # #right frame
        self.right_frame=customtkinter.CTkFrame(self.top0,border_color="blue",border_width=5, width=450, height=800)
        self.right_frame.pack(pady=5,side=LEFT,fill=BOTH, expand=YES)
        #sub-title
        evening_title="EVENING SALES"
        self.evening_title_label=customtkinter.CTkLabel(self.right_frame, text=evening_title, fg_color="orange",text_color="white", text_font=("Consollas 10",-20, "underline","bold"),width=150,height=30)
        self.evening_title_label.grid(row=0, column=0,columnspan=3, pady=5)
        #text labels    
        self.day_label2=customtkinter.CTkLabel(self.right_frame, text="Today:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.day_label2.grid(row=1, column=0, padx=10, pady=3, sticky=W)
        self.today_label2=customtkinter.CTkLabel(self.right_frame, text=self.today)
        self.today_label2.grid(row=1, column=1)
        self.customer_id_label2=customtkinter.CTkLabel(self.right_frame, text="Enter Farmer's ID:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.customer_id_label2.grid(row=2, column=0, pady=3, sticky=W,padx=8)
        self.first_name_label2=customtkinter.CTkLabel(self.right_frame, text="First Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.first_name_label2.grid(row=3, column=0, padx=10, pady=3, sticky=W)
        self.last_name_label2=customtkinter.CTkLabel(self.right_frame, text="Last Name:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.last_name_label2.grid(row=4, column=0, padx=10, pady=3, sticky=W)
        self.evening_label=customtkinter.CTkLabel(self.right_frame, text="Evening-Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15, "bold"),width=120, height=25)
        self.evening_label.grid(row=5, column=0, padx=10, pady=3, sticky=W)
        #entry boxes
        self.customer_id_entry2=customtkinter.CTkEntry(self.right_frame,width=120, height=25,border_color="blue", placeholder_text="Farmer ID", placeholder_text_color="blue")
        self.customer_id_entry2.grid(row=2, column=1)
        self.first_name_entry2=customtkinter.CTkEntry(self.right_frame,width=120, height=25,border_color="blue")
        self.first_name_entry2.grid(row=3, column=1)
        self.last_name_entry2=customtkinter.CTkEntry(self.right_frame,width=120, height=25,border_color="blue")
        self.last_name_entry2.grid(row=4, column=1)
        self.evening_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=120, height=25,border_color="blue",placeholder_text="0.0", placeholder_text_color="blue")
        self.evening_quantity_entry.grid(row=5, column=1)
        #retrieve button
        self.retrieve_button2=customtkinter.CTkButton(self.right_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=80,height=20,command=self.retrieve2)
        self.retrieve_button2.grid(row=2, column=2, pady=5,padx=5,sticky=W)
        #submit button
        self.submit_button2=customtkinter.CTkButton(self.right_frame, text="SAVE RECORD",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100,height=20,command=self.submit2)
        self.submit_button2.grid(row=6, column=0, columnspan=4, padx=10, pady=10, ipadx=70)

        #***************************************************************************************************************************************************************
        #treeview
        #label and entry box
        self.customer_id_label3=customtkinter.CTkLabel(self.tree_frame, text="Enter Farmer's ID:",fg_color="brown", text_color="white", text_font=("Consollas 10", -12, "bold"), width=100, height=30)
        self.customer_id_label3.grid(row=0, column=0, padx=10)
        self.customer_id_entry3=customtkinter.CTkEntry(self.tree_frame,border_color="blue",width=120,height=30,placeholder_text="Enter Farmer's ID",placeholder_text_color="blue")
        self.customer_id_entry3.grid(row=0, column=1, padx=10)
        self.my_frame=Frame(self.tree_frame ,highlightbackground="green", highlightthickness=5, width=450, height=800,bd=0)
        self.my_frame.grid(row=1, column=0, columnspan=20, pady=10)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])

        #treeview scrollbar
        self.tree_scroll=Scrollbar(self.my_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree=ttk.Treeview(self.my_frame, yscrollcommand=self.tree_scroll.set, height=8)
        self.my_tree.pack()
        #configure the scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)
        #define our columns
        self.my_tree['columns']=("First Name", "Last Name", "Customer ID", "Morning Quantity","Serverm", "AfterNoon Quantity","Servera", "Evening Quantity","Servere", "Daily Accumulated", "DATE")
        #format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("First Name", anchor="w", width=80)
        self.my_tree.column("Last Name", anchor="w", width=80)
        self.my_tree.column("Customer ID", anchor="w", width=80)
        self.my_tree.column("Morning Quantity", anchor="w", width=120)
        self.my_tree.column("Serverm", anchor="center", width=150)
        self.my_tree.column("AfterNoon Quantity", anchor="w", width=120)
        self.my_tree.column("Servera", anchor="center", width=150)
        self.my_tree.column("Evening Quantity", anchor="w", width=120)
        self.my_tree.column("Servere", anchor="center", width=150)
        self.my_tree.column("Daily Accumulated", anchor="w", width=120)
        self.my_tree.column("DATE", anchor="w", width=150)
        #create headings
        self.my_tree.heading("#0", text="", anchor="w")
        self.my_tree.heading("First Name", text="First Name", anchor='w')
        self.my_tree.heading("Last Name", text="Last Name", anchor='w')
        self.my_tree.heading("Customer ID", text="Farmer ID", anchor='w')
        self.my_tree.heading("Morning Quantity", text="Morning Quantity", anchor='w')
        self.my_tree.heading("Serverm",text="Server", anchor="center")
        self.my_tree.heading("AfterNoon Quantity", text="AfterNoon Quantity", anchor='w')
        self.my_tree.heading("Servera",text="Server", anchor="center")
        self.my_tree.heading("Evening Quantity", text="Evening Quantity", anchor='w')
        self.my_tree.heading("Servere",text="Server", anchor="center")
        self.my_tree.heading("Daily Accumulated", text="Daily Accumulated", anchor='w')
        self.my_tree.heading("DATE", text="Date", anchor='w')
        #striped row tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="violet")
        #buttons
        self.get_data_button=customtkinter.CTkButton(self.tree_frame, text="PRINT",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150, height=30,command=self.get_data)
        self.get_data_button.grid(row=0, column=2, padx=10)
        self.send_sms_button=customtkinter.CTkButton(self.tree_frame, text="SEND SMS",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150, height=30,command=self.get_data1)
        self.send_sms_button.grid(row=0, column=3, padx=10)
        self.my_button=customtkinter.CTkButton(self.tree_frame, text="Choose Date",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150, height=30, command=self.grab_date)
        self.my_button.grid(row=0, column=4, padx=10)
        '''
        #drop tables
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("DROP TABLE DAILY_TOTALS")
        c.execute("DROP TABLE Morning_Sales")
        c.execute("DROP TABLE Afternoon_Sales")
        c.execute("DROP TABLE Evening_Sales")
        conn.commit()
        conn.close()
        print("tables dropped")
        '''
        #connect to our database
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        #create  daily totals table
        c.execute("""CREATE TABLE IF NOT EXISTS DAILY_TOTALS(
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL,
                Surname TEXT NOT NULL,
                Customer_ID INT,
                Morning_Quantity REAL,
                Morning_Server TEXT,
                AfterNoon_Quantity REAL,
                Afternoon_Server TEXT,
                Evening_Quantity REAL,
                Evening_Server TEXT,
                Daily_Accumulated REAL,
                DATE TEXT NOT NULL,
                MONTH INT NOT NULL,
                YEAR INT NOT NULL,
                DAY INT NOT NULL
                )""")
        conn.commit()
        conn.close()
        #create morning sales table
        #connect to the database
        conn= sqlite3.connect('samaria database.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        c= conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Morning_Sales(
                    Customer_ID INT  NOT NULL,
                    MORNING_QUANTITY REAL NOT NULL,
                    Server TEXT,
                    TIME INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        conn.commit()
        conn.close()
        #create afternoon sales table
        #connect to the database
        conn= sqlite3.connect('samaria database.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        c= conn.cursor()
        #create table
        c.execute("""CREATE TABLE IF NOT EXISTS Afternoon_Sales(
                    Customer_ID INT  NOT NULL,
                    AFTERNOON_QUANTITY REAL NOT NULL,
                    Server TEXT,
                    TIME INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        conn.commit()
        conn.close()
        #create evening sales table
        #connect to the database
        conn= sqlite3.connect('samaria database.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        c= conn.cursor()
        #create table
        c.execute("""CREATE TABLE IF NOT EXISTS Evening_Sales(
                    Customer_ID INT  NOT NULL,
                    EVENING_QUANTITY REAL NOT NULL,
                    Server TEXT,
                    TIME INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        conn.commit()
        conn.close()
        self.show_records()

    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    #retrieve function
    def retrieve(self):
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR","Please Enter Farmer's ID",parent =self.top0)
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT First_name, Last_name,Surname FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
            name=c.fetchall()
            conn.commit()
            conn.close()
            if name==[]:
                messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
            else:
                first_name=''
                last_name=''
                s_name=''
                for record in name:
                    first_name +=(record[0])
                for record in name:
                    last_name +=(record[1])
                for record in name:
                    s_name +=(record[2])
                self.first_name_entry.delete(0, END)
                self.last_name_entry.delete(0, END)
                self.first_name_entry.insert(0, first_name)
                self.last_name_entry.insert(0, last_name)
    #insert data into the records
    def submit(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT First_name, Last_name,Surname FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
        name=c.fetchall()
        conn.commit()
        conn.close()
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
        elif self.morning_quantity_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Morning Quantity",parent=self.top0)
        elif name==[]:
            messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute(" INSERT INTO Morning_Sales VALUES (:Customer_ID,:MORNING_QUANTITY,:Server,:TIME,:DATE)",
                    {
                        'Customer_ID':self.customer_id_entry.get(),
                        'MORNING_QUANTITY':self.morning_quantity_entry.get(),
                        'Server':server,
                        'TIME':self.Time,
                        'DATE':self.today1
                        })
                  
            conn.commit()
            conn.close()
            #daily totals
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            #retreive names
            c.execute("SELECT First_name, Last_name,Surname, Customer_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
            records3=c.fetchall()
            self.first_name3=''
            self.last_name3=''
            self.surname3=''
            self.customer_id3=''
            for record in records3:
                self.first_name3 =(record[0])
            for record in records3:
                self.last_name3 =(record[1])
            for record in records3:
                self.surname3 =(record[2])
            for record in records3:
                self.customer_id3 =(record[3])
            #server  
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Server FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records0=c.fetchone()
            if records0==None:
                self.morn_server=""
            else:
                self.morn_server=records0
            c.execute("SELECT Server FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records1=c.fetchone()
            if records1==None:
                self.after_server=""
            else:
                self.after_server=records1
            c.execute("SELECT Server FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records2=c.fetchone()
            if records2==None:
                self.even_server=""
            else:
                self.even_server=records2
            conn.commit()
            conn.close()
            #sales
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT MORNING_QUANTITY FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records4=c.fetchall()
            self.morning=sum(records4)
            c.execute("SELECT AFTERNOON_QUANTITY FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records5=c.fetchall()
            self.afternoon=sum(records5)
            c.execute("SELECT EVENING_QUANTITY FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry.get()))
            records6=c.fetchall()
            self.evening=sum(records6)
            self.added=(self.morning+self.afternoon+self.evening)
            conn.commit()
            conn.close()
            #update data
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("""UPDATE DAILY_TOTALS SET
                        First_Name=:f_name,
                        Last_Name=:l_name,
                        Surname=:s_name,
                        Customer_ID=:c_id,
                        Morning_Quantity=:mornq,
                        Morning_Server=:morn_s,
                        AfterNoon_Quantity=:afterq,
                        Afternoon_Server=:after_s,
                        Evening_Quantity=:evenq,
                        Evening_Server=:even_s,
                        Daily_Accumulated=:dailyq,
                        DATE=:date,
                        MONTH=:month,
                        YEAR=:year,
                        DAY=:siku

                        WHERE CUSTOMER_ID=:c_id AND DATE=:date""",
                      {
                        'f_name':self.first_name3,
                        'l_name':self.last_name3,
                        's_name':self.surname3,
                        'c_id':self.customer_id3,
                        'mornq':self.morning,
                        'morn_s':self.morn_server,
                        'afterq': self.afternoon,
                        'after_s':self.after_server,
                        'evenq':self.evening,
                        'even_s': self.even_server,
                        'dailyq':self.added,
                        'date':self.today1,
                        'month':self.mwezi,
                        'year':self.mwaka,
                        'siku':self.sday
                        })
            #insert data into our table
            c.execute("INSERT OR IGNORE INTO DAILY_TOTALS VALUES (:First_Name, :Last_Name, :Surname, :Customer_ID, :Morning_Quantity,:Morning_Server, :AfterNoon_Quantity, :Afternoon_Server, :Evening_Quantity, :Evening_Server,:Daily_Accumulated, :DATE,:MONTH, :YEAR,:DAY)", 
                    {
                        'First_Name' :self.first_name3,
                        'Last_Name' : self.last_name3,
                        'Surname' : self.surname3,
                        'Customer_ID' :self.customer_id3,
                        'Morning_Quantity' :self.morning,
                        'Morning_Server':self.morn_server,
                        'AfterNoon_Quantity' :self.afternoon,
                        'Afternoon_Server': self.after_server,
                        'Evening_Quantity' :self.evening,
                        'Evening_Server': self.even_server,
                        'Daily_Accumulated': self.added,
                        'DATE': self.today1,
                        'MONTH':self.mwezi,
                        'YEAR':self.mwaka,
                        'DAY':self.sday
                        })
                                        
            c.execute("DELETE FROM DAILY_TOTALS WHERE rowid NOT IN (SELECT MIN(rowid) FROM DAILY_TOTALS GROUP BY First_Name,Last_Name,Surname,Customer_ID,Morning_Quantity,Morning_Server,AfterNoon_Quantity,Afternoon_Server,Evening_Quantity,Evening_Server,Daily_Accumulated, DATE, MONTH, YEAR,DAY)")
                     
            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka, self.customer_id_entry.get(),))
            records7=c.fetchall()
            for record in records7:
                self.monthly=record[0]
            conn.commit()
            conn.close()
            #clear the text boxes
            self.customer_id_entry.delete(0, END)
            self.morning_quantity_entry.delete(0, END)
            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.show_records()
          #retrieve function
    def retrieve1(self):
              if self.customer_id_entry1.get()=="":
                  messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
              else:
                  conn=sqlite3.connect('samaria database.db')
                  c=conn.cursor()
                  c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry1.get())
                  name1=c.fetchall()
                  conn.commit()
                  conn.close()
                  if name1==[]:
                       messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
                  else:
                      first_name1=''
                      last_name1=''
                      for record1 in name1:
                          first_name1 +=(record1[0])
                      for record1 in name1:
                          last_name1 +=(record1[1])
                      self.first_name_entry1.delete(0, END)
                      self.last_name_entry1.delete(0, END)
                      self.first_name_entry1.insert(0, first_name1)
                      self.last_name_entry1.insert(0, last_name1)   
    #insert data into the records
    def submit1(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry1.get())
        name1=c.fetchall()
        conn.commit()
        conn.close()
        if self.customer_id_entry1.get()=="":
            messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent=self.top0)
        elif self.afternoon_quantity_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Afternoon Quantity",parent=self.top0)
        elif name1==[]:
            messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute(" INSERT INTO Afternoon_Sales VALUES (:Customer_ID,:AFTERNOON_QUANTITY,:Server,:TIME,:DATE)",
                        {         
                            'Customer_ID':self.customer_id_entry1.get(),
                            'AFTERNOON_QUANTITY':self.afternoon_quantity_entry.get(),
                            'Server': server,
                            'TIME':self.Time,
                            'DATE':self.today1
                        })
            conn.commit()
            conn.close()
            #daily totals
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            #retreive names
            c.execute("SELECT First_name, Last_name,Surname, Customer_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry1.get())
            records3=c.fetchall()
            self.first_name3=''
            self.last_name3=''
            self.surname3=''
            self.customer_id3=''
            for record in records3:
                self.first_name3 =(record[0])
            for record in records3:
                self.last_name3 =(record[1])
            for record in records3:
                self.surname3 =(record[2])
            for record in records3:
                self.customer_id3 =(record[3])
            #server  
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Server FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records0=c.fetchone()
            if records0==None:
                self.morn_server=""
            else:
                self.morn_server=records0
            c.execute("SELECT Server FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records1=c.fetchone()
            if records1==None:
                self.after_server=""
            else:
                self.after_server=records1
            c.execute("SELECT Server FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records2=c.fetchone()
            if records2==None:
                self.even_server=""
            else:
                self.even_server=records2
            conn.commit()
            conn.close()
            #sales
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT MORNING_QUANTITY FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records4=c.fetchall()
            self.morning=sum(records4)
            c.execute("SELECT AFTERNOON_QUANTITY FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records5=c.fetchall()
            self.afternoon=sum(records5)
            c.execute("SELECT EVENING_QUANTITY FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry1.get()))
            records6=c.fetchall()
            self.evening=sum(records6)
            self.added=(self.morning+self.afternoon+self.evening)
            conn.commit()
            conn.close()
            #update data
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("""UPDATE DAILY_TOTALS SET
                        First_Name=:f_name,
                        Last_Name=:l_name,
                        Surname=:s_name,
                        Customer_ID=:c_id,
                        Morning_Quantity=:mornq,
                        Morning_Server=:morn_s,
                        AfterNoon_Quantity=:afterq,
                        Afternoon_Server=:after_s,
                        Evening_Quantity=:evenq,
                        Evening_Server=:even_s,
                        Daily_Accumulated=:dailyq,
                        DATE=:date,
                        MONTH=:month,
                        YEAR=:year,
                        DAY=:siku

                        WHERE CUSTOMER_ID=:c_id AND DATE=:date""",
                      {
                        'f_name':self.first_name3,
                        'l_name':self.last_name3,
                        's_name':self.surname3,
                        'c_id':self.customer_id3,
                        'mornq':self.morning,
                        'morn_s':self.morn_server,
                        'afterq': self.afternoon,
                        'after_s':self.after_server,
                        'evenq':self.evening,
                        'even_s': self.even_server,
                        'dailyq':self.added,
                        'date':self.today1,
                        'month':self.mwezi,
                        'year':self.mwaka,
                        'siku':self.sday
                        })
            #insert data into our table
            c.execute("INSERT OR IGNORE INTO DAILY_TOTALS VALUES (:First_Name, :Last_Name, :Surname, :Customer_ID, :Morning_Quantity,:Morning_Server, :AfterNoon_Quantity, :Afternoon_Server, :Evening_Quantity, :Evening_Server,:Daily_Accumulated, :DATE,:MONTH, :YEAR,:DAY)", 
                    {
                        'First_Name' :self.first_name3,
                        'Last_Name' : self.last_name3,
                        'Surname' : self.surname3,
                        'Customer_ID' :self.customer_id3,
                        'Morning_Quantity' :self.morning,
                        'Morning_Server':self.morn_server,
                        'AfterNoon_Quantity' :self.afternoon,
                        'Afternoon_Server': self.after_server,
                        'Evening_Quantity' :self.evening,
                        'Evening_Server': self.even_server,
                        'Daily_Accumulated': self.added,
                        'DATE': self.today1,
                        'MONTH':self.mwezi,
                        'YEAR':self.mwaka,
                        'DAY':self.sday
                        })
                                        
            c.execute("DELETE FROM DAILY_TOTALS WHERE rowid NOT IN (SELECT MIN(rowid) FROM DAILY_TOTALS GROUP BY First_Name,Last_Name,Surname,Customer_ID,Morning_Quantity,Morning_Server,AfterNoon_Quantity,Afternoon_Server,Evening_Quantity,Evening_Server,Daily_Accumulated, DATE, MONTH, YEAR,DAY)")
                     
            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka, self.customer_id_entry1.get(),))
            records7=c.fetchall()
            for record in records7:
                self.monthly=record[0]
            conn.commit()
            conn.close()
            #clear the text boxes
            self.customer_id_entry1.delete(0, END)
            self.afternoon_quantity_entry.delete(0, END)
            self.first_name_entry1.delete(0, END)
            self.last_name_entry1.delete(0, END)
            self.show_records()       
    #retrieve function
    def retrieve2(self):
              if self.customer_id_entry2.get()=="":
                  messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
              else:
                  conn=sqlite3.connect('samaria database.db')
                  c=conn.cursor()
                  c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry2.get())
                  name2=c.fetchall()
                  conn.commit()
                  conn.close()
                  if name2==[]:
                       messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
                  else:
                      first_name2=''
                      last_name2=''
                      for record in name2:
                          first_name2 +=(record[0])
                      for record in name2:
                          last_name2 +=(record[1])
                      self.first_name_entry2.delete(0, END)
                      self.last_name_entry2.delete(0, END)
                      self.first_name_entry2.insert(0, first_name2)
                      self.last_name_entry2.insert(0, last_name2)
    #insert data into the records
    def submit2(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry2.get())
        name2=c.fetchall()
        conn.commit()
        conn.close()
        if self.customer_id_entry2.get()=="":
            messagebox.showerror("ERROR", "Please Enter Customer's ID",parent=self.top0)
        elif self.evening_quantity_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Evening Quantity",parent=self.top0)
        elif name2==[]:
            messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()    
            c.execute(" INSERT INTO Evening_Sales VALUES (:Customer_ID,:EVENING_QUANTITY,:Server,:TIME,:DATE)",
                      {
                        'Customer_ID':self.customer_id_entry2.get(),
                        'EVENING_QUANTITY':self.evening_quantity_entry.get(),
                        'Server': server,
                        'TIME':self.Time,
                        'DATE':self.today1
                        })
            conn.commit()
            conn.close()
            #daily totals
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            #retreive names
            c.execute("SELECT First_name, Last_name,Surname, Customer_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry2.get())
            records3=c.fetchall()
            self.first_name3=''
            self.last_name3=''
            self.surname3=''
            self.customer_id3=''
            for record in records3:
                self.first_name3 =(record[0])
            for record in records3:
                self.last_name3 =(record[1])
            for record in records3:
                self.surname3 =(record[2])
            for record in records3:
                self.customer_id3 =(record[3])
            #server  
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Server FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records0=c.fetchone()
            if records0==None:
                self.morn_server=""
            else:
                self.morn_server=records0
            c.execute("SELECT Server FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records1=c.fetchone()
            if records1==None:
                self.after_server=""
            else:
                self.after_server=records1
            c.execute("SELECT Server FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records2=c.fetchone()
            if records2==None:
                self.even_server=""
            else:
                self.even_server=records2
            conn.commit()
            conn.close()
            #sales
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT MORNING_QUANTITY FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records4=c.fetchall()
            self.morning=sum(records4)
            c.execute("SELECT AFTERNOON_QUANTITY FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records5=c.fetchall()
            self.afternoon=sum(records5)
            c.execute("SELECT EVENING_QUANTITY FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry2.get()))
            records6=c.fetchall()
            self.evening=sum(records6)
            self.added=(self.morning+self.afternoon+self.evening)
            conn.commit()
            conn.close()
            #update data
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("""UPDATE DAILY_TOTALS SET
                        First_Name=:f_name,
                        Last_Name=:l_name,
                        Surname=:s_name,
                        Customer_ID=:c_id,
                        Morning_Quantity=:mornq,
                        Morning_Server=:morn_s,
                        AfterNoon_Quantity=:afterq,
                        Afternoon_Server=:after_s,
                        Evening_Quantity=:evenq,
                        Evening_Server=:even_s,
                        Daily_Accumulated=:dailyq,
                        DATE=:date,
                        MONTH=:month,
                        YEAR=:year,
                        DAY=:siku

                        WHERE CUSTOMER_ID=:c_id AND DATE=:date""",
                      {
                        'f_name':self.first_name3,
                        'l_name':self.last_name3,
                        's_name':self.surname3,
                        'c_id':self.customer_id3,
                        'mornq':self.morning,
                        'morn_s':self.morn_server,
                        'afterq': self.afternoon,
                        'after_s':self.after_server,
                        'evenq':self.evening,
                        'even_s': self.even_server,
                        'dailyq':self.added,
                        'date':self.today1,
                        'month':self.mwezi,
                        'year':self.mwaka,
                        'siku':self.sday
                        })
            #insert data into our table
            c.execute("INSERT OR IGNORE INTO DAILY_TOTALS VALUES (:First_Name, :Last_Name, :Surname, :Customer_ID, :Morning_Quantity,:Morning_Server, :AfterNoon_Quantity, :Afternoon_Server, :Evening_Quantity, :Evening_Server,:Daily_Accumulated, :DATE,:MONTH, :YEAR,:DAY)", 
                    {
                        'First_Name' :self.first_name3,
                        'Last_Name' : self.last_name3,
                        'Surname' : self.surname3,
                        'Customer_ID' :self.customer_id3,
                        'Morning_Quantity' :self.morning,
                        'Morning_Server':self.morn_server,
                        'AfterNoon_Quantity' :self.afternoon,
                        'Afternoon_Server': self.after_server,
                        'Evening_Quantity' :self.evening,
                        'Evening_Server': self.even_server,
                        'Daily_Accumulated': self.added,
                        'DATE': self.today1,
                        'MONTH':self.mwezi,
                        'YEAR':self.mwaka,
                        'DAY':self.sday
                        })
                                        
            c.execute("DELETE FROM DAILY_TOTALS WHERE rowid NOT IN (SELECT MIN(rowid) FROM DAILY_TOTALS GROUP BY First_Name,Last_Name,Surname,Customer_ID,Morning_Quantity,Morning_Server,AfterNoon_Quantity,Afternoon_Server,Evening_Quantity,Evening_Server,Daily_Accumulated, DATE, MONTH, YEAR,DAY)")
                     
            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka, self.customer_id_entry2.get(),))
            records7=c.fetchall()
            for record in records7:
                self.monthly=record[0]
            conn.commit()
            conn.close()
            #clear the text boxes
            self.customer_id_entry2.delete(0, END)
            self.evening_quantity_entry.delete(0, END)
            self.first_name_entry2.delete(0, END)
            self.last_name_entry2.delete(0, END)
            self.show_records()
    #retreive data
    def get_data(self):
              if self.customer_id_entry3.get()=="":
                  messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
              else:
                  conn=sqlite3.connect('samaria database.db')
                  c=conn.cursor()
                  #retreive names
                  c.execute("SELECT First_name, Last_name,Surname, Customer_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry3.get())
                  records3=c.fetchall()
                  if records3==[]:
                       messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
                  else:
                      self.first_name3=''
                      self.last_name3=''
                      self.surname3=''
                      self.customer_id3=''
                      for record in records3:
                          self.first_name3 =(record[0])
                      for record in records3:
                          self.last_name3 =(record[1])
                      for record in records3:
                          self.surname3 =(record[2])
                      for record in records3:
                          self.customer_id3 =(record[3])
                      #server  
                      conn=sqlite3.connect('samaria database.db')
                      conn.row_factory=lambda cursor, row:row[0]
                      c=conn.cursor()
                      c.execute("SELECT Server FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records0=c.fetchone()
                      if records0==None:
                          self.morn_server=""
                      else:
                          self.morn_server=records0
                      c.execute("SELECT Server FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records1=c.fetchone()
                      if records1==None:
                          self.after_server=""
                      else:
                          self.after_server=records1
                      c.execute("SELECT Server FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records2=c.fetchone()
                      if records2==None:
                          self.even_server=""
                      else:
                          self.even_server=records2
                      conn.commit()
                      conn.close()
                      #sales
                      conn=sqlite3.connect('samaria database.db')
                      conn.row_factory=lambda cursor, row:row[0]
                      c=conn.cursor()
                      c.execute("SELECT MORNING_QUANTITY FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records4=c.fetchall()
                      self.morning=sum(records4)
                      c.execute("SELECT AFTERNOON_QUANTITY FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records5=c.fetchall()
                      self.afternoon=sum(records5)
                      c.execute("SELECT EVENING_QUANTITY FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records6=c.fetchall()
                      self.evening=sum(records6)
                      self.added=(self.morning+self.afternoon+self.evening)
                      conn.commit()
                      conn.close()
                      #update data
                      conn=sqlite3.connect('samaria database.db')
                      c=conn.cursor()
                      c.execute("""UPDATE DAILY_TOTALS SET
                                  First_Name=:f_name,
                                  Last_Name=:l_name,
                                  Surname=:s_name,
                                  Customer_ID=:c_id,
                                  Morning_Quantity=:mornq,
                                  Morning_Server=:morn_s,
                                  AfterNoon_Quantity=:afterq,
                                  Afternoon_Server=:after_s,
                                  Evening_Quantity=:evenq,
                                  Evening_Server=:even_s,
                                  Daily_Accumulated=:dailyq,
                                  DATE=:date,
                                  MONTH=:month,
                                  YEAR=:year,
                                  DAY=:siku

                                  WHERE CUSTOMER_ID=:c_id AND DATE=:date""",
                                {
                                    'f_name':self.first_name3,
                                    'l_name':self.last_name3,
                                    's_name':self.surname3,
                                    'c_id':self.customer_id3,
                                    'mornq':self.morning,
                                    'morn_s':self.morn_server,
                                    'afterq': self.afternoon,
                                    'after_s':self.after_server,
                                    'evenq':self.evening,
                                    'even_s': self.even_server,
                                    'dailyq':self.added,
                                    'date':self.today1,
                                    'month':self.mwezi,
                                    'year':self.mwaka,
                                    'siku':self.sday
                                    })
                      #insert data into our table
                      c.execute("INSERT OR IGNORE INTO DAILY_TOTALS VALUES (:First_Name, :Last_Name, :Surname, :Customer_ID, :Morning_Quantity,:Morning_Server, :AfterNoon_Quantity, :Afternoon_Server, :Evening_Quantity, :Evening_Server,:Daily_Accumulated, :DATE,:MONTH, :YEAR,:DAY)", 
                                {
                                    'First_Name' :self.first_name3,
                                    'Last_Name' : self.last_name3,
                                    'Surname' : self.surname3,
                                    'Customer_ID' :self.customer_id3,
                                    'Morning_Quantity' :self.morning,
                                    'Morning_Server':self.morn_server,
                                    'AfterNoon_Quantity' :self.afternoon,
                                    'Afternoon_Server': self.after_server,
                                    'Evening_Quantity' :self.evening,
                                    'Evening_Server': self.even_server,
                                    'Daily_Accumulated': self.added,
                                    'DATE': self.today1,
                                    'MONTH':self.mwezi,
                                    'YEAR':self.mwaka,
                                    'DAY':self.sday
                                    })
                  
                      
                      c.execute("DELETE FROM DAILY_TOTALS WHERE rowid NOT IN (SELECT MIN(rowid) FROM DAILY_TOTALS GROUP BY First_Name,Last_Name,Surname,Customer_ID,Morning_Quantity,Morning_Server,AfterNoon_Quantity,Afternoon_Server,Evening_Quantity,Evening_Server,Daily_Accumulated, DATE, MONTH, YEAR,DAY)")
                     
                      c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka, self.customer_id_entry3.get(),))
                      records7=c.fetchall()
                      for record in records7:
                        self.monthly=record[0]
                      conn.commit()
                      conn.close()
                      self.receipt()
    
    #print function
    def print_receipt(self):
        printText=self.my_receipt.get("1.0", 'end')
        v=str(len(self.my_receipt.get("1.0", 'end')))
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        #print out as hardcopy
        win32api.ShellExecute(0,
                            "printto",
                            filename,
                            '"%s"' % win32print.GetDefaultPrinter(),
                            ".",
                            0
                            )
        self.my_receipt.delete('1.0', 'end')
        self.top.destroy()
    def receipt(self):                      
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold", "underline"),width=150, height=40)
        self.receipt_label.grid(row=0, column=0, columnspan=10,pady=10)
        self.my_receipt=ScrolledText(my_frame, font="Consollas 10", border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1,sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading1="SALES"
        heading2="NAME:"
        heading3="Farmer ID:"
        heading4="Morning Sales:"
        heading5="AfterNoon Sales:"
        heading6="Evening Sales:"
        heading7="Daily Total Quantity:"
        heading8="Monthly Total Quantity:"
        heading9="Served By:"
        #first delete the scrolledtext  contents
        self.my_receipt.delete('1.0', 'end')
        #add stuff into our scrolled text
        self.my_receipt.insert('end', "\n" +title + "\n")
        self.my_receipt.insert('end', "\n" +sub + "\n")
        self.my_receipt.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
        self.my_receipt.insert('end', "\n" +heading1 + "\n")
        self.my_receipt.insert('end', "\n" +heading2 +"\t" + self.first_name3 +"\t" +self.last_name3 +"\t"+self.surname3+"\n")
        self.my_receipt.insert('end', "\n" +heading3 +"\t" + str(self.customer_id3) + "\n")
        if self.morning!=0:
            self.my_receipt.insert('end', "\n" +heading4 + "\t" + f'{self.morning} Litres ' + "\n")
        if self.afternoon!=0:
            self.my_receipt.insert('end', "\n" +heading5 + "\t" + f'{self.afternoon} Litres' + "\n")
        if self.evening!=0:
            self.my_receipt.insert('end', "\n" +heading6 + "\t" + f'{self.evening} Litres' + "\n")
        self.my_receipt.insert('end', "\n" +heading7 + "\t" + f'{self.added} Litres' + "\n")
        self.my_receipt.insert('end', "\n" +heading8 + "\t" + f'{self.monthly} Litres' +"\n")
        self.my_receipt.insert('end', "\n" +heading9 + "\t" + f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame,text="PRINT",fg_color="purple", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150, height=40,command=self.print_receipt)
        self.print_button.grid(row=2, column=0, columnspan=5,pady=10)
        
        #delete entry
        self.customer_id_entry3.delete(0, END)
        self.show_records()
    #retreive data
    def get_data1(self):
              if self.customer_id_entry3.get()=="":
                  messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
              else:
                  conn=sqlite3.connect('samaria database.db')
                  c=conn.cursor()
                  #retreive names
                  c.execute("SELECT First_name, Last_name,Surname, Customer_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry3.get())
                  records3=c.fetchall()
                  if records3==[]:
                       messagebox.showerror("ERROR","Farmer ID Does not Exist,Check And TRY Again",parent=self.top0)
                  else:
                      self.first_name3=''
                      self.last_name3=''
                      self.surname3=''
                      self.customer_id3=''
                      for record in records3:
                          self.first_name3 =(record[0])
                      for record in records3:
                          self.last_name3 =(record[1])
                      for record in records3:
                          self.surname3 =(record[2])
                      for record in records3:
                          self.customer_id3 =(record[3])
                      #server  
                      conn=sqlite3.connect('samaria database.db')
                      conn.row_factory=lambda cursor, row:row[0]
                      c=conn.cursor()
                      c.execute("SELECT Server FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records0=c.fetchone()
                      if records0==None:
                          self.morn_server=""
                      else:
                          self.morn_server=records0
                      c.execute("SELECT Server FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records1=c.fetchone()
                      if records1==None:
                          self.after_server=""
                      else:
                          self.after_server=records1
                      c.execute("SELECT Server FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records2=c.fetchone()
                      if records2==None:
                          self.even_server=""
                      else:
                          self.even_server=records2
                      conn.commit()
                      conn.close()
                      #sales
                      conn=sqlite3.connect('samaria database.db')
                      conn.row_factory=lambda cursor, row:row[0]
                      c=conn.cursor()
                      c.execute("SELECT MORNING_QUANTITY FROM Morning_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records4=c.fetchall()
                      self.morning=sum(records4)
                      c.execute("SELECT AFTERNOON_QUANTITY FROM Afternoon_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records5=c.fetchall()
                      self.afternoon=sum(records5)
                      c.execute("SELECT EVENING_QUANTITY FROM Evening_Sales WHERE DATE=? AND Customer_ID=?",(str(self.today1),self.customer_id_entry3.get()))
                      records6=c.fetchall()
                      self.evening=sum(records6)
                      self.added=(self.morning+self.afternoon+self.evening)
                      conn.commit()
                      conn.close()
                      #update data
                      conn=sqlite3.connect('samaria database.db')
                      c=conn.cursor()
                      c.execute("""UPDATE DAILY_TOTALS SET
                                  First_Name=:f_name,
                                  Last_Name=:l_name,
                                  Surname=:s_name,
                                  Customer_ID=:c_id,
                                  Morning_Quantity=:mornq,
                                  Morning_Server=:morn_s,
                                  AfterNoon_Quantity=:afterq,
                                  Afternoon_Server=:after_s,
                                  Evening_Quantity=:evenq,
                                  Evening_Server=:even_s,
                                  Daily_Accumulated=:dailyq,
                                  DATE=:date,
                                  MONTH=:month,
                                  YEAR=:year,
                                  DAY=:siku

                                  WHERE CUSTOMER_ID=:c_id AND DATE=:date""",
                                {
                                    'f_name':self.first_name3,
                                    'l_name':self.last_name3,
                                    's_name':self.surname3,
                                    'c_id':self.customer_id3,
                                    'mornq':self.morning,
                                    'morn_s':self.morn_server,
                                    'afterq': self.afternoon,
                                    'after_s':self.after_server,
                                    'evenq':self.evening,
                                    'even_s': self.even_server,
                                    'dailyq':self.added,
                                    'date':self.today1,
                                    'month':self.mwezi,
                                    'year':self.mwaka,
                                    'siku':self.sday
                                    })
                      #insert data into our table
                      c.execute("INSERT OR IGNORE INTO DAILY_TOTALS VALUES (:First_Name, :Last_Name, :Surname, :Customer_ID, :Morning_Quantity,:Morning_Server, :AfterNoon_Quantity, :Afternoon_Server, :Evening_Quantity, :Evening_Server,:Daily_Accumulated, :DATE,:MONTH, :YEAR,:DAY)", 
                                {
                                    'First_Name' :self.first_name3,
                                    'Last_Name' : self.last_name3,
                                    'Surname' : self.surname3,
                                    'Customer_ID' :self.customer_id3,
                                    'Morning_Quantity' :self.morning,
                                    'Morning_Server':self.morn_server,
                                    'AfterNoon_Quantity' :self.afternoon,
                                    'Afternoon_Server': self.after_server,
                                    'Evening_Quantity' :self.evening,
                                    'Evening_Server': self.even_server,
                                    'Daily_Accumulated': self.added,
                                    'DATE': self.today1,
                                    'MONTH':self.mwezi,
                                    'YEAR':self.mwaka,
                                    'DAY':self.sday
                                    })                  
                      
                      c.execute("DELETE FROM DAILY_TOTALS WHERE rowid NOT IN (SELECT MIN(rowid) FROM DAILY_TOTALS GROUP BY First_Name,Last_Name,Surname,Customer_ID,Morning_Quantity,Morning_Server,AfterNoon_Quantity,Afternoon_Server,Evening_Quantity,Evening_Server,Daily_Accumulated, DATE, MONTH, YEAR,DAY)")
                     
                      c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka, self.customer_id_entry3.get(),))
                      records7=c.fetchall()
                      for record in records7:
                        self.monthly=record[0]
                      conn.commit()
                      conn.close()
                      self.receipt1()
    def send_message(self):
        #connect to database to retreive phone number
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Phone_number FROM Customers WHERE Customer_ID=?",(self.customer_id_entry3.get(),))
        namba=c.fetchone()
        conn.commit()
        conn.close()
        try:
            #requests mobitechtechnologies
            url = "https://api.mobitechtechnologies.com/sms/sendsms"

            payload = json.dumps({
                "mobile": f'+254{namba}',
                "response_type": "json",
                "sender_name": 23107,
                "service_id": 0,
                "message": self.my_receipt1.get("1.0", 'end')
            })
            headers = {
                'h_api_key': 'ead62d3ed9c918bb366cba5ec6692224d8926bd8b0c339c0a58cc137075b3e4a',
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            x=response.text[20]
            if x != '0':
                #delete text afterwards
                self.customer_id_entry3.delete(0,END)
                self.my_receipt1.delete('1.0', 'end')
                self.top.destroy()
                messagebox.showerror("ERROR","SMS Not Sent,Please Recharge your Account And Try Again",parent=self.top0)
            else:
                #delete text afterwards
                self.customer_id_entry3.delete(0,END)
                self.my_receipt1.delete('1.0', 'end')
                self.top.destroy()
                messagebox.showinfo("BRAVO","SMS Sent Succesfully",parent=self.top0)
        
        except:
            self.customer_id_entry3.delete(0,END)
            self.my_receipt1.delete('1.0', 'end')
            self.top.destroy()
            messagebox.showerror("ERROR","SMS Not Sent,Please Check Your Internet Connectivity And Try Again",parent=self.top0)
    def receipt1(self):                      
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold", "underline"),width=150, height=40)
        self.receipt_label.grid(row=0, column=0, columnspan=10,pady=10)
        self.my_receipt1=ScrolledText(my_frame, font="Consollas 10", border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt1.grid(row=1,sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading1="SALES"
        heading2="NAME:"
        heading3="Farmer_ID:"
        heading4="Morning_Sales:"
        heading5="AfterNoon_Sales:"
        heading6="Evening_Sales:"
        heading7="Daily_Total:"
        heading8="Monthly_Total:"
        heading9="Served By:"
        #first delete the scrolledtext  contents
        self.my_receipt1.delete('1.0', 'end')
        #add stuff into our scrolled text
        self.my_receipt1.insert('end', "\n" +title + "\n")
        self.my_receipt1.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
        self.my_receipt1.insert('end', "\n" +heading2 +"\t" +self.first_name3+"\t" +self.last_name3+"\n")
        self.my_receipt1.insert('end', "\n" +heading3 +"\t" +str(self.customer_id3) + "\n")
        if self.morning!=0:
            self.my_receipt1.insert('end', "\n" +heading4 + "\t" + f'{self.morning} Litres ' + "\n")
        if self.afternoon!=0:
            self.my_receipt1.insert('end', "\n" +heading5 + "\t" + f'{self.afternoon} Litres' + "\n")
        if self.evening!=0:
            self.my_receipt1.insert('end', "\n" +heading6 + "\t" + f'{self.evening} Litres' + "\n")
        self.my_receipt1.insert('end', "\n" +heading7 + "\t" + f'{self.added} Litres' + "\n")
        self.my_receipt1.insert('end', "\n" +heading8 + "\t" + f'{self.monthly} Litres' +"\n")
        self.my_receipt1.insert('end', "\n" +heading9 + "\t" + f'{server}')
        self.print_button=customtkinter.CTkButton(my_frame,text="Send SMS",fg_color="purple", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150, height=40,command=self.send_message)
        self.print_button.grid(row=2, column=0, columnspan=5,pady=10)
        #delete entry
        self.show_records()
    def grab_date(self):
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        self.my_label=customtkinter.CTkLabel(self.top, text="Choose Date", fg_color="purple",text_color="white",text_font=("Consollas 10", -15,"bold"), width=120, height=30).pack()
        self.cal=Calendar(self.top, selectmode="day", cursor="hand1",date_pattern="mm/dd/yyyy",year=self.currentDateTime.year,month=self.currentDateTime.month,day=self.currentDateTime.day)
        self.cal.pack(pady=20)
        self.cal.bind("<<CalendarSelected>>", self.clicker) 
    def clicker(self,e):
        self.selection=self.cal.get_date()
        self.show_records()
        self.cal.destroy()
        self.top.destroy()
        
    def show_records(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT *FROM DAILY_TOTALS WHERE DATE=(?) ORDER BY Customer_ID DESC", (self.selection,))
        records7=c.fetchall()
        self.my_tree.delete(*self.my_tree.get_children())
        global count
        count=0
        for record in records7:
            if count%2==0:
                self.my_tree.insert('',index=0, iid=count, text="", values=(record[0],record[1],record[3],record[4],record[5],record[6],record[7], record[8], record[9],record[10],record[11]),tags=("evenrow",))
            else:
                self.my_tree.insert('',index=0, iid=count, text="", values=(record[0],record[1],record[3],record[4],record[5],record[6],record[7], record[8], record[9],record[10],record[11]),tags=("oddrow",))
            count+=1
              
        conn.commit()
        conn.close()
    #notifications
    def notifications(self):
        #toplevel
        self.top40=Toplevel()
        self.top40.iconbitmap("logo1.ico")
        self.top40.title("SAMARIA MILK GROUP")
        self.title_frame=Frame(self.top40)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="Daily SMS"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.send_button=customtkinter.CTkButton(self.title_frame,text="Send Messages",fg_color="green",text_color="white",text_font=("Consollas 10",-25,"bold"),width=200,height=40,command=self.send_bulk_messages)
        self.send_button.grid(row=3,column=0,columnspan=15,padx=10,pady=20,ipadx=30,ipady=30)
        
    #send bulk messages
    def send_bulk_messages(self):
        #query
        conn=sqlite3.connect('samaria database.db')
        #conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Customer_ID,Phone_Number FROM Customers")
        all_phones=c.fetchall()
        print(all_phones)
        c.execute("SELECT COUNT(Phone_Number) FROM Customers")
        all_no=c.fetchone()
        conn.commit()
        conn.close()
        for record in all_phones:
            if record[1]!='':
                #query
                #name
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT First_name FROM Customers WHERE Customer_ID=?",(record[0],))
                f_name=c.fetchone()
                print(f_name)
                c.execute("SELECT Last_name FROM Customers WHERE Customer_ID=?",(record[0],))
                l_name=c.fetchone()
                print(l_name)
                conn.commit()
                conn.close()
                #daily quantity
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Daily_Accumulated FROM DAILY_TOTALS WHERE Customer_ID=? AND DATE=?",(record[0],self.today1,))
                today_t=c.fetchone()
                if today_t==None:
                    today_t=0.0
                c.execute("SELECT DAY FROM DAILY_TOTALS WHERE Customer_ID=? AND DATE=?",(record[0],self.today1,))
                today_day=c.fetchone()
                if today_day==None:
                    today_day=self.now_day
                print(today_day)
                conn.commit()
                conn.close()
                #monthly quantity
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.mwezi,self.mwaka,record[0],))
                monthly_t=c.fetchone()
                print(monthly_t)
                conn.commit()
                conn.close()
                #message
                farmer_message=f'SAMARIA MILK GROUP NAME:{f_name} {l_name} Farmer_ID:{record[0]} PERIOD: From 1 -{today_day} {self.today_month} {self.mwaka} DATE:{self.today2} Daily_Total:{today_t} Litres Monthly_Total:{monthly_t} Litres Served By:{server}'
                try:
                    #requests mobitechtechnologies
                    url = "https://api.mobitechtechnologies.com/sms/sendsms"

                    payload = json.dumps({
                        "mobile": f'+254{record[1]}',
                        "response_type": "json",
                        "sender_name": 23107,
                        "service_id": 0,
                        "message": farmer_message
                    })
                    headers = {
                        'h_api_key': 'ead62d3ed9c918bb366cba5ec6692224d8926bd8b0c339c0a58cc137075b3e4a',
                        'Content-Type': 'application/json'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload)
                    print(response.text)
                    x=response.text[20]
                    print(x)
                    if x != '0':
                        messagebox.showerror("ERROR",f'SMS NOT Sent,Please Recharge your Account And Try Again',parent=self.top40)
                        break
                    else:
                        messagebox.showinfo("BRAVO",f'SMS Sent Succesfully to {f_name} {l_name}',parent=self.top40)
            
                except:
                    messagebox.showerror("ERROR","SMS Not Sent,Please Check Your Internet Connectivity And Try Again",parent=self.top40)
                    break
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
class Customer_Feeds:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x1000")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
        #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)
        
        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)
        
        unpaid_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Unpaid Feeds", menu=unpaid_menu)
        unpaid_menu.add_command(label="Unpaid Feeds", command=self.pay_by_cash)
        
        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="FARMER FEEDS"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #feeds table
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE FEEDS")
        print("table dropped succesfully")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS FEEDS(
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL,
                Customer_ID INT NOT NULL,
                Feed_Names TEXT NOT NULL,
                Feed_Quantity INT NOT NULL,
                Price REAL NOT NULL,
                Total_Cost REAL NOT NULL,
                Status TEXT NOT NULL,
                MONTH INT NOT NULL,
                YEAR INT NOT NULL,
                DATE INT NOT NULL,
                PERIOD TEXT NOT NULL
                )""")
        '''
        c.execute("DROP TABLE Given_Feeds")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS Given_Feeds(
                    Feed_Name TEXT NOT NULL,
                    Feed_Quantity INT NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL
                    )""")
        '''
        c.execute("DROP TABLE Feeds_Records")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS Feeds_Records(
                        Feeds_Name TEXT NOT NULL,
                        Feeds_Quantity INT NOT NULL,
                        Month INT NOT NULL,
                        Year INT NOT NULL
                        )""")
        '''
        c.execute("DROP TABLE Transport")
        print("table dropped")
        ''' 
        c.execute("""CREATE TABLE IF NOT EXISTS Transport(
                        Farmer_ID INT NOT NULL,
                        Transport_Amount REAL NOT NULL,
                        Status TEXT NOT NULL,
                        DATE INT NOT NULL,
                        PERIOD TEXT NOT NULL
                     )""")
        conn.commit()
        conn.close()
        
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top0,border_color="green",border_width=5, width=400,height=450)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        #dates
        self.currentDateTime=date.today()
        self.today=self.currentDateTime.strftime("%A-%B %d, %Y")
        self.time=datetime.now()
        self.today1=self.time.strftime("%m/%d/%Y")
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.now_day=datetime.now().day
        self.mwezi=datetime.now().month
        self.mwaka=datetime.now().year
        #variables
        self.count=0
        self.start=2
        self.start1=2
        self.start2=2
        #labels
        feeds_title="FARMER FEEDS"
        self.feeds_title_label=customtkinter.CTkLabel(self.left_frame, text=feeds_title, fg_color="orange",text_color="white", text_font=("Consollas 10",-18, "underline","bold"),width=150, height=25)
        self.feeds_title_label.grid(row=0, column=0, columnspan=3,pady=5)
        self.today_label=customtkinter.CTkLabel(self.left_frame, text="Today:",fg_color="brown", text_color="white", text_font=("Consollas 10", -12, "bold"),width=100, height=25)
        self.today_label.grid(row=1, column=0)
        self.today_date=customtkinter.CTkLabel(self.left_frame, text=self.today)
        self.today_date.grid(row=1, column=1)
        self.customer_id_label=customtkinter.CTkLabel(self.left_frame, text="Enter Farmer's ID:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100, height=25)
        self.customer_id_label.grid(row=2, column=0,pady=3)
        self.first_name_label=customtkinter.CTkLabel(self.left_frame, text="First Name:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100, height=25)
        self.first_name_label.grid(row=3, column=0,pady=3)
        self.last_name_label=customtkinter.CTkLabel(self.left_frame, text="Last Name:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100, height=25)
        self.last_name_label.grid(row=4, column=0,pady=3)
        self.feeds_type_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Type:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=100, height=25)
        self.feeds_type_label.grid(row=5, column=0,pady=3)
        #entryboxes
        self.customer_id_entry=customtkinter.CTkEntry(self.left_frame,width=150, height=25,border_color="blue",placeholder_text="Enter Farmer ID", placeholder_text_color="blue")
        self.customer_id_entry.grid(row=2, column=1)
        self.first_name_entry=customtkinter.CTkEntry(self.left_frame, width=150, height=25,border_color="blue")
        self.first_name_entry.grid(row=3, column=1)
        self.last_name_entry=customtkinter.CTkEntry(self.left_frame, width=150, height=25,border_color="blue")
        self.last_name_entry.grid(row=4, column=1)
        #treeview
        self.tree_frame=Frame(self.left_frame, highlightbackground="green", highlightthickness=5, width=300, height=200, bd=0)
        self.tree_frame.grid(row=6, column=0, columnspan=3, padx=20, pady=4)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=15,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                  background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree=ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=7)
        self.my_tree.pack()
        #configure our scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)
        #define our columns
        self.my_tree['columns']=("Feeds Name", "Quantity", "Price","DATE")
        #format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Feeds Name", width=200, anchor="w")
        self.my_tree.column("Quantity", width=80, anchor="w")
        self.my_tree.column("Price", width=100, anchor="w")
        self.my_tree.column("DATE", width=100, anchor="w")
        #create headings
        self.my_tree.heading("#0", text="")
        self.my_tree.heading("Feeds Name", text="Feeds Name", anchor="w")
        self.my_tree.heading("Quantity", text="Quantity", anchor="w")
        self.my_tree.heading("Price", text="Total", anchor="w")
        self.my_tree.heading("DATE", text="Date", anchor="w")
        self.t1=StringVar()
        #create striped row tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="violet")
        self.total_feeds_entry=customtkinter.CTkEntry(self.tree_frame, width=150, height=25,border_color="blue")
        self.total_feeds_entry.pack(anchor="e",padx=10,pady=2)
        #buttons
        self.confirm_button=customtkinter.CTkButton(self.left_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10", -17, "bold"),width=150, height=35,command=self.get_data)
        self.confirm_button.grid(row=2, column=2,pady=3)
        self.choose_type_button=customtkinter.CTkButton(self.left_frame, text="Choose",fg_color="purple", text_color="white", text_font=("Consollas 10", -18, "bold"),width=150, height=35,command=self.choose_feeds)
        self.choose_type_button.grid(row=5, column=1,pady=4)
        self.give_out_button=customtkinter.CTkButton(self.left_frame, text="GRANT FEEDS",fg_color="purple", text_color="white", text_font=("Consollas 10", -18, "bold"),width=150, height=35,command=self.verify_feeds)
        self.give_out_button.grid(row=7, column=0, columnspan=4, padx=20,pady=4)

        #*******************************************************************************************************************************************************************************************************
        #right frame
        self.right_frame=customtkinter.CTkFrame(self.top0,border_color="maroon",border_width=5, width=400,height=450)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #title
        feeds_inventory_title="FEEDS INVENTORY"
        self.feeds_inventory_label=customtkinter.CTkLabel(self.right_frame, text=feeds_inventory_title, fg_color="orange",text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
        self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
        #create another treeview
        self.tree_frame1=Frame(self.right_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
        self.tree_frame1.grid(row=1, column=0, padx=30, pady=10, columnspan=10)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                  background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll1=Scrollbar(self.tree_frame1)
        self.tree_scroll1.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree1=ttk.Treeview(self.tree_frame1, yscrollcommand=self.tree_scroll1.set,height=8)
        self.my_tree1.pack()
        #configure our scrollbar
        self.tree_scroll1.config(command=self.my_tree1.yview)

        #define our columns
        self.my_tree1['columns']=("FEEDS NAME", "QUANTITY", "PRICE")
        #format our columns
        self.my_tree1.column("#0", width=0, stretch=NO)
        self.my_tree1.column("FEEDS NAME", anchor="w", width=270)
        self.my_tree1.column("QUANTITY", anchor="w", width=200)
        self.my_tree1.column("PRICE", anchor="w", width=200)

        #create headings
        self.my_tree1.heading("#0", text="")
        self.my_tree1.heading("FEEDS NAME", text="FEEDS NAME", anchor="w")
        self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="w")
        self.my_tree1.heading("PRICE", text="PRICE", anchor="w")

        #create striped row tags
        self.my_tree1.tag_configure('oddrow', background="white")
        self.my_tree1.tag_configure('evenrow', background="violet")
        # binding single click
        self.my_tree1.bind("<ButtonRelease-1>", self.clicker)
        self.query_database()
        #labels
        self.title_label=customtkinter.CTkLabel(self.right_frame,text="ADD NEW FEEDS", fg_color="green",text_color="white",text_font=("Consollas 10",-20,"bold","underline"),width=200,height=25)
        self.title_label.grid(row=2,column=0, columnspan=2,padx=10, pady=5)
        self.feeds_name_label=customtkinter.CTkLabel(self.right_frame, text="Enter Feeds Name",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=25)
        self.feeds_name_label.grid(row=3, column=0, padx=10, pady=3)
        self.feeds_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Enter Feeds Quantity",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=25)
        self.feeds_quantity_label.grid(row=4, column=0, padx=10, pady=3)
        self.feeds_price_label=customtkinter.CTkLabel(self.right_frame, text="Enter Feeds Price",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=25)
        self.feeds_price_label.grid(row=5, column=0, padx=10, pady=3)
        #entry boxes
        self.feeds_name_entry=customtkinter.CTkEntry(self.right_frame,width=170,height=25, border_color="blue")
        self.feeds_name_entry.grid(row=3, column=1)
        self.feeds_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=130,height=25, border_color="blue")
        self.feeds_quantity_entry.grid(row=4, column=1)
        self.feeds_price_entry=customtkinter.CTkEntry(self.right_frame,width=130,height=25, border_color="blue")
        self.feeds_price_entry.grid(row=5, column=1)
        #button
        self.add_feeds_button=customtkinter.CTkButton(self.right_frame,text="ADD NEW FEEDS",fg_color="purple", text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.verify_admin)
        self.add_feeds_button.grid(row=6,column=0, columnspan=2,padx=10,pady=10,ipadx=20)

        #labels
        self.title_label1=customtkinter.CTkLabel(self.right_frame,text="INCREASE STOCK", fg_color="green",text_color="white",text_font=("Consollas 10",-20,"bold","underline"),width=200,height=25)
        self.title_label1.grid(row=2,column=3, columnspan=3,padx=10, pady=5)
        self.feeds_name_label1=customtkinter.CTkLabel(self.right_frame, text="Enter Feeds Name",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=25)
        self.feeds_name_label1.grid(row=3, column=3, padx=15, pady=3)
        self.feeds_quantity_label1=customtkinter.CTkLabel(self.right_frame, text="Enter NEW Quantity",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=25)
        self.feeds_quantity_label1.grid(row=4, column=3, padx=15, pady=3)
        #entry boxes
        self.feeds_name_entry1=customtkinter.CTkEntry(self.right_frame,width=170,height=25, border_color="blue")
        self.feeds_name_entry1.grid(row=3, column=4)
        self.feeds_quantity_entry1=customtkinter.CTkEntry(self.right_frame,width=130,height=25, border_color="blue")
        self.feeds_quantity_entry1.grid(row=4, column=4)
        #button
        self.add_feeds_button1=customtkinter.CTkButton(self.right_frame,text="INCREASE STOCK",fg_color="red", text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.verify_admin1)
        self.add_feeds_button1.grid(row=5,column=3, columnspan=2,padx=10,pady=10,ipadx=20)

    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    #get customer data
    def get_data(self):
            if self.customer_id_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
            #id validity                
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT First_name FROM Customers WHERE Customer_ID=" +str(self.customer_id_entry.get()))
            fff_name=c.fetchone()
            conn.commit()
            conn.close()
            if fff_name==None:
                messagebox.showerror("ERROR", "Farmer ID Does not exist,Check And Try Again",parent =self.top0)
            else:
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT First_name FROM Customers WHERE Customer_ID=" +str(self.customer_id_entry.get()))
                ff_name=c.fetchone()
                first_name=''
                first_name=ff_name
                self.first_name_entry.delete(0,END)
                self.first_name_entry.insert(0, first_name)
                conn.commit()
                conn.close()
                #last name
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Last_name FROM Customers WHERE Customer_ID=" +str(self.customer_id_entry.get()))
                l_name=c.fetchone()
                last_name=''
                last_name= l_name
                self.last_name_entry.delete(0,END)
                self.last_name_entry.insert(0, last_name)
                conn.commit()
                conn.close()
                #previous feeds
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.customer_id_entry.get(),"NOT PAID",))
                yote=c.fetchall()
                global count
                self.my_tree.delete(* self.my_tree.get_children())
                for record in yote:
                    if self.count%2==0:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[3],record[4],record[5],record[10]), tags=("evenrow"),)
                    else:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[3],record[4], record[5],record[10]), tags=("oddrow"),)
                    self.count+=1
                conn.commit()
                conn.close()
                self.get_total()
    #choose feeds function
    def choose_feeds(self):
        self.top97=Toplevel()
        self.top97.title("SAMARIA MILK GROUP")
        self.top97.iconbitmap("logo1.ico")
        #connect to database
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Feeds_Name FROM Feeds_Inventory")
        self.feeds_names=c.fetchall()
        self.data=[[numbers]for numbers in self.feeds_names]
        #print(self.data)
        conn.commit()
        conn.close()
        self.my_frame=Frame(self.top97)
        self.my_frame.pack(padx=20,pady=20,anchor="w")
        self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE FEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.my_sheet=Sheet(self.my_frame,
                            align = "w",
                            header_font=("Consollas 10",15,"bold"),
                            font=("Consollas 10",13,"normal"),
                            data=self.data,
                            headers= ["Feeds Name","Checkbox","Feeds Quantity"],
                            height=400,
                            show_x_scrollbar = False,
                            show_y_scrollbar =True,
                            width=650)
        self.my_sheet.enable_bindings("copy",
                                   "rc_select",
                                   "arrowkeys",
                                   "double_click_column_resize",
                                   "column_width_resize",
                                   "column_select",
                                   "row_select",
                                   "drag_select",
                                   "single_select",
                                   "select_all")
        self.my_sheet.enable_bindings("edit_header")
        self.my_sheet.grid(row=1,column=0,columnspan=4)
        def get_info(event=None):
            for number in self.data:
                if number[1]==True:
                    print(number[0])
                #print(hdrs)
        def get_quantity(event=None):
            for number in self.data:
                if number[1]==True:
                    print(number[0])
                    print(number[2])
                    if number[2]=="Bags":
                        number[2]=event.text
                        print(number[2])
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(number[0],))
                        pesa=c.fetchone()
                        total_amount=(pesa*float(number[2]))
                        conn.commit()
                        conn.close()
                        initial=self.total_entry.get()
                        if initial=="":
                            initial=0.0
                        updated= float(initial)+total_amount
                        self.total_entry.delete(0,END)
                        self.total_entry.insert(0,updated)
                    #self.my_sheet.get_dropdown_values()
        self.my_sheet.create_dropdown(r="all",c=2,values=["Bags"]+[f'{i}'for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)],selection_function=get_quantity)
        self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
        self.my_sheet.get_checkboxes()
        self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
        self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
        self.my_sheet.default_header_height(height="2")
        self.my_sheet.column_width(column=0,width=300)
        self.my_sheet.column_width(column=2,width=150)
        def grant_feeds():
            self.my_tree.delete(* self.my_tree.get_children())
            for record in self.data:
                if record[1]==True:
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(record[0],))
                    pesa=c.fetchone()
                    c.execute("SELECT Quantity FROM Feeds_Inventory WHERE Feeds_Name=?",(record[0],))
                    initial_q_quantity=c.fetchone()
                    if initial_q_quantity==0:
                        messagebox.showerror("ERROR",f'{record[0]}'" Stock is Depleted, Consider New Stock",parent =self.top0)
                        continue
                    if (initial_q_quantity - float(record[2])) < 0 :
                        messagebox.showerror("ERROR", f'{record[0]}'"Stock is Less Than"f'{record[2]}',parent=self.top0)
                        continue
                    if initial_q_quantity==1:
                        messagebox.showinfo("REMINDER",f'{record[0]}'" Stock Depleting, Consider Adding New Stock",parent =self.top0)
                    total=pesa* float(record[2])
                    if self.count%2==0:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total, self.today1), tags=("evenrow"),)
                    else:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total, self.today1), tags=("oddrow"),)
                    self.count+=1
            self.top97.destroy()
            self.get_total()
        #buttons
        self.total_label=customtkinter.CTkLabel(self.my_frame,text="TOTAL",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=30)
        self.total_label.grid(row=3,column=0,columnspan=2,padx=20,pady=10)
        self.total_entry=customtkinter.CTkEntry(self.my_frame,border_color="blue",width=200,height=30)
        self.total_entry.grid(row=3,column=2,columnspan=2,padx=20,pady=10)
        self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT FEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
        self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
    #get total
    def get_total(self):
            sum1=0.0
            for child in self.my_tree.get_children():
                sum1 +=float(self.my_tree.item(child,"values")[2])
            self.total_feeds_entry.delete(0,END)
            self.total_feeds_entry.insert(0,sum1)
        #get total
    def get_total1(self):
            sum2=0.0
            for child in self.my_tree2.get_children():
                sum2 +=float(self.my_tree2.item(child,"values")[2])
            self.total_feeds_entry2.delete(0,END)
            self.total_feeds_entry2.insert(0, f' Kshs {sum2}')
        #give feeds
    def include_transport(self):
        #toplevel
        self.top80=Toplevel()
        self.top80.title("SAMARIA MILK GROUP")
        self.top80.iconbitmap("logo1.ico")
        my_frame=Frame(self.top80)
        my_frame.pack()
        self.title_label=customtkinter.CTkLabel(my_frame,text="INCLUDE TRANSPORT",fg_color="maroon",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.transport_amount_label=customtkinter.CTkLabel(my_frame,text="Enter Transport Amount(KShs):",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.transport_amount_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
        self.transport_amount_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
        self.transport_amount_entry.grid(row=1,column=2,columnspan=2,padx=5)
        self.save_button=customtkinter.CTkButton(my_frame,text="OK",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.grant_transport_feeds)
        self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20)
    def verify_feeds(self):
        if self.customer_id_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
        if self.my_tree.get_children()==[]:
                messagebox.showerror("ERROR", "Please Choose Feeds",parent =self.top0)
        else:
            response=messagebox.askyesno("Confirm","Do you want to include Transport",parent=self.top0)
            if response==1:
                self.include_transport()
            else:
                self.grant_feeds()
    def grant_feeds(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.customer_id_entry.get(),"NOT PAID",))
        self.previous=c.fetchall()
        self.total_accumulated_price=0.0
        for x in self.previous:
            self.total_accumulated_price+=(x[5])
        conn.commit()
        conn.close()
        for child in self.my_tree.get_children():
            data= self.my_tree.item(child, "values")[0]
            datum=self.my_tree.item(child, "values")[1]
            datam=self.my_tree.item(child, "values")[2]
            if self.now_day<=15:
                #insert data
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO FEEDS VALUES(:First_Name, :Last_Name, :Customer_ID, :Feed_Names, :Feed_Quantity, :Price, :Total_Cost,:Status, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Customer_ID': self.customer_id_entry.get(),
                                'Feed_Names': data,
                                'Feed_Quantity': datum,
                                'Price' : datam,
                                'Total_Cost': (self.total_accumulated_price + float(self.total_feeds_entry.get())),
                                'Status': "NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 1-15"
                                })
                conn.commit()
                conn.close()
            else:
                #insert data
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO FEEDS VALUES(:First_Name, :Last_Name, :Customer_ID, :Feed_Names, :Feed_Quantity, :Price, :Total_Cost,:Status, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Customer_ID': self.customer_id_entry.get(),
                                'Feed_Names': data,
                                'Feed_Quantity': datum,
                                'Price' : datam,
                                'Total_Cost': (self.total_accumulated_price + float(self.total_feeds_entry.get())),
                                'Status': "NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 16"
                                })
                conn.commit()
                conn.close()
            #insert data to given out table
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("DELETE FROM Given_Feeds WHERE rowid NOT IN (SELECT MIN(rowid) FROM Given_Feeds GROUP BY Feed_Name,Feed_Quantity,Month,Year)")
            conn.commit()
            conn.close()
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT DISTINCT Month FROM Given_Feeds WHERE Feed_Name=?",(data,))
            monthmn=c.fetchall()
            if monthmn==[]:
                monthmn=[0]
            c.execute("SELECT DISTINCT Year FROM Given_Feeds WHERE Feed_Name=?",(data,))
            yearmn=c.fetchall()
            if yearmn==[]:
                yearmn=[0]
            conn.commit()
            conn.close()
            for record,records in itertools.product(monthmn,yearmn):
                if ((record==self.mwezi) and (records==self.mwaka)):
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(data,record,records,))
                    initial_quantity=c.fetchone()
                    if initial_quantity==None:
                        initial_quantity=0
                    updated_quantity=(initial_quantity + float(datum))
                    c.execute("""UPDATE Given_Feeds SET
                                Feed_Name=:fe_name,
                                Feed_Quantity=:fe_qty,
                                Month=:momn,
                                Year=:yiar
                                
                                WHERE Feed_Name=:fe_name AND Month=:momn AND Year=:yiar""",
                                {
                                    'fe_name': data,
                                    'fe_qty' : updated_quantity,
                                    'momn' : self.mwezi,
                                    'yiar' : self.mwaka
                                    })
                    c.execute("INSERT OR IGNORE INTO Given_Feeds VALUES(:Feed_Name, :Feed_Quantity, :Month, :Year)",
                                    {
                                        'Feed_Name':data,
                                        'Feed_Quantity':updated_quantity,
                                        'Month':self.mwezi,
                                        'Year':self.mwaka
                                        })
                    conn.commit()
                    conn.close()
                    break
                else:
                    if ((record==monthmn[-1]) and (records==yearmn[-1])):
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(data,self.mwezi,self.mwaka,))
                        initial_quantity=c.fetchone()
                        if initial_quantity==None:
                            initial_quantity=0
                        updated_quantity=(initial_quantity + float(datum))
                        c.execute("INSERT INTO Given_Feeds VALUES(:Feed_Name, :Feed_Quantity, :Month, :Year)",
                                    {
                                        'Feed_Name':data,
                                        'Feed_Quantity':updated_quantity,
                                        'Month':self.mwezi,
                                        'Year':self.mwaka
                                        })
                        conn.commit()
                        conn.close()
                        #break
            #update feeds_inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            initial_quantity=c.fetchone()
            current_quantity=(initial_quantity - float(datum))
            c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            cost=c.fetchone()
            c.execute("SELECT Month From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            monthm=c.fetchone()
            c.execute("SELECT Year From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            yearm=c.fetchone()
            c.execute("SELECT DATE From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            datem=c.fetchone()
            c.execute(""" UPDATE Feeds_Inventory SET
                        Feeds_Name=:f_name,
                        Quantity=:q_ty,
                        Price=:prie,
                        Month=:moth,
                        Year=:yoar,
                        DATE=:datu

                        WHERE Feeds_Name=:f_name""",
                        {
                            'f_name': data,
                            'q_ty' : current_quantity,
                            'prie' : cost,
                            'moth': monthm,
                            'yoar' : yearm,
                            'datu' : datem
                            })
            conn.commit()
            conn.close()
        self.receipt()
    def grant_transport_feeds(self):
        if self.now_day<=15:
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("INSERT INTO Transport VALUES(:Farmer_ID,:Transport_Amount,:Status,:DATE,:PERIOD)",
                        {
                            'Farmer_ID':self.customer_id_entry.get(),
                            'Transport_Amount':self.transport_amount_entry.get(),
                            'Status': "NOT PAID",
                            'DATE':self.today1,
                            'PERIOD':"From 1-15"
                            })
            conn.commit()
            conn.close()
            self.transport_amount_entry.delete(0,END)
            self.top80.destroy()
        else:
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("INSERT INTO Transport VALUES(:Farmer_ID,:Transport_Amount,:Status,:DATE,:PERIOD)",
                        {
                            'Farmer_ID':self.customer_id_entry.get(),
                            'Transport_Amount':self.transport_amount_entry.get(),
                            'Status': "NOT PAID",
                            'DATE':self.today1,
                            'PERIOD':"From 16"
                            })
            conn.commit()
            conn.close()
            self.transport_amount_entry.delete(0,END)
            self.top80.destroy()
        #continue
        conn=sqlite3.connect('samaria feeds database.db')
        #conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.customer_id_entry.get(),"NOT PAID",))
        self.previous=c.fetchall()
        self.total_accumulated_price=0.0
        for x in self.previous:
            self.total_accumulated_price+=(x[5])
        conn.commit()
        conn.close()
        for child in self.my_tree.get_children():
            data= self.my_tree.item(child, "values")[0]
            datum=self.my_tree.item(child, "values")[1]
            datam=self.my_tree.item(child, "values")[2]
            if self.now_day<=15:
                #insert data
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO FEEDS VALUES(:First_Name, :Last_Name, :Customer_ID, :Feed_Names, :Feed_Quantity, :Price, :Total_Cost,:Status, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Customer_ID': self.customer_id_entry.get(),
                                'Feed_Names': data,
                                'Feed_Quantity': datum,
                                'Price' : datam,
                                'Total_Cost': (self.total_accumulated_price + float(self.total_feeds_entry.get())),
                                'Status': "NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 1-15"
                                })
                conn.commit()
                conn.close()
            else:
                #insert data
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO FEEDS VALUES(:First_Name, :Last_Name, :Customer_ID, :Feed_Names, :Feed_Quantity, :Price, :Total_Cost,:Status, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Customer_ID': self.customer_id_entry.get(),
                                'Feed_Names': data,
                                'Feed_Quantity': datum,
                                'Price' : datam,
                                'Total_Cost': (self.total_accumulated_price + float(self.total_feeds_entry.get())),
                                'Status': "NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 16"
                                })
                conn.commit()
                conn.close()
            #insert data to given out table
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("DELETE FROM Given_Feeds WHERE rowid NOT IN (SELECT MIN(rowid) FROM Given_Feeds GROUP BY Feed_Name,Feed_Quantity,Month,Year)")
            conn.commit()
            conn.close()
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT DISTINCT Month FROM Given_Feeds WHERE Feed_Name=?",(data,))
            monthmn=c.fetchall()
            if monthmn==[]:
                monthmn=[0]
            c.execute("SELECT DISTINCT Year FROM Given_Feeds WHERE Feed_Name=?",(data,))
            yearmn=c.fetchall()
            if yearmn==[]:
                yearmn=[0]
            conn.commit()
            conn.close()
            for record,records in itertools.product(monthmn,yearmn):
                if ((record==self.mwezi) and (records==self.mwaka)):
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(data,record,records,))
                    initial_quantity=c.fetchone()
                    if initial_quantity==None:
                        initial_quantity=0
                    updated_quantity=(initial_quantity + float(datum))
                    c.execute("""UPDATE Given_Feeds SET
                                Feed_Name=:fe_name,
                                Feed_Quantity=:fe_qty,
                                Month=:momn,
                                Year=:yiar
                                            
                                WHERE Feed_Name=:fe_name AND Month=:momn AND Year=:yiar""",
                                {
                                    'fe_name': data,
                                    'fe_qty' : updated_quantity,
                                    'momn' : self.mwezi,
                                    'yiar' : self.mwaka
                                    })
                    c.execute("INSERT OR IGNORE INTO Given_Feeds VALUES(:Feed_Name, :Feed_Quantity, :Month, :Year)",
                                    {
                                        'Feed_Name':data,
                                        'Feed_Quantity':updated_quantity,
                                        'Month':self.mwezi,
                                        'Year':self.mwaka
                                        })
                    conn.commit()
                    conn.close()
                    break
                else:
                    if ((record==monthmn[-1]) and (records==yearmn[-1])):
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Feed_Quantity FROM Given_Feeds WHERE Feed_Name=? AND Month=? AND Year=?",(data,self.mwezi,self.mwaka,))
                        initial_quantity=c.fetchone()
                        if initial_quantity==None:
                            initial_quantity=0
                        updated_quantity=(initial_quantity + float(datum))
                        c.execute("INSERT INTO Given_Feeds VALUES(:Feed_Name, :Feed_Quantity, :Month, :Year)",
                                    {
                                        'Feed_Name':data,
                                        'Feed_Quantity':updated_quantity,
                                        'Month':self.mwezi,
                                        'Year':self.mwaka
                                        })
                        conn.commit()
                        conn.close()
                        #break
            #update feeds_inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            initial_quantity=c.fetchone()
            current_quantity=(initial_quantity - float(datum))
            c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            cost=c.fetchone()
            c.execute("SELECT Month From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            monthm=c.fetchone()
            c.execute("SELECT Year From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            yearm=c.fetchone()
            c.execute("SELECT DATE From Feeds_Inventory WHERE Feeds_Name=?",(data,))
            datem=c.fetchone()
            c.execute(""" UPDATE Feeds_Inventory SET
                        Feeds_Name=:f_name,
                        Quantity=:q_ty,
                        Price=:prie,
                        Month=:moth,
                        Year=:yoar,
                        DATE=:datu

                        WHERE Feeds_Name=:f_name""",
                        {
                            'f_name': data,
                            'q_ty' : current_quantity,
                            'prie' : cost,
                            'moth': monthm,
                            'yoar' : yearm,
                            'datu' : datem
                            })
            conn.commit()
            conn.close()
        self.receipt()
    #receipt
    def print_receipt(self):
                        printText=self.my_receipt.get('1.0','end')
                        filename=tempfile.mktemp(".txt")
                        open(filename, "w").write(printText)
                        win32api.ShellExecute(0,
                                              "printto",
                                              filename,
                                              '"%s"' % win32print.GetDefaultPrinter(),
                                              ".",
                                              0
                                              )
                        self.my_receipt.delete('1.0', 'end')
                        self.top1.destroy()
            
    def receipt(self):                
        self.top1=Toplevel()
        self.top1.title("SAMARIA MILK GROUP")
        self.top1.iconbitmap("logo1.ico")
        my_frame1=Frame(self.top1, width=50)
        my_frame1.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame1, text="RECEIPT",fg_color="purple",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame1, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="FEEDS"
        heading1="NAME:"
        heading2="Farmer ID:"
        heading3="Feeds Name"
        heading4="Quantity"
        heading5="Price"
        heading6="DATE:"
        heading7="Previous Granted UnPaid Feeds"
        heading8="Total Feeds Credit"
        heading9="Today Feeds Credit"
        heading10="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0', 'end')
        #add contents to our scrolled widget
        self.my_receipt.insert('end', "\n" + title +"\n")
        self.my_receipt.insert('end', "\n" + sub +"\n")
        self.my_receipt.insert('end', "\n" + heading0 +"\n")
        self.my_receipt.insert('end', "\n" + heading6 + f'{self.today} {self.Time}'+"\n")
        self.my_receipt.insert('end', "\n" + heading1 +f' {self.first_name_entry.get()} {self.last_name_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading2 +f' {self.customer_id_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading3+"\t"+"\t"+ heading4 +"\t" +"\t"+ heading5 +"\n")
        #transport
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT SUM(Transport_Amount)FROM Transport WHERE Farmer_ID=? AND DATE=? AND Status=?",(self.customer_id_entry.get(),self.today1,"NOT PAID",))
        transport_f=c.fetchone()
        if transport_f==None:
            transport_f=0.0
        conn.commit()
        conn.close()
        #previous transport
        #transport
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND DATE!=?",(self.customer_id_entry.get(),"NOT PAID",self.today1,))
        p_transport_fees=c.fetchone()
        if p_transport_fees==None:
            p_transport_fees=0.0
        conn.commit()
        conn.close()
        for child in self.my_tree.get_children():
            data= self.my_tree.item(child, "values")[0]
            datum=self.my_tree.item(child, "values")[1]
            datam=self.my_tree.item(child, "values")[2]
            date=self.my_tree.item(child, "values")[3]
            self.my_receipt.insert('end', "\n" + data +"\t"+"\t"+datum+"\t"+"\t"+datam+"\n")
        if self.previous!=[]:
            self.my_receipt.insert('end', "\n" + heading9 +"\t"+"\t"+ f' {self.total_feeds_entry.get()}'+"\n")
            self.my_receipt.insert('end', "\n" + heading7 +"\n")
            for record in self.previous:
                self.my_receipt.insert('end', "\n" +record[3]+"\t"+"\t"+str(record[4])+"\t"+"\t"+ str(record[5])+"\n")
            if p_transport_fees!=0.0:
                self.my_receipt.insert('end', "\n" +"Previous Transport Fees:"+"\t"+f'Kshs {p_transport_fees}'+"\n")
            if transport_f!=0.0:
                self.my_receipt.insert('end', "\n" +"Today Transport Fee"+"\t"+f'Kshs {transport_f}'+"\n")
            self.my_receipt.insert('end', "\n" + heading8 +"\t"+"\t"+ str(self.total_accumulated_price + float(self.total_feeds_entry.get())+float(p_transport_fees)+float(transport_f))+"\n")
            self.my_receipt.insert('end', "\n" + heading10+ "\t"+ f'{server}' +"\n")
        else:
            if p_transport_fees!=0.0:
                self.my_receipt.insert('end', "\n" +"Previous Transport Fees:"+"\t"+f'Kshs {p_transport_fees}'+"\n")
            if transport_f!=0.0:
                self.my_receipt.insert('end', "\n" +"Today Transport Fee"+"\t"+f'Kshs {transport_f}'+"\n")
            self.my_receipt.insert('end', "\n" + heading8 +"\t"+"\t"+ str(self.total_accumulated_price + float(self.total_feeds_entry.get())+float(p_transport_fees)+float(transport_f))+"\n")
            self.my_receipt.insert('end', "\n" + heading10+ "\t"+ f'{server}' +"\n")
        
        self.my_receipt.configure(state='disabled')
        self.print_button=customtkinter.CTkButton(my_frame1, text="PRINT", command=self.print_receipt,fg_color="maroon",text_color="white", text_font=("Consollas 10",-20, "bold"),width=150, height=40)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
        
        self.my_tree.delete(* self.my_tree.get_children())
        #clear entries
        self.customer_id_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.total_feeds_entry.delete(0, END)
        self.query_database()
        #self.given_out()
    #givenout feeds
    def given_out(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT DISTINCT Feed_Names, SUM(Feed_Quantity) FROM FEEDS GROUP BY Feed_Names")
        group=c.fetchall()
        conn.commit()
        conn.close()
        global count
        for record in group:
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            conn.row_factory=lambda cursor, row:row[0]
            c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(str(record[0]),))
            mapesa=c.fetchone()
            conn.commit()
            conn.close()
            if self.count%2==0:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], record[1], (record[1] * int(mapesa[0]))), tags=("evenrow"),)
            else:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], record[1],(record[1] * int(mapesa[0]))), tags=("oddrow"),)
            self.count+=1
        self.get_total1()
        
    #create query function
    def query_database(self):
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Feeds_Inventory ORDER BY Feeds_Name ASC")
            f_eeds=c.fetchall()
            self.my_tree1.delete(* self.my_tree1.get_children())
            global count
            for record in f_eeds:
                if self.count%2==0:
                    self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[2]}'), tags=("evenrow"),)
                else:
                     self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[2]}'), tags=("oddrow"),)
                self.count+=1
            conn.commit()
            conn.close()
    def verify_admin(self):
        self.top96=Toplevel()
        self.top96.title("SAMARIA MILK GROUP")
        self.top96.iconbitmap("logo1.ico")
        my_frame=Frame(self.top96)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.add_feeds)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #insert our data
    def add_feeds(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()
            try:
                if self.feeds_name_entry.get()=="":
                    messagebox.showerror("ERROR", "Please Enter Feeds Name",parent =self.top0)
                else:
                    self.my_tree1.insert('', index='end', iid=self.count, text="", values=(self.feeds_name_entry.get(), self.feeds_quantity_entry.get(),self.feeds_price_entry.get()))
                    self.count+=1
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO Feeds_Inventory VALUES(:Feeds_Name, :Quantity, :Price,:Month, :Year, :DATE)",
                            {
                                'Feeds_Name': self.feeds_name_entry.get(),
                                'Quantity': self.feeds_quantity_entry.get(),
                                'Price': self.feeds_price_entry.get(),
                                'Month': self.mwezi,
                                'Year' : self.mwaka,
                                'DATE' :self.today1
                                })
                    conn.commit()
                    conn.close()
                    #insert data to our feeds records table
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO Feeds_Records VALUES (:Feeds_Name, :Feeds_Quantity, :Month, :Year)",
                                {
                                    'Feeds_Name': self.feeds_name_entry.get(),
                                    'Feeds_Quantity' : self.feeds_quantity_entry.get(),
                                    'Month' : self.mwezi,
                                    'Year': self.mwaka
                                    })
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Bravo", f'{self.feeds_name_entry.get()} Added Succesfully',parent =self.top0)
            except:
                messagebox.showerror("ERROR",f'{self.feeds_name_entry.get()} Already Exists',parent =self.top0)
            #clear entry boxes
            self.feeds_name_entry.delete(0,END)
            self.feeds_quantity_entry.delete(0,END)
            self.feeds_price_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_database()
    #create binding function
    def clicker(self,e):
        #clear entry boxes
        self.feeds_name_entry1.delete(0,END)
        #grab record number
        selected=self.my_tree1.focus()
        #grab record values
        values=self.my_tree1.item(selected,'values')
        #output to entry boxes
        self.feeds_name_entry1.insert(0,values[0])
        #double click
        #my_tree1.bind("<Double-1>", clicker)
    #create another binding function
    def clicker1(self,e):
        self.farmer_id_entry.delete(0,END)
        self.feeds_total_entry.delete(0,END)
        self.feeds_transport_entry.delete(0,END)
        self.total_cost_entry.delete(0,END)
        #grab record
        selected1=self.my_tree2.focus()
        #grab record values
        values=self.my_tree2.item(selected1,'values')
        #output to entry boxes
        self.farmer_id_entry.insert(0, values[2])
        self.feeds_total_entry.insert(0, values[3])
        self.feeds_transport_entry.insert(0, values[4])
        self.total_cost_entry.insert(0, values[5])
        #self.increase_stock()
    def verify_admin1(self):
        self.top95=Toplevel()
        self.top95.title("SAMARIA MILK GROUP")
        self.top95.iconbitmap("logo1.ico")
        my_frame=Frame(self.top95)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.increase_stock)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #add new stock
    def increase_stock(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()
            
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Feeds_Quantity FROM Feeds_Records WHERE Feeds_Name=? AND Month=? AND Year=?",(self.feeds_name_entry1.get(),self.mwezi,self.mwaka,))
            initial_quantity=c.fetchone()
            if initial_quantity==None:
                initial_quantity=0
            c.execute("SELECT Quantity FROM Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry1.get(),))
            now_quantity=c.fetchone()
            if now_quantity==None:
                now_quantity=0
            c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry1.get(),))
            cost=c.fetchone()
            c.execute("SELECT Month FROM Feeds_Records WHERE Feeds_Name=?",(self.feeds_name_entry1.get(),))
            initial_month=c.fetchone()
            c.execute("SELECT Year FROM Feeds_Records WHERE Feeds_Name=?",(self.feeds_name_entry1.get(),))
            initial_year=c.fetchone()
            conn.commit()
            conn.close()
            final_quantity = (initial_quantity + float(self.feeds_quantity_entry1.get()))
            later_quantity= (now_quantity + float(self.feeds_quantity_entry1.get()))
            if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
                #update feeds inventory table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute(""" UPDATE Feeds_Inventory SET
                                Feeds_Name=:f_name,
                                Quantity=:q_ty,
                                Price=:prie,
                                Month=:moth,
                                Year =:yuar,
                                DATE =:sikuku

                            WHERE Feeds_Name=:f_name""",
                                {
                                    'f_name': self.feeds_name_entry1.get(),
                                    'q_ty' : later_quantity,
                                    'prie' : cost,
                                    'moth' : self.mwezi,
                                    'yuar' : self.mwaka,
                                    'sikuku' : self.today1
                                    })
                conn.commit()
                conn.close()
                #update feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute(""" UPDATE Feeds_Records SET
                            Feeds_Name=:fu_name,
                            Feeds_Quantity=:f_qty,
                            Month=:monthm,
                            Year=:yuar
                        WHERE Feeds_Name=:fu_name""",
                          {
                              'fu_name': self.feeds_name_entry1.get(),
                              'f_qty': final_quantity,
                              'monthm': self.mwezi,
                              'yuar' : self.mwaka
                              })
                conn.commit()
                conn.close()
            else:
                #update feeds inventory table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute(""" UPDATE Feeds_Inventory SET
                                Feeds_Name=:f_name,
                                Quantity=:q_ty,
                                Price=:prie,
                                Month=:moth,
                                Year =:yuar,
                                DATE =:sikuku

                            WHERE Feeds_Name=:f_name""",
                                {
                                    'f_name': self.feeds_name_entry1.get(),
                                    'q_ty' : later_quantity,
                                    'prie' : cost,
                                    'moth' : self.mwezi,
                                    'yuar' : self.mwaka,
                                    'sikuku' : self.today1
                                    })
                conn.commit()
                conn.close()
                #add new record in our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Feeds_Records VALUES (:Feeds_Name, :Feeds_Quantity, :Month, :Year)",
                            {
                                'Feeds_Name': self.feeds_name_entry1.get(),
                                'Feeds_Quantity' : self.feeds_quantity_entry1.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                c.execute("SELECT * FROM Feeds_Records")
                all_feeds=c.fetchall()
                conn.commit()
                conn.close()
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_database()
            #clear entries
            self.feeds_name_entry1.delete(0,END)
            self.feeds_quantity_entry1.delete(0,END)
            messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top0)
    def pay_by_cash(self):
        #toplevel
        self.top89=Toplevel()
        self.top89.iconbitmap("logo1.ico")
        self.top89.state('zoomed')
        self.title_frame=Frame(self.top89)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="UNPAID FARMER FEEDS"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top89,border_color="maroon",border_width=5,corner_radius=8,width=900,height=650)
        self.left_frame.pack(anchor="center")
        #heading
        tender_title="PENDING FARMER FEEDS"
        self.feeds_title_label=customtkinter.CTkLabel(self.left_frame, text=tender_title, fg_color="orange", text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
        self.feeds_title_label.grid(row=0, column=0,pady=5,columnspan=10)
        #tender treeview
        self.tree_frame2=Frame(self.left_frame, highlightbackground="green", highlightthickness=5, width=500, height=500, bd=0)
        self.tree_frame2.grid(row=1, column=0, padx=30, pady=10,columnspan=10)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview_scrollbar
        self.tree_scroll2=Scrollbar(self.tree_frame2)
        self.tree_scroll2.pack(side=RIGHT, fill=Y)
        #create our treeview
        self.my_tree2=ttk.Treeview(self.tree_frame2, yscrollcommand=self.tree_scroll2.set,height=9)
        self.my_tree2.pack()
        #configure the scrollbar
        self.tree_scroll2.config(command=self.my_tree2.yview)
        #define our columns
        self.my_tree2['columns']=("First_Name","Last_Name","Farmer_ID","Feeds_Total","Transport_Fee","Total","Month","Year")
        #format our columns
        self.my_tree2.column("#0", width=0, stretch=NO)
        self.my_tree2.column("First_Name", anchor="w", width=150)
        self.my_tree2.column("Last_Name", anchor="w", width=150)
        self.my_tree2.column("Farmer_ID", anchor="w", width=150)
        self.my_tree2.column("Feeds_Total", anchor="w", width=150)
        self.my_tree2.column("Transport_Fee", anchor="w", width=150)
        self.my_tree2.column("Total", anchor="w", width=150)
        self.my_tree2.column("Month", anchor="w", width=150)
        self.my_tree2.column("Year", anchor="w", width=150)
        #create headings
        self.my_tree2.heading("#0", text="")
        self.my_tree2.heading("First_Name", text="First Name", anchor="w")
        self.my_tree2.heading("Last_Name", text="Last Name", anchor="w")
        self.my_tree2.heading("Farmer_ID", text="Farmer ID", anchor="w")
        self.my_tree2.heading("Feeds_Total", text="Feeds Total", anchor="w")
        self.my_tree2.heading("Transport_Fee", text="Transport", anchor="w")
        self.my_tree2.heading("Total", text="Total", anchor="w")
        self.my_tree2.heading("Month", text="Month", anchor="w")
        self.my_tree2.heading("Year", text="Year", anchor="w")
        #striped row tags
        self.my_tree2.tag_configure('oddrow', background="white")
        self.my_tree2.tag_configure('evenrow', background="violet")
        # binding single click
        self.my_tree2.bind("<ButtonRelease-1>", self.clicker1)
        #variable
        self.svar=StringVar()
        #frame
        self.entry_frame=Frame(self.left_frame)
        self.entry_frame.grid(row=2, column=0,columnspan=10, padx=20,pady=5)
        #entry labels
        self.farmer_id_label=customtkinter.CTkLabel(self.entry_frame,text="Farmer ID:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.farmer_id_label.grid(row=1, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.feeds_total_label=customtkinter.CTkLabel(self.entry_frame,text="Feeds Total:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.feeds_total_label.grid(row=2, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.feeds_transport_label=customtkinter.CTkLabel(self.entry_frame, text="Transport:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.feeds_transport_label.grid(row=3, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.total_cost_label=customtkinter.CTkLabel(self.entry_frame, text="Total:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.total_cost_label.grid(row=4, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.status_label=customtkinter.CTkLabel(self.entry_frame, text="Mark as Paid:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.status_label.grid(row=5, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        #entry boxes
        self.farmer_id_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.farmer_id_entry.grid(row=1, column=5)
        self.feeds_total_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.feeds_total_entry.grid(row=2, column=5)
        self.feeds_transport_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.feeds_transport_entry.grid(row=3, column=5)
        self.total_cost_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.total_cost_entry.grid(row=4, column=5)
        self.status_c=customtkinter.CTkCheckBox(self.entry_frame, text="",variable=self.svar, onvalue="PAID", offvalue="NOT PAID")
        self.status_c.deselect()
        self.status_c.grid(row=5, column=5)
        #update button
        self.update_button=customtkinter.CTkButton(self.entry_frame, text="MARK AS PAID",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=150,height=35,command=self.get_cash_amount)
        self.update_button.grid(row=6, column=0, columnspan=10, padx=20, pady=5)
        self.get_unpaid_data()
    def get_unpaid_data(self):
        #queries
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT First_Name, Last_Name, Customer_ID, SUM(Price),MONTH,YEAR FROM FEEDS WHERE Status=? GROUP BY Customer_ID,MONTH,YEAR",("NOT PAID",))
        all_unpaid=c.fetchall()
        print(all_unpaid)
        conn.commit()
        conn.close()
        for record in all_unpaid:
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=?",(record[2],"NOT PAID",))
            total_trans=c.fetchone()
            if total_trans==None:
                total_trans=0.0
            print(total_trans)
            conn.commit()
            conn.close()
            total=float(record[3])+float(total_trans) 
            #enter
            if self.count%2==0:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0],record[1], record[2],record[3],total_trans,total,record[4],record[5]), tags=("evenrow"),)
            else:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0],record[1], record[2],record[3],total_trans,total,record[4],record[5]), tags=("oddrow"),)
            self.count+=1
    #update data
    def mark_as_paid(self):
        if float(self.total_cost_entry.get())==float(self.cash_amount_entry.get()):
            #query
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.farmer_id_entry.get(),"NOT PAID",))
            all_records=c.fetchall()
            print(all_records)
            conn.commit()
            conn.close()
            for values in all_records:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("""UPDATE FEEDS SET
                            First_Name=:f_jina, 
                            Last_Name=:l_jina,
                            Customer_ID=:customerid,
                            Feed_Names=:feed_jina,
                            Feed_Quantity=:feed_amount,
                            Price=:pesa,
                            Total_Cost=:pesa_total,
                            Status=:stsz,
                            MONTH=:mhtm,
                            YEAR=:mwks,
                            DATE=:leo,
                            PERIOD=:pwd

                            WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND DATE=:leo AND PERIOD=:pwd""",
                          {
                              'f_jina':values[0],
                              'l_jina':values[1],
                              'customerid':values[2],
                              'feed_jina':values[3],
                              'feed_amount':values[4],
                              'pesa':values[5],
                              'pesa_total':values[6],
                              'stsz':"PAID",
                              'mhtm':values[8],
                              'mwks':values[9],
                              'leo':values[10],
                              'pwd':values[11]
                              })
                conn.commit()
                conn.close()
            
            #query
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=?",(self.farmer_id_entry.get(),"NOT PAID",))
            all_transport=c.fetchall()
            conn.commit()
            conn.close()
            for values in all_transport:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("""UPDATE Transport SET
                            Farmer_ID=:f_id,
                            Transport_Amount=:t_amount,
                            Status=:stus,
                            DATE=:data,
                            PERIOD=:pwd
                        
                            WHERE Farmer_ID=:f_id AND DATE=:data""",
                          {
                              'f_id':values[0],
                              't_amount':values[1],
                              'stus':"PAID",
                              'data':values[3],
                              'pwd':values[4]
                              })
                conn.commit()
                conn.close()
        else:
            balaz=float(self.cash_amount_entry.get()) - float(self.total_cost_entry.get())
            new_l=abs(balaz)
            print(new_l)
            #query
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.farmer_id_entry.get(),"NOT PAID",))
            all_records=c.fetchall()
            print(all_records)
            conn.commit()
            conn.close()
            for values in all_records:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("""UPDATE FEEDS SET
                            First_Name=:f_jina, 
                            Last_Name=:l_jina,
                            Customer_ID=:customerid,
                            Feed_Names=:feed_jina,
                            Feed_Quantity=:feed_amount,
                            Price=:pesa,
                            Total_Cost=:pesa_total,
                            Status=:stsz,
                            MONTH=:mhtm,
                            YEAR=:mwks,
                            DATE=:leo,
                            PERIOD=:pwd

                            WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND DATE=:leo AND PERIOD=:pwd""",
                          {
                              'f_jina':values[0],
                              'l_jina':values[1],
                              'customerid':values[2],
                              'feed_jina':values[3],
                              'feed_amount':values[4],
                              'pesa':values[5],
                              'pesa_total':values[6],
                              'stsz':"PAID",
                              'mhtm':values[8],
                              'mwks':values[9],
                              'leo':values[10],
                              'pwd':values[11]
                              })
                conn.commit()
                conn.close()
            
            #query
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=?",(self.farmer_id_entry.get(),"NOT PAID",))
            all_transport=c.fetchall()
            conn.commit()
            conn.close()
            for values in all_transport:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("""UPDATE Transport SET
                            Farmer_ID=:f_id,
                            Transport_Amount=:t_amount,
                            Status=:stus,
                            DATE=:data,
                            PERIOD=:pwd
                        
                            WHERE Farmer_ID=:f_id AND DATE=:data""",
                          {
                              'f_id':values[0],
                              't_amount':values[1],
                              'stus':"PAID",
                              'data':values[3],
                              'pwd':values[4]
                              })
                conn.commit()
                conn.close()
            #loans
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=?",(self.farmer_id_entry.get(),"NOT PAID",))
            record=c.fetchone()
            print(record)
            conn.commit()
            conn.close()
            if record==None:
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=?",(self.farmer_id_entry.get(),))
                results=c.fetchone()
                print(results)
                conn.commit()
                conn.close()
                if self.now_day<=15:
                    #
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                {
                                    'Customer_ID':self.farmer_id_entry.get(),
                                    'First_Name':results[0],
                                    'Last_Name':results[1],
                                    'Pending_Loan':0.0,
                                    'Loan_Amount':new_l,
                                    'Total_Loan':new_l,
                                    'STATUS':"NOT PAID",
                                    'MONTH':self.mwezi,
                                    'YEAR':self.mwaka,
                                    'DATE':self.today1,
                                    'PERIOD':"From 1-15"
                                    })
                    conn.commit()
                    conn.close()
                else:
                    #
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                {
                                    'Customer_ID':self.farmer_id_entry.get(),
                                    'First_Name':results[0],
                                    'Last_Name':results[1],
                                    'Pending_Loan':0.0,
                                    'Loan_Amount':new_l,
                                    'Total_Loan':new_l,
                                    'STATUS':"NOT PAID",
                                    'MONTH':self.mwezi,
                                    'YEAR':self.mwaka,
                                    'DATE':self.today1,
                                    'PERIOD':"From 16"
                                    })
                    conn.commit()
                    conn.close()
            else:
                if self.now_day<=15:
                    new_loan=record[5] + new_l
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("""UPDATE LOANS SET
                                Customer_ID=:c_id,
                                First_Name=:f_name,
                                Last_Name=:l_name,
                                Pending_Loan=:pen_l,
                                Loan_Amount=:lamount,
                                Total_Loan=:t_loan,
                                STATUS=:stxz,
                                MONTH=:mnth,
                                YEAR=:raey,
                                DATE=:date,
                                PERIOD=:pwd
                                
                                WHERE Customer_ID=:c_id AND PERIOD=:pwd""",
                                {
                                    'c_id': record[0],
                                    'f_name': record[1],
                                    'l_name': record[2],
                                    'pen_l':record[3],
                                    'lamount':new_l,
                                    't_loan':new_loan,
                                    'stxz':"NOT PAID",
                                    'mnth':record[7],
                                    'raey':record[8],
                                    'date':record[9],
                                    'pwd':"From 1-15"
                                    })
                    conn.commit()
                    conn.close()
                else:
                    new_loan=record[5] + new_l
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("""UPDATE LOANS SET
                                Customer_ID=:c_id,
                                First_Name=:f_name,
                                Last_Name=:l_name,
                                Pending_Loan=:pen_l,
                                Loan_Amount=:lamount,
                                Total_Loan=:t_loan,
                                STATUS=:stxz,
                                MONTH=:mnth,
                                YEAR=:raey,
                                DATE=:date,
                                PERIOD=:pwd
                                
                                WHERE Customer_ID=:c_id AND PERIOD=:pwd""",
                                {
                                    'c_id': record[0],
                                    'f_name': record[1],
                                    'l_name': record[2],
                                    'pen_l':record[3],
                                    'lamount':new_l,
                                    't_loan':new_loan,
                                    'stxz':"NOT PAID",
                                    'mnth':record[7],
                                    'raey':record[8],
                                    'date':record[9],
                                    'pwd':"From 16"
                                    })
                    conn.commit()
                    conn.close()
        #clear entries
        self.farmer_id_entry.delete(0,END)
        self.feeds_total_entry.delete(0,END)
        self.feeds_transport_entry.delete(0,END)
        self.total_cost_entry.delete(0,END)
        messagebox.showinfo("Bravo","Record Updated Succesfully",parent=self.top89)
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.get_unpaid_data()
        self.top55.destroy()
    def get_cash_amount(self):
        self.top55=Toplevel()
        self.top55.iconbitmap("logo1.ico")
        self.top55.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top55)
        my_frame.pack()
        self.cash_label=customtkinter.CTkLabel(my_frame,text="Cash Received:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.cash_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
        self.cash_amount_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
        self.cash_amount_entry.grid(row=1,column=2,columnspan=2,padx=5)
        self.save_button=customtkinter.CTkButton(my_frame,text="MARK",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.mark_as_paid)
        self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20)
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
class Customer_Payments:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x1000")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
         #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)
        
        notifications_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Notifications", menu=notifications_menu)
        notifications_menu.add_command(label="Notify Farmers",command=self.select_notify_month)
        
        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="MONTHLY PAYMENTS"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #variables
        self.currentDateTime=date.today()
        self.today1=self.currentDateTime.strftime("%A-%B %d, %Y")
        self.time=datetime.now()
        self.today=self.time.strftime("%m/%d/%Y")
        self.today2=self.time.strftime("%d/%m/%Y")
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.t_day=datetime.now().day
        self.t_month=datetime.now().month
        self.th_month=datetime.now().month+ 1
        print(self.th_month)
        if self.th_month==13:
            self.th_month = 1
        print(self.th_month)
        self.mwaka=datetime.now().year
        self.count=0
        self.st="PAID"
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top0,border_color="green",border_width=5, width=400, height=400)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #heading
        header="CASH MODE USERS"
        self.cash_title_label=customtkinter.CTkLabel(self.left_frame, text= header, fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"underline", "bold"),width=200,height=25)
        self.cash_title_label.grid(row=0, column=0, columnspan=12,pady=5)
        
        #labels
        self.today_label=customtkinter.CTkLabel(self.left_frame, text="Today:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.today_label.grid(row=1, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.date_label=customtkinter.CTkLabel(self.left_frame,text=self.today1)
        self.date_label.grid(row=1, column=6,columnspan=3)
        self.set_rate_label=customtkinter.CTkLabel(self.left_frame, text="Set Payment Rate(Kshs)",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.set_rate_label.grid(row=2, column=0,pady=5,columnspan=6,sticky=EW,padx=30)
        self.choose_month_label=customtkinter.CTkLabel(self.left_frame, text="Choose Month:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.choose_month_label.grid(row=3, column=0,columnspan=6,sticky=EW,padx=30, pady=2)
        self.customer_id_label=customtkinter.CTkLabel(self.left_frame, text="Enter Farmer's ID:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.customer_id_label.grid(row=4, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.first_name_label=customtkinter.CTkLabel(self.left_frame, text="First Name:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.first_name_label.grid(row=5, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.last_name_label=customtkinter.CTkLabel(self.left_frame, text="Last Name:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.last_name_label.grid(row=6, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.monthly_total_label=customtkinter.CTkLabel(self.left_frame, text="Total Quantity:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.monthly_total_label.grid(row=7, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.payment_mode_label=customtkinter.CTkLabel(self.left_frame, text="Payment Method:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.payment_mode_label.grid(row=8, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.status_label=customtkinter.CTkLabel(self.left_frame, text="Status:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.status_label.grid(row=9, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.payment_rate_label=customtkinter.CTkLabel(self.left_frame, text="Monthly Rate:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.payment_rate_label.grid(row=10, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.monthly_wages_label=customtkinter.CTkLabel(self.left_frame, text="Monthly Wages:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.monthly_wages_label.grid(row=11, column=0,padx=30,pady=2,columnspan=6,sticky=EW)
        self.pending_loan_label=customtkinter.CTkLabel(self.left_frame, text="Pending Advance:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.pending_loan_label.grid(row=12, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.pending_feeds_label=customtkinter.CTkLabel(self.left_frame, text="Pending Feeds Credit:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.pending_feeds_label.grid(row=13, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.transport_fee_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Transport Fee:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.transport_fee_label.grid(row=14, column=0,padx=30, pady=2,columnspan=6,sticky=EW)
        self.balance_label=customtkinter.CTkLabel(self.left_frame, text="Balance:",fg_color="brown", text_color="white",text_font=("Consollas 10", -15, "bold"),width=150,height=25)
        self.balance_label.grid(row=15, column=0,padx=30, pady=2,columnspan=6,sticky=EW)

        #entry boxes
        self.set_rate_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.set_rate_entry.grid(row=2, column=6,columnspan=3)
        self.customer_id_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.customer_id_entry.grid(row=4,column=6,columnspan=3)
        self.first_name_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.first_name_entry.grid(row=5,column=6,columnspan=3)
        self.last_name_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.last_name_entry.grid(row=6,column=6,columnspan=3)
        self.monthly_total_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.monthly_total_entry.grid(row=7,column=6,columnspan=3)
        self.payment_mode_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.payment_mode_entry.grid(row=8,column=6,columnspan=3)
        self.status_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.status_entry.grid(row=9,column=6,columnspan=3)
        self.payment_rate_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.payment_rate_entry.grid(row=10,column=6,columnspan=3)
        self.monthly_wages_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.monthly_wages_entry.grid(row=11,column=6,columnspan=3)
        self.pending_loan_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.pending_loan_entry.grid(row=12,column=6,columnspan=3)
        self.pending_feeds_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.pending_feeds_entry.grid(row=13,column=6,columnspan=3)
        self.transport_fee_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.transport_fee_entry.grid(row=14,column=6,columnspan=3)
        self.balance_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="green")
        self.balance_entry.grid(row=15,column=6,columnspan=3)
        #buttons
        self.confirm_button=customtkinter.CTkButton(self.left_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=170, height=25,command=self.get_details)
        self.confirm_button.grid(row=4, column=10, padx=10,pady=2)
        self.pay_button=customtkinter.CTkButton(self.left_frame, text="Pay Customer",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=250, height=35,command=self.pay_customer)
        self.pay_button.grid(row=16, column=0, columnspan=12,sticky=EW, padx=30, pady=5, ipadx=80)
        #dropdown menu
        self.clicked=StringVar()
        self.clicked1=StringVar()
        self.month_chooser=StringVar()
        self.chagua_mwaka=StringVar()
        self.year_choser=StringVar()
        self.period_chooser=StringVar()
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        years=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}']
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.clicked,values=months,fg_color="red",text_color="white",width=150,height=25,command=self.select_month)
        self.choose_month_menu.grid(row=3, column=6,columnspan=2,sticky=EW)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.year_choser,values=years,fg_color="red",text_color="white",width=150,height=25)
        self.choose_year_menu.grid(row=3, column=8,columnspan=2,padx=10)
        #*******************************************************************************************************************************************************************************
        #variables
        self.choose=StringVar()
        self.chooser=StringVar()
        self.year_chooser=StringVar()
        #database
        conn=sqlite3.connect("samaria database.db")
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT BANK_NAME FROM BANK_NAMES")
        banks=c.fetchall()
        conn.commit()
        conn.close()
        #center frame
        self.center_frame=customtkinter.CTkFrame(self.top0,border_color="maroon",border_width=5, width=400, height=400)
        self.center_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #header
        header1="BANK MODE USERS"
        self.bank_title_label=customtkinter.CTkLabel(self.center_frame, text= header1, fg_color="orange", text_color="white", text_font=("Consollas 10", -20,"underline","bold"),width=200,height=20)
        self.bank_title_label.grid(row=0, column=0, columnspan=18,pady=10)
        #labels
        self.t1=StringVar()
        self.set_rate_label1=customtkinter.CTkLabel(self.center_frame, text="Set Monthly Rate(Kshs):",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=200,height=30)
        self.set_rate_label1.grid(row=1, column=0,columnspan=6,padx=30,pady=10,sticky=EW)
        self.set_rate_entry1=customtkinter.CTkEntry(self.center_frame,width=150,height=30,border_color="green")
        self.set_rate_entry1.grid(row=1, column=6,columnspan=3)
        self.choose_month_label1=customtkinter.CTkLabel(self.center_frame, text="Choose Month:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=150,height=30)
        self.choose_month_label1.grid(row=2, column=0,padx=30,pady=10,columnspan=6,sticky=EW)
        #dropdown menu
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.center_frame,variable=self.choose,values=months,fg_color="red",text_color="white",width=150,height=30,command=self.choose_month)
        self.choose_month_menu.grid(row=2, column=6,columnspan=2)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.center_frame,variable=self.year_chooser,values=years,fg_color="red",text_color="white",width=150,height=30,command=self.choose_month)
        self.choose_year_menu.grid(row=2, column=8,columnspan=2)
        self.pay_bank_button=customtkinter.CTkButton(self.center_frame, text="Pay Customers",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40,command=self.pay_bankers)
        self.pay_bank_button.grid(row=3, column=0, columnspan=12,padx=30,pady=20,ipadx=50,sticky=EW)
        #***********************************************************************************************************************************************************************
        #variables
        self.t2=StringVar()
        self.year_choose=StringVar()
        self.chagua=StringVar()
        self.clicked2=StringVar()
        #mpesa
        header2="M~PESA MODE USERS"
        self.mpesa_title_label=customtkinter.CTkLabel(self.center_frame, text= header2, fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"underline","bold"),width=200,height=30)
        self.mpesa_title_label.grid(row=5, column=0, columnspan=18,pady=10)
        #labels
        self.set_rate_label2=customtkinter.CTkLabel(self.center_frame, text="Set Monthly Rate(Kshs):", fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=200, height=20)
        self.set_rate_label2.grid(row=6, column=0,columnspan=6,padx=30,pady=10,sticky=EW)
        self.set_rate_entry2=customtkinter.CTkEntry(self.center_frame, width=150,height=25,border_color="green")
        self.set_rate_entry2.grid(row=6, column=6,columnspan=3)
        self.choose_month_label2=customtkinter.CTkLabel(self.center_frame, text="Choose Month:", fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=150, height=30)
        self.choose_month_label2.grid(row=7, column=0,columnspan=6,padx=30,pady=10,sticky=EW)
        #menu
        self.chagua_month_menu=customtkinter.CTkOptionMenu(self.center_frame,variable=self.chagua,values=months,fg_color="red",text_color="white",width=150,height=30,command=self.chagua_month)
        self.chagua_month_menu.grid(row=7, column=6,columnspan=2)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.center_frame,variable=self.year_choose,values=years,fg_color="red",text_color="white",width=150,height=30,command=self.choose_month)
        self.choose_year_menu.grid(row=7, column=8,columnspan=2,padx=10)
        self.pay_mpesa_button=customtkinter.CTkButton(self.center_frame, text="M~pesa Payment Details",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=self.mpesa_details)
        self.pay_mpesa_button.grid(row=8, column=0, columnspan=12,padx=30, pady=20,ipadx=50,sticky=EW)
        #payment table
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        '''
        #drop table
        c.execute("DROP TABLE Payments")
        print("table dropped successfully")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS Payments(
                      FIRST_NAME TEXT NOT NULL,
                      LAST_NAME TEXT NOT NULL,
                      CUSTOMER_ID INT NOT NULL,
                      PERIOD TEXT NOT NULL,
                      MONTHLY_TOTAL REAL NOT NULL,
                      MONTHLY_RATE REAL NOT NULL,
                      STATUS TEXT NOT NULL,
                      MONTHLY_WAGES REAL NOT NULL,
                      PENDING_LOAN REAL NOT NULL,
                      PENDING_FEEDS REAL NOT NULL,
                      Transport_Fee REAL NOT NULL,
                      REMAINING_BALANCE REAL NOT NULL,
                      MONTH INT NOT NULL,
                      YEAR INT NOT NULL,
                      DATE INT NOT NULL
                      )""")
        conn.commit()
        conn.close()
    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    #clear entries
    def clear_entries(self):
            self.set_rate_entry.delete(0, END)
            self.customer_id_entry.delete(0, END)
            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.monthly_total_entry.delete(0, END)
            self.payment_mode_entry.delete(0, END)
            self.status_entry.delete(0, END)
            self.payment_rate_entry.delete(0, END)
            self.monthly_wages_entry.delete(0, END)
            self.pending_loan_entry.delete(0, END)
            self.pending_feeds_entry.delete(0, END)
            self.transport_fee_entry.delete(0,END)
            self.balance_entry.delete(0, END)
    #get details
    def select_month(self,arg=None):
        if self.clicked.get()=="January":
            self.mwezi=1
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="February":
            self.mwezi=2
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="March":
            self.mwezi=3
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="April":
            self.mwezi=4
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="May":
            self.mwezi=5
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="June":
            self.mwezi=6
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="July":
            self.mwezi=7
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="August":
            self.mwezi=8
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="September":
            self.mwezi=9
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="October":
            self.mwezi=10
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="November":
            self.mwezi=11
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
        if self.clicked.get()=="December":
            self.mwezi=12
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.select_period()
    #select period
    def select_period(self):
        self.top98=Toplevel()
        self.top98.title("SAMARIA MILK GROUP")
        self.top98.iconbitmap("logo1.ico")
        top_frame=Frame(self.top98)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT Period:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.clicked1,command=self.close_period,values=[f'From 1-15',f'From 16-{self.last_day}'],width=160,height=25,fg_color="red",text_color="white")
        mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def close_period(self,e):
        get_period=self.clicked1.get()
        #print(get_period)
        self.top98.destroy()
        
    def get_details(self):
        #payment rate
        self.rate= self.set_rate_entry.get()
        if self.rate=="":
            messagebox.showerror("ERROR", "Please set monthly payment Rate",parent=self.top0)
        elif self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "Please enter the Farmer's ID",parent=self.top0)
        elif self.clicked.get()=="":
            messagebox.showerror("ERROR","Please Choose Month",parent=self.top0)
        elif self.clicked1.get()=="":
            messagebox.showerror("ERROR","Please Choose Period",parent=self.top0)
        elif self.year_choser.get()=="":
            messagebox.showerror("ERROR","Please Choose Year",parent=self.top0)
        else:
            self.payment_rate_entry.delete(0,END)
            self.payment_rate_entry.insert(0, self.rate)
            #names
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
            self.names=c.fetchall()
            self.first_name=''
            self.last_name=''
            for record in self.names:
                self.first_name= record[0]
                self.last_name= record[1]
            self.first_name_entry.delete(0,END)
            self.last_name_entry.delete(0,END)
            self.first_name_entry.insert(0, self.first_name)
            self.last_name_entry.insert(0, self.last_name)
            conn.commit()
            conn.close()
            if self.clicked1.get()=="From 1-15":
                try:
                    #monthly_totals
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]# AND DAY BETWEEN 1 AND 15
                    c=conn.cursor()
                    c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 1 AND 15",(self.mwezi, self.year_choser.get(), self.customer_id_entry.get(),))
                    self.accumulated_monthly=c.fetchone()
                    if self.accumulated_monthly==None:
                        self.accumulated_monthly=0.0
                    self.monthly_total_entry.delete(0,END)
                    self.monthly_total_entry.insert(0, self.accumulated_monthly)
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showerror("ERROR", "Please Choose Month",parent =self.top0)
                #payment mode
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Payment_mode FROM Customers WHERE Customer_ID="+self.customer_id_entry.get())
                self.p_mode=c.fetchone()
                #print(self.p_mode)
                self.payment_mode_entry.delete(0,END)
                self.payment_mode_entry.insert(0, self.p_mode)
                conn.commit()
                conn.close()
                #status
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND PERIOD=?",(self.mwezi, self.year_choser.get(), self.customer_id_entry.get(),self.clicked1.get(),))
                self.ifpaid=c.fetchone()
                #print(self.ifpaid)
                if self.ifpaid==None:
                    self.status="NOT PAID"
                else:
                    self.status=self.ifpaid
                self.status_entry.delete(0,END)
                self.status_entry.insert(0, self.status)
                #monthly wages
                self.total_wages= (self.accumulated_monthly * float(self.rate))
                #print(self.total_wages)
                self.monthly_wages_entry.delete(0,END)
                self.monthly_wages_entry.insert(0, self.total_wages)
                conn.commit()
                conn.close()
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Total_Loan) FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                self.p_loan=c.fetchone()
                if self.p_loan==None:
                    self.p_loan=0.0
                #print(self.p_loan)
                self.pending_loan_entry.delete(0,END)
                self.pending_loan_entry.insert(0, self.p_loan)
                conn.commit()
                conn.close()
                #feeds
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                self.feeds=c.fetchall()
                #print(self.feeds)
                self.p_feeds=0.0
                if self.feeds==[]:
                    self.p_feeds=0.0
                else:
                    for x in self.feeds:
                        self.p_feeds+=x
                #print(self.feeds)
                #print(self.p_feeds)
                conn.commit()
                conn.close()
                self.pending_feeds_entry.delete(0,END)
                self.pending_feeds_entry.insert(0, self.p_feeds)
                #transport fee
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                self.transport_fee=c.fetchone()
                if self.transport_fee==None:
                    self.transport_fee=0.0
                conn.commit()
                conn.close()
                self.transport_fee_entry.delete(0, END)
                self.transport_fee_entry.insert(0, self.transport_fee)
                #balance
                self.bal=(self.total_wages - (self.p_loan+ self.p_feeds+self.transport_fee))
                #print(self.bal)
                self.balance_entry.delete(0,END)
                self.balance_entry.insert(0, self.bal)

            else:
                try:
                    #monthly_totals
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 16 AND 'self.last_day'",(self.mwezi, self.year_choser.get(), self.customer_id_entry.get(),))
                    self.accumulated_monthly=c.fetchone()
                    if self.accumulated_monthly==None:
                        self.accumulated_monthly=0.0
                    self.monthly_total_entry.delete(0,END)
                    self.monthly_total_entry.insert(0, self.accumulated_monthly)
                    conn.commit()
                    conn.close()
                except:
                    messagebox.showerror("ERROR", "Please Choose Month",parent =self.top0)
                #payment mode
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Payment_mode FROM Customers WHERE Customer_ID="+self.customer_id_entry.get())
                self.p_mode=c.fetchone()
                #print(self.p_mode)
                self.payment_mode_entry.delete(0,END)
                self.payment_mode_entry.insert(0, self.p_mode)
                conn.commit()
                conn.close()
                #status
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND PERIOD=?",(self.mwezi, self.year_choser.get(), self.customer_id_entry.get(),self.clicked1.get(),))
                self.ifpaid=c.fetchone()
                #print(self.ifpaid)
                if self.ifpaid==None:
                    self.status="NOT PAID"
                else:
                    self.status=self.ifpaid
                self.status_entry.delete(0,END)
                self.status_entry.insert(0, self.status)
                #monthly wages
                self.total_wages= (self.accumulated_monthly * float(self.rate))
                #print(self.total_wages)
                self.monthly_wages_entry.delete(0,END)
                self.monthly_wages_entry.insert(0, self.total_wages)
                conn.commit()
                conn.close()
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Total_Loan) FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                self.p_loan=c.fetchone()
                if self.p_loan==None:
                    self.p_loan=0.0
                #print(self.p_loan)
                self.pending_loan_entry.delete(0,END)
                self.pending_loan_entry.insert(0, self.p_loan)
                conn.commit()
                conn.close()
                #feeds
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                self.feeds=c.fetchall()
                #print(self.feeds)
                self.p_feeds=0.0
                if self.feeds==[]:
                    self.p_feeds=0.0
                else:
                    for x in self.feeds:
                        self.p_feeds+=x
                #print(self.feeds)
                #print(self.p_feeds)
                conn.commit()
                conn.close()
                self.pending_feeds_entry.delete(0,END)
                self.pending_feeds_entry.insert(0, self.p_feeds)
                #transport fee
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                self.transport_fee=c.fetchone()
                if self.transport_fee==None:
                    self.transport_fee=0.0
                conn.commit()
                conn.close()
                self.transport_fee_entry.delete(0, END)
                self.transport_fee_entry.insert(0, self.transport_fee)
                #balance
                self.bal=(self.total_wages - (self.p_loan+ self.p_feeds+self.transport_fee))
                #print(self.bal)
                self.balance_entry.delete(0,END)
                self.balance_entry.insert(0, self.bal)
    def verify_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_p=c.fetchone()
        conn.commit()
        conn.close()
        if admin_p!=self.admin_passcode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Admin Password, Check Password And Try Again",parent =self.top0)
            self.admin_passcode_entry.delete(0, END)
            self.top1.destroy()
        else:
            self.admin_passcode_entry.delete(0, END)
            self.top1.destroy()
            if float(self.bal)<0.0:
                balaz=0.0
                if self.clicked1.get()=="From 1-15":
                    #insert our details to database
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                {
                                    'FIRST_NAME': self.first_name,
                                    'LAST_NAME': self.last_name,
                                    'CUSTOMER_ID': self.customer_id_entry.get(),
                                    'PERIOD':self.clicked1.get(),
                                    'MONTHLY_TOTAL': self.accumulated_monthly,
                                    'MONTHLY_RATE': self.rate,
                                    'STATUS': self.st,
                                    'MONTHLY_WAGES': self.total_wages,
                                    'PENDING_LOAN': self.p_loan,
                                    'PENDING_FEEDS': self.p_feeds,
                                    'Transport_Fee': self.transport_fee,
                                    'REMAINING_BALANCE':balaz,
                                    'MONTH': self.mwezi,
                                    'YEAR': self.year_choser.get(),
                                    'DATE': self.today
                                    })
                    conn.commit()
                    conn.close()
                    #update transport table
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    all_transport=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in all_transport:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE Transport SET
                                    Farmer_ID=:f_id,
                                    Transport_Amount=:t_amount,
                                    Status=:stus,
                                    DATE=:siku,
                                    PERIOD=:pds

                                    WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pds""",
                                  {
                                      'f_id':record[0],
                                      't_amount':record[1],
                                      'stus':"PAID",
                                      'siku':record[3],
                                      'pds':record[4]
                                      })
                        conn.commit()
                        conn.close()
                    #update feeds table
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    unpaid_feeds=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in unpaid_feeds:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE FEEDS SET
                                    First_Name=:f_jina, 
                                    Last_Name=:l_jina,
                                    Customer_ID=:customerid,
                                    Feed_Names=:feed_jina,
                                    Feed_Quantity=:feed_amount,
                                    Price=:pesa,
                                    Total_Cost=:pesa_total,
                                    Status=:stsz,
                                    MONTH=:mhtm,
                                    YEAR=:mwks,
                                    DATE=:leo,
                                    PERIOD=:pwds

                                    WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwds""",
                                  {
                                      'f_jina':record[0],
                                      'l_jina':record[1],
                                      'customerid':self.customer_id_entry.get(),
                                      'feed_jina':record[3],
                                      'feed_amount':record[4],
                                      'pesa':record[5],
                                      'pesa_total':record[6],
                                      'stsz':"PAID",
                                      'mhtm':record[8],
                                      'mwks':record[9],
                                      'leo':record[10],
                                      'pwds':record[11]
                                      })
                        conn.commit()
                        conn.close()
                    #update loans table
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    record=c.fetchone()
                    conn.commit()
                    conn.close()
                    if record!=None:
                        #update
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE LOANS SET
                                    Customer_ID=:c_id,
                                    First_Name=:f_name,
                                    Last_Name=:l_name,
                                    Pending_Loan=:pen_l,
                                    Loan_Amount=:lamount,
                                    Total_Loan=:t_loan,
                                    STATUS=:stxz,
                                    MONTH=:mnth,
                                    YEAR=:raey,
                                    DATE=:date,
                                    PERIOD=:prd
                                
                                    WHERE Customer_ID=:c_id AND PERIOD=:prd""",
                                    {
                                        'c_id': record[0],
                                        'f_name': record[1],
                                        'l_name': record[2],
                                        'pen_l':0.0,
                                        'lamount':0.0,
                                        't_loan':0.0,
                                        'stxz':"PAID",
                                        'mnth':record[7],
                                        'raey':record[8],
                                        'date':record[9],
                                        'prd':record[10]
                                        })
                        conn.commit()
                        conn.close()
                    #insert
                    new_l=abs(self.bal)
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                {
                                    'Customer_ID':self.customer_id_entry.get(),
                                    'First_Name':self.first_name_entry.get(),
                                    'Last_Name':self.last_name_entry.get(),
                                    'Pending_Loan':0.0,
                                    'Loan_Amount':new_l,
                                    'Total_Loan':new_l,
                                    'STATUS':"NOT PAID",
                                    'MONTH':self.mwezi,
                                    'YEAR':self.mwaka,
                                    'DATE':self.today,
                                    'PERIOD':"From 16"
                                    })
                    conn.commit()
                    conn.close()
                    '''
                    else:
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                  {
                                      'Customer_ID':self.customer_id_entry.get(),
                                      'First_Name':self.first_name_entry.get(),
                                      'Last_Name':self.last_name_entry.get(),
                                      'Pending_Loan':0.0,
                                      'Loan_Amount':new_l,
                                      'Total_Loan':new_l,
                                      'STATUS':"NOT PAID",
                                      'MONTH':self.t_month,
                                      'YEAR':self.mwaka,
                                      'DATE':self.today,
                                      'PERIOD':"From 16"
                                      })
                        conn.commit()
                        conn.close()
                        '''
                    self.receipt()
                else:
                    #
                    self.n_month = self.mwezi + 1
                    print(self.n_month)
                    if self.n_month==13:
                        self.n_month = 1
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT STATUS FROM Payments WHERE PERIOD=? AND MONTH=? AND YEAR=? AND CUSTOMER_ID=?",("From 1-15",self.mwezi,self.year_choser.get(),self.customer_id_entry.get(),))
                    check_s=c.fetchone()
                    print(check_s)
                    conn.commit()
                    conn.close()
                    if check_s==None:
                        messagebox.showerror("ERROR","Farmer Not Paid From 1-15,First Pay to Proceed",parent=self.top0)
                        self.clear_entries()
                    else:
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.first_name,
                                        'LAST_NAME': self.last_name,
                                        'CUSTOMER_ID': self.customer_id_entry.get(),
                                        'PERIOD':self.clicked1.get(),
                                        'MONTHLY_TOTAL': self.accumulated_monthly,
                                        'MONTHLY_RATE': self.rate,
                                        'STATUS': self.st,
                                        'MONTHLY_WAGES': self.total_wages,
                                        'PENDING_LOAN': self.p_loan,
                                        'PENDING_FEEDS': self.p_feeds,
                                        'Transport_Fee': self.transport_fee,
                                        'REMAINING_BALANCE':balaz,
                                        'MONTH': self.mwezi,
                                        'YEAR': self.year_choser.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pds

                                        WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pds""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pds':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:pwds

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwds""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.customer_id_entry.get(),
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'pwds':record[11]
                                          })
                            conn.commit()
                            conn.close()

                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        record=c.fetchone()
                        conn.commit()
                        conn.close()
                        if record!=None:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:prd
                                    
                                        WHERE Customer_ID=:c_id AND PERIOD=:prd""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'prd':record[10]
                                            })
                            conn.commit()
                            conn.close()
                        #insert
                        new_l=abs(self.bal)
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                    {
                                        'Customer_ID':self.customer_id_entry.get(),
                                        'First_Name':self.first_name_entry.get(),
                                        'Last_Name':self.last_name_entry.get(),
                                        'Pending_Loan':0.0,
                                        'Loan_Amount':new_l,
                                        'Total_Loan':new_l,
                                        'STATUS':"NOT PAID",
                                        'MONTH':self.n_month,
                                        'YEAR':self.mwaka,
                                        'DATE':self.today,
                                        'PERIOD':"From 1-15"
                                        })
                        conn.commit()
                        conn.close()
                        '''
                        else:
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                      {
                                          'Customer_ID':self.customer_id_entry.get(),
                                          'First_Name':self.first_name_entry.get(),
                                          'Last_Name':self.last_name_entry.get(),
                                          'Pending_Loan':0.0,
                                          'Loan_Amount':new_l,
                                          'Total_Loan':new_l,
                                          'STATUS':"NOT PAID",
                                          'MONTH':self.t_month,
                                          'YEAR':self.mwaka,
                                          'DATE':self.today,
                                          'PERIOD':"From 16"
                                          })
                            conn.commit()
                            conn.close()
                            '''
                        self.receipt()

            else:
                if self.clicked1.get()=="From 1-15":
                    #insert our details to database
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                {
                                    'FIRST_NAME': self.first_name,
                                    'LAST_NAME': self.last_name,
                                    'CUSTOMER_ID': self.customer_id_entry.get(),
                                    'PERIOD':self.clicked1.get(),
                                    'MONTHLY_TOTAL': self.accumulated_monthly,
                                    'MONTHLY_RATE': self.rate,
                                    'STATUS': self.st,
                                    'MONTHLY_WAGES': self.total_wages,
                                    'PENDING_LOAN': self.p_loan,
                                    'PENDING_FEEDS': self.p_feeds,
                                    'Transport_Fee': self.transport_fee,
                                    'REMAINING_BALANCE':self.bal,
                                    'MONTH': self.mwezi,
                                    'YEAR': self.year_choser.get(),
                                    'DATE': self.today
                                    })
                    conn.commit()
                    conn.close()
                    #update transport table
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    all_transport=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in all_transport:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE Transport SET
                                    Farmer_ID=:f_id,
                                    Transport_Amount=:t_amount,
                                    Status=:stus,
                                    DATE=:siku,
                                    PERIOD=:pwd

                                    WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwd""",
                                  {
                                      'f_id':record[0],
                                      't_amount':record[1],
                                      'stus':"PAID",
                                      'siku':record[3],
                                      'pwd':record[4]
                                      })
                        conn.commit()
                        conn.close()
                    #update feeds table
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    unpaid_feeds=c.fetchall()
                    conn.commit()
                    conn.close()
                    for record in unpaid_feeds:
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE FEEDS SET
                                    First_Name=:f_jina, 
                                    Last_Name=:l_jina,
                                    Customer_ID=:customerid,
                                    Feed_Names=:feed_jina,
                                    Feed_Quantity=:feed_amount,
                                    Price=:pesa,
                                    Total_Cost=:pesa_total,
                                    Status=:stsz,
                                    MONTH=:mhtm,
                                    YEAR=:mwks,
                                    DATE=:leo,
                                    PERIOD=:pwds

                                    WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwds""",
                                  {
                                      'f_jina':record[0],
                                      'l_jina':record[1],
                                      'customerid':self.customer_id_entry.get(),
                                      'feed_jina':record[3],
                                      'feed_amount':record[4],
                                      'pesa':record[5],
                                      'pesa_total':record[6],
                                      'stsz':"PAID",
                                      'mhtm':record[8],
                                      'mwks':record[9],
                                      'leo':record[10],
                                      'pwds':record[11]
                                      })
                        conn.commit()
                        conn.close()

                    #update loans table
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                    record=c.fetchone()
                    conn.commit()
                    conn.close()
                    if record!=None:
                        #update
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("""UPDATE LOANS SET
                                    Customer_ID=:c_id,
                                    First_Name=:f_name,
                                    Last_Name=:l_name,
                                    Pending_Loan=:pen_l,
                                    Loan_Amount=:lamount,
                                    Total_Loan=:t_loan,
                                    STATUS=:stxz,
                                    MONTH=:mnth,
                                    YEAR=:raey,
                                    DATE=:date,
                                    PERIOD=:prd
                                
                                    WHERE Customer_ID=:c_id AND PERIOD=:prd""",
                                    {
                                        'c_id': record[0],
                                        'f_name': record[1],
                                        'l_name': record[2],
                                        'pen_l':0.0,
                                        'lamount':0.0,
                                        't_loan':0.0,
                                        'stxz':"PAID",
                                        'mnth':record[7],
                                        'raey':record[8],
                                        'date':record[9],
                                        'prd':record[10]
                                        })
                        conn.commit()
                        conn.close()
                    self.receipt()
                else:
                    #
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT STATUS FROM Payments WHERE PERIOD=? AND MONTH=? AND YEAR=? AND CUSTOMER_ID=?",("From 1-15",self.mwezi,self.year_choser.get(),self.customer_id_entry.get(),))
                    check_s=c.fetchone()
                    print(check_s)
                    conn.commit()
                    conn.close()
                    if check_s==None:
                        messagebox.showerror("ERROR","Farmer Not Paid From 1-15,First Pay to Proceed",parent=self.top0)
                        self.clear_entries()
                    else:
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.first_name,
                                        'LAST_NAME': self.last_name,
                                        'CUSTOMER_ID': self.customer_id_entry.get(),
                                        'PERIOD':self.clicked1.get(),
                                        'MONTHLY_TOTAL': self.accumulated_monthly,
                                        'MONTHLY_RATE': self.rate,
                                        'STATUS': self.st,
                                        'MONTHLY_WAGES': self.total_wages,
                                        'PENDING_LOAN': self.p_loan,
                                        'PENDING_FEEDS': self.p_feeds,
                                        'Transport_Fee': self.transport_fee,
                                        'REMAINING_BALANCE':self.bal,
                                        'MONTH': self.mwezi,
                                        'YEAR': self.year_choser.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pwd

                                        WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwd""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pwd':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:pwds

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwds""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.customer_id_entry.get(),
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'pwds':record[11]
                                          })
                            conn.commit()
                            conn.close()
                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                        record=c.fetchone()
                        conn.commit()
                        conn.close()
                        if record!=None:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:prd
                                    
                                        WHERE Customer_ID=:c_id AND PERIOD=:prd""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'prd':record[10]
                                            })
                            conn.commit()
                            conn.close()
                        self.receipt()
    def pay_customer(self):
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
        else:
            #check
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND PERIOD=?",(self.mwezi, self.year_choser.get(), self.customer_id_entry.get(),self.clicked1.get(),))
            check=c.fetchone()
            c.execute("SELECT Payment_mode FROM Customers WHERE Customer_ID="+self.customer_id_entry.get())
            pay_mode=c.fetchone()
            conn.commit()
            conn.close()
            if check=="PAID":
                messagebox.showerror("ERROR", "Farmer is already paid",parent =self.top0)
                self.clear_entries()
            elif pay_mode!="CASH":
                messagebox.showerror("ERROR", "ONLY FOR CASH PAY MODE FARMERS",parent =self.top0)
                self.clear_entries()
            else:
                self.top1=Toplevel()
                self.top1.title("SAMARIA MILK GROUP")
                self.top1.iconbitmap("logo1.ico")
                my_frame=Frame(self.top1)
                my_frame.pack(anchor="w")
                self.admin_passcode_label=customtkinter.CTkLabel(my_frame, text="Enter Administrator Password:", fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=40)
                self.admin_passcode_label.grid(row=0, column=0, columnspan=2,padx=20, pady=10)
                self.admin_passcode_entry=customtkinter.CTkEntry(my_frame, width=200,height=30,border_color="blue", show="*")
                self.admin_passcode_entry.grid(row=0, column=2)
                self.submit_passcode_button=customtkinter.CTkButton(my_frame, text="SUBMIT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40, command=self.verify_admin)
                self.submit_passcode_button.grid(row=1, column=0, columnspan=4, padx=20, pady=10)
                   
    #print receipt        
    def print_receipt(self):
        printText=self.my_receipt.get('1.0', 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt.delete('1.0', 'end')
        self.top.destroy()
    def receipt(self):                
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10",-20, "underline", "bold"),width=200,height=40)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading1=f'PAYMENT RECEIPT FOR {self.clicked.get()} {self.year_choser.get()}'
        heading4=f'PERIOD:{self.clicked1.get()},{self.clicked.get()}'
        heading2="DATE:"
        heading3="Served By:"
        if self.clicked1.get()=="From 1-15":
            #first delete the text columns
            self.my_receipt.delete('1.0', 'end')
            #add contents
            self.my_receipt.insert('end', "\n" + title +"\n")
            self.my_receipt.insert('end', "\n" + sub +"\n")
            self.my_receipt.insert('end', "\n" + heading1 +"\n")
            self.my_receipt.insert('end', "\n" + heading4 +"\n")
            self.my_receipt.insert('end', "\n" + heading2 + f'{self.today1} {self.Time}' + "\n")
            self.my_receipt.insert('end', "\n" + f' NAME: {self.first_name} {self.last_name}' +"\n")
            self.my_receipt.insert('end', "\n" + f' FARMER ID: {self.customer_id_entry.get()}' +"\n")
            self.my_receipt.insert('end', "\n" + f' Total Quantity: {self.accumulated_monthly} Litres' +"\n")
            self.my_receipt.insert('end', "\n" + f' Payment Rate(Kshs): {self.set_rate_entry.get()}' +"\n")
            self.my_receipt.insert('end', "\n" + f' Total Amount(Kshs): {self.total_wages}' + "\n")
            self.my_receipt.insert('end', "\n" + f' Pending Advance(Kshs): {self.p_loan}' +"\n")
            self.my_receipt.insert('end', "\n" + f' Pending Feeds Credit(Kshs): {self.p_feeds}' + "\n")
            self.my_receipt.insert('end', "\n" + f' Feeds Transport Fee(Kshs): {self.transport_fee}' +"\n")
            self.my_receipt.insert('end', "\n" + f' Balance(Kshs): {self.bal}' +"\n")
            self.my_receipt.insert('end', "\n" + heading3+ "\t"+ f'{server}' +"\n")
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=? AND PERIOD=?",(self.customer_id_entry.get(),self.mwezi,self.year_choser.get(),"From 1-15",))
            period_1=c.fetchone()
            conn.commit()
            conn.close()
            if period_1!=None:
                #first delete the text columns
                self.my_receipt.delete('1.0', 'end')
                #add contents
                self.my_receipt.insert('end', "\n" + title +"\n")
                self.my_receipt.insert('end', "\n" + sub +"\n")
                self.my_receipt.insert('end', "\n" + heading1 +"\n")
                self.my_receipt.insert('end', "\n" + f'PERIOD: From 1-15,{self.clicked.get()} {self.year_choser.get()} Already Paid'+"\n")
                self.my_receipt.insert('end', "\n" + heading4 +"\n")
                self.my_receipt.insert('end', "\n" + heading2 + f'{self.today1} {self.Time}' + "\n")
                self.my_receipt.insert('end', "\n" + f' NAME: {self.first_name} {self.last_name}' +"\n")
                self.my_receipt.insert('end', "\n" + f' FARMER ID: {self.customer_id_entry.get()}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Total Quantity: {self.accumulated_monthly} Litres' +"\n")
                self.my_receipt.insert('end', "\n" + f' Payment Rate(Kshs): {self.set_rate_entry.get()}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Total Amount(Kshs): {self.total_wages}' + "\n")
                self.my_receipt.insert('end', "\n" + f' Pending Advance(Kshs): {self.p_loan}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Pending Feeds Credit(Kshs): {self.p_feeds}' + "\n")
                self.my_receipt.insert('end', "\n" + f' Feeds Transport Fee(Kshs): {self.transport_fee}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Balance(Kshs): {self.bal}' +"\n")
                self.my_receipt.insert('end', "\n" + heading3+ "\t"+ f'{server}' +"\n")
                
            else:
                #first delete the text columns
                self.my_receipt.delete('1.0', 'end')
                #add contents
                self.my_receipt.insert('end', "\n" + title +"\n")
                self.my_receipt.insert('end', "\n" + sub +"\n")
                self.my_receipt.insert('end', "\n" + heading1 +"\n")
                self.my_receipt.insert('end', "\n" + f'PERIOD: From 1-15,{self.clicked.get()} {self.year_choser.get()} Not Paid'+"\n")
                self.my_receipt.insert('end', "\n" + heading4 +"\n")
                self.my_receipt.insert('end', "\n" + heading2 + f'{self.today1} {self.Time}' + "\n")
                self.my_receipt.insert('end', "\n" + f' NAME: {self.first_name} {self.last_name}' +"\n")
                self.my_receipt.insert('end', "\n" + f' FARMER ID: {self.customer_id_entry.get()}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Total Quantity: {self.accumulated_monthly} Litres' +"\n")
                self.my_receipt.insert('end', "\n" + f' Payment Rate(Kshs): {self.set_rate_entry.get()}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Total Amount(Kshs): {self.total_wages}' + "\n")
                self.my_receipt.insert('end', "\n" + f' Pending Advance(Kshs): {self.p_loan}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Pending Feeds Credit(Kshs): {self.p_feeds}' + "\n")
                self.my_receipt.insert('end', "\n" + f' Feeds Transport Fee(Kshs): {self.transport_fee}' +"\n")
                self.my_receipt.insert('end', "\n" + f' Balance(Kshs): {self.bal}' +"\n")
                self.my_receipt.insert('end', "\n" + heading3+ "\t"+ f'{server}' +"\n")
                messagebox.showinfo("Reminder",f'Farmer was not paid From 1-15,{self.clicked.get()},Please Consider Paying Farmer For That Period.',parent=self.top)
        self.print_button=customtkinter.CTkButton(my_frame, text="PRINT",fg_color="red", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40,command=self.print_receipt)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
        self.clear_entries()

    def choose_month(self,arg=None):
        if self.choose.get()=="January":
            self.month=1
        if self.choose.get()=="February":
            self.month=2
        if self.choose.get()=="March":
            self.month=3
        if self.choose.get()=="April":
            self.month=4
        if self.choose.get()=="May":
            self.month=5
        if self.choose.get()=="June":
            self.month=6
        if self.choose.get()=="July":
            self.month=7
        if self.choose.get()=="August":
            self.month=8
        if self.choose.get()=="September":
            self.month=9
        if self.choose.get()=="October":
            self.month=10
        if self.choose.get()=="November":
            self.month=11
        if self.choose.get()=="December":
            self.month=12
    #print receipt        
    def print_receipt1(self):
        printText=self.my_receipt1.get('1.0', 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt1.delete('1.0', 'end')
        self.top2.destroy()
    def receipt1(self):
        self.top2=Toplevel()
        self.top2.title("SAMARIA MILK GROUP")
        self.top2.iconbitmap("logo1.ico")
        my_frame1=Frame(self.top2, width=300, height=100)
        my_frame1.pack(anchor="w")
        self.receipt_label1=customtkinter.CTkLabel(my_frame1, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"underline", "bold"),width=200,height=40)
        self.receipt_label1.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
        self.my_receipt1=ScrolledText(my_frame1, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=150)
        self.my_receipt1.grid(row=1, sticky="W")
        #define headings
        title1="SAMARIA MILK GROUP"
        sub1="Quality Milk, Healthy Life"
        heading=f'PAYMENT RECEIPT FOR {self.choose.get()} {self.year_chooser.get()}'
        heading0="BANK PAY_MODE CUSTOMERS"
        heading1="DATE:"
        heading2="Names"
        heading3="Last_Name"
        heading4="Farmer_ID"
        heading5="Bank_Name"
        heading6="Bank_Account_Number"
        heading7="Monthly_Quantity"
        heading8="Total_Wages"
        heading9="Pending_Loan"
        heading11="Pending_Feeds"
        heading12="Amount"
        heading13="Total_Amount"
        heading14="Served By:"
        #first delete the text columns
        self.my_receipt1.delete('1.0', 'end')
        self.my_receipt1.insert('end', "\n" + title1 + "\n")
        self.my_receipt1.insert('end', "\n" + sub1 + "\n")
        self.my_receipt1.insert('end', "\n" + heading + "\n")
        self.my_receipt1.insert('end', "\n" + heading0 + "\n")
        self.my_receipt1.insert('end', "\n" + heading1 + f'{self.today1} {self.Time}'+ "\n")
        self.my_receipt1.insert('end',  "\n" + heading2+"\t"+"\t"+"\t"+ heading5 +"\t"+ heading6+"\t"+heading12 +"\n")
        #variables
        self.sum1=0.0
        #query
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Customer_ID FROM Customers WHERE Payment_mode='Bank Account'")
        banking=c.fetchall()
        conn.commit()
        conn.close()
        for x in banking:
            #bank name
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT BANK_NAME FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(x))
            b_name=c.fetchone()
            conn.commit()
            conn.close()
            #bank account
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT BANK_ACCOUNT_NUMBER FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(x))
            b_no=c.fetchone()
            conn.commit()
            conn.close()
            #names
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT First_name FROM Customers WHERE Customer_ID="+str(x))
            f_names=c.fetchone()
            conn.commit()
            conn.close()
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Last_name FROM Customers WHERE Customer_ID="+str(x))
            l_names=c.fetchone()
            conn.commit()
            conn.close()
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Surname FROM Customers WHERE Customer_ID="+str(x))
            s_names=c.fetchone()
            conn.commit()
            conn.close()
            #
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT REMAINING_BALANCE FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=?",(x,self.month,self.year_chooser.get(),))
            remaining_b=c.fetchone()
            conn.commit()
            conn.close()
            self.my_receipt1.insert('end',  "\n" +str(f_names)+"\t"+str(l_names)+"\t"+str(s_names)+"\t"+str(b_name)+"\t"+str(b_no)+"\t"+str(remaining_b)+"\n")
            self.sum1 += float(remaining_b)
        self.my_receipt1.insert('end', "\n" + f'{heading13} Kshs {self.sum1}' +"\n")
        self.my_receipt1.insert('end', "\n" + heading14+ "\t"+ f'{server}' +"\n")
        self.print_button1=customtkinter.CTkButton(my_frame1, text="PRINT",fg_color="red", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40,command=self.print_receipt1)
        self.print_button1.grid(row=2, column=0, columnspan=10, pady=10, padx=10)
    def verify_bank_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_p=c.fetchone()
        conn.commit()
        conn.close()
        if admin_p!=self.admin_passcode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Admin Password, Check Password And Try Again",parent =self.top0)
            self.admin_passcode_entry.delete(0, END)
            self.top12.destroy()
        elif self.set_rate_entry1.get()=="":
            messagebox.showerror("ERROR","Please Enter Monthly Rate",parent=self.top0)
        elif self.choose.get()=="":
            messagebox.showerror("ERROR","Please Choose Month",parent=self.top0)
        elif self.year_chooser.get()=="":
            messagebox.showerror("ERROR","Please Choose Year",parent=self.top0)
            self.admin_passcode_entry.delete(0, END)
            self.top12.destroy()
        else:
            self.admin_passcode_entry.delete(0, END)
            self.top12.destroy()
            #check
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Customer_ID FROM Customers WHERE Payment_mode='Bank Account'")
            self.bankers=c.fetchall()
            v=self.bankers[0]
            conn.commit()
            conn.close()
            #status
            self.b_month=self.month + 1
            if self.b_month==13:
                self.b_month = 1
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.month, self.year_chooser.get(), v,))
            self.status1=c.fetchone()
            if self.status1=="PAID":
                messagebox.showerror("ERROR", "Bank Mode Farmers Already Paid",parent =self.top0)
            else:
                for self.x in self.bankers:
                    #names
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT FIRST_NAME FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(self.x))
                    self.fname=c.fetchone()
                    conn.commit()
                    conn.close()
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT LAST_NAME FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(self.x))
                    self.lname=c.fetchone()
                    conn.commit()
                    conn.close()
                    #bank name
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT BANK_NAME FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(self.x))
                    self.b_name=c.fetchone()
                    conn.commit()
                    conn.close()
                    #bank account
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT BANK_ACCOUNT_NUMBER FROM BANK_ACCOUNTS WHERE CUSTOMER_ID="+str(self.x))
                    self.b_no=c.fetchone()
                    conn.commit()
                    conn.close()
                    #monthly totals
                    try:
                        conn=sqlite3.connect('samaria database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=?",(self.month, self.year_chooser.get(), self.x))
                        self.mwezi_total=c.fetchone()
                        if self.mwezi_total==None:
                            self.mwezi_total=0.0
                        conn.commit()
                        conn.close()
                    except:
                        messagebox.showerror("ERROR", "Please Choose Month",parent =self.top0)
                    #monthly_wages
                    self.b_wages=(self.mwezi_total * float(self.set_rate_entry1.get()))
                    #pending loan
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Total_Loan FROM LOANS WHERE Customer_ID=? AND STATUS=?",(self.x,"NOT PAID",))
                    self.b_loan=c.fetchone()
                    if self.b_loan==None:
                        self.b_loan=0.0
                    conn.commit()
                    conn.close()
                    #feeds
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.x,"NOT PAID",))
                    self.feeds=c.fetchall()
                    self.b_feeds=0.0
                    if self.feeds==[]:
                        self.b_feeds=0.0
                    else:
                        for b in self.feeds:
                            self.b_feeds+=b
                    conn.commit()
                    conn.close()
                    #transport fee
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=?",(self.x,"NOT PAID",))
                    self.t_b=c.fetchone()
                    if self.t_b==None:
                        self.t_b=0.0
                    conn.commit()
                    conn.close()
                    #bal
                    self.b_bal=(self.b_wages- (self.b_loan + self.b_feeds+self.t_b))
                    if float(self.b_bal)<0.0:
                        b_balaz=0.0
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD,:MONTHLY_TOTAL, :MONTHLY_RATE,:STATUS,:MONTHLY_WAGES,:PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee,:REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.fname,
                                        'LAST_NAME': self.lname,
                                        'CUSTOMER_ID': self.x,
                                        'PERIOD':"Entire Month",
                                        'MONTHLY_TOTAL': self.mwezi_total,
                                        'MONTHLY_RATE': self.set_rate_entry1.get(),
                                        'STATUS': self.st,
                                        'MONTHLY_WAGES': self.b_wages,
                                        'PENDING_LOAN': self.b_loan,
                                        'PENDING_FEEDS': self.b_feeds,
                                        'Transport_Fee':self.t_b,
                                        'REMAINING_BALANCE':b_balaz,
                                        'MONTH': self.month,
                                        'YEAR': self.year_chooser.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=?",(self.x,"NOT PAID",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pwd

                                        WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwd""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pwd':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.x,"NOT PAID",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:pwd

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.x,
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'pwd':record[11]
                                          })
                            conn.commit()
                            conn.close()
                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=?",(self.x,"NOT PAID",))
                        results=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in results:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:pwd
                                    
                                        WHERE Customer_ID=:c_id AND PERIOD=:pwd""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'pwd':record[10]
                                            })
                            conn.commit()
                            conn.close()
                            #insert
                            new_l=abs(self.b_bal)
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                      {
                                          'Customer_ID':self.x,
                                          'First_Name':self.fname,
                                          'Last_Name':self.lname,
                                          'Pending_Loan':0.0,
                                          'Loan_Amount':new_l,
                                          'Total_Loan':new_l,
                                          'STATUS':"NOT PAID",
                                          'MONTH':self.b_month,
                                          'YEAR':self.mwaka,
                                          'DATE':self.today,
                                          'PERIOD':"From 1-15"
                                          })
                            conn.commit()
                            conn.close()
                    else:
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.fname,
                                        'LAST_NAME': self.lname,
                                        'CUSTOMER_ID': self.x,
                                        'PERIOD':"Entire Month",
                                        'MONTHLY_TOTAL': self.mwezi_total,
                                        'MONTHLY_RATE': self.set_rate_entry1.get(),
                                        'STATUS': self.st,
                                        'MONTHLY_WAGES': self.b_wages,
                                        'PENDING_LOAN': self.b_loan,
                                        'PENDING_FEEDS': self.b_feeds,
                                        'Transport_Fee':self.t_b,
                                        'REMAINING_BALANCE':self.b_bal,
                                        'MONTH': self.month,
                                        'YEAR': self.year_chooser.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=?",(self.x,"NOT PAID",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pzd

                                        WHERE Farmer_ID=:f_id AND DATE=:siku""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pzd':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=?",(self.x,"NOT PAID",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:prd

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.x,
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'prd':record[11]
                                          })
                            conn.commit()
                            conn.close()
                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=?",(self.x,"NOT PAID",))
                        results=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in results:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:prds
                                    
                                        WHERE Customer_ID=:c_id""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'prds':record[10]
                                            })
                            conn.commit()
                            conn.close()
                self.receipt1()
                self.set_rate_entry1.delete(0, END)
    def pay_bankers(self):
        self.top12=Toplevel()
        self.top12.geometry("500x150")
        self.top12.title("SAMARIA MILK GROUP")
        self.top12.iconbitmap("logo1.ico")
        my_frame=Frame(self.top12)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=customtkinter.CTkLabel(my_frame, text="Enter Administrator Password:", fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=30)
        self.admin_passcode_label.grid(row=0, column=0, columnspan=2,padx=20, pady=10)
        self.admin_passcode_entry=customtkinter.CTkEntry(my_frame, width=150,height=25,border_color="blue", show="*")
        self.admin_passcode_entry.grid(row=0, column=2)
        self.submit_passcode_button=customtkinter.CTkButton(my_frame, text="SUBMIT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40, command=self.verify_bank_admin)
        self.submit_passcode_button.grid(row=1, column=0, columnspan=4, padx=20, pady=10)        
    def chagua_month(self,arg=None):
        if self.chagua.get()=="January":
            self.monthm=1
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="February":
            self.monthm=2
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="March":
            self.monthm=3
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="April":
            self.monthm=4
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="May":
            self.monthm=5
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="June":
            self.monthm=6
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="July":
            self.monthm=7
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="August":
            self.monthm=8
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="September":
            self.monthm=9
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="October":
            self.monthm=10
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="November":
            self.monthm=11
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
        if self.chagua.get()=="December":
            self.monthm=12
            mm_details=calendar.monthrange(self.mwaka,self.monthm)
            self.last_daym=mm_details[1]
            self.select_periodm()
    #select period
    def select_periodm(self):
        self.top97=Toplevel()
        self.top97.title("SAMARIA MILK GROUP")
        self.top97.iconbitmap("logo1.ico")
        top_frame=Frame(self.top97)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT Period:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.clicked2,command=self.close_periodm,values=[f'From 1-15',f'From 16-{self.last_daym}'],width=160,height=25,fg_color="red",text_color="white")
        mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def close_periodm(self,e):
        self.top97.destroy()
    def clicker1(self,e):
        self.farmer_id_entry.delete(0,END)
        self.first_name_entry.delete(0,END)
        self.phone_number_entry.delete(0,END)
        self.balance_entry.delete(0,END)
        #grab record
        selected1=self.my_tree2.focus()
        #grab record values
        values=self.my_tree2.item(selected1,'values')
        #output to entry boxes
        self.farmer_id_entry.insert(0, values[1])
        self.first_name_entry.insert(0, values[0])
        self.phone_number_entry.insert(0, values[2])
        self.balance_entry.insert(0, values[9])
    def mpesa_details(self):
        if self.chagua.get()=="":
            messagebox.showerror("ERROR","Please Choose Month",parent=self.top0)
        elif self.clicked2.get()=="":
            messagebox.showerror("ERROR","Please Choose Period",parent=self.top0)
        elif self.set_rate_entry2.get()=="":
            messagebox.showerror("ERROR","Please Enter Payment Rate",parent=self.top0)
        elif self.year_choose.get()=="":
            messagebox.showerror("ERROR","Please Choose Year",parent=self.top0)
        else:
            #toplevel
            self.top89=Toplevel()
            self.top89.iconbitmap("logo1.ico")
            self.top89.state('zoomed')
            self.title_frame=Frame(self.top89)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="M~PESA PAYMENT DETAILS"
            self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
            self.my_img_label=Label(self.title_frame, image=self.img1)
            self.my_img_label.grid(row=0, column=0, rowspan=3)
            self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
            self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
            self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
            self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
            self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
            self.my_sub1_text.grid(row=2, column=1, columnspan=4)
            #left frame
            self.left_frame=customtkinter.CTkFrame(self.top89,border_color="maroon",border_width=5,corner_radius=8,width=900,height=650)
            self.left_frame.pack(anchor="center")
            #heading
            mpesa_title=f'PERIOD: {self.clicked2.get()},{self.chagua.get()} {self.year_choose.get()}'
            self.mpesa_title_label=customtkinter.CTkLabel(self.left_frame, text=mpesa_title, fg_color="orange", text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
            self.mpesa_title_label.grid(row=0, column=0,pady=5,columnspan=10)
            #tender treeview
            self.tree_frame2=Frame(self.left_frame, highlightbackground="green", highlightthickness=5, width=500, height=500, bd=0)
            self.tree_frame2.grid(row=1, column=0, padx=30, pady=10,columnspan=10)
            #style our treeview
            style=ttk.Style()
            #pick a theme
            style.theme_use("default")
            style.configure("Treeview",
                            background="white",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="white"
                            )
            #change selected color
            style.map('Treeview',
                    background=[('selected', 'green')])
            #treeview_scrollbar
            self.tree_scroll2=Scrollbar(self.tree_frame2)
            self.tree_scroll2.pack(side=RIGHT, fill=Y)
            #create our treeview
            self.my_tree2=ttk.Treeview(self.tree_frame2, yscrollcommand=self.tree_scroll2.set,height=9)
            self.my_tree2.pack()
            #configure the scrollbar
            self.tree_scroll2.config(command=self.my_tree2.yview)
            #define our columns
            self.my_tree2['columns']=("First_Name","Farmer_ID","Phone_Number", "Total_Quantity","Payment_Rate","Total_Amount","Pending_Advance","Pending_Feeds","Transport_Fee","Balance","Status")
            #format our columns
            self.my_tree2.column("#0", width=0, stretch=NO)
            self.my_tree2.column("First_Name", anchor="w", width=100)
            self.my_tree2.column("Farmer_ID", anchor="w", width=100)
            self.my_tree2.column("Phone_Number", anchor="w", width=100)
            self.my_tree2.column("Total_Quantity", anchor="w", width=100)
            self.my_tree2.column("Payment_Rate", anchor="w", width=100)
            self.my_tree2.column("Total_Amount", anchor="w", width=100)
            self.my_tree2.column("Pending_Advance", anchor="w", width=100)
            self.my_tree2.column("Pending_Feeds", anchor="w", width=100)
            self.my_tree2.column("Transport_Fee", anchor="w", width=100)
            self.my_tree2.column("Balance", anchor="w", width=100)
            self.my_tree2.column("Status", anchor="w", width=100)
            #create headings
            self.my_tree2.heading("#0", text="")
            self.my_tree2.heading("First_Name", text="First Name", anchor="w")
            self.my_tree2.heading("Farmer_ID", text="Farmer ID", anchor="w")
            self.my_tree2.heading("Phone_Number", text="Phone Number", anchor="w")
            self.my_tree2.heading("Total_Quantity", text="Total_Quantity", anchor="w")
            self.my_tree2.heading("Payment_Rate", text="Payment_Rate", anchor="w")
            self.my_tree2.heading("Total_Amount", text="Total_Amount", anchor="w")
            self.my_tree2.heading("Pending_Advance", text="Pending_Advance", anchor="w")
            self.my_tree2.heading("Pending_Feeds", text="Pending_Feeds", anchor="w")
            self.my_tree2.heading("Transport_Fee", text="Transport_Fee", anchor="w")
            self.my_tree2.heading("Balance", text="Balance", anchor="w")
            self.my_tree2.heading("Status", text="Status", anchor="w")
            #striped row tags
            self.my_tree2.tag_configure('oddrow', background="white")
            self.my_tree2.tag_configure('evenrow', background="violet")
            # binding single click
            self.my_tree2.bind("<ButtonRelease-1>",self.clicker1)
            #variable
            self.svar=StringVar()
            #frame
            self.entry_frame=Frame(self.left_frame)
            self.entry_frame.grid(row=2, column=0,columnspan=10, padx=20,pady=5)
            #entry labels
            self.farmer_id_label=customtkinter.CTkLabel(self.entry_frame,text="Farmer ID:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
            self.farmer_id_label.grid(row=1, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
            self.first_name_label=customtkinter.CTkLabel(self.entry_frame,text="First Name:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
            self.first_name_label.grid(row=2, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
            self.phone_number_label=customtkinter.CTkLabel(self.entry_frame, text="Phone Number:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
            self.phone_number_label.grid(row=3, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
            self.balance_label=customtkinter.CTkLabel(self.entry_frame, text="Balance:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
            self.balance_label.grid(row=4, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
            self.status_label=customtkinter.CTkLabel(self.entry_frame, text="Mark as Paid:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
            self.status_label.grid(row=5, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
            #entry boxes
            self.farmer_id_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
            self.farmer_id_entry.grid(row=1, column=5)
            self.first_name_entry=customtkinter.CTkEntry(self.entry_frame, width=200,height=25,border_color="blue")
            self.first_name_entry.grid(row=2, column=5)
            self.phone_number_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
            self.phone_number_entry.grid(row=3, column=5)
            self.balance_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
            self.balance_entry.grid(row=4, column=5)
            self.status_c=customtkinter.CTkCheckBox(self.entry_frame, text="",variable=self.svar, onvalue="PAID", offvalue="NOT PAID")
            self.status_c.deselect()
            self.status_c.grid(row=5, column=5)
            #update button
            self.update_button=customtkinter.CTkButton(self.entry_frame, text="MARK AS PAID",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=150,height=35,command=self.pay_mpesas)
            self.update_button.grid(row=6, column=0, columnspan=10, padx=20, pady=5)
            self.mpesa_data()
    #print receipt
    def print_receipt2(self):
        printText=self.my_receipt2.get('1.0', 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt2.delete('1.0', 'end')
        self.top3.destroy()
    #receipt
    def receipt2(self):      
            self.top3=Toplevel()
            self.top3.title("SAMARIA MILK GROUP")
            self.top3.iconbitmap("logo1.ico")
            my_frame2=Frame(self.top3, width=300, height=100)
            my_frame2.pack(anchor="w")
            self.receipt_label2=customtkinter.CTkLabel(my_frame2, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "underline", "bold"),width=200,height=30)
            self.receipt_label2.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
            self.my_receipt2=ScrolledText(my_frame2, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=150)
            self.my_receipt2.grid(row=1, sticky="W")                
            #define headings
            title2="SAMARIA MILK GROUP"
            sub2="Quality Milk, Healthy Life"
            headings=f'PAYMENT RECEIPT FOR {self.chagua.get()} {self.year_choose.get()}'
            headings0="MPESA PAY_MODE CUSTOMERS"
            headings1="DATE:"
            headings2="First_Name"
            headings3="Last_Name"
            headings4="Farmer_ID"
            headings5="MPESA_Number"
            headings6="Monthly_Quantity"
            headings7="Total_Wages"
            headings8="Pending_Loan"
            headings9 ="Interval_Loan"
            headings10="Pending_Feeds"
            headings11="Balance"
            headings12="Total Amount"
            heading13="Served By:"
            #first delete the text columns
            self.my_receipt2.delete('1.0', 'end')
            self.my_receipt2.insert('end', "\n" + title2 + "\n")
            self.my_receipt2.insert('end', "\n" + sub2 + "\n")
            self.my_receipt2.insert('end', "\n" + headings + "\n")
            self.my_receipt2.insert('end', "\n" + headings0 + "\n")
            self.my_receipt2.insert('end', "\n" + headings1 + f'{self.today1} {self.Time}'+ "\n")
            self.my_receipt2.insert('end',  "\n" + headings2 + headings4+ headings5 + headings6 + headings7 + headings9 +headings10+"Transport_Fee"+ headings11 +"\n")
            #enter data to receipt
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Customer_ID FROM Customers WHERE Payment_mode='MPESA'")
            mpesas=c.fetchall()
            conn.commit()
            conn.close()
            #variables
            sum2=0.0
            #queries
            for p in mpesas:
                #mpesa number
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Phone_Number FROM Customers WHERE Customer_ID="+str(p))
                m_no=c.fetchone()
                conn.commit()
                conn.close()
                #payments
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=?",(p,self.monthm,self.year_choose.get(),))
                all_mpesas=c.fetchall()
                conn.commit()
                conn.close()
                for record in all_mpesas:
                    self.my_receipt2.insert('end',  "\n" +str(record[0])+"\t"+"\t"+str(p)+"\t"+f'0{m_no}'+"\t"+str(record[3])+"\t"+str(record[6])+"\t"+str(record[7])+"\t"+str(record[8])+"\t"+str(record[9])+"\t"+str(record[10])+"\n")
                    sum2 += float(record[10])
            self.my_receipt2.insert('end', "\n" + f'{headings12} Kshs {sum2}' +"\n")
            self.my_receipt2.insert('end', "\n" + heading13+ "\t"+ f'{server}' +"\n")
            print_button2=customtkinter.CTkButton(my_frame2, text="PRINT", fg_color="red", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40,command=self.print_receipt2)
            print_button2.grid(row=3, column=0, columnspan=10, padx=10, pady=10)
    def mpesa_data(self):
        #check
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Customer_ID FROM Customers WHERE Payment_mode='MPESA'")
        self.mpesas=c.fetchall()
        conn.commit()
        conn.close()
        if self.clicked2.get()=='From 1-15':
            for p in self.mpesas:
                #names
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT First_name FROM Customers WHERE CUSTOMER_ID="+str(p))
                self.f_name=c.fetchone()
                conn.commit()
                conn.close()
                #mpesa number
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Phone_Number FROM Customers WHERE Customer_ID="+str(p))
                self.m_no=c.fetchone()
                conn.commit()
                conn.close()
                #monthly_totals
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 1 AND 15",(self.monthm, self.year_choose.get(),p,))
                self.mwezi_1st=c.fetchone()
                if self.mwezi_1st==None:
                    self.mwezi_1st=0.0
                conn.commit()
                conn.close()
                #monthly_wages
                self.m_wages=(self.mwezi_1st * float(self.set_rate_entry2.get()))
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Total_Loan FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(p,"NOT PAID","From 1-15",))
                self.m_loan=c.fetchone()
                if self.m_loan==None:
                    self.m_loan=0.0
                conn.commit()
                conn.close()
                #feeds
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(p,"NOT PAID","From 1-15",))
                self.mufeeds=c.fetchall()
                self.m_feeds=0.0
                if self.mufeeds==[]:
                    self.m_feeds=0.0
                else:
                    for x in self.mufeeds:
                        self.m_feeds+=x
                conn.commit()
                conn.close()
                #transport fee
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(p,"NOT PAID","From 1-15",))
                self.t_m_fee=c.fetchone()
                if self.t_m_fee==None:
                    self.t_m_fee=0.0
                conn.commit()
                conn.close()
                #bal
                self.m_bal=(self.m_wages- (self.m_loan + self.m_feeds+self.t_m_fee))
                #status
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT STATUS FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=? AND PERIOD=?",(p,self.monthm,self.year_choose.get(),self.clicked2.get(),))
                status_1st=c.fetchone()
                if status_1st==None:
                    status_1st="NOT PAID"
                conn.commit()
                conn.close()
                #insert into treeview
                if self.count%2==0:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(self.f_name,p,f'0{self.m_no}',self.mwezi_1st,self.set_rate_entry2.get(),self.m_wages,self.m_loan,self.m_feeds,self.t_m_fee,self.m_bal,status_1st), tags=("evenrow"),)
                else:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(self.f_name,p,f'0{self.m_no}',self.mwezi_1st,self.set_rate_entry2.get(),self.m_wages,self.m_loan,self.m_feeds,self.t_m_fee,self.m_bal,status_1st), tags=("oddrow"),)
                self.count+=1
        else:
            for p in self.mpesas:
                #names
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT First_name FROM Customers WHERE CUSTOMER_ID="+str(p))
                self.f_name=c.fetchone()
                conn.commit()
                conn.close()
                #mpesa number
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Phone_Number FROM Customers WHERE Customer_ID="+str(p))
                self.m_no=c.fetchone()
                conn.commit()
                conn.close()
                #monthly_totals
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 16 AND 'self.last_daym'",(self.monthm,self.year_choose.get(),p,))
                self.mwezi_1st=c.fetchone()
                if self.mwezi_1st==None:
                    self.mwezi_1st=0.0
                conn.commit()
                conn.close()
                #monthly_wages
                self.m_wages=(self.mwezi_1st * float(self.set_rate_entry2.get()))
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Total_Loan FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(p,"NOT PAID","From 16",))
                self.m_loan=c.fetchone()
                if self.m_loan==None:
                    self.m_loan=0.0
                conn.commit()
                conn.close()
                #feeds
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(p,"NOT PAID","From 16",))
                self.mufeeds=c.fetchall()
                self.m_feeds=0.0
                if self.mufeeds==[]:
                    self.m_feeds=0.0
                else:
                    for x in self.mufeeds:
                        self.m_feeds+=x
                conn.commit()
                conn.close()
                #transport fee
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(p,"NOT PAID","From 16",))
                self.t_m_fee=c.fetchone()
                if self.t_m_fee==None:
                    self.t_m_fee=0.0
                conn.commit()
                conn.close()
                #bal
                self.m_bal=(self.m_wages- (self.m_loan + self.m_feeds+self.t_m_fee))
                #status
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT STATUS FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=? AND PERIOD=?",(p,self.monthm,self.year_choose.get(),self.clicked2.get(),))
                status_1st=c.fetchone()
                if status_1st==None:
                    status_1st="NOT PAID"
                conn.commit()
                conn.close()
                #insert into treeview
                if self.count%2==0:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(self.f_name,p,f'0{self.m_no}',self.mwezi_1st,self.set_rate_entry2.get(),self.m_wages,self.m_loan,self.m_feeds,self.t_m_fee,self.m_bal,status_1st), tags=("evenrow"),)
                else:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(self.f_name,p,f'0{self.m_no}',self.mwezi_1st,self.set_rate_entry2.get(),self.m_wages,self.m_loan,self.m_feeds,self.t_m_fee,self.m_bal,status_1st), tags=("oddrow"),)
                self.count+=1
    def verify_mpesa_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_p=c.fetchone()
        conn.commit()
        conn.close()
        if admin_p!=self.admin_passcode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Admin Password, Check Password And Try Again",parent =self.top0)
            self.admin_passcode_entry.delete(0, END)
            self.top13.destroy()
        else:
            self.admin_passcode_entry.delete(0, END)
            self.top13.destroy()
            #status
            self.n_m_month=self.monthm + 1
            if self.n_m_month==13:
                self.n_m_month = 1
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND PERIOD=?",(self.monthm, self.year_choose.get(),self.farmer_id_entry.get(),self.clicked2.get(),))
            status_2=c.fetchone()
            if status_2=="PAID":
                messagebox.showerror("ERROR", "Farmer is Already Paid",parent =self.top89)
            elif self.svar.get()=="NOT PAID":
                messagebox.showerror("ERROR","Please Mark As Paid",parent=self.top89)
            else:
                #get details
                #names
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT First_name FROM Customers WHERE CUSTOMER_ID=?",(self.farmer_id_entry.get(),))
                self.f_name=c.fetchone()
                conn.commit()
                conn.close()
                #lname
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Last_name FROM Customers WHERE CUSTOMER_ID=?",(self.farmer_id_entry.get(),))
                self.l_name=c.fetchone()
                conn.commit()
                conn.close()
                #mpesa number
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Phone_Number FROM Customers WHERE Customer_ID=?",(self.farmer_id_entry.get(),))
                self.m_no=c.fetchone()
                conn.commit()
                conn.close()
                if self.clicked2.get()=='From 1-15':
                    #monthly_totals
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 1 AND 15",(self.monthm, self.year_choose.get(),self.farmer_id_entry.get(),))
                    self.mwezi_1st=c.fetchone()
                    if self.mwezi_1st==None:
                        self.mwezi_1st=0.0
                    conn.commit()
                    conn.close()
                    #monthly_wages
                    self.m_wages=(self.mwezi_1st * float(self.set_rate_entry2.get()))
                    #pending loan
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Total_Loan FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                    self.m_loan=c.fetchone()
                    if self.m_loan==None:
                        self.m_loan=0.0
                    conn.commit()
                    conn.close()
                    #feeds
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                    self.mufeeds=c.fetchall()
                    self.m_feeds=0.0
                    if self.mufeeds==[]:
                        self.m_feeds=0.0
                    else:
                        for x in self.mufeeds:
                            self.m_feeds+=x
                    conn.commit()
                    conn.close()
                    #transport fee
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                    self.t_m_fee=c.fetchone()
                    if self.t_m_fee==None:
                        self.t_m_fee=0.0
                    conn.commit()
                    conn.close()
                    #bal
                    self.m_bal=(self.m_wages- (self.m_loan + self.m_feeds+self.t_m_fee))
                    
                    if float(self.m_bal)<0.0:
                        balaz=0.0
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.f_name,
                                        'LAST_NAME': self.l_name,
                                        'CUSTOMER_ID': self.farmer_id_entry.get(),
                                        'PERIOD':self.clicked2.get(),
                                        'MONTHLY_TOTAL': self.mwezi_1st,
                                        'MONTHLY_RATE': self.set_rate_entry2.get(),
                                        'STATUS': "PAID",
                                        'MONTHLY_WAGES': self.m_wages,
                                        'PENDING_LOAN': self.m_loan,
                                        'PENDING_FEEDS': self.m_feeds,
                                        'Transport_Fee': self.t_m_fee,
                                        'REMAINING_BALANCE':balaz,
                                        'MONTH': self.monthm,
                                        'YEAR': self.year_choose.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pwd

                                        WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwd""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pwd':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:pwd

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwd""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.farmer_id_entry.get(),
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'pwd':record[11]
                                          })
                            conn.commit()
                            conn.close()
                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        record=c.fetchone()
                        conn.commit()
                        conn.close()
                        if record!=None:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:pwd
                                    
                                        WHERE Customer_ID=:c_id AND PERIOD=:pwd""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'pwd':record[10]
                                            })
                            conn.commit()
                            conn.close()
                            #insert
                            new_l=abs(self.m_bal)
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                      {
                                          'Customer_ID':self.farmer_id_entry.get(),
                                          'First_Name':self.f_name,
                                          'Last_Name':self.l_name,
                                          'Pending_Loan':0.0,
                                          'Loan_Amount':new_l,
                                          'Total_Loan':new_l,
                                          'STATUS':"NOT PAID",
                                          'MONTH':self.monthm,
                                          'YEAR':self.mwaka,
                                          'DATE':self.today,
                                          'PERIOD':"From 16"
                                          })
                            conn.commit()
                            conn.close()
                    else:
                        #insert our details to database
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                    {
                                        'FIRST_NAME': self.f_name,
                                        'LAST_NAME': self.l_name,
                                        'CUSTOMER_ID': self.farmer_id_entry.get(),
                                        'PERIOD':self.clicked2.get(),
                                        'MONTHLY_TOTAL': self.mwezi_1st,
                                        'MONTHLY_RATE': self.set_rate_entry2.get(),
                                        'STATUS': "PAID",
                                        'MONTHLY_WAGES': self.m_wages,
                                        'PENDING_LOAN': self.m_loan,
                                        'PENDING_FEEDS': self.m_feeds,
                                        'Transport_Fee': self.t_m_fee,
                                        'REMAINING_BALANCE':self.m_bal,
                                        'MONTH': self.monthm,
                                        'YEAR': self.year_choose.get(),
                                        'DATE': self.today
                                        })
                        conn.commit()
                        conn.close()
                        #update transport table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        all_transport=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in all_transport:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE Transport SET
                                        Farmer_ID=:f_id,
                                        Transport_Amount=:t_amount,
                                        Status=:stus,
                                        DATE=:siku,
                                        PERIOD=:pwdx

                                        WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwdx""",
                                      {
                                          'f_id':record[0],
                                          't_amount':record[1],
                                          'stus':"PAID",
                                          'siku':record[3],
                                          'pwdx':record[4]
                                          })
                            conn.commit()
                            conn.close()
                        #update feeds table
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        unpaid_feeds=c.fetchall()
                        conn.commit()
                        conn.close()
                        for record in unpaid_feeds:
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE FEEDS SET
                                        First_Name=:f_jina, 
                                        Last_Name=:l_jina,
                                        Customer_ID=:customerid,
                                        Feed_Names=:feed_jina,
                                        Feed_Quantity=:feed_amount,
                                        Price=:pesa,
                                        Total_Cost=:pesa_total,
                                        Status=:stsz,
                                        MONTH=:mhtm,
                                        YEAR=:mwks,
                                        DATE=:leo,
                                        PERIOD=:pwdx

                                        WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwdx""",
                                      {
                                          'f_jina':record[0],
                                          'l_jina':record[1],
                                          'customerid':self.farmer_id_entry.get(),
                                          'feed_jina':record[3],
                                          'feed_amount':record[4],
                                          'pesa':record[5],
                                          'pesa_total':record[6],
                                          'stsz':"PAID",
                                          'mhtm':record[8],
                                          'mwks':record[9],
                                          'leo':record[10],
                                          'pwdx':record[11]
                                          })
                            conn.commit()
                            conn.close()
                        #update loans table
                        conn=sqlite3.connect('samaria database.db')
                        c=conn.cursor()
                        c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 1-15",))
                        record=c.fetchone()
                        conn.commit()
                        conn.close()
                        if record!=None:
                            #update
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("""UPDATE LOANS SET
                                        Customer_ID=:c_id,
                                        First_Name=:f_name,
                                        Last_Name=:l_name,
                                        Pending_Loan=:pen_l,
                                        Loan_Amount=:lamount,
                                        Total_Loan=:t_loan,
                                        STATUS=:stxz,
                                        MONTH=:mnth,
                                        YEAR=:raey,
                                        DATE=:date,
                                        PERIOD=:pwdc
                                    
                                        WHERE Customer_ID=:c_id AND PERIOD=:pwdc""",
                                        {
                                            'c_id': record[0],
                                            'f_name': record[1],
                                            'l_name': record[2],
                                            'pen_l':0.0,
                                            'lamount':0.0,
                                            't_loan':0.0,
                                            'stxz':"PAID",
                                            'mnth':record[7],
                                            'raey':record[8],
                                            'date':record[9],
                                            'pwdc':record[10]
                                            })
                            conn.commit()
                            conn.close()
                    messagebox.showinfo("BRAVO","Farmer Paid Succesfully",parent=self.top89)
                    #clear entries
                    self.farmer_id_entry.delete(0,END)
                    self.first_name_entry.delete(0,END)
                    self.phone_number_entry.delete(0,END)
                    self.balance_entry.delete(0,END)
                    #refresh treeview
                    self.my_tree2.delete(* self.my_tree2.get_children())
                    self.mpesa_data()

                else:
                    #check
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND MONTH=? AND YEAR=? AND PERIOD=?",(self.farmer_id_entry.get(),self.monthm,self.year_choose.get(),"From 1-15",))
                    period_1=c.fetchone()
                    conn.commit()
                    conn.close()
                    if period_1==None:
                        messagebox.showerror("ERROR",f'Farmer was not paid From 1-15,{self.chagua.get()},Please Consider Paying Farmer For That Period.',parent=self.top89)
                        #clear entries
                        self.farmer_id_entry.delete(0,END)
                        self.first_name_entry.delete(0,END)
                        self.phone_number_entry.delete(0,END)
                        self.balance_entry.delete(0,END)
                    else:
                        #monthly_totals
                        conn=sqlite3.connect('samaria database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 16 AND 'self.last_daym'",(self.monthm,self.year_choose.get(),self.farmer_id_entry.get(),))
                        self.mwezi_1st=c.fetchone()
                        if self.mwezi_1st==None:
                            self.mwezi_1st=0.0
                        conn.commit()
                        conn.close()
                        #monthly_wages
                        self.m_wages=(self.mwezi_1st * float(self.set_rate_entry2.get()))
                        #pending loan
                        conn=sqlite3.connect('samaria database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Total_Loan FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                        self.m_loan=c.fetchone()
                        if self.m_loan==None:
                            self.m_loan=0.0
                        conn.commit()
                        conn.close()
                        #feeds
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                        self.mufeeds=c.fetchall()
                        self.m_feeds=0.0
                        if self.mufeeds==[]:
                            self.m_feeds=0.0
                        else:
                            for x in self.mufeeds:
                                self.m_feeds+=x
                        conn.commit()
                        conn.close()
                        #transport fee
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                        self.t_m_fee=c.fetchone()
                        if self.t_m_fee==None:
                            self.t_m_fee=0.0
                        conn.commit()
                        conn.close()
                        #bal
                        self.m_bal=(self.m_wages- (self.m_loan + self.m_feeds+self.t_m_fee))
                        
                        if float(self.m_bal)<0.0:
                            balaz=0.0
                            #insert our details to database
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                        {
                                            'FIRST_NAME': self.f_name,
                                            'LAST_NAME': self.l_name,
                                            'CUSTOMER_ID': self.farmer_id_entry.get(),
                                            'PERIOD':self.clicked2.get(),
                                            'MONTHLY_TOTAL': self.mwezi_1st,
                                            'MONTHLY_RATE': self.set_rate_entry2.get(),
                                            'STATUS': "PAID",
                                            'MONTHLY_WAGES': self.m_wages,
                                            'PENDING_LOAN': self.m_loan,
                                            'PENDING_FEEDS': self.m_feeds,
                                            'Transport_Fee': self.t_m_fee,
                                            'REMAINING_BALANCE':balaz,
                                            'MONTH': self.monthm,
                                            'YEAR': self.year_choose.get(),
                                            'DATE': self.today
                                            })
                            conn.commit()
                            conn.close()
                            #update transport table
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            all_transport=c.fetchall()
                            conn.commit()
                            conn.close()
                            for record in all_transport:
                                conn=sqlite3.connect('samaria feeds database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE Transport SET
                                            Farmer_ID=:f_id,
                                            Transport_Amount=:t_amount,
                                            Status=:stus,
                                            DATE=:siku,
                                            PERIOD=:pwds

                                            WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwds""",
                                          {
                                              'f_id':record[0],
                                              't_amount':record[1],
                                              'stus':"PAID",
                                              'siku':record[3],
                                              'pwds':record[4]
                                              })
                                conn.commit()
                                conn.close()
                            #update feeds table
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            unpaid_feeds=c.fetchall()
                            conn.commit()
                            conn.close()
                            for record in unpaid_feeds:
                                conn=sqlite3.connect('samaria feeds database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE FEEDS SET
                                            First_Name=:f_jina, 
                                            Last_Name=:l_jina,
                                            Customer_ID=:customerid,
                                            Feed_Names=:feed_jina,
                                            Feed_Quantity=:feed_amount,
                                            Price=:pesa,
                                            Total_Cost=:pesa_total,
                                            Status=:stsz,
                                            MONTH=:mhtm,
                                            YEAR=:mwks,
                                            DATE=:leo,
                                            PERIOD=:pwds

                                            WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwds""",
                                          {
                                              'f_jina':record[0],
                                              'l_jina':record[1],
                                              'customerid':self.farmer_id_entry.get(),
                                              'feed_jina':record[3],
                                              'feed_amount':record[4],
                                              'pesa':record[5],
                                              'pesa_total':record[6],
                                              'stsz':"PAID",
                                              'mhtm':record[8],
                                              'mwks':record[9],
                                              'leo':record[10],
                                              'pwds':record[11]
                                              })
                                conn.commit()
                                conn.close()
                            #update loans table
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            record=c.fetchone()
                            conn.commit()
                            conn.close()
                            if record!=None:
                                #update
                                conn=sqlite3.connect('samaria database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE LOANS SET
                                            Customer_ID=:c_id,
                                            First_Name=:f_name,
                                            Last_Name=:l_name,
                                            Pending_Loan=:pen_l,
                                            Loan_Amount=:lamount,
                                            Total_Loan=:t_loan,
                                            STATUS=:stxz,
                                            MONTH=:mnth,
                                            YEAR=:raey,
                                            DATE=:date,
                                            PERIOD=:pwdz
                                        
                                            WHERE Customer_ID=:c_id AND PERIOD=:pwdz""",
                                            {
                                                'c_id': record[0],
                                                'f_name': record[1],
                                                'l_name': record[2],
                                                'pen_l':0.0,
                                                'lamount':0.0,
                                                't_loan':0.0,
                                                'stxz':"PAID",
                                                'mnth':record[7],
                                                'raey':record[8],
                                                'date':record[9],
                                                'pwdz':record[10]
                                                })
                                conn.commit()
                                conn.close()
                                #insert
                                new_l=abs(self.m_bal)
                                conn=sqlite3.connect('samaria database.db')
                                c=conn.cursor()
                                c.execute("INSERT INTO LOANS VALUES(:Customer_ID,:First_Name,:Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS,:MONTH,:YEAR,:DATE,:PERIOD)",
                                          {
                                              'Customer_ID':self.farmer_id_entry.get(),
                                              'First_Name':self.f_name,
                                              'Last_Name':self.l_name,
                                              'Pending_Loan':0.0,
                                              'Loan_Amount':new_l,
                                              'Total_Loan':new_l,
                                              'STATUS':"NOT PAID",
                                              'MONTH':self.n_m_month,
                                              'YEAR':self.mwaka,
                                              'DATE':self.today,
                                              'PERIOD':"From 1-15"
                                              })
                                conn.commit()
                                conn.close()
                        else:
                            #insert our details to database
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("INSERT INTO Payments VALUES(:FIRST_NAME, :LAST_NAME, :CUSTOMER_ID,:PERIOD, :MONTHLY_TOTAL, :MONTHLY_RATE, :STATUS, :MONTHLY_WAGES, :PENDING_LOAN, :PENDING_FEEDS,:Transport_Fee, :REMAINING_BALANCE, :MONTH, :YEAR,:DATE)",
                                        {
                                            'FIRST_NAME': self.f_name,
                                            'LAST_NAME': self.l_name,
                                            'CUSTOMER_ID': self.farmer_id_entry.get(),
                                            'PERIOD':self.clicked2.get(),
                                            'MONTHLY_TOTAL': self.mwezi_1st,
                                            'MONTHLY_RATE': self.set_rate_entry2.get(),
                                            'STATUS': "PAID",
                                            'MONTHLY_WAGES': self.m_wages,
                                            'PENDING_LOAN': self.m_loan,
                                            'PENDING_FEEDS': self.m_feeds,
                                            'Transport_Fee': self.t_m_fee,
                                            'REMAINING_BALANCE':self.m_bal,
                                            'MONTH': self.monthm,
                                            'YEAR': self.year_choose.get(),
                                            'DATE': self.today
                                            })
                            conn.commit()
                            conn.close()
                            #update transport table
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM Transport WHERE Farmer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            all_transport=c.fetchall()
                            conn.commit()
                            conn.close()
                            for record in all_transport:
                                conn=sqlite3.connect('samaria feeds database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE Transport SET
                                            Farmer_ID=:f_id,
                                            Transport_Amount=:t_amount,
                                            Status=:stus,
                                            DATE=:siku,
                                            PERIOD=:pwds

                                            WHERE Farmer_ID=:f_id AND DATE=:siku AND PERIOD=:pwds""",
                                          {
                                              'f_id':record[0],
                                              't_amount':record[1],
                                              'stus':"PAID",
                                              'siku':record[3],
                                              'pwds':record[4]
                                              })
                                conn.commit()
                                conn.close()
                            #update feeds table
                            conn=sqlite3.connect('samaria feeds database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM FEEDS WHERE Customer_ID=? AND Status=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            unpaid_feeds=c.fetchall()
                            conn.commit()
                            conn.close()
                            for record in unpaid_feeds:
                                conn=sqlite3.connect('samaria feeds database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE FEEDS SET
                                            First_Name=:f_jina, 
                                            Last_Name=:l_jina,
                                            Customer_ID=:customerid,
                                            Feed_Names=:feed_jina,
                                            Feed_Quantity=:feed_amount,
                                            Price=:pesa,
                                            Total_Cost=:pesa_total,
                                            Status=:stsz,
                                            MONTH=:mhtm,
                                            YEAR=:mwks,
                                            DATE=:leo,
                                            PERIOD=:pwdx

                                            WHERE Customer_ID=:customerid AND Feed_Names=:feed_jina AND PERIOD=:pwdx""",
                                          {
                                              'f_jina':record[0],
                                              'l_jina':record[1],
                                              'customerid':self.farmer_id_entry.get(),
                                              'feed_jina':record[3],
                                              'feed_amount':record[4],
                                              'pesa':record[5],
                                              'pesa_total':record[6],
                                              'stsz':"PAID",
                                              'mhtm':record[8],
                                              'mwks':record[9],
                                              'leo':record[10],
                                              'pwdx':record[11]
                                              })
                                conn.commit()
                                conn.close()
                            #update loans table
                            conn=sqlite3.connect('samaria database.db')
                            c=conn.cursor()
                            c.execute("SELECT * FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.farmer_id_entry.get(),"NOT PAID","From 16",))
                            record=c.fetchone()
                            conn.commit()
                            conn.close()
                            if record!=None:
                                #update
                                conn=sqlite3.connect('samaria database.db')
                                c=conn.cursor()
                                c.execute("""UPDATE LOANS SET
                                            Customer_ID=:c_id,
                                            First_Name=:f_name,
                                            Last_Name=:l_name,
                                            Pending_Loan=:pen_l,
                                            Loan_Amount=:lamount,
                                            Total_Loan=:t_loan,
                                            STATUS=:stxz,
                                            MONTH=:mnth,
                                            YEAR=:raey,
                                            DATE=:date,
                                            PERIOD=:pwdv
                                        
                                            WHERE Customer_ID=:c_id AND PERIOD=:pwdv""",
                                            {
                                                'c_id': record[0],
                                                'f_name': record[1],
                                                'l_name': record[2],
                                                'pen_l':0.0,
                                                'lamount':0.0,
                                                't_loan':0.0,
                                                'stxz':"PAID",
                                                'mnth':record[7],
                                                'raey':record[8],
                                                'date':record[9],
                                                'pwdv':record[10]
                                                })
                                conn.commit()
                                conn.close()
                        messagebox.showinfo("BRAVO","Farmer Paid Succesfully",parent=self.top89)
                        #clear entries
                        self.farmer_id_entry.delete(0,END)
                        self.first_name_entry.delete(0,END)
                        self.phone_number_entry.delete(0,END)
                        self.balance_entry.delete(0,END)
                        #refresh treeview
                        self.my_tree2.delete(* self.my_tree2.get_children())
                        self.mpesa_data()
    #pay mpesas
    def pay_mpesas(self):
        self.top13=Toplevel()
        self.top13.geometry("500x150")
        self.top13.title("SAMARIA MILK GROUP")
        self.top13.iconbitmap("logo1.ico")
        my_frame=Frame(self.top13)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=customtkinter.CTkLabel(my_frame, text="Enter Administrator Password:", fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=30)
        self.admin_passcode_label.grid(row=0, column=0, columnspan=2,padx=20, pady=10)
        self.admin_passcode_entry=customtkinter.CTkEntry(my_frame, width=150,height=30,border_color="blue", show="*")
        self.admin_passcode_entry.grid(row=0, column=2)
        self.submit_passcode_button=customtkinter.CTkButton(my_frame, text="SUBMIT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40, command=self.verify_mpesa_admin)
        self.submit_passcode_button.grid(row=1, column=0, columnspan=4, padx=20, pady=10)
    #notifications
    def notifications(self):
        #toplevel
        self.top40=Toplevel()
        self.top40.iconbitmap("logo1.ico")
        self.top40.title("SAMARIA MILK GROUP")
        self.title_frame=Frame(self.top40)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="STATUS SMS"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.send_button=customtkinter.CTkButton(self.title_frame,text="Send Messages",fg_color="green",text_color="white",text_font=("Consollas 10",-25,"bold"),width=200,height=40,command=self.send_bulk_messages)
        self.send_button.grid(row=3,column=0,columnspan=15,padx=10,pady=20,ipadx=30,ipady=30)
        self.print_button=customtkinter.CTkButton(self.title_frame,text="PRINT OUT",fg_color="purple",text_color="white",text_font=("Consollas 10",-25,"bold"),width=200,height=40,command=self.print_entire_printout)
        self.print_button.grid(row=4,column=0,columnspan=15,padx=10,pady=20,ipadx=30,ipady=30)
    def select_notify_month(self):
        self.top55=Toplevel()
        self.top55.iconbitmap("logo1.ico")
        self.top55.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top55)
        my_frame.pack()
        self.month_name_label=customtkinter.CTkLabel(my_frame,text="Select Month:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.month_name_label.grid(row=0,column=0,padx=20,pady=10,columnspan=2)
        self.month_select_menu=customtkinter.CTkOptionMenu(my_frame,variable=self.month_chooser,command=self.choose_notify_month,values=["January","February","March","April","May","June","July","August","September","October","November","December"],fg_color="red",text_color="white",width=150,height=30)
        self.month_select_menu.grid(row=0,column=2,columnspan=2,padx=5)
        self.year_select_menu=customtkinter.CTkOptionMenu(my_frame,variable=self.chagua_mwaka,values=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}'],fg_color="red",text_color="white",width=150,height=30)
        self.year_select_menu.grid(row=0,column=4,columnspan=2,padx=5)
    def enter_rate(self):
        self.top56=Toplevel()
        self.top56.iconbitmap("logo1.ico")
        self.top56.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top56)
        my_frame.pack()
        self.enter_rate_label=customtkinter.CTkLabel(my_frame,text="Enter Monthly Rate(Kshs):",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.enter_rate_label.grid(row=0,column=0,padx=20,pady=10,columnspan=2)
        self.rate_entry=customtkinter.CTkEntry(my_frame,border_color="green",width=200,height=30)
        self.rate_entry.grid(row=0,column=2,columnspan=2,padx=5)
        self.ok_button=customtkinter.CTkButton(my_frame, text="OK",text_color="white",fg_color="purple",text_font=("Consollas 10",-17,"bold"),width=200,height=30,command=self.notifications)
        self.ok_button.grid(row=1,column=0,columnspan=4,sticky=EW,padx=20,pady=10)
    def choose_notify_month(self,arg=None):
        if self.month_chooser.get()=="January":
            self.mwezi=1
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="February":
            self.mwezi=2
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="March":
            self.mwezi=3
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="April":
            self.mwezi=4
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="May":
            self.mwezi=5
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="June":
            self.mwezi=6
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="July":
            self.mwezi=7
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="August":
            self.mwezi=8
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="September":
            self.mwezi=9
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="October":
            self.mwezi=10
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="November":
            self.mwezi=11
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
        if self.month_chooser.get()=="December":
            self.mwezi=12
            m_details=calendar.monthrange(self.mwaka,self.mwezi)
            self.last_day=m_details[1]
            self.top55.destroy()
            self.select_notify_period()
    #select period
    def select_notify_period(self):
        if self.chagua_mwaka.get()=="":
            messagebox.showerror("ERROR","Please Choose Year First",parent=self.top0)
        else:
            self.top98=Toplevel()
            self.top98.title("SAMARIA MILK GROUP")
            self.top98.iconbitmap("logo1.ico")
            top_frame=Frame(self.top98)
            top_frame.pack(anchor="w")
            select_label=customtkinter.CTkLabel(top_frame,text="SELECT Period:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
            select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
            mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.period_chooser,command=self.close_notify_period,values=[f'From 1-15',f'From 16-{self.last_day}'],width=160,height=25,fg_color="red",text_color="white")
            mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def close_notify_period(self,e):
        get_period=self.month_chooser.get()
        self.top98.destroy()
        self.enter_rate()
    #send bulk messages
    def send_bulk_messages(self):
        #query
        conn=sqlite3.connect('samaria database.db')
        #conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Customer_ID,Phone_Number FROM Customers ORDER BY Customer_ID ASC")
        all_phones=c.fetchall()
        c.execute("SELECT COUNT(Phone_Number) FROM Customers")
        all_no=c.fetchone()
        conn.commit()
        conn.close()
        self.rate=self.rate_entry.get()
        if self.rate=='':
            messagebox.showerror("ERROR","Please Enter Monthly Rate",parent=self.top0)
            self.top56.destroy()
        else:
            for record in all_phones:
                if record[1]!='':
                    #names
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT First_name FROM Customers WHERE Customer_ID=?",(record[0],))
                    f_name=c.fetchone()
                    c.execute("SELECT Last_name FROM Customers WHERE Customer_ID=?",(record[0],))
                    l_name=c.fetchone()
                    conn.commit()
                    conn.close()
                    if self.period_chooser.get()=="From 1-15":
                        try:
                            #monthly_totals
                            conn=sqlite3.connect('samaria database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 1 AND 15",(self.mwezi, self.chagua_mwaka.get(), record[0],))
                            accumulated_period=c.fetchone()
                            if accumulated_period==None:
                                accumulated_period=0.0
                            conn.commit()
                            conn.close()
                        except:
                            messagebox.showerror("ERROR","Please Choose Month",parent=self.top0)
                    else:
                        try:
                            #monthly_totals
                            conn=sqlite3.connect('samaria database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 16 AND 'self.last_day'",(self.mwezi, self.chagua_mwaka.get(),record[0],))
                            accumulated_period=c.fetchone()
                            if accumulated_period==None:
                                accumulated_period=0.0
                            conn.commit()
                            conn.close()
                        except:
                            messagebox.showerror("ERROR", "Please Choose Month",parent =self.top0)
                    #monthly wages
                    total_wages=float(accumulated_period) * float(self.rate)
                    #pending loan
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Loan_Amount) FROM LOANS WHERE Customer_ID=? AND STATUS=?",(record[0],"NOT PAID",))
                    p_loan=c.fetchone()
                    if p_loan==None:
                        p_loan=0.0
                    conn.commit()
                    conn.close()
                    #feeds
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=?",(record[0],"NOT PAID",))
                    p_feeds=c.fetchall()
                    p_f_total=0.0
                    if p_feeds==[]:
                        p_f_total=0.0
                    else:
                        for x in p_feeds:
                            p_f_total+=x
                    conn.commit()
                    conn.close()
                    #transport fee
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=?",(record[0],"NOT PAID",))
                    p_trans=c.fetchone()
                    if p_trans==None:
                        p_trans=0.0
                    conn.commit()
                    conn.close()
                    #balance
                    bal=(total_wages - (p_loan+p_f_total+p_trans))
                    #status
                    conn=sqlite3.connect("samaria database.db")
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND PERIOD=? AND CUSTOMER_ID=?",(self.mwezi,self.chagua_mwaka.get(),self.period_chooser.get(),record[0],))
                    period_status=c.fetchone()
                    print(period_status)
                    conn.commit()
                    conn.close()
                    if period_status=="PAID":
                        messagebox.showinfo("Notice",f'{f_name} {l_name} Already Paid, Next...',parent=self.top40)
                        continue
                    else:
                        #message
                        farmer_message=f'SAMARIA MILK GROUP NAME:{f_name} {l_name} Farmer_ID:{record[0]} DATE:{self.today2} PERIOD:{self.period_chooser.get()} {self.month_chooser.get()} {self.chagua_mwaka.get()} Accumulated_Total:{accumulated_period} Litres Monthly_Rate:Kshs {self.rate} Total_Wages:Kshs {total_wages} Pending_Advance:Kshs {p_loan} Pending_Feeds:Kshs {p_f_total} Feeds_Transport:Kshs {p_trans} Balance:Kshs {bal} Served By:{server}'
                        try:
                            #requests mobitechtechnologies
                            url = "https://api.mobitechtechnologies.com/sms/sendsms"

                            payload = json.dumps({
                                "mobile": f'+254{record[1]}',
                                "response_type": "json",
                                "sender_name": 23107,
                                "service_id": 0,
                                "message": farmer_message
                            })
                            headers = {
                                'h_api_key': 'ead62d3ed9c918bb366cba5ec6692224d8926bd8b0c339c0a58cc137075b3e4a',
                                'Content-Type': 'application/json'
                            }

                            response = requests.request("POST", url, headers=headers, data=payload)
                            print(response.text)
                            x=response.text[20]
                            print(x)
                            if x != '0':
                                messagebox.showerror("ERROR",f'SMS NOT Sent,Please Recharge your Account And Try Again',parent=self.top40)
                                break
                            else:
                                messagebox.showinfo("BRAVO",f'SMS Sent Succesfully to {f_name} {l_name}',parent=self.top40)
                        except:
                            messagebox.showerror("ERROR","SMS Not Sent,Please Check Your Internet Connectivity And Try Again",parent=self.top40)
                            break
            self.top56.destroy()
    def print_entire_printout(self):
        #toplevel
        self.top40=Toplevel()
        self.top40.iconbitmap("logo1.ico")
        self.top40.title("SAMARIA MILK GROUP")
        self.top40.state('zoomed')
        self.title_frame=Frame(self.top40)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="Period Printout"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top40,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.notify_title_label=customtkinter.CTkLabel(self.left_frame,text="Report",fg_color="brown",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30)
        self.notify_title_label.grid(row=0,column=0,columnspan=10,padx=20,pady=15,sticky=EW)
        self.my_receipt40=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=20)
        self.my_receipt40.grid(row=1,column=0,columnspan=10,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=self.print_printout)
        self.print_button.grid(row=2,column=0,columnspan=15,padx=10,pady=10)
        self.printout_now()
    def print_printout(self):
        printText=self.my_receipt40.get('1.0', 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt40.delete('1.0', 'end')
        self.top56.destroy()
        self.top40.destroy()
    def printout_now(self):
        #receipt
        #define headings
        title2="SAMARIA MILK GROUP"
        sub2="Quality Milk, Healthy Life"
        headings0=f'Payment Rollout For{self.month_chooser.get()}'
        headings1=f'Period: {self.period_chooser.get()}'
        headings2=f'Date: {self.today2}'
        #first delete the text columns
        self.my_receipt40.delete('1.0', 'end')
        self.my_receipt40.insert('end', "\n" +"\t"+"\t"+"\t"+ title2 + "\n")
        self.my_receipt40.insert('end', "\n" +"\t"+"\t"+"\t"+ sub2 + "\n")
        self.my_receipt40.insert('end', "\n" +"\t"+"\t"+"\t"+ headings0 + "\n")
        self.my_receipt40.insert('end', "\n" +"\t"+"\t"+"\t"+ headings1 + "\n")
        self.my_receipt40.insert('end', "\n" +"\t"+"\t"+"\t"+ headings2 + "\n")
        self.my_receipt40.insert('end', "\n" + "NAME"+"\t"+"\t"+"ID"+" Quantity"+" Rate(Kshs)"+" Wages"+" Advance"+" Feeds"+" Transport"+"  Balance"+"\n")
        #query
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT Customer_ID FROM Customers ORDER BY Customer_ID ASC ")
        all_phones=c.fetchall()
        conn.commit()
        conn.close()
        self.rate=self.rate_entry.get()
        if self.rate=='':
            messagebox.showerror("ERROR","Please Enter Monthly Rate",parent=self.top0)
            self.top56.destroy()
        else:
            total_positive=0.0
            total_negative=0.0
            for record in all_phones:
                #status
                conn=sqlite3.connect("samaria database.db")
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT STATUS FROM Payments WHERE MONTH=? AND YEAR=? AND PERIOD=? AND CUSTOMER_ID=?",(self.mwezi,self.chagua_mwaka.get(),self.period_chooser.get(),record[0],))
                period_status=c.fetchone()
                conn.commit()
                conn.close()
                if period_status=="PAID":
                    conn=sqlite3.connect("samaria database.db")
                    #conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT * FROM Payments WHERE Customer_ID=? AND PERIOD=? AND MONTH=? AND YEAR=?",(record[0],self.period_chooser.get(),self.mwezi,self.chagua_mwaka.get(),))
                    all_data=c.fetchone()
                    conn.commit()
                    conn.close()
                    bal=float(all_data[7]) - float(all_data[9] + all_data[8] + all_data[10])
                    self.my_receipt40.insert('end', "\n" +str(all_data[0])+"\t"+"\t"+str(record[0])+"\t"+str(all_data[4])+"\t"+str(all_data[5])+"\t"+str(all_data[7])+"\t"+str(all_data[8])+"\t"+str(all_data[9])+"\t"+str(all_data[10])+"\t"+str(bal)+"\t"+str(period_status)+"\n")
                else:
                    #names
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT First_name FROM Customers WHERE Customer_ID=?",(record[0],))
                    f_name=c.fetchone()
                    c.execute("SELECT Last_name FROM Customers WHERE Customer_ID=?",(record[0],))
                    l_name=c.fetchone()
                    conn.commit()
                    conn.close()
                    if self.period_chooser.get()=="From 1-15":
                        try:
                            #monthly_totals
                            conn=sqlite3.connect('samaria database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 1 AND 15",(self.mwezi, self.chagua_mwaka.get(), record[0],))
                            accumulated_period=c.fetchone()
                            if accumulated_period==None:
                                accumulated_period=0.0
                            conn.commit()
                            conn.close()
                        except:
                            messagebox.showerror("ERROR","Please Choose Month",parent=self.top0)
                    else:
                        try:
                            #monthly_totals
                            conn=sqlite3.connect('samaria database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT SUM(Daily_Accumulated) FROM Daily_Totals WHERE MONTH=? AND YEAR=? AND Customer_ID=? AND DAY BETWEEN 16 AND 'self.last_day'",(self.mwezi, self.chagua_mwaka.get(),record[0],))
                            accumulated_period=c.fetchone()
                            if accumulated_period==None:
                                accumulated_period=0.0
                            conn.commit()
                            conn.close()
                        except:
                            messagebox.showerror("ERROR", "Please Choose Month",parent =self.top0)
                    #monthly wages
                    total_wages=float(accumulated_period) * float(self.rate)
                    #pending loan
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Loan_Amount) FROM LOANS WHERE Customer_ID=? AND STATUS=?",(record[0],"NOT PAID",))
                    p_loan=c.fetchone()
                    print(p_loan)
                    if p_loan==None:
                        p_loan=0.0
                    conn.commit()
                    conn.close()
                    #feeds
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM FEEDS WHERE Customer_ID=? AND Status=?",(record[0],"NOT PAID",))
                    p_feeds=c.fetchall()
                    p_f_total=0.0
                    if p_feeds==[]:
                        p_f_total=0.0
                    else:
                        for x in p_feeds:
                            p_f_total+=x
                    conn.commit()
                    conn.close()
                    #transport fee
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Transport_Amount) FROM Transport WHERE Farmer_ID=? AND Status=?",(record[0],"NOT PAID",))
                    p_trans=c.fetchone()
                    if p_trans==None:
                        p_trans=0.0
                    conn.commit()
                    conn.close()
                    #balance
                    bal=(total_wages - (p_loan+p_f_total+p_trans))
                    self.my_receipt40.insert('end', "\n" +str(f_name)+"\t"+"\t"+str(record[0])+"\t"+str(accumulated_period)+"\t"+str(self.rate)+"\t"+str(total_wages)+"\t"+str(p_loan)+"\t"+str(p_f_total)+"\t"+str(p_trans)+"\t"+str(bal)+"\n")
                if bal >0:
                    total_positive+=bal
                else:
                    total_negative+=abs(bal)
            self.my_receipt40.insert('end', "\n" +"Total Payable Kshs:"+"\t"+str(total_positive)+"\n")
            self.my_receipt40.insert('end', "\n" +"Total Negatives Kshs:"+"\t"+str(total_negative)+"\n")
            self.my_receipt40.insert('end', "\n" +"Served By:"+"\t"+server+"\n")
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
class Local_Sales:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x1000")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
         #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)

        add_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Creditors", menu=add_menu)
        add_menu.add_command(label="Add Creditor Name", command=self.add_creditor_name)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        report_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Report", menu=report_menu)
        report_menu.add_command(label="Creditor Report",command=self.creditor_report)
        
        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)
        
        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)
    
        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="LOCAL SALES"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #variables
        self.remainder=0.0
        self.total=0.0
        self.start=2
        self.start1=2
        self.count=0
        self.time=datetime.now()
        self.currentdatetime=date.today()
        self.yesterday=datetime.now() - timedelta(2)
        self.yesterday1=self.yesterday.strftime("%m/%d/%Y")
        self.today=self.currentdatetime.strftime("%A-%B %d, %Y")
        self.today1=self.time.strftime("%m/%d/%Y")
        self.Time=self.time.strftime("%I:%M:%S,%p")
        self.selection=self.today1
        self.selected_date=self.today1
        self.mwezi=datetime.now().month
        self.mwaka=datetime.now().year
        print(self.selection)
        #database
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        #drop table
        '''
        c.execute("DROP TABLE Tenders")
        c.execute("DROP TABLE Creditors")
        print("table dropped successfully")
        '''
        #create tender table
        c.execute("""CREATE TABLE IF NOT EXISTS Tenders(
                    Tender_Name TEXT NOT NULL,
                    Quantity REAL NOT NULL,
                    DATE INT NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL,
                    STATUS TEXT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS Creditors(
                    CREDITOR_NAME TEXT PRIMARY KEY NOT NULL
                    )""")
        conn.commit()
        conn.close()
        #get daily milk quantity
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Daily_Accumulated FROM DAILY_TOTALS WHERE DATE=(?)", (self.selection,))
        records=c.fetchall()
        conn.commit()
        conn.close()
        self.daily=0.0
        self.daily=sum(records)
        print(self.daily)
        #left_frame
        #variable
        self.t=StringVar()
        self.r=StringVar()
        self.svar=StringVar()
        #database
        conn=sqlite3.connect("samaria database.db")
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT CREDITOR_NAME FROM Creditors")
        creditors=c.fetchall()
        if creditors==None:
            creditors=[]
        print(creditors)
        conn.commit()
        conn.close()
        #frame
        self.left_frame=customtkinter.CTkFrame(self.top0,border_color="green",border_width=5, width=400,height=450)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #labels
        self.tender_title="CREDITORS"
        self.tender_title_label=customtkinter.CTkLabel(self.left_frame, text=self.tender_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"underline","bold"),width=200,height=30)
        self.tender_title_label.grid(row=0, column=0,columnspan=4,pady=5) 
        self.date_label=customtkinter.CTkLabel(self.left_frame, text="Today:",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.date_label.grid(row=1, column=0, sticky=W, padx=10, pady=2)
        self.today_label=customtkinter.CTkLabel(self.left_frame, text=self.today)
        self.today_label.grid(row=1, column=1, sticky=W)
        self.daily_accumulated_label=customtkinter.CTkLabel(self.left_frame, text="Daily Milk Quantity:",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.daily_accumulated_label.grid(row=2, column=0,columnspan=2, padx=10)
        self.daily_accumulated_label1=customtkinter.CTkLabel(self.left_frame, text=f"{self.daily} Litres")
        self.daily_accumulated_label1.grid(row=3, column=0, columnspan=2)
        #treeview frame
        self.tree_frame=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,height=200, bd=0)
        self.tree_frame.grid(row=5,column=0,padx=10,columnspan=5)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree=ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=5)
        self.my_tree.pack()
        #configure the scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)
        #define our columns
        self.my_tree['columns']=("Creditor Name", "Quantity", "Date","Status")
        #format our columns
        self.my_tree.column("#0", width=0,stretch=NO)
        self.my_tree.column("Creditor Name", anchor="w", width=150)
        self.my_tree.column("Quantity", anchor="w", width=100)
        self.my_tree.column("Date", anchor="w", width=90)
        self.my_tree.column("Status", anchor="w", width=90)
        #create headings
        self.my_tree.heading("#0", text="")
        self.my_tree.heading("Creditor Name", text="Creditor Name", anchor="w")
        self.my_tree.heading("Quantity", text="Quantity(LTRS)", anchor="w")
        self.my_tree.heading("Date", text="Date", anchor="w")
        self.my_tree.heading("Status", text="Status", anchor="w")
        self.total_entry=customtkinter.CTkEntry(self.tree_frame,width=120,height=25,border_color="blue",textvariable=self.t)
        self.total_entry.pack(anchor="e",pady=2)
        #create striped row tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="violet")
        #binding function
        self.my_tree.bind("<ButtonRelease-1>", self.clicker1)
        #entry labels
        self.choose_tender_name_label=customtkinter.CTkLabel(self.left_frame, text="Choose Creditor Name:",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.choose_tender_name_label.grid(row=6,padx=7,column=0,pady=2,sticky=W)
        self.tender_name_label=customtkinter.CTkLabel(self.left_frame, text="Enter Creditor Name:",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.tender_name_label.grid(row=7,padx=7,column=0,pady=2,sticky=W)
        self.quantity_label=customtkinter.CTkLabel(self.left_frame, text="Enter Quantity:",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.quantity_label.grid(row=8, column=0, padx=10, pady=2,sticky=W)
        self.status_label=customtkinter.CTkLabel(self.left_frame, text="Mark as PAID?",fg_color="brown", text_color="white", text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.status_label.grid(row=9, column=0, padx=10, pady=2,sticky=W)
        #variable
        self.chooser=StringVar()
        #entry boxes
        self.choice_menu=customtkinter.CTkOptionMenu(self.left_frame,width=200,height=25,fg_color="red",text_color="white",variable=self.chooser,values=creditors,command=self.insert_creditor)
        self.choice_menu.grid(row=6,column=1,sticky=W)
        self.tender_name_entry=customtkinter.CTkEntry(self.left_frame,width=170,height=25,border_color="blue")
        self.tender_name_entry.grid(row=7, column=1,sticky=W)
        self.quantity_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue")
        self.quantity_entry.grid(row=8, column=1, sticky=W)
        self.status_c =customtkinter.CTkCheckBox(self.left_frame,text="",variable=self.svar, onvalue="PAID", offvalue="NOT PAID")
        self.status_c.deselect()
        self.status_c.grid(row=9, column=1, sticky=W)
        #buttons
        self.date_chooser_button=customtkinter.CTkButton(self.left_frame, text="Choose Date", fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=150, height=30,command=self.grab_date)
        self.date_chooser_button.grid(row=4, column=0,sticky=W,padx=10,pady=3)
        self.add_button=customtkinter.CTkButton(self.left_frame, text="Add Order",fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=150, height=30,command=self.add_record)
        self.add_button.grid(row=10, column=0,columnspan=2,padx=30,pady=3,)
        self.update_button=customtkinter.CTkButton(self.left_frame, text="Update Order", fg_color="purple", text_color="white", text_font=("Consollas 10", -15, "bold"),width=150, height=30,command=self.update_record)
        self.update_button.grid(row=10, column=2,padx=5,pady=3,sticky=W)
        #remaining quantity
        self.remaining_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Remaining Quantity For Local Sale:", fg_color="brown",text_color="white",text_font=("Consollas 10", -13, "bold"),width=120, height=25)
        self.remaining_quantity_label.grid(row=11, column=0, columnspan=2,sticky=W, padx=10, pady=5)
        self.remaining_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue",textvariable=self.r)
        self.remaining_quantity_entry.grid(row=11, column=2,padx=10,sticky=W)
        self.query_database()
        self.get_total()
        self.get_remainder()
        #*******************************************************************************************************************************************************************************************************
        #Right frame
        self.right_frame=customtkinter.CTkFrame(self.top0,border_color="purple",border_width=5,width=800,height=450)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #heading
        tender_title="OUR PRODUCTS"
        self.tender_title_label=customtkinter.CTkLabel(self.right_frame, text=tender_title, fg_color="orange", text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
        self.tender_title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=5)
        #create a treeview
        self.tree_frame3=Frame(self.right_frame, highlightbackground="green", highlightthickness=5, bd=0)
        self.tree_frame3.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky=W)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll3=Scrollbar(self.tree_frame3)
        self.tree_scroll3.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree3=ttk.Treeview(self.tree_frame3, yscrollcommand=self.tree_scroll3.set,height=9)
        #configure the scrollbar
        self.tree_scroll3.config(command=self.my_tree3.yview)
        #define our columns
        self.my_tree3['columns']=("PRODUCT NAME","QUANTITY","PRICE")
        #format our columns
        self.my_tree3.column("#0", width=0,stretch=NO)
        self.my_tree3.column("PRODUCT NAME", anchor="w", width=180)
        self.my_tree3.column("QUANTITY", anchor="w", width=120)
        self.my_tree3.column("PRICE", anchor="w", width=120)
        #create headings
        self.my_tree3.heading("#0", text="")
        self.my_tree3.heading("PRODUCT NAME", text="PRODUCT NAME", anchor="w")
        self.my_tree3.heading("QUANTITY", text="QUANTITY(LTRS)", anchor="w")
        self.my_tree3.heading("PRICE", text="PRICE(KSHS)", anchor="w")
        #striped row tags
        self.my_tree3.tag_configure('oddrow', background="white")
        self.my_tree3.tag_configure('evenrow', background="violet")
        self.my_tree3.pack()
        #single click binding
        self.my_tree3.bind("<ButtonRelease-1>", self.clicker2)
        #connect to the database
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE Products")
        print("table dropped successfully")
        c.execute("DROP TABLE Local_Sales")
        print("table dropped succesfully")
        c.execute("DROP TABLE Product_Records")
        print("table dropped succesfully")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS Products(
                    PRODUCT_NAME TEXT NOT NULL PRIMARY KEY,
                    PRODUCT_QUANTITY INT NOT NULL,
                    PRICE REAL NOT NULL,
                    MONTH INT NOT NULL,
                    YEAR INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS Local_Sales(
                        Product_Name TEXT NOT NULL,
                        Quantity INT NOT NULL,
                        Price REAL NOT NULL,
                        Total REAL NOT NULL,
                        Date INT NOT NULL
                        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS Product_Records(
                        Product_Name TEXT NOT NULL,
                        Product_Quantity INT NOT NULL,
                        DATE INT NOT NULL
                        )""")
        conn.commit()
        conn.close()
        print("table created succesfully")
         #labels
        self.product_name_label=customtkinter.CTkLabel(self.right_frame, text="Product's NAME:", fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.product_name_label.grid(row=2, column=0, padx=10,sticky=W,pady=5)
        self.product_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Product's QUANTITY:", fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.product_quantity_label.grid(row=3, column=0, padx=10, sticky=W, pady=5)
        self.product_price_label=customtkinter.CTkLabel(self.right_frame, text="Product's PRICE(KSHS):", fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.product_price_label.grid(row=4, column=0, padx=10, sticky=W, pady=5)
        #entry boxes
        self.product_name_entry=customtkinter.CTkEntry(self.right_frame, width=170,height=25,border_color="blue")
        self.product_name_entry.grid(row=2, column=1, sticky=W)
        self.product_quantity_entry=customtkinter.CTkEntry(self.right_frame, width=120,height=25,border_color="blue")
        self.product_quantity_entry.grid(row=3, column=1, sticky=W)
        self.product_price_entry=customtkinter.CTkEntry(self.right_frame, width=120,height=25,border_color="blue")
        self.product_price_entry.grid(row=4, column=1, sticky=W)
        #buttons
        self.add_product_button=customtkinter.CTkButton(self.right_frame, text="ADD PRODUCT",fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"bold"),width=150,height=30,command=self.verify_admin)
        self.add_product_button.grid(row=5, column=0,sticky=W, padx=10, pady=10)
        self.increase_stock_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red", text_color="white", text_font=("Consollas 10", -20,"bold"),width=150,height=30,command=self.verify_admin2)
        self.increase_stock_button.grid(row=5, column=1,padx=10,pady=10,sticky=W)
        self.update_price_button=customtkinter.CTkButton(self.right_frame, text="UPDATE PRICE",fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"bold"),width=150,height=30,command=self.verify_admin1)
        self.update_price_button.grid(row=6, column=0,padx=10, pady=10)
        self.delete_product_button=customtkinter.CTkButton(self.right_frame, text="DELETE PRODUCT",fg_color="red", text_color="white", text_font=("Consollas 10", -20,"bold"),width=150,height=30,command=self.verify_admin3)
        self.delete_product_button.grid(row=6, column=1, padx=10, pady=10)
        self.query_database1()
        # center frame
        self.center_frame=customtkinter.CTkFrame(self.top0,border_color="maroon",border_width=5, width=800,height=450)
        self.center_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #heading
        tender_title="PRODUCTS SALES"
        self.tender_title_label=customtkinter.CTkLabel(self.center_frame, text=tender_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
        self.tender_title_label.grid(row=0, column=0, columnspan=4, pady=5)
        self.order_button=customtkinter.CTkButton(self.center_frame, text="ORDER PRODUCTS",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=120, height=30,command=self.choose_product)
        self.order_button.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
        #define our variable
        self.t1=StringVar()
        self.t2=StringVar()
        #treeview frame
        self.tree_frame1=Frame(self.center_frame, highlightbackground="green", highlightthickness=5,bd=0)
        self.tree_frame1.grid(row=3,column=0, columnspan=4,padx=10)
        #create a treeview
        #style a treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll1=Scrollbar(self.tree_frame1)
        self.tree_scroll1.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree1=ttk.Treeview(self.tree_frame1, yscrollcommand=self.tree_scroll1.set, height=10)
        #configure the scrollbar
        self.tree_scroll1.config(command=self.my_tree1.yview)
        #define our columns
        self.my_tree1['columns']=("Product Name", "Quantity", "Total")
        #format our columns
        self.my_tree1.column("#0", width=0,stretch=NO)
        self.my_tree1.column("Product Name", anchor="w", width=130)
        self.my_tree1.column("Quantity", anchor="w", width=90)
        self.my_tree1.column("Total", anchor="w", width=90)
        #create headings
        self.my_tree1.heading("#0", text="")
        self.my_tree1.heading("Product Name", text="Product Name", anchor="w")
        self.my_tree1.heading("Quantity", text="Quantity", anchor="w")
        self.my_tree1.heading("Total", text="Total", anchor="w")
        #striped row tags
        self.my_tree1.tag_configure('oddrow', background="white")
        self.my_tree1.tag_configure('evenrow', background="violet")
        self.my_tree1.pack()
        self.total_entry1=customtkinter.CTkEntry(self.tree_frame1,width=120,height=20,border_color="blue",textvariable=self.t1)
        self.total_entry1.pack(anchor="e", pady=5)
        #my_tree1.bind('<Control-a>', lambda * args: e.selection_add(e.get_children()))
        self.my_tree1.bind('<Control-c>', self.copy)
        #buttons
        self.print_button=customtkinter.CTkButton(self.center_frame, text="PRINT",fg_color="purple", text_color="white", text_font=("Consollas 10", -25, "bold"),width=150,height=30,command=self.copy)
        self.print_button.grid(row=4, column=0,columnspan=4, padx=10, pady=3)
    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    def add_creditor_name(self):
        self.top55=Toplevel()
        self.top55.iconbitmap("logo1.ico")
        self.top55.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top55)
        my_frame.pack()
        self.title_label=customtkinter.CTkLabel(my_frame,text="ADD CREDITOR",fg_color="maroon",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.creditor_name_label=customtkinter.CTkLabel(my_frame,text="Enter Creditor's Name:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.creditor_name_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
        self.creditor_name_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
        self.creditor_name_entry.grid(row=1,column=2,columnspan=2,padx=5)
        self.save_button=customtkinter.CTkButton(my_frame,text="ADD CREDITOR NAME",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.save_creditor_name)
        self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20)
    def save_creditor_name(self):
        self.top0.destroy()
        if self.creditor_name_entry.get()=="":
            messagebox.showerror("ERROR","Please Enter Creditor Name",parent=self.top55)
        else:
            try:
                conn=sqlite3.connect("samaria database.db")
                c=conn.cursor()
                c.execute("INSERT INTO Creditors VALUES(:CREDITOR_NAME)",
                          {
                              'CREDITOR_NAME':self.creditor_name_entry.get()
                          })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo","Creditor Name Added Succesfully",parent=self.top55)
            except:
                messagebox.showerror("ERROR","Creditor Name Already Exists",parent=self.top55)
            self.creditor_name_entry.delete(0,END)
            self.top55.destroy()
            l_sales=Local_Sales(root)
            root.mainloop()
    def insert_creditor(self,e):
        self.tender_name_entry.delete(0,END)
        self.tender_name_entry.insert(0,self.chooser.get())
    #clear entry boxes
    def clear_entries(self):
        self.tender_name_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
    def grab_date(self):
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        self.my_label=customtkinter.CTkLabel(self.top, text="Choose Date:", fg_color="purple",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=30).pack(anchor="center",padx=10,pady=10)
        self.cal=Calendar(self.top, selectmode="day", cursor="hand1", date_pattern="mm/dd/yyyy",year=self.currentdatetime.year,month=self.currentdatetime.month,day=self.currentdatetime.day)
        self.cal.pack(padx=10,pady=10, anchor="w")
        self.cal.bind("<<CalendarSelected>>", self.clicker)
    def clicker(self,e):
        self.selection=self.cal.get_date()
        self.total_entry.delete(0,END)
        self.query_database()
        self.get_total()
        self.cal.destroy()
        self.top.destroy()
    #create query function
    def query_database(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Tenders WHERE DATE=(?)", (self.selection,))
        records=c.fetchall()
        self.my_tree.delete(*self.my_tree.get_children())
        #add our data to the treeview
        for record in records:
            if self.count%2==0:
                self.my_tree.insert('',index='end', iid=self.count, text="", values=(record[0], record[1], record[2],record[5]), tags=("evenrow",))
            else:
                self.my_tree.insert('',index='end', iid=self.count, text="", values=(record[0], record[1], record[2], record[5]), tags=("oddrow",))
            self.count+=1
        conn.commit()
        conn.close()
    #total function
    def get_total(self):
        sum2=0.0
        for child in self.my_tree.get_children():
            sum2 += float(self.my_tree.item(child, "values")[1])
        self.t.set(sum2)
    #remainder function
    def get_remainder(self):
        self.remainder=self.daily-float(self.total_entry.get())
        self.r.set(self.remainder)
    
    #create binding function
    def clicker1(self,e):
        #clear entry boxes
        self.clear_entries()
        #grab record number
        selected=self.my_tree.focus()
        #grab record values
        values=self.my_tree.item(selected,'values')
        #output to entry boxes
        self.tender_name_entry.insert(0, values[0])
        self.quantity_entry.insert(0, values[1])
        #double click
        #my_tree.bind("<Double-1>", clicker)
        #single click(button release)
            
    #insert data into the treeview
    def add_record(self):
        #check
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Tender_Name FROM Tenders WHERE DATE=? AND STATUS=?",(self.today1,"NOT PAID",))
        t_creditor_name=c.fetchone()
        conn.commit()
        conn.close()
        if self.tender_name_entry.get() =="" :
            messagebox.showerror("Error", "Please enter Tender Name",parent =self.top0)
        elif self.quantity_entry.get() =="":
            messagebox.showerror("Error", "Please enter Tender Quantity",parent =self.top0)
        elif self.tender_name_entry.get()==t_creditor_name:
            messagebox.showerror("ERROR","Creditor Has A Record Today,Please Consider Updating That Record",parent=self.top0)
        else:
            try:
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                #add new record
                c.execute("INSERT INTO Tenders VALUES(:Tender_Name, :Quantity, :DATE, :Month, :Year, :STATUS)",
                            {                            
                                'Tender_Name': self.tender_name_entry.get(),
                                'Quantity': self.quantity_entry.get(),
                                'DATE': self.today1,
                                'Month' : self.mwezi,
                                'Year' : self.mwaka,
                                'STATUS': self.svar.get()
                                })
                c.execute("SELECT * FROM Tenders")
                zote=c.fetchall()
                print(zote)
                conn.commit()
                conn.close()
            except:
                messagebox.showerror("ERROR","Tender already Exists",parent=self.top0)
            #enter data into our treeview
            self.my_tree.insert('',index='end', iid=self.count, text="", values=(self.tender_name_entry.get(),self.quantity_entry.get(), self.today1, self.svar.get()))
            self.count+=1
            #clear entry boxes
            self.clear_entries()
            #refresh the treeview
            #clear the treeview
            self.my_tree.delete(* self.my_tree.get_children())
            #run to pull data again to the treeview from the database
            self.query_database()
            self.total_entry.delete(0, END)
            self.get_total()
            self.remaining_quantity_entry.delete(0, END)
            self.get_remainder()
    def get_amount_per_litre(self):
        self.top65=Toplevel()
        self.top65.iconbitmap("logo1.ico")
        self.top65.title=("SAMARIA MILK GROUP")
        my_frame=Frame(self.top65)
        my_frame.pack()
        self.amount_litre_label=customtkinter.CTkLabel(my_frame,text="Enter Price Per Litre:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.amount_litre_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
        self.amount_litre_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
        self.amount_litre_entry.grid(row=1,column=2,columnspan=2,padx=5)
        self.save_button=customtkinter.CTkButton(my_frame,text="OK",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.update_paid_credit)
        self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20)
    def update_paid_credit(self):
        self.rate_l=float(self.amount_litre_entry.get())
        self.amount_litre_entry.delete(0,END)
        self.top65.destroy()
        #update the database
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute(""" UPDATE Tenders SET
                    Tender_Name =:t_name,
                    Quantity=:qtity,
                    DATE=:date,
                    Month=:monthm,
                    Year=:yoar,
                    STATUS=:sts

                    WHERE Tender_Name=:t_name AND DATE=:date""",
                    {   
                        't_name': self.tender_name_entry.get(),
                        'qtity': self.quantity_entry.get(),
                        'date':self.selection,
                        'monthm':self.mwezi,
                        'yoar':self.mwaka,
                        'sts':self.svar.get()
                        })
        conn.commit()
        conn.close()
        self.total_amount=(self.rate_l * float(self.quantity_entry.get()))
        self.creditor_receipt()
        #clear entry boxes
        self.clear_entries()
        self.status_c.deselect()
        self.total_entry.delete(0, END)
        self.get_total()
        self.remaining_quantity_entry.delete(0, END)
        self.get_remainder()
    #update data into our treeview and database
    def update_record(self):
        #check
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT STATUS FROM Tenders WHERE Tender_Name=? AND Quantity=? AND DATE=?",(self.tender_name_entry.get(),self.quantity_entry.get(),self.selection,))
        t_status=c.fetchone()
        conn.commit()
        conn.close()
        if self.tender_name_entry.get() =="" :
            messagebox.showerror("Error", "Please Select Tender",parent =self.top0)
        elif t_status=="PAID":
            messagebox.showerror("ERROR","Credit Already Paid",parent=self.top0)
        else:
            #grab the record
            selected=self.my_tree.focus()
            #update record
            self.my_tree.item(selected, text="", values=(self.tender_name_entry.get(), self.quantity_entry.get(), self.today1, self.svar.get()))
            if self.svar.get()!="PAID":
                #update the database
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute(""" UPDATE Tenders SET
                            Tender_Name =:t_name,
                            Quantity=:qtity,
                            DATE=:date,
                            Month=:monthm,
                            Year=:yoar,
                            STATUS=:sts

                            WHERE Tender_Name=:t_name AND DATE=:date""",
                            {   
                                't_name': self.tender_name_entry.get(),
                                'qtity': self.quantity_entry.get(),
                                'date':self.selection,
                                'monthm':self.mwezi,
                                'yoar':self.mwaka,
                                'sts':self.svar.get()
                                })
                conn.commit()
                conn.close()
                #clear entry boxes
                self.clear_entries()
                self.status_c.deselect()
                self.total_entry.delete(0, END)
                self.get_total()
                self.remaining_quantity_entry.delete(0, END)
                self.get_remainder()
            else:
                self.get_amount_per_litre()
    def creditor_receipt(self):
        self.top3=Toplevel()
        self.top3.title("SAMARIA MILK GROUP")
        self.top3.iconbitmap("logo1.ico")
        my_frame=Frame(self.top3, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label1=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"underline", "bold"),width=200,height=40)
        self.receipt_label1.grid(row=0, column=0, columnspan=8, pady=10)
        self.my_receipt1=ScrolledText(my_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt1.grid(row=1, sticky="W", padx=10, pady=5)
        #define headings
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="Date:"
        heading1="Payment Receipt"
        heading2="Creditor Name:"
        heading3="Quantity:"
        heading4="Date Granted:"
        heading5="Served By:"
        heading6="Price Per Litre:"
        heading7="Total:"
        #first delete the text contents
        self.my_receipt1.delete('1.0','end')
        #add stuff into our scrolledtext widget
        self.my_receipt1.insert('end', "\n" +title + "\n")
        self.my_receipt1.insert('end', "\n" +sub +"\n")
        self.my_receipt1.insert('end', "\n" +heading0 + f'{self.today} {self.Time}' +"\n")
        self.my_receipt1.insert('end', "\n" +"\t"+heading1 +"\n")
        self.my_receipt1.insert('end', "\n" +heading2 + f'{self.tender_name_entry.get()}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading3 + f'{self.quantity_entry.get()} Litres'+"\n")
        self.my_receipt1.insert('end', "\n" +heading4 + f'{self.selection}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading6 + f'Kshs {self.rate_l}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading7 + f'Kshs {self.total_amount}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading5 + server+"\n")
        self.Print_button1=customtkinter.CTkButton(my_frame, text="PRINT",fg_color="red", text_color="white", text_font=("Consollas 10", -17, "bold"),width=150,height=35,command=self.print_receipt1)
        self.Print_button1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    def print_receipt1(self):
        printText=self.my_receipt1.get("1.0", 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        #print out as hardcopy
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt1.delete('1.0', 'end')
        self.top3.destroy()
    #choose products function
    def choose_product(self):
        self.top94=Toplevel()
        self.top94.title("SAMARIA MILK GROUP")
        self.top94.iconbitmap("logo1.ico")
        #connect to database
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT PRODUCT_NAME FROM Products")
        self.feeds_names=c.fetchall()
        self.data=[[numbers]for numbers in self.feeds_names]
        #print(self.data)
        conn.commit()
        conn.close()
        self.my_frame=Frame(self.top94)
        self.my_frame.pack(padx=20,pady=20,anchor="w")
        self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE PRODUCTS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.my_sheet=Sheet(self.my_frame,
                            align = "w",
                            header_font=("Consollas 10",15,"bold"),
                            font=("Consollas 10",13,"normal"),
                            data=self.data,
                            headers= ["Product Name","Checkbox","Feeds Quantity"],
                            height=400,
                            show_x_scrollbar = False,
                            show_y_scrollbar =True,
                            width=650)
        self.my_sheet.enable_bindings("copy",
                                   "rc_select",
                                   "arrowkeys",
                                   "double_click_column_resize",
                                   "column_width_resize",
                                   "column_select",
                                   "row_select",
                                   "drag_select",
                                   "single_select",
                                   "select_all")
        self.my_sheet.enable_bindings("edit_header")
        self.my_sheet.grid(row=1,column=0,columnspan=4)
        def get_info(event=None):
            for number in self.data:
                if number[1]==True:
                    print(number[0])
                #print(hdrs)
        def get_quantity(event=None):
            for number in self.data:
                if number[1]==True:
                    print(number[0])
                    print(number[2])
                    if number[2]=="Quantity":
                        number[2]=event.text
                        conn=sqlite3.connect('samaria database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT PRICE FROM Products WHERE PRODUCT_NAME=?",(number[0],))
                        pesa=c.fetchone()
                        total_amount=(pesa*float(number[2]))
                        conn.commit()
                        conn.close()
                        initial=self.total_entry.get()
                        if initial=="":
                            initial=0.0
                        updated= float(initial)+total_amount
                        self.total_entry.delete(0,END)
                        self.total_entry.insert(0,updated)
                    #self.my_sheet.get_dropdown_values()
        self.my_sheet.create_dropdown(r="all",c=2,values=["Quantity"]+[f'{i}'for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)],selection_function=get_quantity)
        self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
        self.my_sheet.get_checkboxes()
        self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
        self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
        self.my_sheet.default_header_height(height="2")
        self.my_sheet.column_width(column=0,width=300)
        self.my_sheet.column_width(column=2,width=150)
        def grant_products():
            self.my_tree1.delete(* self.my_tree1.get_children())
            for record in self.data:
                if record[1]==True:
                    conn=sqlite3.connect('samaria database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT PRICE FROM Products WHERE PRODUCT_NAME=?",(record[0],))
                    pesa=c.fetchone()
                    c.execute("SELECT PRODUCT_QUANTITY FROM Products WHERE PRODUCT_NAME=?",(record[0],))
                    initial_q_quantity=c.fetchone()
                    if initial_q_quantity==0:
                        messagebox.showerror("ERROR",f'{record[0]}'" Stock is Depleted, Consider New Stock",parent =self.top0)
                        continue
                    if (initial_q_quantity - float(record[2])) < 0 :
                        messagebox.showerror("ERROR", f'{record[0]}'"Stock is Less Than"f'{quan}',parent=self.top0)
                        continue
                    if initial_q_quantity==1:
                        messagebox.showinfo("REMINDER",f'{record[0]}'" Stock Depleting, Consider Adding New Stock",parent =self.top0)
                    total=pesa* float(record[2])
                    if self.count%2==0:
                        self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total), tags=("evenrow"),)
                    else:
                        self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total), tags=("oddrow"),)
                    self.count+=1
            self.top94.destroy()
            self.get_total1()
        #buttons
        self.total_label=customtkinter.CTkLabel(self.my_frame,text="TOTAL",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=30)
        self.total_label.grid(row=3,column=0,columnspan=2,padx=20,pady=10)
        self.total_entry=customtkinter.CTkEntry(self.my_frame,border_color="blue",width=200,height=30)
        self.total_entry.grid(row=3,column=2,columnspan=2,padx=20,pady=10)
        self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT PRODUCTS",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_products)
        self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
    #total function 1
    def get_total1(self):
        sum1=0.0
        for child in self.my_tree1.get_children():
            sum1 += float(self.my_tree1.item(child, "values")[2])
            self.t1.set(sum1)

    #store daily transactions in our database
    def copy(self):
        self.get_total1()
        for child in self.my_tree1.get_children():
            data= self.my_tree1.item(child, "values")[0]
            datum=self.my_tree1.item(child, "values")[1]
            datam=self.my_tree1.item(child, "values")[2]
            #insert data 
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT PRICE FROM Products WHERE PRODUCT_NAME=?",(data,))
            pesa=c.fetchone()
            c.execute("INSERT INTO Local_Sales VALUES(:Product_Name, :Quantity, :Price, :Total, :Date)",
                    {
                            'Product_Name' : data,
                            'Quantity' : datum,
                            'Price' : pesa,
                            'Total' : datam,
                            'Date' : self.today1
                            })
            conn.commit()
            conn.close()
            #update products inventory
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT PRODUCT_QUANTITY FROM Products WHERE PRODUCT_NAME=?",(data,))
            initial_q=c.fetchone()
            final_qty=(float(initial_q) - float(datum))
            c.execute("""UPDATE Products SET
                        PRODUCT_NAME=:P_name,
                        PRODUCT_QUANTITY=:P_qnty,
                        PRICE=:cost,
                        MONTH=:mthm,
                        YEAR=:yr
                        
                        WHERE PRODUCT_NAME=:P_name""",
                        {
                            'P_name':data,
                            'P_qnty':final_qty,
                            'cost':pesa,
                            'mthm':self.mwezi,
                            'yr':self.mwaka
                            })
            conn.commit()
            conn.close()
        self.receipt()
        self.my_tree1.delete(*self.my_tree1.get_children())
        self.total_entry1.delete(0, END)
        #refresh the treeview
        self.my_tree3.delete(*self.my_tree3.get_children())
        #run to pull data again from database
        self.query_database1()
        #self.daily_sales()    
    #print function
    def print_receipt(self):
        printText=self.my_receipt.get("1.0", 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        #print out as hardcopy
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt.delete('1.0', 'end')
        self.top2.destroy()
    def receipt(self):    
        self.top2=Toplevel()
        self.top2.title("SAMARIA MILK GROUP")
        self.top2.iconbitmap("logo1.ico")
        my_frame=Frame(self.top2, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"underline", "bold"),width=200,height=40)
        self.receipt_label.grid(row=0, column=0, columnspan=8, pady=10)
        self.my_receipt=ScrolledText(my_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W", padx=10, pady=5)
        #define headings
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="DATE:"
        heading1="Product Name"
        heading2="Quantity"
        heading3="Total"
        heading4="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0','end')
        #add stuff into our scrolledtext widget
        self.my_receipt.insert('end', "\n" + title + "\n")
        self.my_receipt.insert('end', "\n" +sub +"\n")
        self.my_receipt.insert('end', "\n" + heading0 + f'{self.today} {self.Time}' +"\n")
        self.my_receipt.insert('end',  "\n" + heading1 +"\t" + heading2 +"\t"+ heading3 +"\n")    
        for child in self.my_tree1.get_children():
            data= self.my_tree1.item(child, "values")[0]
            datum=self.my_tree1.item(child, "values")[1]
            datam=self.my_tree1.item(child, "values")[2]
            if datum=="0.25":
                datum="1/4"
            if datum=="0.5":
                datum="1/2"
            self.my_receipt.insert('end', "\n" +data +"\t"+datum+"\t" +datam+"\n")
        self.my_receipt.insert('end', "\n" +heading3+"\t"+f'Kshs {self.total_entry1.get()}' +"\n")
        self.my_receipt.insert('end', "\n" + heading4+ "\t"+ f'{server}' +"\n")
        self.Print_button=customtkinter.CTkButton(my_frame, text="PRINT",fg_color="red", text_color="white", text_font=("Consollas 10", -17, "bold"),width=150,height=35,command=self.print_receipt)
        self.Print_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)    
    
    def daily_sales(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Local_Sales WHERE Date=(?)", (self.selected_date,))
        zote=c.fetchall()
        c.execute("SELECT DISTINCT Product_Name, SUM(Quantity) FROM Local_Sales WHERE Date=(?) GROUP BY Product_Name", (self.selected_date,))
        results=c.fetchall()
        conn.commit()
        conn.close()
        for record in results:
            conn=sqlite3.connect('samaria database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Price FROM Local_Sales WHERE Product_Name=?",(str(record[0]),))
            money=c.fetchone()
            conn.commit()
            conn.close()
            if self.count%2==0:
                self.my_tree2.insert('', index=0, iid=self.count, text="", values=(record[0],record[1],money,(record[1] * int(money)),self.selected_date), tags=("evenrow"),)
            else:
                self.my_tree2.insert('', index=0, iid=self.count, text="", values=(record[0],record[1],money,(record[1] * int(money)),self.selected_date), tags=("oddrow"),)
            self.count+=1
        self.get_total2()
        
    #clear entry boxes
    def clear_entries1(self):
        self.product_name_entry.delete(0, END)
        self.product_quantity_entry.delete(0,END)
        self.product_price_entry.delete(0, END)
    def query_database1(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Products")
        records=c.fetchall()
        #add data to our treeview
        for record in records:
            if self.count%2==0:
                self.my_tree3.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2]), tags=("evenrow",))
            else:
                self.my_tree3.insert(parent='',index='end', iid=self.count, text="", values=(record[0],record[1],record[2]), tags=("oddrow",))
            self.count+=1
        conn.commit()
        conn.close()
    def verify_admin(self):
        self.top95=Toplevel()
        self.top95.title("SAMARIA MILK GROUP")
        self.top95.iconbitmap("logo1.ico")
        my_frame=Frame(self.top95)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.add_record1)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   
    #add new product
    def add_record1(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()
            if self.product_name_entry.get()=="":
                messagebox.showerror("ERROR","Please Enter Product Name",parent =self.top0)
            else:
                try:
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("INSERT INTO Products VALUES( :PRODUCT_NAME,:PRODUCT_QUANTITY, :PRICE,:MONTH,:YEAR,:DATE)",
                            {
                                'PRODUCT_NAME': self.product_name_entry.get(),
                                'PRODUCT_QUANTITY': self.product_quantity_entry.get(),
                                'PRICE': self.product_price_entry.get(),
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE':self.today1
                                })
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Bravo",f'{self.product_name_entry.get()} Added Succesfully',parent=self.top0)
                except:
                    messagebox.showerror("ERROR",f'{self.product_name_entry.get()} Already Exists',parent=self.top0)
                #feeds records
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Product_Records VALUES(:Product_Name,:Product_Quantity,:DATE)",
                          {
                              'Product_Name':self.product_name_entry.get(),
                              'Product_Quantity':self.product_quantity_entry.get(),
                              'DATE':self.today1
                              })
                conn.commit()
                conn.close()
            #clear  entry boxes
            self.clear_entries1()
            #refresh the treeview
            self.my_tree3.delete(*self.my_tree3.get_children())
            #run to pull data again from database
            self.query_database1()
    def verify_admin1(self):
        self.top96=Toplevel()
        self.top96.title("SAMARIA MILK GROUP")
        self.top96.iconbitmap("logo1.ico")
        my_frame=Frame(self.top96)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.update_price)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   
    #update price
    def update_price(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()
            if self.product_name_entry.get()=="":
                messagebox.showerror("ERROR","Please Enter Product Name",parent =self.top0)
            else:
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT PRODUCT_QUANTITY FROM Products WHERE PRODUCT_NAME=?",(self.product_name_entry.get(),))
                initial_q=c.fetchone()
                c.execute("""UPDATE Products SET
                            PRODUCT_NAME=:P_name,
                            PRODUCT_QUANTITY=:P_qnty,
                            PRICE=:cost,
                            MONTH=:mthm,
                            YEAR=:yr,
                            DATE=:dute

                            WHERE PRODUCT_NAME=:P_name""",
                          {
                              'P_name':self.product_name_entry.get(),
                              'P_qnty':initial_q,
                              'cost':self.product_price_entry.get(),
                              'mthm':self.mwezi,
                              'yr':self.mwaka,
                              'dute':self.today1
                              })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.product_name_entry.get()} Price Updated Successfully',parent=self.top0)
                #clear entries
                self.clear_entries1()
                #refresh the treeview
                self.my_tree3.delete(*self.my_tree3.get_children())
                #run to pull data again from database
                self.query_database1()
    def verify_admin2(self):
        self.top97=Toplevel()
        self.top97.title("SAMARIA MILK GROUP")
        self.top97.iconbitmap("logo1.ico")
        my_frame=Frame(self.top97)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.increase_stock)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   
    #increase stock
    def increase_stock(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top97.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top97.destroy()
            if self.product_name_entry.get()=="":
                messagebox.showerror("ERROR","Please Enter Product Name",parent =self.top0)
            else:
                conn=sqlite3.connect("samaria database.db")
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT PRICE FROM Products WHERE PRODUCT_NAME=?",(self.product_name_entry.get(),))
                initial_price=c.fetchone()
                c.execute("SELECT PRODUCT_QUANTITY FROM Products WHERE PRODUCT_NAME=?",(self.product_name_entry.get(),))
                initial_qt=c.fetchone()
                final_qty=(float(initial_qt) + float(self.product_quantity_entry.get()))
                c.execute("""UPDATE Products SET
                            PRODUCT_NAME=:P_name,
                            PRODUCT_QUANTITY=:P_qnty,
                            PRICE=:cost,
                            MONTH=:mthm,
                            YEAR=:yr,
                            DATE=:dote

                            WHERE PRODUCT_NAME=:P_name""",
                          {
                              'P_name':self.product_name_entry.get(),
                              'P_qnty':final_qty,
                              'cost':initial_price,
                              'mthm':self.mwezi,
                              'yr':self.mwaka,
                              'dote':self.today1
                              })
                conn.commit()
                conn.close()
                #update feeds_records
                conn=sqlite3.connect("samaria database.db")
                c=conn.cursor()
                c.execute("SELECT * FROM Product_Records WHERE Product_Name=? AND DATE=?",(self.product_name_entry.get(),self.today1,))
                any_r=c.fetchall()
                conn.commit()
                conn.close()
                #
                conn=sqlite3.connect("samaria database.db")
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Product_Quantity FROM Product_Records WHERE Product_Name=? AND DATE=?",(self.product_name_entry.get(),self.today1,))
                int_qty=c.fetchone()
                if int_qty==None:
                    int_qty=0
                conn.commit()
                conn.close()
                total_qty=(int(int_qty)+int(self.product_quantity_entry.get()))
                if any_r ==[]:
                    #insert new record
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("INSERT INTO Product_Records VALUES(:Product_Name,:Product_Quantity,:DATE)",
                              {
                                  'Product_Name':self.product_name_entry.get(),
                                  'Product_Quantity':self.product_quantity_entry.get(),
                                  'DATE':self.today1
                                  })
                    conn.commit()
                    conn.close()
                else:
                    #update record
                    conn=sqlite3.connect("samaria database.db")
                    c=conn.cursor()
                    c.execute("""UPDATE Product_Records SET
                                Product_Name=:pp_name,
                                Product_Quantity=:pp_qty,
                                DATE=:date

                                WHERE Product_Name=:pp_name AND DATE=:date""",
                              {
                                  'pp_name':self.product_name_entry.get(),
                                  'pp_qty':total_qty,
                                  'date':self.today1
                                  })
                    conn.commit()
                    conn.close()
                messagebox.showinfo("Bravo","New Stock Added Successfully",parent=self.top0)
                #clear entries
                self.clear_entries1()
                #refresh the treeview
                self.my_tree3.delete(*self.my_tree3.get_children())
                #run to pull data again from database
                self.query_database1()
    #create binding function
    def clicker2(self,e):
        #clear entry boxes
        self.clear_entries1()
        #grab record number
        selected=self.my_tree3.focus()
        #grab record values
        values=self.my_tree3.item(selected, 'values')
        #output to entry boxes
        self.product_name_entry.insert(0, values[0])
        self.product_quantity_entry.insert(0, values[1])
        self.product_price_entry.insert(0, values[2])
        
    def verify_admin3(self):
        self.top98=Toplevel()
        self.top98.title("SAMARIA MILK GROUP")
        self.top98.iconbitmap("logo1.ico")
        my_frame=Frame(self.top98)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.delete_record1)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)   
        
    #delete a record
    def delete_record1(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top98.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top98.destroy()
            #messagebox
            response=messagebox.askyesno("Confirm", "Are you sure you want to delete this product",parent =self.top0)
            if response==1:
                #check
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT PRODUCT_QUANTITY FROM Products WHERE PRODUCT_NAME=?", (self.product_name_entry.get(),))
                initial_q=c.fetchone()
                conn.commit()
                conn.close()
                
                if initial_q!=0:
                    messagebox.showerror("ERROR","You Cannot Delete Feeds If NOT Depleted",parent=self.top0)
                else:
                    #delete from database
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("DELETE FROM Products WHERE PRODUCT_NAME=?", (self.product_name_entry.get(),))
                    conn.commit()
                    conn.close()
                    #clear entry boxes
                    self.clear_entries1()
                    #messagebox
                    messagebox.showinfo("Information", "Product deleted succesfully",parent =self.top0)
                    #refresh the treeview
                    self.my_tree3.delete(*self.my_tree3.get_children())
                    #run to pull data again from database
                    self.query_database1()
    def creditor_report(self):
        #variables
        self.choser=StringVar()
        self.year_choser=StringVar()
        self.choser_creditor=StringVar()
        months=["January","February","March","April","May","June","July","August","September","October","November","December"]
        years=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}']
        #query
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT * FROM Creditors")
        creditors=c.fetchall()
        conn.commit()
        conn.close()
        #print function
        def print_receipt85():
            printText=self.my_receipt85.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt85.delete('1.0', 'end')
        def choose_month(event):
            if self.choser.get()=="January":
                self.choosed=1
            if self.choser.get()=="February":
                self.choosed=2
            if self.choser.get()=="March":
                self.choosed=3
            if self.choser.get()=="April":
                self.choosed=4
            if self.choser.get()=="May":
                self.monthm=5
            if self.choser.get()=="June":
                self.choosed=6
            if self.choser.get()=="July":
                self.choosed=7
            if self.choser.get()=="August":
                self.choosed=8
            if self.choser.get()=="September":
                self.choosed=9
            if self.choser.get()=="October":
                self.choosed=10
            if self.choser.get()=="November":
                self.choosed=11
            if self.choser.get()=="December":
                self.choosed=12
        def generate_creditor_report():
            if self.choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Month",parent=self.top85)
            elif self.year_choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Year",parent=self.top85)
            elif self.choser_creditor.get()=="":
                messagebox.showerror("ERROR","Please Choose a Creditor",parent=self.top85)
            else:
                total_credits=0.0
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1="Served By:"
                heading2="Creditor Name:"
                heading3="Month:"
                heading4="Total Quantity:"
                #first delete the scrolledtext  contents
                self.my_receipt85.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt85.insert('end', "\n" +title + "\n")
                self.my_receipt85.insert('end', "\n" +sub + "\n")
                self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                self.my_receipt85.insert('end', "\n" +"\t"+"Pending Credits"+"\n")
                self.my_receipt85.insert('end', "\n" +heading2+"\t"+f'{self.choser_creditor.get()}'+"\n")
                self.my_receipt85.insert('end', "\n" +heading3+ f'{self.choser.get()}'+ f' {self.year_choser.get()}'+"\n")
                self.my_receipt85.insert('end', "\n" +"Quantity"+"\t"+"Date"+"\n")
                #queries
                conn=sqlite3.connect('samaria database.db')
                c=conn.cursor()
                c.execute("SELECT * FROM Tenders WHERE STATUS=? AND Tender_Name=? AND MONTH=? AND YEAR=?",("NOT PAID",self.choser_creditor.get(),self.choosed,self.year_choser.get(),))
                all_credits=c.fetchall()
                conn.commit()
                conn.close()
                for x in all_credits:
                    self.my_receipt85.insert('end', "\n" +f'{x[1]} Litres'+"\t"+str(x[2])+"\n")
                    total_credits+=float(x[1])
                self.my_receipt85.insert('end', "\n" +heading4+ f'{total_credits} Litres'+"\n")
                self.my_receipt85.insert('end', "\n" +heading1 +"\t"+server+"\n")
        #toplevel
        self.top85=Toplevel()
        self.top85.iconbitmap("logo1.ico")
        self.top85.state('zoomed')
        self.title_frame=Frame(self.top85)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="CREDITOR'S REPORT"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top85,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.choose_creditor_label=customtkinter.CTkLabel(self.left_frame,text="Choose Creditor:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.choose_creditor_label.grid(row=0,column=0,columnspan=2,padx=10,pady=20)
        self.choose_creditor_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.choser_creditor,values=creditors,width=250,height=25,fg_color="red",text_color="white")
        self.choose_creditor_menu.grid(row=0, column=2,columnspan=3)
        self.choose_month_label=customtkinter.CTkLabel(self.left_frame,text="Choose Month:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.choose_month_label.grid(row=0,column=5,columnspan=2,padx=10,pady=20)
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.choser,values=months,width=200,height=25,fg_color="red",text_color="white",command=choose_month)
        self.choose_month_menu.grid(row=0, column=7,columnspan=2)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.year_choser,values=years,width=200,height=25,fg_color="red",text_color="white")
        self.choose_year_menu.grid(row=0, column=9,columnspan=2,padx=10)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_creditor_report)
        self.generate_button.grid(row=0,column=11,padx=20,pady=20,columnspan=4,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt85=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
        self.my_receipt85.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt85)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
class Loans:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x1000")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
         #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        report_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Report", menu=report_menu)
        report_menu.add_command(label="Loans Report", command=self.loan_report)

        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)

        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)

       #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="ADVANCES"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #create loans table
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        '''
        #drop loan table
        c.execute("DROP TABLE LOANS")
        print("table dropped succesfully")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS LOANS(
                    Customer_ID INT NOT NULL,
                    First_Name TEXT NOT NULL,
                    Last_Name TEXT NOT NULL,
                    Pending_Loan REAL NOT NULL,
                    Loan_Amount REAL NOT NULL,
                    Total_Loan REAL NOT NULL,
                    STATUS TEXT NOT NULL,
                    MONTH INT NOT NULL,
                    YEAR INT NOT NULL,
                    DATE INT NOT NULL,
                    PERIOD TEXT NOT NULL)""")
        conn.commit()
        conn.close()
        #dates
        self.currentDateTime=date.today()
        self.time=datetime.now()
        self.now_day=datetime.now().day
        self.then_day=self.now_day
        self.yesterday=datetime.now() - timedelta(2)
        self.yesterday1=self.yesterday.strftime("%m/%d/%Y")
        self.today=self.currentDateTime.strftime("%A-%B %d, %Y")
        self.today1=self.time.strftime("%m/%d/%Y")
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.mwezij=(datetime.now().month-1)
        self.mwezi=datetime.now().month
        self.mwaka=datetime.now().year
        #variables
        self.var= BooleanVar()
        self.var1= BooleanVar()
        self.count=0
        self.svar=StringVar()
        self.pl=StringVar()
        self.p2=StringVar()
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top0,border_color="green",border_width=5, width=400,height=450)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        loans_title="FARMER ADVANCES"
        self.loans_title_label=customtkinter.CTkLabel(self.left_frame, text=loans_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"underline","bold"),width=150,height=30)
        self.loans_title_label.grid(row=0, column=0,columnspan=3,pady=20)                        
        #add widgets
        self.date_label=customtkinter.CTkLabel(self.left_frame, text="Today:", fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.date_label.grid(row=1, column=0,padx=10, pady=10,sticky=W)
        self.today_label=customtkinter.CTkLabel(self.left_frame, text=self.today)
        self.today_label.grid(row=1, column=1)
        #labels
        self.customer_id_label=customtkinter.CTkLabel(self.left_frame, text="ENTER FARMER ID:",fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.customer_id_label.grid(row=2, column=0,padx=10, pady=20,sticky=W)
        self.first_name_label=customtkinter.CTkLabel(self.left_frame, text="FIRST NAME:",fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.first_name_label.grid(row=3, column=0,padx=10,pady=20,sticky=W)
        self.last_name_label=customtkinter.CTkLabel(self.left_frame, text="LAST NAME:",fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.last_name_label.grid(row=4, column=0,padx=10, pady=20,sticky=W)
        self.pending_loan_label=customtkinter.CTkLabel(self.left_frame, text="PENDING ADVANCE:",fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.pending_loan_label.grid(row=5, column=0,padx=10, pady=20,sticky=W)
        self.loan_request_label=customtkinter.CTkLabel(self.left_frame, text="ADVANCE REQUESTED:",fg_color="brown", text_color="white", text_font=("Consollas 10",-13,"bold"),width=120,height=25)
        self.loan_request_label.grid(row=6, column=0,padx=10, pady=20,sticky=W)
        #entry boxes
        self.customer_id_entry=customtkinter.CTkEntry(self.left_frame, width=120,height=25,border_color="blue")
        self.customer_id_entry.grid(row=2, column=1)
        self.first_name_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue")
        self.first_name_entry.grid(row=3, column=1)
        self.last_name_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue")
        self.last_name_entry.grid(row=4, column=1)
        self.pending_loan_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue")
        self.pending_loan_entry.grid(row=5, column=1)
        self.loan_request_entry=customtkinter.CTkEntry(self.left_frame,width=120,height=25,border_color="blue")
        self.loan_request_entry.grid(row=6, column=1)
        #buttons
        self.confirm_button=customtkinter.CTkButton(self.left_frame, text="Confirm",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=150,height=25,command=self.retreive)
        self.confirm_button.grid(row=2, column=2,pady=4)
        self.grant_loan_button=customtkinter.CTkButton(self.left_frame, text="GRANT ADVANCE",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.grant_loan)
        self.grant_loan_button.grid(row=7, column=0, columnspan=4, ipadx=100, padx=20, pady=20,ipady=10)
        #self.insert_data()  
        #*********************************************************************************************************************************************************************
        #right frame
        self.right_frame=customtkinter.CTkFrame(self.top0,border_color="maroon",border_width=5, width=600,height=450)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #heading
        tender_title="PENDING CREDITS"
        self.tender_title_label=customtkinter.CTkLabel(self.right_frame, text=tender_title, fg_color="orange", text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
        self.tender_title_label.grid(row=0, column=0,columnspan=3,pady=10)
        #tender treeview
        self.tree_frame1=Frame(self.right_frame, highlightbackground="green", highlightthickness=5, width=500, height=500, bd=0)
        self.tree_frame1.grid(row=1, column=0,columnspan=3,padx=30, pady=5)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview_scrollbar
        self.tree_scroll1=Scrollbar(self.tree_frame1)
        self.tree_scroll1.pack(side=RIGHT, fill=Y)
        #create our treeview
        self.my_tree1=ttk.Treeview(self.tree_frame1, yscrollcommand=self.tree_scroll1.set)
        self.my_tree1.pack()
        #configure the scrollbar
        self.tree_scroll1.config(command=self.my_tree1.yview)
        #define our columns
        self.my_tree1['columns']=("Creditor Name", "Quantity", "Date","Month","Year","Status")
        #format our columns
        self.my_tree1.column("#0", width=0, stretch=NO)
        self.my_tree1.column("Creditor Name", anchor="w", width=250)
        self.my_tree1.column("Quantity", anchor="w", width=80)
        self.my_tree1.column("Date", anchor="w", width=100)
        self.my_tree1.column("Month", anchor="w", width=80)
        self.my_tree1.column("Year", anchor="w", width=80)
        self.my_tree1.column("Status", anchor="w", width=100)
        #create headings
        self.my_tree1.heading("#0", text="")
        self.my_tree1.heading("Creditor Name", text="Creditor Name", anchor="w")
        self.my_tree1.heading("Quantity", text="Quantity", anchor="w")
        self.my_tree1.heading("Date", text="Date", anchor="w")
        self.my_tree1.heading("Month", text="Month", anchor="w")
        self.my_tree1.heading("Year", text="Year", anchor="w")
        self.my_tree1.heading("Status", text="Status", anchor="w")
        #striped row tags
        self.my_tree1.tag_configure('oddrow', background="white")
        self.my_tree1.tag_configure('evenrow', background="violet")
        #single click(button release)
        self.my_tree1.bind("<ButtonRelease-1>", self.clicker)
        #double click my_tree1.bind("<Double-1>", clicker)
        self.get_total()
        self.total_tender_entry=customtkinter.CTkEntry(self.tree_frame1, width=100,height=20,border_color="blue")
        self.total_tender_entry.insert(0, f'{self.unpaid_tenders} Litres')
        self.total_tender_entry.pack(anchor="e")
        #frame
        self.entry_frame=Frame(self.right_frame)
        self.entry_frame.grid(row=2, column=0,columnspan=2, padx=20,pady=5)
        #entry labels
        self.tender_name_label=customtkinter.CTkLabel(self.entry_frame,text="Creditor Name:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.tender_name_label.grid(row=1, column=0, padx=10,pady=2, sticky=W)
        self.tender_quantity_label=customtkinter.CTkLabel(self.entry_frame, text="Quantity:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.tender_quantity_label.grid(row=2, column=0, padx=10,pady=2, sticky=W)
        self.date_label=customtkinter.CTkLabel(self.entry_frame, text="Date:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.date_label.grid(row=3, column=0, padx=10,pady=2, sticky=W)
        self.status_label=customtkinter.CTkLabel(self.entry_frame, text="Mark as Paid:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.status_label.grid(row=4, column=0, padx=10,pady=2, sticky=W)
        #entry boxes
        self.tender_name_box=customtkinter.CTkEntry(self.entry_frame, width=200,height=25,border_color="blue")
        self.tender_name_box.grid(row=1, column=1)
        self.tender_quantity_box=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.tender_quantity_box.grid(row=2, column=1)
        self.date_box=customtkinter.CTkEntry(self.entry_frame,width=150,height=25,border_color="blue")
        self.date_box.grid(row=3,column=1)
        self.status_c=customtkinter.CTkCheckBox(self.entry_frame, text="",variable=self.svar, onvalue="PAID", offvalue="NOT PAID")
        self.status_c.deselect()
        self.status_c.grid(row=4, column=1)
        #update button
        self.update_button=customtkinter.CTkButton(self.entry_frame, text="MARK AS PAID",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=150,height=35,command=self.get_amount_per_litre)
        self.update_button.grid(row=5, column=0, columnspan=2, padx=20, pady=5)
        
        self.query_database()
        
    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    #clearentries
    def clear_entries(self):
        self.customer_id_entry.delete(0, END)
        self.first_name_entry.delete(0, END)
        self.last_name_entry.delete(0, END)
        self.pending_loan_entry.delete(0, END)
        self.loan_request_entry.delete(0,END)
    #total loan lendered
    def total_loans(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT SUM(Loan_Amount) FROM LOANS")
        self.totals=c.fetchone()
        if self.totals==None:
            self.totals=0.0
        conn.commit()
        conn.close()       
    #retreive name and other aspects
    def retreive(self):
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Farmer ID",parent =self.top0)
        else:
            conn=sqlite3.connect('samaria database.db')
            c=conn.cursor()
            c.execute("SELECT First_name, Last_name FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
            name=c.fetchall()
            self.first_name=''
            self.last_name=''
            for record in name:
                self.first_name +=(record[0])
            for record in name:
                self.last_name +=(record[1])
            full_name=self.first_name+""+self.last_name
            self.first_name_entry.delete(0,END)
            self.last_name_entry.delete(0,END)
            self.first_name_entry.insert(0, self.first_name)
            self.last_name_entry.insert(0, self.last_name)
            conn.commit()
            conn.close()
            if self.then_day<=15:
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Total_Loan) FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 1-15",))
                self.pending_loan=c.fetchone()
                if self.pending_loan==None:
                    self.pending_loan=0.0
                self.pending_loan_entry.delete(0,END)
                self.pending_loan_entry.insert(0, self.pending_loan)
                c.execute("SELECT National_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
                national=c.fetchall()
                self.national_id=national[0]
                conn.commit()
                conn.close()
            else:
                #pending loan
                conn=sqlite3.connect('samaria database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT SUM(Total_Loan) FROM LOANS WHERE Customer_ID=? AND STATUS=? AND PERIOD=?",(self.customer_id_entry.get(),"NOT PAID","From 16",))
                self.pending_loan=c.fetchone()
                if self.pending_loan==None:
                    self.pending_loan=0.0
                self.pending_loan_entry.delete(0,END)
                self.pending_loan_entry.insert(0, self.pending_loan)
                c.execute("SELECT National_ID FROM Customers WHERE Customer_ID=" +self.customer_id_entry.get())
                national=c.fetchall()
                self.national_id=national[0]
                conn.commit()
                conn.close()
    def grant_loan(self):
        if self.customer_id_entry.get()=="":
            messagebox.showerror("ERROR", "Please Enter Farmer's ID",parent =self.top0)
        else:
            self.top10=Toplevel()
            self.top10.geometry("500x150")
            self.top10.title("SAMARIA MILK GROUP")
            self.top10.iconbitmap("logo1.ico")
            my_frame=Frame(self.top10)
            my_frame.pack(anchor="w")
            self.admin_passcode_label=customtkinter.CTkLabel(my_frame, text="Enter Administrator Password:", fg_color="brown", text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=30)
            self.admin_passcode_label.grid(row=0, column=0, columnspan=2,padx=20, pady=10)
            self.admin_passcode_entry=customtkinter.CTkEntry(my_frame, width=150,height=30,border_color="blue",show="*")
            self.admin_passcode_entry.grid(row=0, column=2)
            self.submit_passcode_button=customtkinter.CTkButton(my_frame, text="SUBMIT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=200,height=40,command=self.verify_loan_admin)
            self.submit_passcode_button.grid(row=1, column=0, columnspan=4, padx=20, pady=10)
    def verify_loan_admin(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_p=c.fetchone()
        conn.commit()
        conn.close()
        if admin_p!=self.admin_passcode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Admin Password, Check Password And Try Again",parent =self.top0)
            self.admin_passcode_entry.delete(0, END)
            self.top10.destroy()
        else:
            try:
                if self.then_day <=15:
                    self.admin_passcode_entry.delete(0, END)
                    self.top10.destroy()
                    self.total_advance=float(self.pending_loan_entry.get()) + float(self.loan_request_entry.get())
                    #payment method
                    conn = sqlite3.connect('samaria database.db')
                    c = conn.cursor()
                    #update data
                    c.execute("""UPDATE LOANS SET
                                Customer_ID=:c_id,
                                First_Name=:f_name,
                                Last_Name=:l_name,
                                Pending_Loan=:p_loan,
                                Loan_amount=:l_amount,
                                Total_Loan=:t_loan,
                                STATUS=:stas,
                                MONTH=:monthi,
                                YEAR=:yoar,
                                DATE=:siku,
                                PERIOD=:dayz
                                
                                WHERE Customer_ID=:c_id AND STATUS=:stas AND MONTH=:monthi AND YEAR=:yoar AND PERIOD=:dayz""",
                              {
                                  'c_id':self.customer_id_entry.get(),
                                  'f_name':self.first_name_entry.get(),
                                  'l_name':self.last_name_entry.get(),
                                  'p_loan':self.pending_loan_entry.get(),
                                  'l_amount':self.loan_request_entry.get(),
                                  't_loan':self.total_advance,
                                  'stas':"NOT PAID",
                                  'monthi':self.mwezi,
                                  'yoar':self.mwaka,
                                  'siku':self.today1,
                                  'dayz':"From 1-15"
                                  })
                    #insert data
                    c.execute("INSERT OR IGNORE INTO LOANS VALUES(:Customer_ID, :First_Name, :Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'Customer_ID' : self.customer_id_entry.get(),
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Pending_Loan':self.pending_loan_entry.get(),
                                'Loan_Amount': self.loan_request_entry.get(),
                                'Total_Loan':self.total_advance,
                                'STATUS':"NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 1-15"
                                })
                    c.execute("DELETE FROM LOANS WHERE rowid NOT IN (SELECT MIN(rowid) FROM LOANS GROUP BY Customer_ID,First_Name,Last_Name,Pending_Loan,Loan_Amount,Total_Loan,STATUS,MONTH,YEAR,DATE,PERIOD)")
                    c.execute("SELECT * FROM LOANS")
                    zote=c.fetchall()
                    print(zote)
                    conn.commit()
                    conn.close()
                    self.receipt()
                    self.clear_entries()
                else:
                    self.admin_passcode_entry.delete(0, END)
                    self.top10.destroy()
                    self.total_advance=float(self.pending_loan_entry.get()) + float(self.loan_request_entry.get())
                    #payment method
                    conn = sqlite3.connect('samaria database.db')
                    c = conn.cursor()
                    #update data
                    c.execute("""UPDATE LOANS SET
                                Customer_ID=:c_id,
                                First_Name=:f_name,
                                Last_Name=:l_name,
                                Pending_Loan=:p_loan,
                                Loan_amount=:l_amount,
                                Total_Loan=:t_loan,
                                STATUS=:stas,
                                MONTH=:monthi,
                                YEAR=:yoar,
                                DATE=:siku,
                                PERIOD=:dayz
                                
                                WHERE Customer_ID=:c_id AND STATUS=:stas AND MONTH=:monthi AND YEAR=:yoar AND PERIOD=:dayz""",
                              {
                                  'c_id':self.customer_id_entry.get(),
                                  'f_name':self.first_name_entry.get(),
                                  'l_name':self.last_name_entry.get(),
                                  'p_loan':self.pending_loan_entry.get(),
                                  'l_amount':self.loan_request_entry.get(),
                                  't_loan':self.total_advance,
                                  'stas':"NOT PAID",
                                  'monthi':self.mwezi,
                                  'yoar':self.mwaka,
                                  'siku':self.today1,
                                  'dayz':"From 16"
                                  })
                    #insert data
                    c.execute("INSERT OR IGNORE INTO LOANS VALUES(:Customer_ID, :First_Name, :Last_Name,:Pending_Loan,:Loan_Amount,:Total_Loan,:STATUS, :MONTH, :YEAR, :DATE,:PERIOD)",
                            {
                                'Customer_ID' : self.customer_id_entry.get(),
                                'First_Name': self.first_name_entry.get(),
                                'Last_Name': self.last_name_entry.get(),
                                'Pending_Loan':self.pending_loan_entry.get(),
                                'Loan_Amount': self.loan_request_entry.get(),
                                'Total_Loan':self.total_advance,
                                'STATUS':"NOT PAID",
                                'MONTH': self.mwezi,
                                'YEAR': self.mwaka,
                                'DATE': self.today1,
                                'PERIOD':"From 16"
                                })
                    c.execute("DELETE FROM LOANS WHERE rowid NOT IN (SELECT MIN(rowid) FROM LOANS GROUP BY Customer_ID,First_Name,Last_Name,Pending_Loan,Loan_Amount,Total_Loan,STATUS,MONTH,YEAR,DATE,PERIOD)")
                    c.execute("SELECT * FROM LOANS")
                    zote=c.fetchall()
                    print(zote)
                    conn.commit()
                    conn.close()
                    self.receipt()
                    self.clear_entries()
            except ValueError:
                messagebox.showerror("ERROR","Please First Confirm Requested Farmer",parent=self.top0)
    #print receipt                   
    def print_receipt(self):
        printText=self.my_receipt.get("1.0", 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        #print out
        copies=2
        for copy in range(copies):
            win32api.ShellExecute(0,
                                    "printto",
                                    filename,
                                    '"%s"' % win32print.GetDefaultPrinter(),
                                    ".",
                                    0
                                    )
        self.my_receipt.delete('1.0', 'end')
        self.top.destroy()
     #receipt
    def receipt(self):                
        self.top=Toplevel()
        self.top.title("SAMARIA MILK GROUP")
        self.top.iconbitmap("logo1.ico")
        my_frame=Frame(self.top, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame,text="RECEIPT", fg_color="purple", text_color="white",text_font=("Consollas 10",-20,"underline", "bold"),width=200,height=30)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading1="ADVANCE AGREEMENT FORM"
        heading2="DATE:"
        heading4="Pending Advance(KShs):"
        heading5="Total Advance(KShs):"
        heading3="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0', 'end')
        #add contents to our scrolledtext widget
        self.my_receipt.insert('end', "\n" + title +"\n")
        self.my_receipt.insert('end', "\n" + sub +"\n")
        self.my_receipt.insert('end', "\n" + heading1 +"\n")
        self.my_receipt.insert('end', "\n" + heading2 + f'{self.today} {self.Time}' + "\n")
        self.my_receipt.insert('end', "\n" + f' I, {self.first_name} {self.last_name}' +"\n")
        self.my_receipt.insert('end', "\n" + f' of ID Number: {self.national_id}' +"\n")
        self.my_receipt.insert('end', "\n" + f' hereby comply to take an advance' +"\n")
        self.my_receipt.insert('end', "\n" + f' of KSHS: {self.loan_request_entry.get()}' +"\n")
        self.my_receipt.insert('end', "\n" + f' that is due in 1 month' +"\n")
        if self.pending_loan==0.0:
            self.my_receipt.insert('end', "\n" + heading5+ f'{self.total_advance}'+"\n")
            self.my_receipt.insert('end', "\n" + f' Signature: .....................' + "\n" )
            self.my_receipt.insert('end', "\n" + heading3+ "\t"+ f'{server}' +"\n")
        else:
            self.my_receipt.insert('end', "\n" + heading4+ f'{self.pending_loan}'+"\n")
            self.my_receipt.insert('end', "\n" + heading5+ f'{self.total_advance}'+"\n")
            self.my_receipt.insert('end', "\n" + f' Signature: .....................' + "\n" )
            self.my_receipt.insert('end', "\n" + heading3+ "\t"+ f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame, text="PRINT",fg_color="red", text_color="white",text_font=("Consollas 10",-20, "bold"),width=200,height=35,command=self.print_receipt)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
    
    #enter data into our treeview
    def insert_data(self):
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM LOANS WHERE Loan_Amount > 0.0")
        results=c.fetchall()
        for record in results:
            if self.count%2==0:
                self.my_tree.insert('', 'end', iid=self.count, text="", values=(record[1],record[2],record[0],record[6],record[3],record[4],record[5],record[7]),tags=("evenrow",))
            else:
                self.my_tree.insert('', 'end', iid=self.count, text="", values=(record[1],record[2],record[0],record[6],record[3],record[4],record[5],record[7]),tags=("oddrow",))
            self.count+=1
        conn.commit()
        conn.close()      

    #unpaid tenders
    def get_total(self):    
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT SUM(Quantity) FROM Tenders WHERE STATUS=('NOT PAID')")
        result=c.fetchone()
        if result==None:
            self.unpaid_tenders=0.0
        else:
            self.unpaid_tenders=result
        conn.commit()
        conn.close()
        
    #enter data into our treeview
    def query_database(self):    
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Tenders WHERE STATUS=('NOT PAID')")
        unpaid=c.fetchall()
        for record in unpaid:
            if self.count%2==0:
                self.my_tree1.insert('', 'end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]),tags=("evenrow",))
            else:
                self.my_tree1.insert('', 'end', iid=self.count, text="", values=(record[0],record[1],record[2],record[3],record[4],record[5]),tags=("oddrow",))
            self.count+=1
        conn.commit()
        conn.close()
    
    #create binding function
    def clicker(self,e):
        #clear entry boxes
        self.tender_name_box.delete(0, END)
        self.tender_quantity_box.delete(0, END)
        self.date_box.delete(0,END)
        #grab record
        selected=self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #output to entryboxes
        self.tender_name_box.insert(0, values[0])
        self.tender_quantity_box.insert(0, values[1])
        self.date_box.insert(0, values[2])
    def get_amount_per_litre(self):
        if self.tender_name_box.get() =="":
            messagebox.showerror("ERROR", "Please Select Tender",parent=self.top0)
        elif self.svar.get()!="PAID":
            messagebox.showerror("ERROR","Please Mark As Paid",parent=self.top0)
        else:
            self.top65=Toplevel()
            self.top65.iconbitmap("logo1.ico")
            self.top65.title=("SAMARIA MILK GROUP")
            my_frame=Frame(self.top65)
            my_frame.pack()
            self.amount_litre_label=customtkinter.CTkLabel(my_frame,text="Enter Price Per Litre:",fg_color="brown",text_color="white", text_font=("Consollas 10",-15,"bold"),width=150,height=30)
            self.amount_litre_label.grid(row=1,column=0,padx=20,pady=10,columnspan=2)
            self.amount_litre_entry=customtkinter.CTkEntry(my_frame,width=200,height=30,border_color="green")
            self.amount_litre_entry.grid(row=1,column=2,columnspan=2,padx=5)
            self.save_button=customtkinter.CTkButton(my_frame,text="OK",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=35,command=self.update_paid_credit)
            self.save_button.grid(row=2,column=0,columnspan=4,padx=20,pady=20)
    def update_paid_credit(self):
        self.rate_l=float(self.amount_litre_entry.get())
        self.amount_litre_entry.delete(0,END)
        self.top65.destroy()
        #check
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Tenders WHERE Tender_Name=? AND Quantity=? AND DATE=?",(self.tender_name_box.get(),self.tender_quantity_box.get(),self.date_box.get(),))
        record=c.fetchone()
        conn.commit()
        conn.close()
        #update the database
        conn=sqlite3.connect('samaria database.db')
        c=conn.cursor()
        c.execute(""" UPDATE Tenders SET
                    Tender_Name =:t_name,
                    Quantity=:qtity,
                    DATE=:date,
                    Month=:monthm,
                    Year=:yoar,
                    STATUS=:sts

                    WHERE Tender_Name=:t_name AND DATE=:date""",
                    {   
                        't_name': self.tender_name_box.get(),
                        'qtity': self.tender_quantity_box.get(),
                        'date':self.date_box.get(),
                        'monthm':record[3],
                        'yoar':record[4],
                        'sts':self.svar.get()
                        })
        conn.commit()
        conn.close()
        self.total_amount=(self.rate_l * float(self.tender_quantity_box.get()))
        self.creditor_receipt()
        #clear entry boxes
        self.tender_name_box.delete(0, END)
        self.tender_quantity_box.delete(0, END)
        self.date_box.delete(0,END)
        self.status_c.deselect()
        self.total_tender_entry.delete(0, END)
        self.get_total()
        self.total_tender_entry.insert(0, f'{self.unpaid_tenders} Litres')
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_database()
    def creditor_receipt(self):
        self.top3=Toplevel()
        self.top3.title("SAMARIA MILK GROUP")
        self.top3.iconbitmap("logo1.ico")
        my_frame=Frame(self.top3, width=50)
        my_frame.pack(anchor="w")
        self.receipt_label1=customtkinter.CTkLabel(my_frame, text="RECEIPT", fg_color="purple", text_color="white", text_font=("Consollas 10", -20,"underline", "bold"),width=200,height=40)
        self.receipt_label1.grid(row=0, column=0, columnspan=8, pady=10)
        self.my_receipt1=ScrolledText(my_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt1.grid(row=1, sticky="W", padx=10, pady=5)
        #define headings
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="Date:"
        heading1="Payment Receipt"
        heading2="Creditor Name:"
        heading3="Quantity:"
        heading4="Date Granted:"
        heading5="Served By:"
        heading6="Price Per Litre:"
        heading7="Total:"
        #first delete the text contents
        self.my_receipt1.delete('1.0','end')
        #add stuff into our scrolledtext widget
        self.my_receipt1.insert('end', "\n" +title + "\n")
        self.my_receipt1.insert('end', "\n" +sub +"\n")
        self.my_receipt1.insert('end', "\n" +heading0 + f'{self.today} {self.Time}' +"\n")
        self.my_receipt1.insert('end', "\n" +"\t"+heading1 +"\n")
        self.my_receipt1.insert('end', "\n" +heading2 + f'{self.tender_name_box.get()}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading3 + f'{self.tender_quantity_box.get()} Litres'+"\n")
        self.my_receipt1.insert('end', "\n" +heading4 + f'{self.date_box.get()}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading6 + f'Kshs {self.rate_l}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading7 + f'Kshs {self.total_amount}'+"\n")
        self.my_receipt1.insert('end', "\n" +heading5 + server+"\n")
        self.Print_button1=customtkinter.CTkButton(my_frame, text="PRINT",fg_color="red", text_color="white", text_font=("Consollas 10", -17, "bold"),width=150,height=35,command=self.print_receipt1)
        self.Print_button1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    def print_receipt1(self):
        printText=self.my_receipt1.get("1.0", 'end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        #print out as hardcopy
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt1.delete('1.0', 'end')
        self.top3.destroy()
    def loan_report(self):
        #variables
        self.choser=StringVar()
        self.year_choser=StringVar()
        months=["ALL","January","February","March","April","May","June","July","August","September","October","November","December"]
        years=[f'{self.mwaka - 4}',f'{self.mwaka - 3}', f'{self.mwaka - 2}',f'{self.mwaka - 1}',f'{self.mwaka}',f'{self.mwaka +1}',f'{self.mwaka +2}',f'{self.mwaka +3}',f'{self.mwaka +4}']
        #print function
        def print_receipt85():
            printText=self.my_receipt85.get("1.0", 'end')
            filename=tempfile.mktemp(".txt")
            open(filename, "w").write(printText)
            #print out as hardcopy
            win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
            self.my_receipt85.delete('1.0', 'end')
        def choose_month(event):
            if self.choser.get()=="January":
                self.choosed=1
            if self.choser.get()=="February":
                self.choosed=2
            if self.choser.get()=="March":
                self.choosed=3
            if self.choser.get()=="April":
                self.choosed=4
            if self.choser.get()=="May":
                self.monthm=5
            if self.choser.get()=="June":
                self.choosed=6
            if self.choser.get()=="July":
                self.choosed=7
            if self.choser.get()=="August":
                self.choosed=8
            if self.choser.get()=="September":
                self.choosed=9
            if self.choser.get()=="October":
                self.choosed=10
            if self.choser.get()=="November":
                self.choosed=11
            if self.choser.get()=="December":
                self.choosed=12
        def generate_loan_report():
            if self.choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Month",parent=self.top85)
            elif self.year_choser.get()=="":
                messagebox.showerror("ERROR","Please Choose Year",parent=self.top85)
            else:
                if self.choser.get()=="ALL":
                    advances_all_total=0.0
                    #receipt
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1="Served By:"
                    heading2=f'Total Advance(Kshs):'
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +"ALL DEBTORS"+ f' {self.year_choser.get()}'+"\n")
                    self.my_receipt85.insert('end', "\n" +"Name"+"\t"+"Farmer_ID"+"\t"+"Advance_Amount"+" Month"+"\t"+"Year"+"\n")
                    #queries
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE STATUS=? AND YEAR=? ORDER BY Customer_ID ASC",("NOT PAID",self.year_choser.get(),))
                    all_debtors=c.fetchall()
                    conn.commit()
                    conn.close()
                    for x in all_debtors:
                        self.my_receipt85.insert('end', "\n" +str(x[1])+"\t"+str(x[2])+"\t"+str(x[0])+"\t"+f'Kshs{x[5]}'+"\t"+str(x[7])+"\t"+str(x[8])+"\n")
                        advances_all_total+=float(x[5])
                    self.my_receipt85.insert('end', "\n" +heading2 + f'{advances_all_total}'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading1 +"\t"+server+"\n")
                else:
                    #receipt
                    advances_m_total=0.0
                    #define headings
                    title="SAMARIA MILK GROUP"
                    sub="Quality Milk, Healthy Life"
                    heading1="Served By:"
                    heading2="Total Advance(Kshs):"
                    #first delete the scrolledtext  contents
                    self.my_receipt85.delete('1.0', 'end')
                    #add stuff into our scrolled text
                    self.my_receipt85.insert('end', "\n" +title + "\n")
                    self.my_receipt85.insert('end', "\n" +sub + "\n")
                    self.my_receipt85.insert('end', "\n" +self.today +','+self.Time+"\n")
                    self.my_receipt85.insert('end', "\n" +f'DEBTORS For {self.choser.get()}'+ f' {self.year_choser.get()}'+"\n")
                    self.my_receipt85.insert('end', "\n" +"Name"+"\t"+"  Farmer_ID"+"\t"+" Advance_Amount"+"\n")
                    #queries
                    conn=sqlite3.connect('samaria database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOANS WHERE STATUS=? AND MONTH=? AND YEAR=? ORDER BY Customer_ID ASC",("NOT PAID",self.choosed,self.year_choser.get(),))
                    monthly_debtors=c.fetchall()
                    conn.commit()
                    conn.close()
                    for x in monthly_debtors:
                        self.my_receipt85.insert('end', "\n" +str(x[1])+"\t"+str(x[2])+"\t"+str(x[0])+"\t"+f'Kshs{x[5]}'+"\n")
                        advances_m_total+=float(x[5])
                    self.my_receipt85.insert('end', "\n" +heading2 + f'{advances_m_total}'+"\n")
                    self.my_receipt85.insert('end', "\n" +heading1 +"\t"+server+"\n")
        #toplevel
        self.top85=Toplevel()
        self.top85.iconbitmap("logo1.ico")
        self.top85.state('zoomed')
        self.title_frame=Frame(self.top85)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="LOANS REPORT"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top85,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.choose_month_label=customtkinter.CTkLabel(self.left_frame,text="Choose Month:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=25)
        self.choose_month_label.grid(row=0,column=0,columnspan=5,padx=10,pady=20)
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.choser,values=months,width=200,height=25,fg_color="red",text_color="white",command=choose_month)
        self.choose_month_menu.grid(row=0, column=5,columnspan=3)
        self.choose_year_menu=customtkinter.CTkOptionMenu(self.left_frame,variable=self.year_choser,values=years,width=200,height=25,fg_color="red",text_color="white")
        self.choose_year_menu.grid(row=0, column=8,columnspan=2)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_loan_report)
        self.generate_button.grid(row=0,column=10,padx=20,pady=20,columnspan=5,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt85=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
        self.my_receipt85.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt85)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
class Local_Feeds:
    def __init__(self, master) -> None:
        self.top0=Toplevel()
        self.top0.geometry("1360x1000")
        self.top0.iconbitmap("logo1.ico")
        self.top0.state('zoomed')
         #menu
        my_menu = Menu(self.top0)
        self.top0.config(menu=my_menu)
        #create menu item
        records_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Records", menu=records_menu)
        records_menu.add_command(label="Farmer Records", command=self.load_customer_records_window)
        
        farmers_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Sales",menu=farmers_menu)
        farmers_menu.add_command(label="Farmer's Sales",command=self.load_customer_sales_window)
        farmers_menu.add_separator()
        farmers_menu.add_command(label="Local Sales", command=self.load_local_sales_window)
        
        loans_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Advance",menu=loans_menu)
        loans_menu.add_command(label="Advance", command=self.load_loan_window)
        
        feeds_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Feeds",menu=feeds_menu)
        feeds_menu.add_command(label="Local Feeds", command=self.load_local_feeds_window)
        feeds_menu.add_separator()
        feeds_menu.add_command(label="Farmer Feeds", command=self.load_customer_feeds_window)
        
        payments_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Payments",menu=payments_menu)
        payments_menu.add_command(label="Payments", command=self.load_customer_payments_window)

        help_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Help", menu=help_menu)

        creditors_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Creditors", menu=creditors_menu)
        creditors_menu.add_command(label="Feeds Creditors",command=self.pay_by_cash)

        about_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu)
        about_menu.add_command(label="About Samaria APP",command=self.about_menu)
        
        #create label widget containing logo
        self.title_frame=Frame(self.top0)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub1="LOCAL FEEDS"
        self.img=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img)
        self.my_img_label.grid(row=0, column=0,rowspan=4, sticky=W)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title,width=200, height=50, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"))
        self.my_title_text.grid(row=0, column=1,columnspan=4, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub,width=150,height=35, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"))
        self.my_sub_text.grid(row=1, column=1,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub1,width=150, height=35, fg_color="orange",text_color="white", text_font=("Consollas 10", -30, "underline","bold"))
        self.my_sub1_text.grid(row=2, column=1,columnspan=4)
        #feeds table
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE Local_Feeds")
        print("table dropped succesfully")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS Local_Feeds(
                    Feed_Names TEXT NOT NULL,
                    Feed_Quantity REAL NOT NULL,
                    Price REAL NOT NULL,
                    DATE INT NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS LOCAL_CREDITORS(
                    Creditors_Name TEXT NOT NULL,
                    Phone_Number INT NOT NULL,
                    Feeds_Name TEXT NOT NULL,
                    Feeds_Quantity REAL NOT NULL,
                    Total REAL NOT NULL,
                    MONTH INT NOT NULL,
                    YEAR INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        conn.commit()
        conn.close()
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top0,border_color="green",border_width=5, width=400,height=450)
        self.left_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #dates
        self.currentDateTime=date.today()
        self.today=self.currentDateTime.strftime("%A-%B %d, %Y")
        self.time=datetime.now()
        self.today1=self.time.strftime("%m/%d/%Y")
        self.Time=self.time.strftime("%I:%M:%S %p")
        self.mwaka=datetime.now().year
        self.mwezi=datetime.now().month
        print(self.mwezi)
        #variables
        self.count=0
        self.start=2
        self.start1=2
        self.start2=2
        self.t1=StringVar()
        self.t2=StringVar()
        #labels
        feeds_title="MONTHLY FEEDS SALES"
        self.feeds_title_label=customtkinter.CTkLabel(self.left_frame, text=feeds_title, fg_color="orange",text_color="white", text_font=("Consollas 10",-20, "underline","bold"),width=170,height=25)
        self.feeds_title_label.grid(row=0, column=0, columnspan=3,pady=6)
        self.today_label=customtkinter.CTkLabel(self.left_frame, text="Today:",fg_color="brown", text_color="white", text_font=("Consollas 10", -15, "bold"),width=120,height=25)
        self.today_label.grid(row=1, column=0)
        self.today_date=customtkinter.CTkLabel(self.left_frame, text=self.today)
        self.today_date.grid(row=1, column=1,sticky=W)
        #creditors
        self.creditors_label=customtkinter.CTkLabel(self.left_frame,text="Enter Creditors Name:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.creditors_label.grid(row=2,column=0,padx=10,pady=3)
        self.creditors_phone_label=customtkinter.CTkLabel(self.left_frame,text="Enter Phone Number:",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=150,height=30)
        self.creditors_phone_label.grid(row=3,column=0,padx=10,pady=3)
        self.creditors_name_entry=customtkinter.CTkEntry(self.left_frame,width=200,height=30,border_color="blue")
        self.creditors_name_entry.grid(row=2,column=1)
        self.creditors_p_number_entry=customtkinter.CTkEntry(self.left_frame,width=200,height=30,border_color="blue")
        self.creditors_p_number_entry.grid(row=3,column=1)
        #treeview
        self.tree_frame=Frame(self.left_frame, highlightbackground="green", highlightthickness=5, width=300, height=200, bd=0)
        self.tree_frame.grid(row=5, column=0, columnspan=3, padx=20, pady=5)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=15,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll=Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree=ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=7)
        self.my_tree.pack()
        #configure our scrollbar
        self.tree_scroll.config(command=self.my_tree.yview)
        #define our columns
        self.my_tree['columns']=("Feeds Name", "Quantity", "Price","DATE")
        #format our columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("Feeds Name", width=200, anchor="w")
        self.my_tree.column("Quantity", width=100, anchor="w")
        self.my_tree.column("Price", width=100, anchor="w")
        self.my_tree.column("DATE", width=100, anchor="w")
        #create headings
        self.my_tree.heading("#0", text="")
        self.my_tree.heading("Feeds Name", text="Feeds Name", anchor="w")
        self.my_tree.heading("Quantity", text="Quantity", anchor="w")
        self.my_tree.heading("Price", text="Total", anchor="w")
        self.my_tree.heading("DATE", text="Date", anchor="w")
        #create striped row tags
        self.my_tree.tag_configure('oddrow', background="white")
        self.my_tree.tag_configure('evenrow', background="violet")
        self.total_feeds_entry=customtkinter.CTkEntry(self.tree_frame, width=100,height=25,border_color="blue",textvariable=self.t1)
        self.total_feeds_entry.pack(anchor="e", pady=2, padx=10)
        #buttons
        self.choose_type_button=customtkinter.CTkButton(self.left_frame, text="Choose",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150,height=25,command=self.choose_feeds)
        self.choose_type_button.grid(row=4, column=0,columnspan=3,pady=10)
        self.give_out_button=customtkinter.CTkButton(self.left_frame, text="GRANT FEEDS",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150,height=25,command=self.grant_feeds)
        self.give_out_button.grid(row=6, column=0, columnspan=4, padx=20,pady=8)
        #dropdown menu
        self.clicked=StringVar()
        #self.given_out()
        #*******************************************************************************************************************************************************************************************************
        #right frame
        self.right_frame=customtkinter.CTkFrame(self.top0,border_color="maroon",border_width=5, width=400,height=450)
        self.right_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        #title
        feeds_inventory_title="FEEDS INVENTORY"
        self.feeds_inventory_label=customtkinter.CTkLabel(self.right_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
        self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
        #create another treeview
        self.tree_frame1=Frame(self.right_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
        self.tree_frame1.grid(row=1, column=0, padx=30, pady=10, columnspan=10)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview scrollbar
        self.tree_scroll1=Scrollbar(self.tree_frame1)
        self.tree_scroll1.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree1=ttk.Treeview(self.tree_frame1, yscrollcommand=self.tree_scroll1.set,height=8)
        self.my_tree1.pack()
        #configure our scrollbar
        self.tree_scroll1.config(command=self.my_tree1.yview)
        #define our columns
        self.my_tree1['columns']=("FEEDS NAME", "QUANTITY", "PRICE")
        #format our columns
        self.my_tree1.column("#0", width=0, stretch=NO)
        self.my_tree1.column("FEEDS NAME", anchor="w", width=270)
        self.my_tree1.column("QUANTITY", anchor="w", width=200)
        self.my_tree1.column("PRICE", anchor="w", width=200)
        #create headings
        self.my_tree1.heading("#0", text="")
        self.my_tree1.heading("FEEDS NAME", text="FEEDS NAME", anchor="w")
        self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="w")
        self.my_tree1.heading("PRICE", text="PRICE", anchor="w")
        #create striped row tags
        self.my_tree1.tag_configure('oddrow', background="white")
        self.my_tree1.tag_configure('evenrow', background="violet")
        #single click binding
        self.my_tree1.bind("<ButtonRelease-1>", self.clicker)

        self.query_database()
        #labels
        self.title_label=customtkinter.CTkLabel(self.right_frame, text="UPDATE FEEDS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
        self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=5)
        self.feeds_name_label=customtkinter.CTkLabel(self.right_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
        self.feeds_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=5)
        self.feeds_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
        self.feeds_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=5)
        self.feeds_price_label=customtkinter.CTkLabel(self.right_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
        self.feeds_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=5)
        #entryboxes
        self.feeds_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
        self.feeds_name_entry.grid(row=3, column=2)
        self.feeds_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
        self.feeds_quantity_entry.grid(row=4, column=2)
        self.feeds_price_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
        self.feeds_price_entry.grid(row=5, column=2)
        #buttons
        #self.add_feeds_button=customtkinter.CTkButton(self.right_frame, text="ADD FEEDS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_feeds)
        #self.add_feeds_button.grid(row=6, column=0,padx=5, pady=10, sticky=E)
        self.update_feeds_button=customtkinter.CTkButton(self.right_frame, text="UPDATE FEEDS",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.verify_admin)
        self.update_feeds_button.grid(row=6, column=1,padx=5, pady=10,sticky=W)
        self.remove_feeds_button=customtkinter.CTkButton(self.right_frame, text="REMOVE FEEDS",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.verify_admin1)
        self.remove_feeds_button.grid(row=6, column=2,padx=5, pady=10,sticky=W)
        #create feeds inventory table
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE Feeds_Inventory")
        print("Table dropped")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS Feeds_Inventory(
                    Feeds_Name TEXT PRIMARY KEY NOT NULL,
                    Quantity INT NOT NULL,
                    Price REAL NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        conn.commit()
        conn.close()
    #about menu
    def about_menu(self):
        #author
        def author_info():
            self.my_txt.delete(1.0,END)
            self.my_img1=ImageTk.PhotoImage(Image.open('Vinicious.jpg'))
            self.my_txt.tag_configure('center',justify='center')
            self.my_txt.image_create(1.0, image=self.my_img1)
            self.my_txt.tag_add("center","1.0","end")
            self.my_txt.tag_configure('bold',font=("Consollas 10",20,"bold"))
            self.my_txt.tag_configure('medium',font=("Consollas 10",13,"bold"))
            self.my_txt.configure(state='normal')
            self.my_txt.insert(END,'\n                    VINIUS M MUTHII\n','bold')
            quote1="""
                He is a software developer/engineer with great mastery
                in desktop applications. Can navigate from Dairy Firm
                Projects, Agrovets, MiniShops & Supermarkets to
                Wholesale dealers and many more.....
                Passionate to meet clients desires and produce
                applications for optimal business management.
                                           Contacts:
                            Phone Number: 0713810930
                            Email : viniusmugo@gmail.com
                    Businness Flourish with Samaria APP!!!
                """
            self.my_txt.insert(END, quote1,'medium')
            self.my_txt.configure(state='disabled')
        self.top99=Toplevel()
        self.top99.title("SAMARIA MILK GROUP")
        self.top99.iconbitmap("logo1.ico")
        self.my_frame=customtkinter.CTkFrame(self.top99,border_width=2,border_color="darkblue",width=915,height=70)
        self.my_frame.pack(side=BOTTOM)
        self.author_button=customtkinter.CTkButton(self.my_frame,text="Author",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'),command=author_info)
        self.author_button.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        self.license_button=customtkinter.CTkButton(self.my_frame,text="License",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.license_button.grid(row=0,column=5,columnspan=5,padx=10,pady=10)
        self.credits_button=customtkinter.CTkButton(self.my_frame,text="Credits",text_color="blue",corner_radius=10,width=290,height=30,text_font=("Consollas 10",-15,'bold'))
        self.credits_button.grid(row=0,column=10,columnspan=5,padx=10,pady=10)
        self.my_text=Text(self.top99,height=25,width=43,bg="lightgrey")
        self.my_text.pack(side=LEFT)
        #image label
        self.my_img=ImageTk.PhotoImage(Image.open('Samaria Mega1Logo.jpg'))
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.insert(END,'\n')
        self.my_text.configure(state='normal')
        self.my_text.image_create(END, image=self.my_img)
        self.my_text.configure(state='disabled')
        #description
        self.my_txt=Text(self.top99,height=25,width=70,bg="lightgrey")
        self.my_txt.tag_configure('bold',font=("Consollas 10", 13,'bold'))
        self.my_txt.tag_configure('big',font=("Consollas 10", 35,"bold"),foreground="green")
        self.my_txt.configure(state='normal')
        self.my_txt.insert(END,'\n  SAMARIA MILK APP\n','big')
        quote="""
            Samaria Milk APP is an intergrated,user friendly desktop
            application that helps an individual or a group of
            people to maintain key records in a Dairy Firm Context.
            It entails key modules like:
                        RECORDS
                        SALES
                        FEEDS
                        LOANS
                        PAYMENTS
            These Modules helps the firm to manage every aspect of
            their customers and also maintain updated records
            regarding the firm.
                    ALL DETAILS AT YOUR TIPS!!!!!
            """
        self.my_txt.insert(END, quote, 'bold')
        #self.my_txt.configure(state='disabled')
        self.my_txt.pack(side=LEFT)
    #choose feeds function
    def choose_feeds(self):
        self.top97=Toplevel()
        self.top97.title("SAMARIA MILK GROUP")
        self.top97.iconbitmap("logo1.ico")
        #connect to database
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Feeds_Name FROM Feeds_Inventory")
        self.feeds_names=c.fetchall()
        self.data=[[numbers]for numbers in self.feeds_names]
        #print(self.data)
        conn.commit()
        conn.close()
        self.my_frame=Frame(self.top97)
        self.my_frame.pack(padx=20,pady=20,anchor="w")
        self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE FEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
        self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
        self.my_sheet=Sheet(self.my_frame,
                            align = "w",
                            header_font=("Consollas 10",15,"bold"),
                            font=("Consollas 10",13,"normal"),
                            data=self.data,
                            headers= ["Feeds Name","Checkbox","Feeds Quantity"],
                            height=400,
                            show_x_scrollbar = False,
                            show_y_scrollbar =True,
                            width=650)
        self.my_sheet.enable_bindings("copy",
                                   "rc_select",
                                   "arrowkeys",
                                   "double_click_column_resize",
                                   "column_width_resize",
                                   "column_select",
                                   "row_select",
                                   "drag_select",
                                   "single_select",
                                   "select_all")
        self.my_sheet.enable_bindings("edit_header")
        self.my_sheet.grid(row=1,column=0,columnspan=4)
        def get_info(event=None):
            for number in self.data:
                if number[1]==True:
                    print(number[0])
                #print(hdrs)
        def get_quantity(event=None):
            for number in self.data:
                if number[1]==True:
                    if number[2]=="Bags":
                        number[2]=event.text
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(number[0],))
                        pesa=c.fetchone()
                        total_amount=(pesa*float(number[2]))
                        conn.commit()
                        conn.close()
                        initial=self.total_entry.get()
                        if initial=="":
                            initial=0.0
                        updated= float(initial)+total_amount
                        self.total_entry.delete(0,END)
                        self.total_entry.insert(0,updated)
                    #self.my_sheet.get_dropdown_values()
        self.my_sheet.create_dropdown(r="all",c=2,values=["Bags"]+[f"{i}" for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)],selection_function=get_quantity)
        self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
        self.my_sheet.get_checkboxes()
        self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
        self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
        self.my_sheet.default_header_height(height="2")
        self.my_sheet.column_width(column=0,width=300)
        self.my_sheet.column_width(column=2,width=150)
        def grant_feeds():
            self.my_tree.delete(* self.my_tree.get_children())
            for record in self.data:
                if record[1]==True:
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM Feeds_Inventory WHERE Feeds_Name=?",(record[0],))
                    pesa=c.fetchone()
                    c.execute("SELECT Quantity FROM Feeds_Inventory WHERE Feeds_Name=?",(record[0],))
                    initial_q_quantity=c.fetchone()
                    if initial_q_quantity==0:
                        messagebox.showerror("ERROR",f'{record[0]}'" Stock is Depleted, Consider New Stock",parent =self.top0)
                        continue
                    if (initial_q_quantity - float(record[2])) < 0 :
                        messagebox.showerror("ERROR", f'{record[0]}'"Stock is Less Than"f'{record[2]}',parent=self.top0)
                        continue
                    if initial_q_quantity==1:
                        messagebox.showinfo("REMINDER",f'{record[0]}'" Stock Depleting, Consider Adding New Stock",parent =self.top0)
                    total=pesa* float(record[2])
                    if self.count%2==0:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total, self.today1), tags=("evenrow"),)
                    else:
                        self.my_tree.insert('', index='end', iid=self.count, text="", values=(record[0],record[2],total, self.today1), tags=("oddrow"),)
                    self.count+=1
            self.top97.destroy()
            self.get_total()
        #buttons
        self.total_label=customtkinter.CTkLabel(self.my_frame,text="TOTAL",fg_color="brown",text_color="white",text_font=("Consollas 10",-15,"bold"),width=200,height=30)
        self.total_label.grid(row=3,column=0,columnspan=2,padx=20,pady=10)
        self.total_entry=customtkinter.CTkEntry(self.my_frame,border_color="blue",width=200,height=30)
        self.total_entry.grid(row=3,column=2,columnspan=2,padx=20,pady=10)
        self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT FEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
        self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
    #get total
    def get_total(self):
        self.t1
        sum1=0.0
        for child in self.my_tree.get_children():
            sum1 +=float(self.my_tree.item(child,"values")[2])
            self.t1.set(sum1)
    #get total
    def get_total1(self):
        self.t2
        sum2=0.0
        for child in self.my_tree2.get_children():
            sum2 +=float(self.my_tree2.item(child,"values")[2])
            self.t2.set(sum2)      
    #give feeds
    def grant_feeds(self):
        check= self.my_tree.get_children()
        if check==():
            messagebox.showerror("ERROR", "Please Choose Feeds",parent =self.top0)
        else:
            response=messagebox.askyesno("Confirm", "Do you want to add a creditor?",parent =self.top0)
            if response==1:
                #check
                if self.creditors_name_entry.get()=="":
                    messagebox.showerror("ERROR","Please Enter Creditor's Name",parent=self.top0)
                elif self.creditors_p_number_entry.get()=="":
                    messagebox.showerror("ERROR","Please Enter Creditor's Phone Number",parent=self.top0)
                else:
                    #database
                    for child in self.my_tree.get_children():
                        data= self.my_tree.item(child, "values")[0]
                        datum=self.my_tree.item(child, "values")[1]
                        datam=self.my_tree.item(child, "values")[2]
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        #insert data
                        c.execute("INSERT INTO Local_Feeds VALUES(:Feed_Names, :Feed_Quantity, :Price,:DATE,:Month, :Year)",
                                {
                                    'Feed_Names': data,
                                    'Feed_Quantity': datum,
                                    'Price' : datam,
                                    'DATE': self.today1,
                                    'Month': self.mwezi,
                                    'Year': self.mwaka
                                    })
                        conn.commit()
                        conn.close()
                        #update feeds_inventory table
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                        initial_quantity=c.fetchone()
                        current_quantity=(initial_quantity - float(datum))
                        c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                        cost=c.fetchone()
                        c.execute("SELECT Month From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                        monthm=c.fetchone()
                        c.execute("SELECT Year From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                        yearm=c.fetchone()
                        c.execute("SELECT DATE From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                        datem=c.fetchone()
                        c.execute(""" UPDATE Feeds_Inventory SET
                                    Feeds_Name=:f_name,
                                    Quantity=:q_ty,
                                    Price=:prie,
                                    Month=:moth,
                                    Year =:yoar,
                                    DATE =:siku
                            
                                    WHERE Feeds_Name=:f_name""",
                                    {
                                        'f_name': data,
                                        'q_ty' : current_quantity,
                                        'prie' : cost,
                                        'moth': monthm,
                                        'yoar' : yearm,
                                        'siku' : datem
                                        })
                        conn.commit()
                        conn.close()
                        #creditors database
                        conn=sqlite3.connect('samaria feeds database.db')
                        c=conn.cursor()
                        c.execute("INSERT INTO LOCAL_CREDITORS VALUES(:Creditors_Name,:Phone_Number,:Feeds_Name,:Feeds_Quantity,:Total,:MONTH,:YEAR,:DATE)",
                                  {
                                      'Creditors_Name':self.creditors_name_entry.get(),
                                      'Phone_Number':self.creditors_p_number_entry.get(),
                                      'Feeds_Name':data,
                                      'Feeds_Quantity':datum,
                                      'Total':datam,
                                      'MONTH':self.mwezi,
                                      'YEAR':self.mwaka,
                                      'DATE':self.today1
                                      })
                        conn.commit()
                        conn.close()
                    #call receipt function
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM LOCAL_CREDITORS")
                    ZOTE=c.fetchall()
                    print(ZOTE)
                    conn.commit()
                    conn.close()
                    self.receipt1()  
                    self.my_tree.delete(* self.my_tree.get_children())
                    #clear entries
                    self.creditors_name_entry.delete(0,END)
                    self.creditors_p_number_entry.delete(0,END)
                    self.total_feeds_entry.delete(0, END)
                    self.query_database()
            else:
                for child in self.my_tree.get_children():
                    data= self.my_tree.item(child, "values")[0]
                    datum=self.my_tree.item(child, "values")[1]
                    datam=self.my_tree.item(child, "values")[2]
                    conn=sqlite3.connect('samaria feeds database.db')
                    c=conn.cursor()
                    #insert data
                    c.execute("INSERT INTO Local_Feeds VALUES(:Feed_Names, :Feed_Quantity, :Price,:DATE,:Month, :Year)",
                            {
                                'Feed_Names': data,
                                'Feed_Quantity': datum,
                                'Price' : datam,
                                'DATE': self.today1,
                                'Month': self.mwezi,
                                'Year': self.mwaka
                                })
                    conn.commit()
                    conn.close()
                    #update feeds_inventory table
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                    initial_quantity=c.fetchone()
                    current_quantity=(initial_quantity - float(datum))
                    c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                    cost=c.fetchone()
                    c.execute("SELECT Month From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                    monthm=c.fetchone()
                    c.execute("SELECT Year From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                    yearm=c.fetchone()
                    c.execute("SELECT DATE From Feeds_Inventory WHERE Feeds_Name=?",(data,))
                    datem=c.fetchone()
                    c.execute(""" UPDATE Feeds_Inventory SET
                                Feeds_Name=:f_name,
                                Quantity=:q_ty,
                                Price=:prie,
                                Month=:moth,
                                Year =:yoar,
                                DATE =:siku
                        
                                WHERE Feeds_Name=:f_name""",
                                {
                                    'f_name': data,
                                    'q_ty' : current_quantity,
                                    'prie' : cost,
                                    'moth': monthm,
                                    'yoar' : yearm,
                                    'siku' : datem
                                    })
                    conn.commit()
                    conn.close()  
                #call receipt function                
                self.receipt()  
                self.my_tree.delete(* self.my_tree.get_children())
                #clear entries
                self.creditors_name_entry.delete(0,END)
                self.creditors_p_number_entry.delete(0,END)
                self.total_feeds_entry.delete(0, END)
                self.query_database()
    #receipt
    def receipt1(self):                                     
        self.top1=Toplevel()
        self.top1.title("SAMARIA MILK GROUP")
        self.top1.iconbitmap("logo1.ico")
        my_frame1=Frame(self.top1, width=50)
        my_frame1.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame1, text="RECEIPT",fg_color="purple",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=200,height=35)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame1, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="FEEDS"
        heading1="Feeds Name"
        heading2="Quantity"
        heading3="Price"
        heading4="DATE:"
        heading5="Total Amount:"
        heading6="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0', 'end')
        #add contents to our scrolled widget
        self.my_receipt.insert('end', "\n" + title +"\n")
        self.my_receipt.insert('end', "\n" + sub +"\n")
        self.my_receipt.insert('end', "\n" + heading0 +"\n")
        self.my_receipt.insert('end', "\n" + heading4 + f'{self.today} {self.Time}'+"\n")
        self.my_receipt.insert('end', "\n" + f'Creditor Name: {self.creditors_name_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading1+"\t"+"\t"+ heading2 +"\t" +"\t"+ heading3 +"\n")
        for child in self.my_tree.get_children():
            data= self.my_tree.item(child, "values")[0]
            datum=self.my_tree.item(child, "values")[1]
            datam=self.my_tree.item(child, "values")[2]
            date=self.my_tree.item(child, "values")[3]
            self.my_receipt.insert('end', "\n" + data +"\t"+"\t"+datum+"\t"+"\t"+f' KShs {datam}'+"\n")
        self.my_receipt.insert('end', "\n" + heading5 +"\t"+"\t"+ f' KShs {self.total_feeds_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading6+ "\t"+ f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame1, text="PRINT", command=self.print_receipt,fg_color="red",text_color="white", text_font=("Consollas 10",-20, "bold"),width=200,height=40)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
    def print_receipt(self):
        printText=self.my_receipt.get('1.0','end')
        filename=tempfile.mktemp(".txt")
        open(filename, "w").write(printText)
        win32api.ShellExecute(0,
                                "printto",
                                filename,
                                '"%s"' % win32print.GetDefaultPrinter(),
                                ".",
                                0
                                )
        self.my_receipt.delete('1.0', 'end')
        self.top1.destroy()
    #receipt
    def receipt(self):                                     
        self.top1=Toplevel()
        self.top1.title("SAMARIA MILK GROUP")
        self.top1.iconbitmap("logo1.ico")
        my_frame1=Frame(self.top1, width=50)
        my_frame1.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame1, text="RECEIPT",fg_color="purple",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=200,height=35)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame1, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="FEEDS"
        heading1="Feeds Name"
        heading2="Quantity"
        heading3="Price"
        heading4="DATE:"
        heading5="Total Amount:"
        heading6="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0', 'end')
        #add contents to our scrolled widget
        self.my_receipt.insert('end', "\n" + title +"\n")
        self.my_receipt.insert('end', "\n" + sub +"\n")
        self.my_receipt.insert('end', "\n" + heading0 +"\n")
        self.my_receipt.insert('end', "\n" + heading4 + f'{self.today} {self.Time}'+"\n")
        self.my_receipt.insert('end', "\n" + heading1+"\t"+"\t"+ heading2 +"\t" +"\t"+ heading3 +"\n")
        for child in self.my_tree.get_children():
            data= self.my_tree.item(child, "values")[0]
            datum=self.my_tree.item(child, "values")[1]
            datam=self.my_tree.item(child, "values")[2]
            date=self.my_tree.item(child, "values")[3]
            self.my_receipt.insert('end', "\n" + data +"\t"+"\t"+datum+"\t"+"\t"+f' KShs {datam}'+"\n")
        self.my_receipt.insert('end', "\n" + heading5 +"\t"+"\t"+ f' KShs {self.total_feeds_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading6+ "\t"+ f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame1, text="PRINT", command=self.print_receipt,fg_color="red",text_color="white", text_font=("Consollas 10",-20, "bold"),width=200,height=40)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
    #givenout feeds
    def given_out(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT DISTINCT Feed_Names, SUM(Feed_Quantity) FROM Local_Feeds WHERE Month=? AND Year=? GROUP BY Feed_Names",(self.mwezi,self.mwaka,))
        group=c.fetchall()
        conn.commit()
        conn.close()
        for record in group:
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            conn.row_factory=lambda cursor, row:row[0]
            c.execute("SELECT Price From Feeds_Inventory WHERE Feeds_Name=?",(str(record[0]),))
            mapesa=c.fetchone()
            conn.commit()
            conn.close()
            if mapesa !=None:
                if self.count%2==0:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], record[1], (record[1] * int(mapesa[0]))), tags=("evenrow"),)
                else:
                    self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], record[1],(record[1] * int(mapesa[0]))), tags=("oddrow"),)
                self.count+=1
            else:
                pass
        self.get_total1()
    #select month
    def select_month(self,event):
        if self.clicked.get()==f'January-{self.mwaka}':
            self.mwezi=1
        if self.clicked.get()==f'February-{self.mwaka}':
            self.mwezi=2
        if self.clicked.get()==f'March-{self.mwaka}':
            self.mwezi=3
        if self.clicked.get()==f'April-{self.mwaka}':
            self.mwezi=4
        if self.clicked.get()==f'May-{self.mwaka}':
            self.mwezi=5
        if self.clicked.get()==f'June-{self.mwaka}':
            self.mwezi=6
        if self.clicked.get()==f'July-{self.mwaka}':
            self.mwezi=7
        if self.clicked.get()==f'August-{self.mwaka}':
            self.mwezi=8
        if self.clicked.get()==f'September-{self.mwaka}':
            self.mwezi=9
        if self.clicked.get()==f'October-{self.mwaka}':
            self.mwezi=10
        if self.clicked.get()==f'November-{self.mwaka}':
            self.mwezi=11
        if self.clicked.get()==f'December-{self.mwaka}':
            self.mwezi=12
        self.total_feeds_entry2.delete(0, END)
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.given_out()
    #clear entries
    def clear_entries(self):
        self.feeds_name_entry.delete(0, END)
        self.feeds_quantity_entry.delete(0, END)
        self.feeds_price_entry.delete(0, END)
    #create binding function
    def clicker(self,e):
        #clear entries
        self.clear_entries()
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.feeds_name_entry.insert(0, values[0])
        self.feeds_quantity_entry.insert(0, values[1])
        self.feeds_price_entry.insert(0, values[2])
    #create query function
    def query_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Feeds_Inventory ORDER BY Feeds_Name ASC")
        f_eeds=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in f_eeds:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[2]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[2]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def verify_admin(self):
        self.top95=Toplevel()
        self.top95.title("SAMARIA MILK GROUP")
        self.top95.iconbitmap("logo1.ico")
        my_frame=Frame(self.top95)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.update_feeds)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #update our data
    def update_feeds(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top95.destroy()   
            response=messagebox.askyesno("Confirm", "Are you Sure?",parent =self.top0)
            if response ==1:
                #grab the record
                selected = self.my_tree1.focus()
                #update record
                self.my_tree1.item(selected, text="", values=(self.feeds_name_entry.get(), self.feeds_quantity_entry.get(),self.feeds_price_entry.get()))
                #update the database
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                quantum=c.fetchone()
                c.execute("SELECT Month From Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                monthmn=c.fetchone()
                c.execute("SELECT Year From Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                yearmn=c.fetchone()
                c.execute("SELECT DATE From Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                datemn=c.fetchone()
                c.execute(""" UPDATE Feeds_Inventory SET
                                Feeds_Name=:f_name,
                                Quantity=:q_ty,
                                Price=:prie,
                                Month=:moth,
                                Year =:yuar,
                                DATE =:sikuku

                            WHERE Feeds_Name=:f_name""",
                                {
                                    'f_name': self.feeds_name_entry.get(),
                                    'q_ty' : quantum,
                                    'prie' : self.feeds_price_entry.get(),
                                    'moth' : monthmn,
                                    'yuar' : yearmn,
                                    'sikuku' : datemn
                                    })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.feeds_name_entry.get()} Price Updated Succesfully',parent =self.top0)
            #clear entries
            self.clear_entries()
    def verify_admin1(self):
        self.top96=Toplevel()
        self.top96.title("SAMARIA MILK GROUP")
        self.top96.iconbitmap("logo1.ico")
        my_frame=Frame(self.top96)
        my_frame.pack(anchor="w")
        self.admin_passcode_label=Label(my_frame, text="Enter Administrator Password:",fg="brown", bg="white", font=("Consollas 10", 10, "bold"))
        self.admin_passcode_label.grid(row=0, column=0, padx=10, pady=10)
        self.admin_passode_entry=customtkinter.CTkEntry(my_frame, show="*", width=150, height=40,border_color="blue",placeholder_text="Admin Password",placeholder_text_color="violet")
        self.admin_passode_entry.grid(row=0, column=1, padx=5)
        self.admin_button=customtkinter.CTkButton(my_frame, text="VERIFY ADMIN", fg_color="maroon", text_color="white", text_font=("Consollas 10", -18, "bold"),width=200,height=40,command=self.remove_feeds)
        self.admin_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    #remove data
    def remove_feeds(self):
        conn=sqlite3.connect('samaria database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Password FROM User_Data WHERE User_Mode='Administrator'")
        admin_password=c.fetchone()
        conn.commit()
        conn.close()
        if admin_password!=self.admin_passode_entry.get():
            messagebox.showerror("ERROR", "Incorrect Password, Check Password And Try Again",parent=self.top0)
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()
        else:
            self.admin_passode_entry.delete(0, END)
            self.top96.destroy()   
            response=messagebox.askyesno("Danger", "Do you want to delete this Feeds?",parent =self.top0)
            if response ==1:
                x= self.my_tree1.selection()[0]
                #delete from database
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Quantity From Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                quantumn=c.fetchone()
                if quantumn != 0:
                    messagebox.showerror("ERROR", "You Cannot Delete Feeds If NOT Depleted", parent=self.top0)
                else:
                    self.my_tree1.delete(x)
                    c.execute("DELETE FROM Feeds_Inventory WHERE Feeds_Name=?",(self.feeds_name_entry.get(),))
                    messagebox.showinfo("Bravo",f'{self.feeds_name_entry.get()} Deleted Succesfully',parent =self.top0)
                conn.commit()
                conn.close()
            #clear entries
            self.clear_entries()
    def clicker1(self,e):
        self.creditor_name_entry.delete(0,END)
        self.total_cost_entry.delete(0,END)
        #grab record
        selected1=self.my_tree2.focus()
        #grab record values
        values=self.my_tree2.item(selected1,'values')
        #output to entry boxes
        self.creditor_name_entry.insert(0, values[0])
        self.total_cost_entry.insert(0, values[2])
    def get_creditors(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT Creditors_Name,Phone_Number,SUM(Total),MONTH,YEAR FROM LOCAL_CREDITORS GROUP BY Creditors_Name,MONTH,YEAR")
        all_creditors=c.fetchall()
        conn.commit()
        conn.close()
        for record in all_creditors:
            if self.count%2==0:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], f'0{record[1]}', f' KShs{record[2]}',record[3],record[4]), tags=("evenrow"),)
            else:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0], f'0{record[1]}', f' KShs{record[2]}',record[3],record[4]), tags=("oddrow"),)
            self.count+=1
    def pay_by_cash(self):
        #toplevel
        self.top89=Toplevel()
        self.top89.iconbitmap("logo1.ico")
        self.top89.state('zoomed')
        self.title_frame=Frame(self.top89)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="UNPAID LOCAL FEEDS"
        self.img1=ImageTk.PhotoImage(Image.open('Samaria Group Logo.jpg'))
        self.my_img_label=Label(self.title_frame, image=self.img1)
        self.my_img_label.grid(row=0, column=0, rowspan=3)
        self.my_title_text=customtkinter.CTkLabel(self.title_frame, text=title, fg_color="purple",text_color="white", text_font=("Consollas 10", -40, "bold"),width=300,height=50)
        self.my_title_text.grid(row=0, column=1, columnspan=3, padx=10, pady=5)
        self.my_sub_text=customtkinter.CTkLabel(self.title_frame, text=sub, fg_color="maroon",text_color="white", text_font=("Consollas 10", -30,"italic"),width=200,height=30)
        self.my_sub_text.grid(row=1, column=1, pady=5,columnspan=4)
        self.my_sub1_text=customtkinter.CTkLabel(self.title_frame, text=sub0, fg_color="orange",text_color="white", text_font=("Consollas 10", -30,"bold","underline"),width=200,height=30)
        self.my_sub1_text.grid(row=2, column=1, columnspan=4)
        #left frame
        self.left_frame=customtkinter.CTkFrame(self.top89,border_color="maroon",border_width=5,corner_radius=8,width=900,height=650)
        self.left_frame.pack(anchor="center")
        #heading
        tender_title="PENDING CREDITORS FEEDS"
        self.feeds_title_label=customtkinter.CTkLabel(self.left_frame, text=tender_title, fg_color="orange", text_color="white",text_font=("Consollas 10", -20, "underline","bold"),width=200,height=30)
        self.feeds_title_label.grid(row=0, column=0,pady=5,columnspan=10)
        #tender treeview
        self.tree_frame2=Frame(self.left_frame, highlightbackground="green", highlightthickness=5, width=500, height=500, bd=0)
        self.tree_frame2.grid(row=1, column=0, padx=30, pady=10,columnspan=10)
        #style our treeview
        style=ttk.Style()
        #pick a theme
        style.theme_use("default")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white"
                        )
        #change selected color
        style.map('Treeview',
                background=[('selected', 'green')])
        #treeview_scrollbar
        self.tree_scroll2=Scrollbar(self.tree_frame2)
        self.tree_scroll2.pack(side=RIGHT, fill=Y)
        #create our treeview
        self.my_tree2=ttk.Treeview(self.tree_frame2, yscrollcommand=self.tree_scroll2.set,height=9)
        self.my_tree2.pack()
        #configure the scrollbar
        self.tree_scroll2.config(command=self.my_tree2.yview)
        #define our columns
        self.my_tree2['columns']=("Creditor_Name","Phone_Number","Total_Credit","Month","Year")
        #format our columns
        self.my_tree2.column("#0", width=0, stretch=NO)
        self.my_tree2.column("Creditor_Name", anchor="w", width=200)
        self.my_tree2.column("Phone_Number", anchor="w", width=200)
        self.my_tree2.column("Total_Credit", anchor="w", width=150)
        self.my_tree2.column("Month", anchor="w", width=150)
        self.my_tree2.column("Year", anchor="w", width=150)
        #create headings
        self.my_tree2.heading("#0", text="")
        self.my_tree2.heading("Creditor_Name", text="Creditor Name", anchor="w")
        self.my_tree2.heading("Phone_Number", text="Phone Number", anchor="w")
        self.my_tree2.heading("Total_Credit", text="Total Credit", anchor="w")
        self.my_tree2.heading("Month", text="Month", anchor="w")
        self.my_tree2.heading("Year", text="Year", anchor="w")
        #striped row tags
        self.my_tree2.tag_configure('oddrow', background="white")
        self.my_tree2.tag_configure('evenrow', background="violet")
        # binding single click
        self.my_tree2.bind("<ButtonRelease-1>", self.clicker1)
        #variable
        self.svar=StringVar()
        #frame
        self.entry_frame=Frame(self.left_frame)
        self.entry_frame.grid(row=2, column=0,columnspan=10, padx=20,pady=5)
        #entry labels
        self.creditor_name_label=customtkinter.CTkLabel(self.entry_frame,text="Creditor Name:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.creditor_name_label.grid(row=1, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.total_cost_label=customtkinter.CTkLabel(self.entry_frame, text="Total:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.total_cost_label.grid(row=4, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        self.status_label=customtkinter.CTkLabel(self.entry_frame, text="Mark as Paid:",fg_color="brown", text_color="white", text_font=("Consollas 10",-15,"bold"),width=120,height=25)
        self.status_label.grid(row=5, column=0,columnspan=5, padx=10,pady=5, sticky=EW)
        #entry boxes
        self.creditor_name_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.creditor_name_entry.grid(row=1, column=5)
        self.total_cost_entry=customtkinter.CTkEntry(self.entry_frame, width=150,height=25,border_color="blue")
        self.total_cost_entry.grid(row=4, column=5)
        self.status_c=customtkinter.CTkCheckBox(self.entry_frame, text="",variable=self.svar, onvalue="PAID", offvalue="NOT PAID")
        self.status_c.deselect()
        self.status_c.grid(row=5, column=5)
        #update button
        self.update_button=customtkinter.CTkButton(self.entry_frame, text="MARK AS PAID",fg_color="purple", text_color="white", text_font=("Consollas 10",-20,"bold"),width=150,height=35,command=self.pay_credit)
        self.update_button.grid(row=6, column=0, columnspan=10, padx=20, pady=5)
        self.get_creditors()
    def pay_credit(self):
        if self.creditor_name_entry.get()=="":
            messagebox.showerror("ERROR","Please Select Creditor",parent=self.top89)
        elif self.svar.get()!="PAID":
            messagebox.showerror("ERROR","Please Mark as Paid",parent=self.top89)
        else:
            #update
            self.receipt2()
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("DELETE FROM LOCAL_CREDITORS WHERE Creditors_Name=?",(self.creditor_name_entry.get(),))
            conn.commit()
            conn.close()
            #check
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute("SELECT * FROM LOCAL_CREDITORS")
            wote=c.fetchall()
            print(wote)
            conn.commit()
            conn.close()
        #clear entries
        self.creditor_name_entry.delete(0,END)
        self.total_cost_entry.delete(0,END)
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.get_creditors()
    #receipt
    def receipt2(self):                                     
        self.top1=Toplevel()
        self.top1.title("SAMARIA MILK GROUP")
        self.top1.iconbitmap("logo1.ico")
        my_frame1=Frame(self.top1, width=50)
        my_frame1.pack(anchor="w")
        self.receipt_label=customtkinter.CTkLabel(my_frame1, text="RECEIPT",fg_color="purple",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=200,height=35)
        self.receipt_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.my_receipt=ScrolledText(my_frame1, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff')
        self.my_receipt.grid(row=1, sticky="W")
        #define headings
        title="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        heading0="PAYMENT RECEIPT"
        heading1="Feeds Name"
        heading2="Quantity"
        heading3="Total"
        heading4="DATE:"
        heading5="Total Amount:"
        heading6="Served By:"
        #first delete the text contents
        self.my_receipt.delete('1.0', 'end')
        #add contents to our scrolled widget
        self.my_receipt.insert('end', "\n" + title +"\n")
        self.my_receipt.insert('end', "\n" + sub +"\n")
        self.my_receipt.insert('end', "\n" + heading0 +"\n")
        self.my_receipt.insert('end', "\n" + heading4 + f'{self.today} {self.Time}'+"\n")
        self.my_receipt.insert('end', "\n" + f'Creditor Name: {self.creditor_name_entry.get()}'+"\n")
        self.my_receipt.insert('end', "\n" + heading1+"\t"+"\t"+ heading2 +"\t" +"\t"+ heading3 +"\n")
        #query
        total_amount=0.0
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM LOCAL_CREDITORS WHERE Creditors_Name=?",(self.creditor_name_entry.get(),))
        results=c.fetchall()
        conn.commit()
        conn.close()
        for record in results:
            self.my_receipt.insert('end', "\n" + str(record[2]) +"\t"+"\t"+str(record[3])+"\t"+f' KShs {record[4]}'+"\n")
            total_amount+=float(record[3])
        self.my_receipt.insert('end', "\n" + heading5 +"\t"+"\t"+ f' KShs {total_amount}'+"\n")
        self.my_receipt.insert('end', "\n" + heading6+ "\t"+ f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame1, text="PRINT", command=self.print_receipt,fg_color="red",text_color="white", text_font=("Consollas 10",-20, "bold"),width=200,height=40)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)
    #loading functions
    def load_customer_records_window(self):
        root.quit()
        self.top0.destroy()
        records=Customer_Records(root)
        root.mainloop()
    def load_customer_sales_window(self):
        root.quit()
        self.top0.destroy()
        sales=Customer_Sales(root)
        root.mainloop()
    def load_customer_feeds_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Feeds(root)
        root.mainloop()
    def load_customer_payments_window(self):
        root.quit()
        self.top0.destroy()
        feeds=Customer_Payments(root)
        root.mainloop()  
    def load_local_sales_window(self):
        root.quit()
        self.top0.destroy()
        l_sales=Local_Sales(root)
        root.mainloop()    
    def load_loan_window(self):
        root.quit()
        self.top0.destroy()
        w_loan=Loans(root)
        root.mainloop()
    def load_local_feeds_window(self):
        root.quit()
        self.top0.destroy()
        l_feeds=Local_Feeds(root)
        root.mainloop()       
app=Login(root)
root.mainloop()
