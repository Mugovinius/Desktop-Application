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
        home=Local_Feeds(root)
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
        accounts_menu= Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Accounts", menu=accounts_menu)
        accounts_menu.add_command(label="New User", command=self.sign_up)
        accounts_menu.add_separator()
        accounts_menu.add_command(label="Change Password",command=self.change_password)
        accounts_menu.add_separator()
        accounts_menu.add_command(label="Remove User",command=self.remove_user)
        
        intake_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Intake",menu=intake_menu)
        intake_menu.add_command(label="New Stock", command=self.select_intake_type)

        report_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Report",menu=report_menu)
        report_menu.add_command(label="Daily Report", command=self.daily_report)
        report_menu.add_separator()
        report_menu.add_command(label="Monthly Report", command=self.monthly_report)
        
        creditors_menu=Menu(my_menu,tearoff=0)
        my_menu.add_cascade(label="Creditors",menu=creditors_menu)
        creditors_menu.add_command(label="Pending Credits",command=self.pending_credits)

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
        c.execute("DROP TABLE Local_Sales")
        c.execute("DROP TABLE LOCAL_CREDITORS")
        print("table dropped succesfully")
        '''
        c.execute(""" CREATE TABLE IF NOT EXISTS Local_Sales(
                    Item_Name TEXT NOT NULL,
                    Item_Quantity REAL NOT NULL,
                    Item_Type TEXT NOT NULL,
                    Price REAL NOT NULL,
                    DATE INT NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS LOCAL_CREDITORS(
                    Creditors_Name TEXT NOT NULL,
                    Phone_Number INT NOT NULL,
                    Item_Name TEXT NOT NULL,
                    Item_Quantity REAL NOT NULL,
                    Item_Type TEXT NOT NULL,
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
        feeds_title=" CASH SALES"
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
        self.choose_type_button=customtkinter.CTkButton(self.left_frame, text="Choose",fg_color="purple", text_color="white", text_font=("Consollas 10", -20, "bold"),width=150,height=25,command=self.select_output_type)
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
        feeds_inventory_title="STORE INVENTORY"
        self.feeds_inventory_label=customtkinter.CTkLabel(self.right_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
        self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
        #create another treeview
        self.tree_frame2=Frame(self.right_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
        self.tree_frame2.grid(row=1, column=0, padx=30, pady=10, columnspan=10)
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
        self.tree_scroll2=Scrollbar(self.tree_frame2)
        self.tree_scroll2.pack(side=RIGHT, fill=Y)
        #create a treeview
        self.my_tree2=ttk.Treeview(self.tree_frame2, yscrollcommand=self.tree_scroll2.set,height=15)
        self.my_tree2.pack()
        #configure our scrollbar
        self.tree_scroll2.config(command=self.my_tree2.yview)
        #define our columns
        self.my_tree2['columns']=("FEEDS NAME", "QUANTITY", "PRICE")
        #format our columns
        self.my_tree2.column("#0", width=0, stretch=NO)
        self.my_tree2.column("FEEDS NAME", anchor="w", width=270)
        self.my_tree2.column("QUANTITY", anchor="w", width=200)
        self.my_tree2.column("PRICE", anchor="w", width=200)
        #create headings
        self.my_tree2.heading("#0", text="")
        self.my_tree2.heading("FEEDS NAME", text="FEEDS NAME", anchor="w")
        self.my_tree2.heading("QUANTITY", text="QUANTITY", anchor="w")
        self.my_tree2.heading("PRICE", text="PRICE", anchor="w")
        #create striped row tags
        self.my_tree2.tag_configure('oddrow', background="white")
        self.my_tree2.tag_configure('evenrow', background="violet")
        
        self.query_database()
        #create feeds inventory table
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        '''
        c.execute("DROP TABLE Store_Inventory")
        c.execute("DROP TABLE Store_Records")
        print("Table dropped")
        '''
        c.execute("""CREATE TABLE IF NOT EXISTS Store_Inventory(
                    Item_Name TEXT PRIMARY KEY NOT NULL,
                    Quantity INT NOT NULL,
                    Item_Type TEXT NOT NULL,
                    Price REAL NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL,
                    DATE INT NOT NULL
                    )""")
        c.execute("""CREATE TABLE IF NOT EXISTS Store_Records(
                    Item_Name TEXT PRIMARY KEY NOT NULL,
                    Item_Quantity INT NOT NULL,
                    Month INT NOT NULL,
                    Year INT NOT NULL
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
    #signup
    def add_user(self):
        if self.pass_word_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("ERROR","Password Does Not Match",parent=self.top)
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
                self.ok_button=customtkinter.CTkButton(top_frame, text="VERIFY",fg_color="maroon", text_color="white", text_font=("Consollas 10", -20,"bold"),width=200, height=50,command=self.verify_admin2)
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
    def verify_admin2(self):
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
            messagebox.showinfo("Congratulations", "New User Succesfully Added",parent=self.top0)
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
    #select intake type
    def select_intake_type(self):
        #variable
        self.type=StringVar()
        #
        self.top60=Toplevel()
        self.top60.title("SAMARIA MILK GROUP")
        self.top60.iconbitmap("logo1.ico")
        top_frame=Frame(self.top60)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT TYPE:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        mode_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.type,command=self.choose_intake_type,values=["Animal Feeds","Fertilizers","Herbicides","Seeds","Farm Tools"],width=160,height=25,fg_color="red",text_color="white")
        mode_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def select_output_type(self):
        #variable
        self.output=StringVar()
        #
        self.top61=Toplevel()
        self.top61.title("SAMARIA MILK GROUP")
        self.top61.iconbitmap("logo1.ico")
        top_frame=Frame(self.top61)
        top_frame.pack(anchor="w")
        select_label=customtkinter.CTkLabel(top_frame,text="SELECT TYPE:",fg_color="brown",text_color="white",text_font=("Consollas 10",15,"bold"),width=200,height=40)
        select_label.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
        output_option_menu=customtkinter.CTkOptionMenu(top_frame,variable=self.output,command=self.choose_output_type,values=["Animal Feeds","Fertilizers","Herbicides","Seeds","Farm Tools"],width=160,height=25,fg_color="red",text_color="white")
        output_option_menu.grid(row=0,column=2,columnspan=2,padx=20,pady=20)
    def feeds_intake(self):
        try:
            self.top55.destroy()
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="ANIMAL FEEDS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="ANIMAL FEEDS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1.column("FEEDS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("FEEDS NAME", text="FEEDS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_feeds)

            self.query_feeds_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE FEEDS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.feeds_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.feeds_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.feeds_increase_name_entry.grid(row=3, column=3)
            self.feeds_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.feeds_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.feeds_increase_quantity_entry.grid(row=4, column=3)
            self.increase_feeds_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_feeds_stock)
            self.increase_feeds_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE FEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.feeds_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.feeds_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.feeds_remove_name_entry.grid(row=7, column=3)
            self.remove_feeds_button=customtkinter.CTkButton(self.right_frame, text="REMOVE FEEDS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_feeds)
            self.remove_feeds_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW FEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.feeds_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.feeds_new_name_entry.grid(row=3, column=2)
            self.feeds_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_new_quantity_entry.grid(row=4, column=2)
            self.feeds_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_new_price_entry.grid(row=5, column=2)
            self.add_feeds_button=customtkinter.CTkButton(self.left_frame, text="ADD FEEDS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_feeds)
            self.add_feeds_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE FEEDS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.feeds_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.feeds_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.feeds_update_price_name_entry.grid(row=3, column=8)
            self.feeds_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.feeds_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_update_price_entry.grid(row=4, column=8)
            self.update_feeds_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_feeds_price)
            self.update_feeds_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
        except AttributeError:
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="ANIMAL FEEDS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="ANIMAL FEEDS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1.column("FEEDS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("FEEDS NAME", text="FEEDS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_feeds)

            self.query_feeds_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE FEEDS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.feeds_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.feeds_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.feeds_increase_name_entry.grid(row=3, column=3)
            self.feeds_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.feeds_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.feeds_increase_quantity_entry.grid(row=4, column=3)
            self.increase_feeds_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_feeds_stock)
            self.increase_feeds_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE FEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.feeds_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.feeds_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.feeds_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.feeds_remove_name_entry.grid(row=7, column=3)
            self.remove_feeds_button=customtkinter.CTkButton(self.right_frame, text="REMOVE FEEDS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_feeds)
            self.remove_feeds_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW FEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.feeds_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.feeds_new_name_entry.grid(row=3, column=2)
            self.feeds_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_new_quantity_entry.grid(row=4, column=2)
            self.feeds_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.feeds_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_new_price_entry.grid(row=5, column=2)
            self.add_feeds_button=customtkinter.CTkButton(self.left_frame, text="ADD FEEDS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_feeds)
            self.add_feeds_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE FEEDS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.feeds_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Feeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.feeds_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.feeds_update_price_name_entry.grid(row=3, column=8)
            self.feeds_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.feeds_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.feeds_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.feeds_update_price_entry.grid(row=4, column=8)
            self.update_feeds_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_feeds_price)
            self.update_feeds_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
    def fertilizer_intake(self):
        try:
            self.top55.destroy()
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)

            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="FERTILIZERS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="FERTILIZERS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("FERTILIZER NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("FERTILIZER NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("FERTILIZER NAME", text="FERTILIZER NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_fertilizer)

            self.query_fertilizer_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE FERTILIZER STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.fertilizer_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.fertilizer_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.fertilizer_increase_name_entry.grid(row=3, column=3)
            self.fertilizer_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.fertilizer_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.fertilizer_increase_quantity_entry.grid(row=4, column=3)
            self.increase_fertilizer_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_fertilizer_stock)
            self.increase_fertilizer_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE FERTILIZER", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.fertilizer_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.fertilizer_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.fertilizer_remove_name_entry.grid(row=7, column=3)
            self.remove_fertilizer_button=customtkinter.CTkButton(self.right_frame, text="REMOVE FERTILIZER",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_fertilizer)
            self.remove_fertilizer_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW FERTILIZER", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.fertilizer_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.fertilizer_new_name_entry.grid(row=3, column=2)
            self.fertilizer_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_new_quantity_entry.grid(row=4, column=2)
            self.fertilizer_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_new_price_entry.grid(row=5, column=2)
            self.add_fertilizer_button=customtkinter.CTkButton(self.left_frame, text="ADD FERTILIZER", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_fertilizers)
            self.add_fertilizer_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE FERTILIZER PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.fertilizer_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.fertilizer_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.fertilizer_update_price_name_entry.grid(row=3, column=8)
            self.fertilizer_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.fertilizer_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_update_price_entry.grid(row=4, column=8)
            self.update_fertilizer_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_fertilizer_price)
            self.update_fertilizer_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
        except AttributeError:
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)

            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="FERTILIZERS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="FERTILIZERS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("FERTILIZER NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("FERTILIZER NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("FERTILIZER NAME", text="FERTILIZER NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_fertilizer)

            self.query_fertilizer_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE FERTILIZER STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.fertilizer_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.fertilizer_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.fertilizer_increase_name_entry.grid(row=3, column=3)
            self.fertilizer_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.fertilizer_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.fertilizer_increase_quantity_entry.grid(row=4, column=3)
            self.increase_fertilizer_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_fertilizer_stock)
            self.increase_fertilizer_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE FERTILIZER", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.fertilizer_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.fertilizer_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.fertilizer_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.fertilizer_remove_name_entry.grid(row=7, column=3)
            self.remove_fertilizer_button=customtkinter.CTkButton(self.right_frame, text="REMOVE FERTILIZER",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_fertilizer)
            self.remove_fertilizer_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW FERTILIZER", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.fertilizer_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.fertilizer_new_name_entry.grid(row=3, column=2)
            self.fertilizer_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_new_quantity_entry.grid(row=4, column=2)
            self.fertilizer_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.fertilizer_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_new_price_entry.grid(row=5, column=2)
            self.add_fertilizer_button=customtkinter.CTkButton(self.left_frame, text="ADD FERTILIZER", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_fertilizers)
            self.add_fertilizer_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5,sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE FERTILIZER PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.fertilizer_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Fertilizer Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.fertilizer_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.fertilizer_update_price_name_entry.grid(row=3, column=8)
            self.fertilizer_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.fertilizer_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.fertilizer_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.fertilizer_update_price_entry.grid(row=4, column=8)
            self.update_fertilizer_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_fertilizer_price)
            self.update_fertilizer_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
    def herbicides_intake(self):
        try:
            self.top55.destroy()
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="HERBICIDES"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="HERBICIDES INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("HERBICIDES NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("HERBICIDES NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("HERBICIDES NAME", text="HERBICIDES NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_herbicides)

            self.query_herbicides_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE HERBICIDES STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.herbicides_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.herbicides_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.herbicides_increase_name_entry.grid(row=3, column=3)
            self.herbicides_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.herbicides_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.herbicides_increase_quantity_entry.grid(row=4, column=3)
            self.increase_herbicides_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_herbicides_stock)
            self.increase_herbicides_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE HERBICIDES", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.herbicides_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.herbicides_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.herbicides_remove_name_entry.grid(row=7, column=3)
            self.remove_herbicides_button=customtkinter.CTkButton(self.right_frame, text="REMOVE HERBICIDES",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_herbicides)
            self.remove_herbicides_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW HERBICIDES", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.herbicides_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.herbicides_new_name_entry.grid(row=3, column=2)
            self.herbicides_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_new_quantity_entry.grid(row=4, column=2)
            self.herbicides_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_new_price_entry.grid(row=5, column=2)
            self.add_herbicides_button=customtkinter.CTkButton(self.left_frame, text="ADD HERBICIDES", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_herbicides)
            self.add_herbicides_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE HERBICIDES PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.herbicides_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.herbicides_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.herbicides_update_price_name_entry.grid(row=3, column=8)
            self.herbicides_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.herbicides_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_update_price_entry.grid(row=4, column=8)
            self.update_herbicides_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_herbicides_price)
            self.update_herbicides_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
        except AttributeError:
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="HERBICIDES"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="HERBICIDES INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("HERBICIDES NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("HERBICIDES NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("HERBICIDES NAME", text="HERBICIDES NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_herbicides)

            self.query_herbicides_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE HERBICIDES STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.herbicides_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.herbicides_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.herbicides_increase_name_entry.grid(row=3, column=3)
            self.herbicides_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.herbicides_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.herbicides_increase_quantity_entry.grid(row=4, column=3)
            self.increase_herbicides_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_herbicides_stock)
            self.increase_herbicides_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE HERBICIDES", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.herbicides_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.herbicides_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.herbicides_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.herbicides_remove_name_entry.grid(row=7, column=3)
            self.remove_herbicides_button=customtkinter.CTkButton(self.right_frame, text="REMOVE HERBICIDES",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_herbicides)
            self.remove_herbicides_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW HERBICIDES", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.herbicides_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.herbicides_new_name_entry.grid(row=3, column=2)
            self.herbicides_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_new_quantity_entry.grid(row=4, column=2)
            self.herbicides_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.herbicides_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_new_price_entry.grid(row=5, column=2)
            self.add_herbicides_button=customtkinter.CTkButton(self.left_frame, text="ADD HERBICIDES", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_herbicides)
            self.add_herbicides_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE HERBICIDES PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.herbicides_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Herbicides Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.herbicides_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.herbicides_update_price_name_entry.grid(row=3, column=8)
            self.herbicides_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.herbicides_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.herbicides_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.herbicides_update_price_entry.grid(row=4, column=8)
            self.update_herbicides_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_herbicides_price)
            self.update_herbicides_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
    def seeds_intake(self):
        try:
            self.top55.destroy()
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="SEEDS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="SEEDS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("SEEDS NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("SEEDS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("SEEDS NAME", text="SEEDS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_seeds)

            self.query_seeds_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE SEEDS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.seeds_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.seeds_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.seeds_increase_name_entry.grid(row=3, column=3)
            self.seeds_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.seeds_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.seeds_increase_quantity_entry.grid(row=4, column=3)
            self.increase_seeds_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_seeds_stock)
            self.increase_seeds_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE SEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.seeds_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.seeds_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.seeds_remove_name_entry.grid(row=7, column=3)
            self.remove_seeds_button=customtkinter.CTkButton(self.right_frame, text="REMOVE SEEDS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_seeds)
            self.remove_seeds_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW SEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.seeds_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.seeds_new_name_entry.grid(row=3, column=2)
            self.seeds_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_new_quantity_entry.grid(row=4, column=2)
            self.seeds_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_new_price_entry.grid(row=5, column=2)
            self.add_seeds_button=customtkinter.CTkButton(self.left_frame, text="ADD SEEDS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_seeds)
            self.add_seeds_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE SEEDS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.seeds_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.seeds_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.seeds_update_price_name_entry.grid(row=3, column=8)
            self.seeds_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.seeds_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_update_price_entry.grid(row=4, column=8)
            self.update_seeds_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_seeds_price)
            self.update_seeds_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
        except AttributeError:
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="SEEDS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="SEEDS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("SEEDS NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("SEEDS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("SEEDS NAME", text="SEEDS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_seeds)

            self.query_seeds_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE SEEDS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.seeds_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.seeds_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.seeds_increase_name_entry.grid(row=3, column=3)
            self.seeds_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.seeds_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.seeds_increase_quantity_entry.grid(row=4, column=3)
            self.increase_seeds_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_seeds_stock)
            self.increase_seeds_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE SEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.seeds_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.seeds_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.seeds_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.seeds_remove_name_entry.grid(row=7, column=3)
            self.remove_seeds_button=customtkinter.CTkButton(self.right_frame, text="REMOVE SEEDS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_seeds)
            self.remove_seeds_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW SEEDS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.seeds_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.seeds_new_name_entry.grid(row=3, column=2)
            self.seeds_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_new_quantity_entry.grid(row=4, column=2)
            self.seeds_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.seeds_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_new_price_entry.grid(row=5, column=2)
            self.add_seeds_button=customtkinter.CTkButton(self.left_frame, text="ADD SEEDS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_seeds)
            self.add_seeds_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE SEEDS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.seeds_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Seeds Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.seeds_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.seeds_update_price_name_entry.grid(row=3, column=8)
            self.seeds_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.seeds_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.seeds_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.seeds_update_price_entry.grid(row=4, column=8)
            self.update_seeds_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_seeds_price)
            self.update_seeds_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
    def tools_intake(self):
        try:
            self.top55.destroy()
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="FARM TOOLS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="TOOLS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("TOOLS NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("TOOLS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("TOOLS NAME", text="TOOLS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_tools)

            self.query_tools_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE TOOLS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.tools_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.tools_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.tools_increase_name_entry.grid(row=3, column=3)
            self.tools_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.tools_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.tools_increase_quantity_entry.grid(row=4, column=3)
            self.increase_tools_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_tools_stock)
            self.increase_tools_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE TOOLS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.tools_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.tools_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.tools_remove_name_entry.grid(row=7, column=3)
            self.remove_tools_button=customtkinter.CTkButton(self.right_frame, text="REMOVE TOOLS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_tools)
            self.remove_tools_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW TOOLS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.tools_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.tools_new_name_entry.grid(row=3, column=2)
            self.tools_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_new_quantity_entry.grid(row=4, column=2)
            self.tools_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_new_price_entry.grid(row=5, column=2)
            self.add_tools_button=customtkinter.CTkButton(self.left_frame, text="ADD TOOLS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_tools)
            self.add_tools_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE TOOLS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.tools_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.tools_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.tools_update_price_name_entry.grid(row=3, column=8)
            self.tools_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.tools_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_update_price_entry.grid(row=4, column=8)
            self.update_tools_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_tools_price)
            self.update_tools_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)
        except AttributeError:
            self.top60.destroy()
            #
            self.top55=Toplevel()
            self.top55.title("SAMARIA MILK GROUP")
            self.top55.iconbitmap("logo1.ico")
            self.top55.state('zoomed')
            #menu
            my_other_menu = Menu(self.top55)
            self.top55.config(menu=my_other_menu)
            #create menu item
            feeds_menu= Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Feeds", menu=feeds_menu)
            feeds_menu.add_command(label="Feeds Intake", command=self.feeds_intake)
            
            fertilizer_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Fertilizer",menu=fertilizer_menu)
            fertilizer_menu.add_command(label="Fertilizer Intake",command=self.fertilizer_intake)

            herbicides_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Herbicides",menu=herbicides_menu)
            herbicides_menu.add_command(label="Herbicides Intake",command=self.herbicides_intake)
            
            seeds_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Seeds",menu=seeds_menu)
            seeds_menu.add_command(label="Seeds Intake",command=self.seeds_intake)

            tools_menu=Menu(my_other_menu,tearoff=0)
            my_other_menu.add_cascade(label="Tools", menu=tools_menu)
            tools_menu.add_command(label="Tools Intake",command=self.tools_intake)
            
            self.title_frame=Frame(self.top55)
            self.title_frame.pack(anchor="center")
            title ="SAMARIA MILK GROUP"
            sub="Quality Milk, Healthy Life"
            sub0="FARM TOOLS"
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
            self.left_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.left_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            #title
            feeds_inventory_title="TOOLS INVENTORY"
            self.feeds_inventory_label=customtkinter.CTkLabel(self.left_frame, text=feeds_inventory_title, fg_color="orange",text_color="white", text_font=("Consollas 10", -20, "underline","bold"),width=200,height=25)
            self.feeds_inventory_label.grid(row=0, column=0, columnspan=12,pady=5)
            #create another treeview
            self.tree_frame1=Frame(self.left_frame, highlightbackground="green", highlightthickness=5,width=500, height=300, bd=0)
            self.tree_frame1.grid(row=1, column=0, padx=30,columnspan=12)
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
            self.my_tree1['columns']=("TOOLS NAME", "QUANTITY", "PRICE")
            #format our columns
            self.my_tree1.column("#0", width=0, stretch=NO)
            self.my_tree1.column("TOOLS NAME", anchor="w", width=350)
            self.my_tree1.column("QUANTITY", anchor="center", width=250)
            self.my_tree1.column("PRICE", anchor="center", width=250)
            #create headings
            self.my_tree1.heading("#0", text="")
            self.my_tree1.heading("TOOLS NAME", text="TOOLS NAME", anchor="center")
            self.my_tree1.heading("QUANTITY", text="QUANTITY", anchor="center")
            self.my_tree1.heading("PRICE", text="PRICE", anchor="center")
            #create striped row tags
            self.my_tree1.tag_configure('oddrow', background="white")
            self.my_tree1.tag_configure('evenrow', background="violet")
            #single click binding
            self.my_tree1.bind("<ButtonRelease-1>", self.clicker_tools)

            self.query_tools_database()
            #frame
            self.right_frame=customtkinter.CTkFrame(self.top55,corner_radius=8,width=900,height=650)
            self.right_frame.pack(side=LEFT,fill=BOTH,expand=YES)
            self.title_increase_label=customtkinter.CTkLabel(self.right_frame, text="INCREASE TOOLS STOCK", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_increase_label.grid(row=0, column=0,columnspan=6,padx=20, pady=10)
            self.tools_increase_name_label=customtkinter.CTkLabel(self.right_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_increase_name_label.grid(row=3, column=0,columnspan=3, padx=20, pady=12)
            self.tools_increase_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.tools_increase_name_entry.grid(row=3, column=3)
            self.tools_increase_quantity_label=customtkinter.CTkLabel(self.right_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_increase_quantity_label.grid(row=4, column=0,columnspan=3, padx=20, pady=12)
            self.tools_increase_quantity_entry=customtkinter.CTkEntry(self.right_frame,width=150,height=25,border_color="blue")
            self.tools_increase_quantity_entry.grid(row=4, column=3)
            self.increase_tools_button=customtkinter.CTkButton(self.right_frame, text="INCREASE STOCK",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.increase_tools_stock)
            self.increase_tools_button.grid(row=5, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #
            self.title_remove_label=customtkinter.CTkLabel(self.right_frame, text="REMOVE TOOLS", fg_color="orange",text_color="white", text_font=("Consollas 10", -22,"bold","underline"),width=200,height=30)
            self.title_remove_label.grid(row=6, column=0,columnspan=6,padx=20, pady=20)
            self.tools_remove_name_label=customtkinter.CTkLabel(self.right_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -17,"bold"),width=150,height=30)
            self.tools_remove_name_label.grid(row=7, column=0,columnspan=3, padx=10, pady=20)
            self.tools_remove_name_entry=customtkinter.CTkEntry(self.right_frame,width=180,height=25,border_color="blue")
            self.tools_remove_name_entry.grid(row=7, column=3)
            self.remove_tools_button=customtkinter.CTkButton(self.right_frame, text="REMOVE TOOLS",fg_color="red",text_color="white", text_font=("Consollas 10", -25,"bold"),width=170,height=30, command=self.remove_tools)
            self.remove_tools_button.grid(row=8, column=0,columnspan=4,padx=10, pady=20,sticky=EW)
            #labels
            self.title_label=customtkinter.CTkLabel(self.left_frame, text="ADD NEW TOOLS", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_label.grid(row=2, column=0,columnspan=4,padx=10, pady=3)
            self.tools_new_name_label=customtkinter.CTkLabel(self.left_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_name_label.grid(row=3, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.tools_new_name_entry.grid(row=3, column=2)
            self.tools_new_quantity_label=customtkinter.CTkLabel(self.left_frame, text="Quantity:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_quantity_label.grid(row=4, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_quantity_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_new_quantity_entry.grid(row=4, column=2)
            self.tools_new_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_new_price_label.grid(row=5, column=0,columnspan=2, padx=10, pady=3)
            self.tools_new_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_new_price_entry.grid(row=5, column=2)
            self.add_tools_button=customtkinter.CTkButton(self.left_frame, text="ADD TOOLS", fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30,command=self.add_tools)
            self.add_tools_button.grid(row=6, column=0,columnspan=4,padx=20,pady=5, sticky=EW)
            #labels
            self.title_update_price_label=customtkinter.CTkLabel(self.left_frame, text="UPDATE TOOLS PRICE", fg_color="orange",text_color="white", text_font=("Consollas 10", -20,"bold","underline"),width=200,height=25)
            self.title_update_price_label.grid(row=2, column=4,columnspan=8,padx=10, pady=10)
            self.tools_update_price_name_label=customtkinter.CTkLabel(self.left_frame, text="Tools Name:", fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_update_price_name_label.grid(row=3, column=4,columnspan=4, padx=10, pady=10)
            self.tools_update_price_name_entry=customtkinter.CTkEntry(self.left_frame,width=180,height=25,border_color="blue")
            self.tools_update_price_name_entry.grid(row=3, column=8)
            self.tools_update_price_label=customtkinter.CTkLabel(self.left_frame, text="Price:",fg_color="brown",text_color="white", text_font=("Consollas 10", -15,"bold"),width=150,height=25)
            self.tools_update_price_label.grid(row=4, column=4,columnspan=4, padx=10, pady=10)
            self.tools_update_price_entry=customtkinter.CTkEntry(self.left_frame,width=150,height=25,border_color="blue")
            self.tools_update_price_entry.grid(row=4, column=8)
            self.update_tools_button=customtkinter.CTkButton(self.left_frame, text="UPDATE PRICE",fg_color="purple",text_color="white", text_font=("Consollas 10", -17,"bold"),width=170,height=30, command=self.update_tools_price)
            self.update_tools_button.grid(row=5, column=4,columnspan=8,sticky=EW,padx=20, pady=10)

    # intake type
    def choose_intake_type(self,e):
        if self.type.get()=="Animal Feeds":
            self.feeds_intake()
        if self.type.get()=="Fertilizers":
            self.fertilizer_intake()
        if self.type.get()=="Herbicides":
            self.herbicides_intake()
        if self.type.get()=="Seeds":
            self.seeds_intake()
        if self.type.get()=="Farm Tools":
            self.tools_intake()
    #choose feeds function
    def choose_output_type(self,e):
        if self.output.get()=="Animal Feeds":
            self.top61.destroy()
            #
            self.top97=Toplevel()
            self.top97.title("SAMARIA MILK GROUP")
            self.top97.iconbitmap("logo1.ico")
            #connect to database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Item_Name FROM Store_Inventory WHERE Item_Type='Animal Feeds'")
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
                            c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(number[0],))
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
                for record in self.data:
                    if record[1]==True:
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                        pesa=c.fetchone()
                        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(record[0],))
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
        if self.output.get()=="Fertilizers":
            self.top61.destroy()
            #
            self.top97=Toplevel()
            self.top97.title("SAMARIA MILK GROUP")
            self.top97.iconbitmap("logo1.ico")
            #connect to database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Item_Name FROM Store_Inventory WHERE Item_Type='Fertilizers'")
            self.feeds_names=c.fetchall()
            self.data=[[numbers]for numbers in self.feeds_names]
            #print(self.data)
            conn.commit()
            conn.close()
            self.my_frame=Frame(self.top97)
            self.my_frame.pack(padx=20,pady=20,anchor="w")
            self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE FERTILIZERS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
            self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
            self.my_sheet=Sheet(self.my_frame,
                                align = "w",
                                header_font=("Consollas 10",15,"bold"),
                                font=("Consollas 10",13,"normal"),
                                data=self.data,
                                headers= ["Fertilizer Name","Checkbox","Fertilizer Quantity"],
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
                            c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(number[0],))
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
            self.my_sheet.column_width(column=2,width=180)
            def grant_feeds():
                for record in self.data:
                    if record[1]==True:
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                        pesa=c.fetchone()
                        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(record[0],))
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
            self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT FERTILIZER",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
            self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
        if self.output.get()=="Herbicides":
            self.top61.destroy()
            #
            self.top97=Toplevel()
            self.top97.title("SAMARIA MILK GROUP")
            self.top97.iconbitmap("logo1.ico")
            #connect to database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Item_Name FROM Store_Inventory WHERE Item_Type='Herbicides'")
            self.feeds_names=c.fetchall()
            self.data=[[numbers]for numbers in self.feeds_names]
            #print(self.data)
            conn.commit()
            conn.close()
            self.my_frame=Frame(self.top97)
            self.my_frame.pack(padx=20,pady=20,anchor="w")
            self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE HERBICIDES",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
            self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
            self.my_sheet=Sheet(self.my_frame,
                                align = "w",
                                header_font=("Consollas 10",15,"bold"),
                                font=("Consollas 10",13,"normal"),
                                data=self.data,
                                headers= ["Herbicides Name","Checkbox","Herbicides Quantity"],
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
                        if number[2]=="Packets":
                            number[2]=event.text
                            conn=sqlite3.connect('samaria feeds database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(number[0],))
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
            self.my_sheet.create_dropdown(r="all",c=2,values=["Packets"]+[f"{i}" for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)],selection_function=get_quantity)
            self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
            self.my_sheet.get_checkboxes()
            self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
            self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
            self.my_sheet.default_header_height(height="2")
            self.my_sheet.column_width(column=0,width=300)
            self.my_sheet.column_width(column=2,width=180)
            def grant_feeds():
                for record in self.data:
                    if record[1]==True:
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                        pesa=c.fetchone()
                        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(record[0],))
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
            self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT HERBICIDES",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
            self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
        if self.output.get()=="Seeds":
            self.top61.destroy()
            #
            self.top97=Toplevel()
            self.top97.title("SAMARIA MILK GROUP")
            self.top97.iconbitmap("logo1.ico")
            #connect to database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Item_Name FROM Store_Inventory WHERE Item_Type='Seeds'")
            self.feeds_names=c.fetchall()
            self.data=[[numbers]for numbers in self.feeds_names]
            #print(self.data)
            conn.commit()
            conn.close()
            self.my_frame=Frame(self.top97)
            self.my_frame.pack(padx=20,pady=20,anchor="w")
            self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE SEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
            self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
            self.my_sheet=Sheet(self.my_frame,
                                align = "w",
                                header_font=("Consollas 10",15,"bold"),
                                font=("Consollas 10",13,"normal"),
                                data=self.data,
                                headers= ["Seeds Name","Checkbox","Seeds Quantity"],
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
                        if number[2]=="Packets":
                            number[2]=event.text
                            conn=sqlite3.connect('samaria feeds database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(number[0],))
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
            self.my_sheet.create_dropdown(r="all",c=2,values=["Packets"]+[f"{i}" for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)],selection_function=get_quantity)
            self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
            self.my_sheet.get_checkboxes()
            self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
            self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
            self.my_sheet.default_header_height(height="2")
            self.my_sheet.column_width(column=0,width=300)
            self.my_sheet.column_width(column=2,width=180)
            def grant_feeds():
                for record in self.data:
                    if record[1]==True:
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                        pesa=c.fetchone()
                        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(record[0],))
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
            self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT SEEDS",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
            self.confirm_button.grid(row=4,column=0,columnspan=4,ipadx=50,pady=10,padx=20)
        if self.output.get()=="Farm Tools":
            self.top61.destroy()
            #
            self.top97=Toplevel()
            self.top97.title("SAMARIA MILK GROUP")
            self.top97.iconbitmap("logo1.ico")
            #connect to database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Item_Name FROM Store_Inventory WHERE Item_Type='Farm Tools'")
            self.feeds_names=c.fetchall()
            self.data=[[numbers]for numbers in self.feeds_names]
            #print(self.data)
            conn.commit()
            conn.close()
            self.my_frame=Frame(self.top97)
            self.my_frame.pack(padx=20,pady=20,anchor="w")
            self.title_label=customtkinter.CTkLabel(self.my_frame,text="CHOOSE TOOLS",fg_color="purple",text_color="white",text_font=("Consollas 10",-30,"bold"),width=250,height=35)
            self.title_label.grid(row=0,column=0,columnspan=4,padx=20,pady=10)
            self.my_sheet=Sheet(self.my_frame,
                                align = "w",
                                header_font=("Consollas 10",15,"bold"),
                                font=("Consollas 10",13,"normal"),
                                data=self.data,
                                headers= ["Tools Name","Checkbox","Tools Quantity"],
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
                        if number[2]=="Pieces":
                            number[2]=event.text
                            conn=sqlite3.connect('samaria feeds database.db')
                            conn.row_factory=lambda cursor, row:row[0]
                            c=conn.cursor()
                            c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(number[0],))
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
            self.my_sheet.create_dropdown(r="all",c=2,values=["Pieces"]+[f"{i}" for i in(1/4,1/2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)],selection_function=get_quantity)
            self.my_sheet.create_checkbox(r="all",c=1,text="Choose",check_function=get_info)
            self.my_sheet.get_checkboxes()
            self.my_sheet.highlight_cells("all",1,bg="white",fg="purple")
            self.my_sheet.highlight_cells("all",2,bg="white",fg="blue")
            self.my_sheet.default_header_height(height="2")
            self.my_sheet.column_width(column=0,width=300)
            self.my_sheet.column_width(column=2,width=180)
            def grant_feeds():
                for record in self.data:
                    if record[1]==True:
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                        pesa=c.fetchone()
                        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(record[0],))
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
            self.confirm_button=customtkinter.CTkButton(self.my_frame,text="GRANT TOOLS",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=40,command=grant_feeds)
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
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Item_Type FROM Store_Inventory WHERE Item_Name=?",(data,))
                        each_type=c.fetchone()
                        conn.commit()
                        conn.close()
                        #update feeds_inventory table
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(data,))
                        initial_quantity=c.fetchone()
                        current_quantity=(initial_quantity - float(datum))
                        c.execute("SELECT Price From Store_Inventory WHERE Item_Name=?",(data,))
                        cost=c.fetchone()
                        c.execute("SELECT Month From Store_Inventory WHERE Item_Name=?",(data,))
                        monthm=c.fetchone()
                        c.execute("SELECT Year From Store_Inventory WHERE Item_Name=?",(data,))
                        yearm=c.fetchone()
                        c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=?",(data,))
                        datem=c.fetchone()
                        c.execute(""" UPDATE Store_Inventory SET
                                    Item_Name=:f_name,
                                    Quantity=:q_ty,
                                    Item_Type=:i_ty,
                                    Price=:prie,
                                    Month=:moth,
                                    Year =:yoar,
                                    DATE =:siku
                            
                                    WHERE Item_Name=:f_name""",
                                    {
                                        'f_name': data,
                                        'q_ty' : current_quantity,
                                        'i_ty' : each_type,
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
                        c.execute("INSERT INTO LOCAL_CREDITORS VALUES(:Creditors_Name,:Phone_Number,:Item_Name,:Item_Quantity,:Item_Type,:Total,:MONTH,:YEAR,:DATE)",
                                  {
                                      'Creditors_Name':self.creditors_name_entry.get(),
                                      'Phone_Number':self.creditors_p_number_entry.get(),
                                      'Item_Name':data,
                                      'Item_Quantity':datum,
                                      'Item_Type':each_type,
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
                    c.execute("SELECT * FROM Local_Sales")
                    yote=c.fetchall()
                    print(yote)
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
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Item_Type FROM Store_Inventory WHERE Item_Name=?",(data,))
                    each_type=c.fetchone()
                    #insert data
                    c.execute("INSERT INTO Local_Sales VALUES(:Item_Name, :Item_Quantity, :Item_Type, :Price,:DATE,:Month, :Year)",
                            {
                                'Item_Name': data,
                                'Item_Quantity': datum,
                                'Item_Type':each_type,
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
                    c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(data,))
                    initial_quantity=c.fetchone()
                    current_quantity=(initial_quantity - float(datum))
                    c.execute("SELECT Price From Store_Inventory WHERE Item_Name=?",(data,))
                    cost=c.fetchone()
                    c.execute("SELECT Month From Store_Inventory WHERE Item_Name=?",(data,))
                    monthm=c.fetchone()
                    c.execute("SELECT Year From Store_Inventory WHERE Item_Name=?",(data,))
                    yearm=c.fetchone()
                    c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=?",(data,))
                    datem=c.fetchone()
                    c.execute(""" UPDATE Store_Inventory SET
                                Item_Name=:f_name,
                                Quantity=:q_ty,
                                Item_Type=:i_ty,
                                Price=:prie,
                                Month=:moth,
                                Year =:yoar,
                                DATE =:siku
                        
                                WHERE Item_Name=:f_name""",
                                {
                                    'f_name': data,
                                    'q_ty' : current_quantity,
                                    'i_ty' : each_type,
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
        heading0="Credit Sales"
        heading1="Item Name"
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
        heading0="Cash Sale"
        heading1="Item Name"
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
    #create update binding function
    def clicker_feeds(self,e):
        #clear entries
        self.feeds_update_price_name_entry.delete(0,END)
        self.feeds_increase_name_entry.delete(0,END)
        self.feeds_remove_name_entry.delete(0,END)
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.feeds_update_price_name_entry.insert(0, values[0])
        self.feeds_increase_name_entry.insert(0, values[0])
        self.feeds_remove_name_entry.insert(0, values[0])
    def clicker_fertilizer(self,e):
        #clear entries
        self.fertilizer_update_price_name_entry.delete(0,END)
        self.fertilizer_increase_name_entry.delete(0,END)
        self.fertilizer_remove_name_entry.delete(0,END)
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.fertilizer_update_price_name_entry.insert(0, values[0])
        self.fertilizer_increase_name_entry.insert(0, values[0])
        self.fertilizer_remove_name_entry.insert(0, values[0])
    def clicker_herbicides(self,e):
        #clear entries
        self.herbicides_update_price_name_entry.delete(0,END)
        self.herbicides_increase_name_entry.delete(0,END)
        self.herbicides_remove_name_entry.delete(0,END)
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.herbicides_update_price_name_entry.insert(0, values[0])
        self.herbicides_increase_name_entry.insert(0, values[0])
        self.herbicides_remove_name_entry.insert(0, values[0])
    def clicker_seeds(self,e):
        #clear entries
        self.seeds_update_price_name_entry.delete(0,END)
        self.seeds_increase_name_entry.delete(0,END)
        self.seeds_remove_name_entry.delete(0,END)
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.seeds_update_price_name_entry.insert(0, values[0])
        self.seeds_increase_name_entry.insert(0, values[0])
        self.seeds_remove_name_entry.insert(0, values[0])
    def clicker_tools(self,e):
        #clear entries
        self.tools_update_price_name_entry.delete(0,END)
        self.tools_increase_name_entry.delete(0,END)
        self.tools_remove_name_entry.delete(0,END)
        #grab record number
        selected= self.my_tree1.focus()
        #grab record values
        values= self.my_tree1.item(selected, 'values')
        #print(values)
        #output to entry boxes
        self.tools_update_price_name_entry.insert(0, values[0])
        self.tools_increase_name_entry.insert(0, values[0])
        self.tools_remove_name_entry.insert(0, values[0])
    #create query function
    def query_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory")
        all_items=c.fetchall()
        self.my_tree2.delete(* self.my_tree2.get_children())
        for record in all_items:
            if self.count%2==0:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0],record[1], f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree2.insert('', index='end', iid=self.count, text="", values=(record[0],record[1], f' KShs {record[3]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def query_feeds_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory WHERE Item_Type='Animal Feeds'")
        f_eeds=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in f_eeds:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[3]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def query_fertilizer_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory WHERE Item_Type='Fertilizers'")
        f_ertilizer=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in f_ertilizer:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} bags', f' KShs {record[3]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def query_herbicides_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory WHERE Item_Type='Herbicides'")
        h_erbicides=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in h_erbicides:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} packets', f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} packets', f' KShs {record[3]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def query_seeds_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory WHERE Item_Type='Seeds'")
        s_eeds=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in s_eeds:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} sackets', f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} sackets', f' KShs {record[3]}'), tags=("oddrow"),)
            self.count+=1
        conn.commit()
        conn.close()
    def query_tools_database(self):
        conn=sqlite3.connect('samaria feeds database.db')
        c=conn.cursor()
        c.execute("SELECT * FROM Store_Inventory WHERE Item_Type='Farm Tools'")
        f_tools=c.fetchall()
        self.my_tree1.delete(* self.my_tree1.get_children())
        for record in f_tools:
            if self.count%2==0:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} pieces', f' KShs {record[3]}'), tags=("evenrow"),)
            else:
                self.my_tree1.insert('', index='end', iid=self.count, text="", values=(record[0], f'{record[1]} pieces', f' KShs {record[3]}'), tags=("oddrow"),)
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
    def update_feeds_price(self):
        response=messagebox.askyesno("Confirm", "Are you Sure?",parent=self.top55)
        if response ==1:
            #update the database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.feeds_update_price_name_entry.get(),self.type.get(),))
            quantum=c.fetchone()
            c.execute("SELECT Month From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.feeds_update_price_name_entry.get(),self.type.get(),))
            monthmn=c.fetchone()
            c.execute("SELECT Year From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.feeds_update_price_name_entry.get(),self.type.get(),))
            yearmn=c.fetchone()
            c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.feeds_update_price_name_entry.get(),self.type.get(),))
            datemn=c.fetchone()
            c.execute(""" UPDATE Store_Inventory SET
                        Item_Name=:f_name,
                        Quantity=:q_ty,
                        Item_Type=:i_ty,
                        Price=:prie,
                        Month=:moth,
                        Year =:yuar,
                        DATE =:sikuku

                        WHERE Item_Name=:f_name""",
                      {
                          'f_name': self.feeds_update_price_name_entry.get(),
                          'q_ty' : quantum,
                          'i_ty' : self.type.get(),
                          'prie' : self.feeds_update_price_entry.get(),
                          'moth' : monthmn,
                          'yuar' : yearmn,
                          'sikuku' : datemn
                        })
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", f'{self.feeds_update_price_name_entry.get()} Price Updated Succesfully',parent =self.top55)
        #clear entries
        self.feeds_update_price_name_entry.delete(0,END)
        self.feeds_increase_name_entry.delete(0,END)
        self.feeds_remove_name_entry.delete(0,END)
        self.feeds_update_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_feeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def update_fertilizer_price(self):
        response=messagebox.askyesno("Confirm", "Are you Sure?",parent=self.top55)
        if response ==1:
            #update the database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.fertilizer_update_price_name_entry.get(),self.type.get(),))
            quantum=c.fetchone()
            c.execute("SELECT Month From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.fertilizer_update_price_name_entry.get(),self.type.get(),))
            monthmn=c.fetchone()
            c.execute("SELECT Year From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.fertilizer_update_price_name_entry.get(),self.type.get(),))
            yearmn=c.fetchone()
            c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.fertilizer_update_price_name_entry.get(),self.type.get(),))
            datemn=c.fetchone()
            c.execute(""" UPDATE Store_Inventory SET
                        Item_Name=:f_name,
                        Quantity=:q_ty,
                        Item_Type=:i_ty,
                        Price=:prie,
                        Month=:moth,
                        Year =:yuar,
                        DATE =:sikuku

                        WHERE Item_Name=:f_name""",
                      {
                          'f_name': self.fertilizer_update_price_name_entry.get(),
                          'q_ty' : quantum,
                          'i_ty' : self.type.get(),
                          'prie' : self.fertilizer_update_price_entry.get(),
                          'moth' : monthmn,
                          'yuar' : yearmn,
                          'sikuku' : datemn
                        })
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", f'{self.fertilizer_update_price_name_entry.get()} Price Updated Succesfully',parent =self.top55)
        #clear entries
        self.fertilizer_update_price_name_entry.delete(0,END)
        self.fertilizer_increase_name_entry.delete(0,END)
        self.fertilizer_remove_name_entry.delete(0,END)
        self.fertilizer_update_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_fertilizer_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def update_herbicides_price(self):
        response=messagebox.askyesno("Confirm", "Are you Sure?",parent=self.top55)
        if response ==1:
            #update the database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.herbicides_update_price_name_entry.get(),self.type.get(),))
            quantum=c.fetchone()
            c.execute("SELECT Month From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.herbicides_update_price_name_entry.get(),self.type.get(),))
            monthmn=c.fetchone()
            c.execute("SELECT Year From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.herbicides_update_price_name_entry.get(),self.type.get(),))
            yearmn=c.fetchone()
            c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.herbicides_update_price_name_entry.get(),self.type.get(),))
            datemn=c.fetchone()
            c.execute(""" UPDATE Store_Inventory SET
                        Item_Name=:f_name,
                        Quantity=:q_ty,
                        Item_Type=:i_ty,
                        Price=:prie,
                        Month=:moth,
                        Year =:yuar,
                        DATE =:sikuku

                        WHERE Item_Name=:f_name""",
                      {
                          'f_name': self.herbicides_update_price_name_entry.get(),
                          'q_ty' : quantum,
                          'i_ty' : self.type.get(),
                          'prie' : self.herbicides_update_price_entry.get(),
                          'moth' : monthmn,
                          'yuar' : yearmn,
                          'sikuku' : datemn
                        })
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", f'{self.herbicides_update_price_name_entry.get()} Price Updated Succesfully',parent =self.top55)
        #clear entries
        self.herbicides_update_price_name_entry.delete(0,END)
        self.herbicides_increase_name_entry.delete(0,END)
        self.herbicides_remove_name_entry.delete(0,END)
        self.herbicides_update_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_herbicides_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def update_seeds_price(self):
        response=messagebox.askyesno("Confirm", "Are you Sure?",parent=self.top55)
        if response ==1:
            #update the database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.seeds_update_price_name_entry.get(),self.type.get(),))
            quantum=c.fetchone()
            c.execute("SELECT Month From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.seeds_update_price_name_entry.get(),self.type.get(),))
            monthmn=c.fetchone()
            c.execute("SELECT Year From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.seeds_update_price_name_entry.get(),self.type.get(),))
            yearmn=c.fetchone()
            c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.seeds_update_price_name_entry.get(),self.type.get(),))
            datemn=c.fetchone()
            c.execute(""" UPDATE Store_Inventory SET
                        Item_Name=:f_name,
                        Quantity=:q_ty,
                        Item_Type=:i_ty,
                        Price=:prie,
                        Month=:moth,
                        Year =:yuar,
                        DATE =:sikuku

                        WHERE Item_Name=:f_name""",
                      {
                          'f_name': self.seeds_update_price_name_entry.get(),
                          'q_ty' : quantum,
                          'i_ty' : self.type.get(),
                          'prie' : self.seeds_update_price_entry.get(),
                          'moth' : monthmn,
                          'yuar' : yearmn,
                          'sikuku' : datemn
                        })
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", f'{self.seeds_update_price_name_entry.get()} Price Updated Succesfully',parent =self.top55)
        #clear entries
        self.seeds_update_price_name_entry.delete(0,END)
        self.seeds_increase_name_entry.delete(0,END)
        self.seeds_remove_name_entry.delete(0,END)
        self.seeds_update_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_seeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def update_tools_price(self):
        response=messagebox.askyesno("Confirm", "Are you Sure?",parent=self.top55)
        if response ==1:
            #update the database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.tools_update_price_name_entry.get(),self.type.get(),))
            quantum=c.fetchone()
            c.execute("SELECT Month From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.tools_update_price_name_entry.get(),self.type.get(),))
            monthmn=c.fetchone()
            c.execute("SELECT Year From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.tools_update_price_name_entry.get(),self.type.get(),))
            yearmn=c.fetchone()
            c.execute("SELECT DATE From Store_Inventory WHERE Item_Name=? AND Item_Type=?",(self.tools_update_price_name_entry.get(),self.type.get(),))
            datemn=c.fetchone()
            c.execute(""" UPDATE Store_Inventory SET
                        Item_Name=:f_name,
                        Quantity=:q_ty,
                        Item_Type=:i_ty,
                        Price=:prie,
                        Month=:moth,
                        Year =:yuar,
                        DATE =:sikuku

                        WHERE Item_Name=:f_name""",
                      {
                          'f_name': self.tools_update_price_name_entry.get(),
                          'q_ty' : quantum,
                          'i_ty' : self.type.get(),
                          'prie' : self.tools_update_price_entry.get(),
                          'moth' : monthmn,
                          'yuar' : yearmn,
                          'sikuku' : datemn
                        })
            conn.commit()
            conn.close()
            messagebox.showinfo("Bravo", f'{self.tools_update_price_name_entry.get()} Price Updated Succesfully',parent =self.top55)
        #clear entries
        self.tools_update_price_name_entry.delete(0,END)
        self.tools_increase_name_entry.delete(0,END)
        self.tools_remove_name_entry.delete(0,END)
        self.tools_update_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_tools_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
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
        heading1="Item Name"
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
        
    def add_feeds(self):
        try:
            if self.feeds_new_name_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Feeds Name",parent =self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Inventory VALUES(:Item_Name, :Quantity, :Item_Type, :Price,:Month, :Year, :DATE)",
                        {
                            'Item_Name': self.feeds_new_name_entry.get(),
                            'Quantity': self.feeds_new_quantity_entry.get(),
                            'Item_Type':self.type.get(),
                            'Price': self.feeds_new_price_entry.get(),
                            'Month': self.mwezi,
                            'Year' : self.mwaka,
                            'DATE' :self.today1
                            })
                conn.commit()
                conn.close()
                #insert data to our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                            {
                                'Item_Name': self.feeds_new_name_entry.get(),
                                'Item_Quantity' : self.feeds_new_quantity_entry.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.feeds_new_name_entry.get()} Added Succesfully',parent =self.top55)
        except:
            messagebox.showerror("ERROR",f'{self.feeds_new_name_entry.get()} Already Exists',parent =self.top55)
        #clear entry boxes
        self.feeds_new_name_entry.delete(0,END)
        self.feeds_new_quantity_entry.delete(0,END)
        self.feeds_new_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_feeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def add_fertilizers(self):
        try:
            if self.fertilizer_new_name_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Fertilizer Name",parent =self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Inventory VALUES(:Item_Name, :Quantity, :Item_Type, :Price,:Month, :Year, :DATE)",
                        {
                            'Item_Name': self.fertilizer_new_name_entry.get(),
                            'Quantity': self.fertilizer_new_quantity_entry.get(),
                            'Item_Type':self.type.get(),
                            'Price': self.fertilizer_new_price_entry.get(),
                            'Month': self.mwezi,
                            'Year' : self.mwaka,
                            'DATE' :self.today1
                            })
                conn.commit()
                conn.close()
                #insert data to our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                            {
                                'Item_Name': self.fertilizer_new_name_entry.get(),
                                'Item_Quantity' : self.fertilizer_new_quantity_entry.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.fertilizer_new_name_entry.get()} Added Succesfully',parent=self.top55)
        except:
            messagebox.showerror("ERROR",f'{self.fertilizer_new_name_entry.get()} Already Exists',parent=self.top55)
        #clear entry boxes
        self.fertilizer_new_name_entry.delete(0,END)
        self.fertilizer_new_quantity_entry.delete(0,END)
        self.fertilizer_new_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_fertilizer_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def add_herbicides(self):
        try:
            if self.herbicides_new_name_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Herbicides Name",parent =self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Inventory VALUES(:Item_Name, :Quantity, :Item_Type, :Price,:Month, :Year, :DATE)",
                        {
                            'Item_Name': self.herbicides_new_name_entry.get(),
                            'Quantity': self.herbicides_new_quantity_entry.get(),
                            'Item_Type':self.type.get(),
                            'Price': self.herbicides_new_price_entry.get(),
                            'Month': self.mwezi,
                            'Year' : self.mwaka,
                            'DATE' :self.today1
                            })
                conn.commit()
                conn.close()
                #insert data to our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                            {
                                'Item_Name': self.herbicides_new_name_entry.get(),
                                'Item_Quantity' : self.herbicides_new_quantity_entry.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.herbicides_new_name_entry.get()} Added Succesfully',parent=self.top55)
        except:
            messagebox.showerror("ERROR",f'{self.herbicides_new_name_entry.get()} Already Exists',parent=self.top55)
        #clear entry boxes
        self.herbicides_new_name_entry.delete(0,END)
        self.herbicides_new_quantity_entry.delete(0,END)
        self.herbicides_new_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_herbicides_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def add_seeds(self):
        try:
            if self.seeds_new_name_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Seeds Name",parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Inventory VALUES(:Item_Name, :Quantity, :Item_Type, :Price,:Month, :Year, :DATE)",
                        {
                            'Item_Name': self.seeds_new_name_entry.get(),
                            'Quantity': self.seeds_new_quantity_entry.get(),
                            'Item_Type':self.type.get(),
                            'Price': self.seeds_new_price_entry.get(),
                            'Month': self.mwezi,
                            'Year' : self.mwaka,
                            'DATE' :self.today1
                            })
                conn.commit()
                conn.close()
                #insert data to our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                            {
                                'Item_Name': self.seeds_new_name_entry.get(),
                                'Item_Quantity' : self.seeds_new_quantity_entry.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.seeds_new_name_entry.get()} Added Succesfully',parent=self.top55)
        except:
            messagebox.showerror("ERROR",f'{self.seeds_new_name_entry.get()} Already Exists',parent=self.top55)
        #clear entry boxes
        self.seeds_new_name_entry.delete(0,END)
        self.seeds_new_quantity_entry.delete(0,END)
        self.seeds_new_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_seeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def add_tools(self):
        try:
            if self.tools_new_name_entry.get()=="":
                messagebox.showerror("ERROR", "Please Enter Tools's Name",parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Inventory VALUES(:Item_Name, :Quantity, :Item_Type, :Price,:Month, :Year, :DATE)",
                        {
                            'Item_Name': self.tools_new_name_entry.get(),
                            'Quantity': self.tools_new_quantity_entry.get(),
                            'Item_Type':self.type.get(),
                            'Price': self.tools_new_price_entry.get(),
                            'Month': self.mwezi,
                            'Year' : self.mwaka,
                            'DATE' :self.today1
                            })
                conn.commit()
                conn.close()
                #insert data to our feeds records table
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                            {
                                'Item_Name': self.tools_new_name_entry.get(),
                                'Item_Quantity' : self.tools_new_quantity_entry.get(),
                                'Month' : self.mwezi,
                                'Year': self.mwaka
                                })
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo", f'{self.tools_new_name_entry.get()} Added Succesfully',parent=self.top55)
        except:
            messagebox.showerror("ERROR",f'{self.tools_new_name_entry.get()} Already Exists',parent=self.top55)
        #clear entry boxes
        self.tools_new_name_entry.delete(0,END)
        self.tools_new_quantity_entry.delete(0,END)
        self.tools_new_price_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_tools_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    #add new stock
    def increase_feeds_stock(self):
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(self.feeds_increase_name_entry.get(),self.mwezi,self.mwaka,))
        initial_quantity=c.fetchone()
        if initial_quantity==None:
            initial_quantity=0
        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(self.feeds_increase_name_entry.get(),))
        now_quantity=c.fetchone()
        if now_quantity==None:
            now_quantity=0
        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(self.feeds_increase_name_entry.get(),))
        cost=c.fetchone()
        c.execute("SELECT Month FROM Store_Records WHERE Item_Name=?",(self.feeds_increase_name_entry.get(),))
        initial_month=c.fetchone()
        c.execute("SELECT Year FROM Store_Records WHERE Item_Name=?",(self.feeds_increase_name_entry.get(),))
        initial_year=c.fetchone()
        conn.commit()
        conn.close()
        final_quantity = (initial_quantity + float(self.feeds_increase_quantity_entry.get()))
        later_quantity= (now_quantity + float(self.feeds_increase_quantity_entry.get()))
        if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
            #update feeds inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku

                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.feeds_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty': self.type.get(),
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
            c.execute(""" UPDATE Store_Records SET
                        Item_Name=:fu_name,
                        Item_Quantity=:f_qty,
                        Month=:monthm,
                        Year=:yuar
                        
                        WHERE Item_Name=:fu_name""",
                        {
                            'fu_name': self.feeds_increase_name_entry.get(),
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
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku
                            
                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.feeds_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty' : self.type.get(),
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
            c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                        {
                            'Item_Name': self.feeds_increase_name_entry.get(),
                            'Item_Quantity' : self.feeds_increase_quantity_entry.get(),
                            'Month' : self.mwezi,
                            'Year': self.mwaka
                            })
            conn.commit()
            conn.close()
        messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top55)
        #clear entries
        self.feeds_update_price_name_entry.delete(0,END)
        self.feeds_increase_name_entry.delete(0,END)
        self.feeds_increase_quantity_entry.delete(0,END)
        self.feeds_remove_name_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_feeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def increase_fertilizer_stock(self):
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(self.fertilizer_increase_name_entry.get(),self.mwezi,self.mwaka,))
        initial_quantity=c.fetchone()
        if initial_quantity==None:
            initial_quantity=0
        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(self.fertilizer_increase_name_entry.get(),))
        now_quantity=c.fetchone()
        if now_quantity==None:
            now_quantity=0
        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(self.fertilizer_increase_name_entry.get(),))
        cost=c.fetchone()
        c.execute("SELECT Month FROM Store_Records WHERE Item_Name=?",(self.fertilizer_increase_name_entry.get(),))
        initial_month=c.fetchone()
        c.execute("SELECT Year FROM Store_Records WHERE Item_Name=?",(self.fertilizer_increase_name_entry.get(),))
        initial_year=c.fetchone()
        conn.commit()
        conn.close()
        final_quantity = (initial_quantity + float(self.fertilizer_increase_quantity_entry.get()))
        later_quantity= (now_quantity + float(self.fertilizer_increase_quantity_entry.get()))
        if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
            #update feeds inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku

                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.fertilizer_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty': self.type.get(),
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
            c.execute(""" UPDATE Store_Records SET
                        Item_Name=:fu_name,
                        Item_Quantity=:f_qty,
                        Month=:monthm,
                        Year=:yuar
                        
                        WHERE Item_Name=:fu_name""",
                        {
                            'fu_name': self.fertilizer_increase_name_entry.get(),
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
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku
                            
                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.fertilizer_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty' : self.type.get(),
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
            c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                        {
                            'Item_Name': self.fertilizer_increase_name_entry.get(),
                            'Item_Quantity' : self.fertilizer_increase_quantity_entry.get(),
                            'Month' : self.mwezi,
                            'Year': self.mwaka
                            })
            conn.commit()
            conn.close()
        messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top55)
        #clear entries
        self.fertilizer_update_price_name_entry.delete(0,END)
        self.fertilizer_increase_name_entry.delete(0,END)
        self.fertilizer_increase_quantity_entry.delete(0,END)
        self.fertilizer_remove_name_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_fertilizer_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def increase_herbicides_stock(self):
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(self.herbicides_increase_name_entry.get(),self.mwezi,self.mwaka,))
        initial_quantity=c.fetchone()
        if initial_quantity==None:
            initial_quantity=0
        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(self.herbicides_increase_name_entry.get(),))
        now_quantity=c.fetchone()
        if now_quantity==None:
            now_quantity=0
        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(self.herbicides_increase_name_entry.get(),))
        cost=c.fetchone()
        c.execute("SELECT Month FROM Store_Records WHERE Item_Name=?",(self.herbicides_increase_name_entry.get(),))
        initial_month=c.fetchone()
        c.execute("SELECT Year FROM Store_Records WHERE Item_Name=?",(self.herbicides_increase_name_entry.get(),))
        initial_year=c.fetchone()
        conn.commit()
        conn.close()
        final_quantity = (initial_quantity + float(self.herbicides_increase_quantity_entry.get()))
        later_quantity= (now_quantity + float(self.herbicides_increase_quantity_entry.get()))
        if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
            #update feeds inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku

                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.herbicides_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty': self.type.get(),
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
            c.execute(""" UPDATE Store_Records SET
                        Item_Name=:fu_name,
                        Item_Quantity=:f_qty,
                        Month=:monthm,
                        Year=:yuar
                        
                        WHERE Item_Name=:fu_name""",
                        {
                            'fu_name': self.herbicides_increase_name_entry.get(),
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
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku
                            
                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.herbicides_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty' : self.type.get(),
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
            c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                        {
                            'Item_Name': self.herbicides_increase_name_entry.get(),
                            'Item_Quantity' : self.herbicides_increase_quantity_entry.get(),
                            'Month' : self.mwezi,
                            'Year': self.mwaka
                            })
            conn.commit()
            conn.close()
        messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top55)
        #clear entries
        self.herbicides_update_price_name_entry.delete(0,END)
        self.herbicides_increase_name_entry.delete(0,END)
        self.herbicides_increase_quantity_entry.delete(0,END)
        self.herbicides_remove_name_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_herbicides_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def increase_seeds_stock(self):
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(self.seeds_increase_name_entry.get(),self.mwezi,self.mwaka,))
        initial_quantity=c.fetchone()
        if initial_quantity==None:
            initial_quantity=0
        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(self.seeds_increase_name_entry.get(),))
        now_quantity=c.fetchone()
        if now_quantity==None:
            now_quantity=0
        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(self.seeds_increase_name_entry.get(),))
        cost=c.fetchone()
        c.execute("SELECT Month FROM Store_Records WHERE Item_Name=?",(self.seeds_increase_name_entry.get(),))
        initial_month=c.fetchone()
        c.execute("SELECT Year FROM Store_Records WHERE Item_Name=?",(self.seeds_increase_name_entry.get(),))
        initial_year=c.fetchone()
        conn.commit()
        conn.close()
        final_quantity = (initial_quantity + float(self.seeds_increase_quantity_entry.get()))
        later_quantity= (now_quantity + float(self.seeds_increase_quantity_entry.get()))
        if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
            #update feeds inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku

                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.seeds_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty': self.type.get(),
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
            c.execute(""" UPDATE Store_Records SET
                        Item_Name=:fu_name,
                        Item_Quantity=:f_qty,
                        Month=:monthm,
                        Year=:yuar
                        
                        WHERE Item_Name=:fu_name""",
                        {
                            'fu_name': self.seeds_increase_name_entry.get(),
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
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku
                            
                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.seeds_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty' : self.type.get(),
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
            c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                        {
                            'Item_Name': self.seeds_increase_name_entry.get(),
                            'Item_Quantity' : self.seeds_increase_quantity_entry.get(),
                            'Month' : self.mwezi,
                            'Year': self.mwaka
                            })
            conn.commit()
            conn.close()
        messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top55)
        #clear entries
        self.seeds_update_price_name_entry.delete(0,END)
        self.seeds_increase_name_entry.delete(0,END)
        self.seeds_increase_quantity_entry.delete(0,END)
        self.seeds_remove_name_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_seeds_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    def increase_tools_stock(self):
        conn=sqlite3.connect('samaria feeds database.db')
        conn.row_factory=lambda cursor, row:row[0]
        c=conn.cursor()
        c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(self.tools_increase_name_entry.get(),self.mwezi,self.mwaka,))
        initial_quantity=c.fetchone()
        if initial_quantity==None:
            initial_quantity=0
        c.execute("SELECT Quantity FROM Store_Inventory WHERE Item_Name=?",(self.tools_increase_name_entry.get(),))
        now_quantity=c.fetchone()
        if now_quantity==None:
            now_quantity=0
        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(self.tools_increase_name_entry.get(),))
        cost=c.fetchone()
        c.execute("SELECT Month FROM Store_Records WHERE Item_Name=?",(self.tools_increase_name_entry.get(),))
        initial_month=c.fetchone()
        c.execute("SELECT Year FROM Store_Records WHERE Item_Name=?",(self.tools_increase_name_entry.get(),))
        initial_year=c.fetchone()
        conn.commit()
        conn.close()
        final_quantity = (initial_quantity + float(self.tools_increase_quantity_entry.get()))
        later_quantity= (now_quantity + float(self.tools_increase_quantity_entry.get()))
        if ((initial_month==self.mwezi)and(initial_year==self.mwaka)):
            #update feeds inventory table
            conn=sqlite3.connect('samaria feeds database.db')
            c=conn.cursor()
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku

                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.tools_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty': self.type.get(),
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
            c.execute(""" UPDATE Store_Records SET
                        Item_Name=:fu_name,
                        Item_Quantity=:f_qty,
                        Month=:monthm,
                        Year=:yuar
                        
                        WHERE Item_Name=:fu_name""",
                        {
                            'fu_name': self.tools_increase_name_entry.get(),
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
            c.execute(""" UPDATE Store_Inventory SET
                            Item_Name=:f_name,
                            Quantity=:q_ty,
                            Item_Type=:i_ty,
                            Price=:prie,
                            Month=:moth,
                            Year =:yuar,
                            DATE =:sikuku
                            
                            WHERE Item_Name=:f_name""",
                            {
                                'f_name': self.tools_increase_name_entry.get(),
                                'q_ty' : later_quantity,
                                'i_ty' : self.type.get(),
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
            c.execute("INSERT INTO Store_Records VALUES (:Item_Name, :Item_Quantity, :Month, :Year)",
                        {
                            'Item_Name': self.tools_increase_name_entry.get(),
                            'Item_Quantity' : self.tools_increase_quantity_entry.get(),
                            'Month' : self.mwezi,
                            'Year': self.mwaka
                            })
            conn.commit()
            conn.close()
        messagebox.showinfo("Bravo","New Stock Succesfully Added",parent=self.top55)
        #clear entries
        self.tools_update_price_name_entry.delete(0,END)
        self.tools_increase_name_entry.delete(0,END)
        self.tools_increase_quantity_entry.delete(0,END)
        self.tools_remove_name_entry.delete(0,END)
        #refresh the treeview
        self.my_tree1.delete(* self.my_tree1.get_children())
        self.query_tools_database()
        #refresh the treeview
        self.my_tree2.delete(* self.my_tree2.get_children())
        self.query_database()
    #remove data
    def remove_feeds(self):
        response=messagebox.askyesno("Danger", "Do you want to delete this Feeds?",parent=self.top55)
        if response ==1:
            #delete from database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(self.feeds_remove_name_entry.get(),))
            quantumn=c.fetchone()
            conn.commit()
            conn.close()
            if quantumn != 0:
                messagebox.showerror("ERROR", "You Cannot Delete Feeds If NOT Depleted", parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Store_Inventory WHERE Item_Name=?",(self.feeds_remove_name_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.feeds_remove_name_entry.get()} Deleted Succesfully',parent=self.top55)
            #clear entries
            self.feeds_update_price_name_entry.delete(0,END)
            self.feeds_increase_name_entry.delete(0,END)
            self.feeds_remove_name_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_feeds_database()
            #refresh the treeview
            self.my_tree2.delete(* self.my_tree2.get_children())
            self.query_database()
    def remove_fertilizer(self):
        response=messagebox.askyesno("Danger", "Do you want to delete this Fertilizer?",parent=self.top55)
        if response ==1:
            #delete from database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(self.fertilizer_remove_name_entry.get(),))
            quantumn=c.fetchone()
            conn.commit()
            conn.close()
            if quantumn != 0:
                messagebox.showerror("ERROR", "You Cannot Delete Fertilizer If NOT Depleted", parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Store_Inventory WHERE Item_Name=?",(self.fertilizer_remove_name_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.fertilizer_remove_name_entry.get()} Deleted Succesfully',parent=self.top55)
            #clear entries
            self.fertilizer_update_price_name_entry.delete(0,END)
            self.fertilizer_increase_name_entry.delete(0,END)
            self.fertilizer_remove_name_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_fertilizer_database()
            #refresh the treeview
            self.my_tree2.delete(* self.my_tree2.get_children())
            self.query_database()
    def remove_herbicides(self):
        response=messagebox.askyesno("Danger", "Do you want to delete this Herbicide?",parent=self.top55)
        if response ==1:
            #delete from database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(self.herbicides_remove_name_entry.get(),))
            quantumn=c.fetchone()
            conn.commit()
            conn.close()
            if quantumn != 0:
                messagebox.showerror("ERROR", "You Cannot Delete Herbicides If NOT Depleted", parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Store_Inventory WHERE Item_Name=?",(self.herbicides_remove_name_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.herbicides_remove_name_entry.get()} Deleted Succesfully',parent=self.top55)
            #clear entries
            self.herbicides_update_price_name_entry.delete(0,END)
            self.herbicides_increase_name_entry.delete(0,END)
            self.herbicides_remove_name_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_herbicides_database()
            #refresh the treeview
            self.my_tree2.delete(* self.my_tree2.get_children())
            self.query_database()
    def remove_seeds(self):
        response=messagebox.askyesno("Danger", "Do you want to delete this Seeds?",parent=self.top55)
        if response ==1:
            #delete from database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(self.seeds_remove_name_entry.get(),))
            quantumn=c.fetchone()
            conn.commit()
            conn.close()
            if quantumn != 0:
                messagebox.showerror("ERROR", "You Cannot Delete Seeds If NOT Depleted", parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Store_Inventory WHERE Item_Name=?",(self.seeds_remove_name_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.seeds_remove_name_entry.get()} Deleted Succesfully',parent=self.top55)
            #clear entries
            self.seeds_update_price_name_entry.delete(0,END)
            self.seeds_increase_name_entry.delete(0,END)
            self.seeds_remove_name_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_seeds_database()
            #refresh the treeview
            self.my_tree2.delete(* self.my_tree2.get_children())
            self.query_database()
    def remove_tools(self):
        response=messagebox.askyesno("Danger", "Do you want to delete this Farm Tool?",parent=self.top55)
        if response ==1:
            #delete from database
            conn=sqlite3.connect('samaria feeds database.db')
            conn.row_factory=lambda cursor, row:row[0]
            c=conn.cursor()
            c.execute("SELECT Quantity From Store_Inventory WHERE Item_Name=?",(self.tools_remove_name_entry.get(),))
            quantumn=c.fetchone()
            conn.commit()
            conn.close()
            if quantumn != 0:
                messagebox.showerror("ERROR", "You Cannot Delete Farm Tool If NOT Depleted", parent=self.top55)
            else:
                conn=sqlite3.connect('samaria feeds database.db')
                c=conn.cursor()
                c.execute("DELETE FROM Store_Inventory WHERE Item_Name=?",(self.tools_remove_name_entry.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Bravo",f'{self.tools_remove_name_entry.get()} Deleted Succesfully',parent=self.top55)
            #clear entries
            self.tools_update_price_name_entry.delete(0,END)
            self.tools_increase_name_entry.delete(0,END)
            self.tools_remove_name_entry.delete(0,END)
            #refresh the treeview
            self.my_tree1.delete(* self.my_tree1.get_children())
            self.query_tools_database()
            #refresh the treeview
            self.my_tree2.delete(* self.my_tree2.get_children())
            self.query_database()
    def daily_report(self):
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
        def generate_daily_report():
            try:
                total_daily=0.0
                credit_daily=0.0
                conn=sqlite3.connect("samaria feeds database.db")
                c=conn.cursor()
                c.execute("SELECT Item_Name, SUM(Item_Quantity) FROM Local_Sales WHERE DATE=? GROUP BY Item_Name",(self.selection88,))
                all_sales=c.fetchall()
                print(all_sales)
                conn.commit()
                conn.close()
                #
                conn=sqlite3.connect("samaria feeds database.db")
                c=conn.cursor()
                c.execute("SELECT Creditors_Name,Item_Name,Item_Quantity FROM LOCAL_CREDITORS WHERE DATE=? GROUP BY Creditors_Name",(self.selection88,))
                all_creditors=c.fetchall()
                print(all_creditors)
                conn.commit()
                conn.close()
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1=f'DAILY REPORT FOR {self.selection88}'
                heading2="Served By:"
                #first delete the scrolledtext  contents
                self.my_receipt88.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt88.insert('end', "\n" +title + "\n")
                self.my_receipt88.insert('end', "\n" +sub + "\n")
                self.my_receipt88.insert('end', "\n" +heading1+"\n")
                self.my_receipt88.insert('end', "\n" +self.today + "\t"+ self.Time +"\n")
                self.my_receipt88.insert('end', "\n" +"Item_Name"+"\t"+"\t"+"Quantity"+"\t"+"Total"+"\n")
                for record in all_sales:
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[0],))
                    item_price=c.fetchone()
                    conn.commit()
                    conn.close()
                    total=float(record[1]) * float(item_price)
                    self.my_receipt88.insert('end', "\n" +str(record[0])+"\t"+str(record[1])+"\t"+str(total)+"\n")
                    total_daily+=total
                self.my_receipt88.insert('end', "\n" + "Total Sales:"+"\t"+f'Kshs {total_daily}'+"\n")
                if all_creditors!=[]:
                    total_credits=0.0
                    self.my_receipt88.insert('end', "\n" + "\t"+"CREDITORS"+"\n")
                    for record in all_creditors:
                        self.my_receipt88.insert('end', "\n" +" Creditor:"+"\t"+str(record[0])+"\n")
                        self.my_receipt88.insert('end', "\n" +"Item_Name"+"\t"+"Quantity"+"\t"+"Total"+"\n")
                        #
                        conn=sqlite3.connect('samaria feeds database.db')
                        conn.row_factory=lambda cursor, row:row[0]
                        c=conn.cursor()
                        c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record[1],))
                        item_p=c.fetchone()
                        conn.commit()
                        conn.close()
                        total=float(record[2]) * float(item_p)
                        self.my_receipt88.insert('end', "\n" +str(record[1])+"\t"+str(record[2])+"\t"+str(total)+"\n")
                        total_credits+=total
                    self.my_receipt88.insert('end', "\n" + "Total Credit:"+"\t"+f'Kshs {total_credits}'+"\n")
                self.my_receipt88.insert('end', "\n"+ heading2+"\t"+server+"\n")
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
        self.left_frame=customtkinter.CTkFrame(self.top89,border_color="green",border_width=5,corner_radius=8,width=600,height=450)
        self.left_frame.pack(anchor="center")
        self.choose_date_button=customtkinter.CTkButton(self.left_frame,text="Choose Date",text_color="white",fg_color="red",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=grab_date88)
        self.choose_date_button.grid(row=0,column=0,columnspan=5,pady=10,padx=30,ipadx=30)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_daily_report)
        self.generate_button.grid(row=0,column=5,padx=20,pady=10,columnspan=5,sticky=W,ipadx=30)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=10, padx=10)
        self.my_receipt88=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=20)
        self.my_receipt88.grid(row=2,column=0,columnspan=10,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt89)
        self.print_button.grid(row=3,column=0,columnspan=10,padx=10,pady=10,ipadx=30)
    def monthly_report(self):
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
            if self.month_chooser.get()=="":
                messagebox.showerror("ERROR","Please Choose Month",parent=self.top85)
            else:
                #receipt
                #define headings
                title="SAMARIA MILK GROUP"
                sub="Quality Milk, Healthy Life"
                heading1=f'MONTHLY REPORT FOR {self.month_chooser.get()}'
                heading3="Served By:"
                #first delete the scrolledtext  contents
                self.my_receipt85.delete('1.0', 'end')
                #add stuff into our scrolled text
                self.my_receipt85.insert('end', "\n" +title + "\n")
                self.my_receipt85.insert('end', "\n" +sub + "\n")
                self.my_receipt85.insert('end', "\n" +heading1+"\n")
                self.my_receipt85.insert('end', "\n" +self.today+','+self.Time+"\n")
                self.my_receipt85.insert('end', "\n" +"Item NAME"+"\t"+"\t"+"Carry IN"+"\t"+"Added"+" Sold Out"+" Price"+" Total"+"\t"+"Carry OUT"+"\n")
                #queries
                conn=sqlite3.connect('samaria feeds database.db')
                conn.row_factory=lambda cursor, row:row[0]
                c=conn.cursor()
                c.execute("SELECT Item_Name FROM Store_Records")
                all_feeds=c.fetchall()
                conn.commit()
                conn.close()
                self.monthmn = self.choosed-1
                if self.monthmn==1:
                    self.monthmn=12
                totalfeeds=0.0
                for record in all_feeds:
                    #carry in from last month
                    #remainder from last month
                    #added last month
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(record,self.monthmn,self.mwaka,))
                    p_added=c.fetchone()
                    if p_added==None:
                        p_added=0
                    conn.commit()
                    conn.close()
                    #sold out last month
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Item_Quantity) FROM LOCAL_CREDITORS WHERE Item_Name=? AND MONTH=? AND YEAR=?",(record,self.monthmn,self.mwaka,))
                    p_customer_given_out=c.fetchone()
                    if p_customer_given_out==None:
                        p_customer_given_out=0
                    c.execute("SELECT SUM(Item_Quantity) FROM Local_Sales WHERE Item_Name=? AND Month=? AND Year=? GROUP BY Item_Name",(record,self.monthmn,self.mwaka,))
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
                    c.execute("SELECT Item_Quantity FROM Store_Records WHERE Item_Name=? AND Month=? AND Year=?",(record,self.choosed,self.mwaka,))
                    added=c.fetchone()
                    if added==None:
                        added=0
                    conn.commit()
                    conn.close()
                    #sold out this month
                    conn=sqlite3.connect('samaria feeds database.db')
                    conn.row_factory=lambda cursor, row:row[0]
                    c=conn.cursor()
                    c.execute("SELECT SUM(Item_Quantity) FROM LOCAL_CREDITORS WHERE Item_Name=? AND MONTH=? AND YEAR=?",(record,self.choosed,self.mwaka,))
                    customer_given_out=c.fetchone()
                    if customer_given_out==None:
                        customer_given_out=0
                    c.execute("SELECT SUM(Item_Quantity) FROM Local_Sales WHERE Item_Name=? AND Month=? AND Year=? GROUP BY Item_Name",(record,self.choosed,self.mwaka,))
                    local_sold_out=c.fetchone()
                    if local_sold_out==None:
                        local_sold_out=0
                    sold_out=(customer_given_out+local_sold_out)
                    #price
                    c.execute("SELECT Price FROM Store_Inventory WHERE Item_Name=?",(record,))
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
                self.my_receipt85.insert('end', "\n" +"Total Amount:"+"\t"+f'Kshs {totalfeeds}'+"\n")
                self.my_receipt85.insert('end', "\n" +heading3+"\t"+server+"\n")
        def choose_month(event):
            if self.month_chooser.get()==f'January-{self.mwaka}':
                self.choosed=1
            if self.month_chooser.get()==f'February-{self.mwaka}':
                self.choosed=2
            if self.month_chooser.get()==f'March-{self.mwaka}':
                self.choosed=3
            if self.month_chooser.get()==f'April-{self.mwaka}':
                self.choosed=4
            if self.month_chooser.get()==f'May-{self.mwaka}':
                self.choosed=5
            if self.month_chooser.get()==f'June-{self.mwaka}':
                self.choosed=6
            if self.month_chooser.get()==f'July-{self.mwaka}':
                self.choosed=7
            if self.month_chooser.get()==f'August-{self.mwaka}':
                self.choosed=8
            if self.month_chooser.get()==f'September-{self.mwaka}':
                self.choosed=9
            if self.month_chooser.get()==f'October-{self.mwaka}':
                self.choosed=10
            if self.month_chooser.get()==f'November-{self.mwaka}':
                self.choosed=11
            if self.month_chooser.get()==f'December-{self.mwaka}':
                self.choosed=12
        #variables
        months=[f'January-{self.mwaka}',f'February-{self.mwaka}',f'March-{self.mwaka}',f'April-{self.mwaka}',f'May-{self.mwaka}',f'June-{self.mwaka}',f'July-{self.mwaka}',f'August-{self.mwaka}',f'September-{self.mwaka}',f'October-{self.mwaka}',f'November-{self.mwaka}',f'December-{self.mwaka}']
        self.month_chooser=StringVar()
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
        self.choose_month_label.grid(row=0,column=0,columnspan=5,pady=20,padx=10)
        self.choose_month_menu=customtkinter.CTkOptionMenu(self.left_frame,fg_color="red",text_color="white",variable=self.month_chooser,values=months,width=250,height=25,command=choose_month)
        self.choose_month_menu.grid(row=0,column=5,columnspan=5)
        self.generate_button=customtkinter.CTkButton(self.left_frame,text="Generate Report",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=25,command=generate_monthly_report)
        self.generate_button.grid(row=0,column=10,padx=20,pady=20,columnspan=5,sticky=E)
        self.receipt_label=customtkinter.CTkLabel(self.left_frame, text="REPORT",fg_color="orange",text_color="white", text_font=("Consollas 10",-20,"underline", "bold"),width=150, height=35)
        self.receipt_label.grid(row=1, column=0, columnspan=15, padx=10)
        self.my_receipt85=ScrolledText(self.left_frame, font="Consollas 10",border=7, relief="groove",background='#282c34', foreground='#fff',width=140,height=23)
        self.my_receipt85.grid(row=2,column=0,columnspan=15,padx=20)
        self.print_button=customtkinter.CTkButton(self.left_frame,text="PRINT",fg_color="purple",text_color="white",text_font=("Consollas 10",-20,"bold"),width=200,height=30,command=print_receipt85)
        self.print_button.grid(row=3,column=0,columnspan=15,padx=10,pady=10)
    def pending_credits(self):
        #toplevel
        self.top89=Toplevel()
        self.top89.iconbitmap("logo1.ico")
        self.top89.state('zoomed')
        self.title_frame=Frame(self.top89)
        self.title_frame.pack(anchor="center")
        title ="SAMARIA MILK GROUP"
        sub="Quality Milk, Healthy Life"
        sub0="UNPAID ITEMS"
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
        tender_title="PENDING CREDITS"
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
            self.my_receipt.insert('end', "\n" + str(record[2]) +"\t"+"\t"+str(record[3])+"\t"+f' KShs {record[5]}'+"\n")
            total_amount+=float(record[5])
        self.my_receipt.insert('end', "\n" + heading5 +"\t"+"\t"+ f' KShs {total_amount}'+"\n")
        self.my_receipt.insert('end', "\n" + heading6+ "\t"+ f'{server}' +"\n")
        self.print_button=customtkinter.CTkButton(my_frame1, text="PRINT", command=self.print_receipt,fg_color="red",text_color="white", text_font=("Consollas 10",-20, "bold"),width=200,height=40)
        self.print_button.grid(row=2, column=0, columnspan=5,padx=10, pady=10)

app=Login(root)
root.mainloop()
