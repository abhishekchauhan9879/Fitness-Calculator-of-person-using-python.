import os
import sqlite3
from re import *
from tkinter import *
from tkinter import (BooleanVar, Button, Checkbutton, Frame, Tk, font,messagebox)
from PIL import Image, ImageTk

#===========================================fullscreen================================================================
def fullscreen(f):
    f.attributes('-fullscreen', True)
#===========================================loginpage=================================================================
conn=sqlite3.connect('first.db')
c=conn.cursor()
t=Tk()
t.title('signin page')
t.option_add("*Font",'Algerian')
fullscreen(t)
#====================================================================================================================
im=Image.open('illustration-step1.jpg')
photo=ImageTk.PhotoImage(im)
l=Label(t,fg='white',image=photo,background='black')
l.place(x=0,y=510)
t.configure(bg='black')
ima=Image.open('wfl2.jpg')
p1=ImageTk.PhotoImage(ima)
s=Label(t,image=p1,background='black')
s.place(x=100,y=10)
#=======================================event_for_signup_and_forgot===================================================
def update_the_picture(bh):
    myimg = bh
    updated_picture = ImageTk.PhotoImage(Image.open(myimg))
    b1=Label(t)
    b1.place(x=0,y=0)
    b1.configure(image = updated_picture)
def ente(event,e):
    e.config(foreground='red')
def leav(event,e,t):
    e.config(foreground='#0c0656')
def ssignup(event,e):
    e.config(state='normal')
def click(event,ag):
    if ag.get() != '':
       ag.delete(0, "end")
       ag.insert(0, '')
       ag.config(fg = 'black')
def out(event,ag,txt):
    if ag.get() == '':
        ag.insert(0,txt)
        ag.config(fg = 'grey',show='')
def clickpwd(event,ag):
    if ag.get() != '':
       ag.delete(0, "end")
       ag.insert(0, '')
       ag.config(fg = 'black',show='*')
b1=Button(t,justify=CENTER,text='X',font='Algerian 10',command=quit,bg='#e0e0e0')
b1.place(x=1515,y=0)
def dest():
        for i in t.winfo_children():
                i.destroy()
        b1=Button(t,justify=CENTER,text='X',font='Algerian 10',command=quit,bg='#e0e0e0')
        b1.place(x=1515,y=0)
#==============================================signup================================================================
def signup():
        Form3 = Frame(t,relief=RIDGE)
        Form3.place(x=450,y=170)
        Form3.configure(bg='white',bd=1)
        Label(Form3,text='Signup',bg='black',fg='#efe6e6',bd=8,font='Algerian 25 bold',width='20').grid(row=0,column=0,ipady=6,sticky='new')
        e1=Entry(Form3,fg='grey', bg='#f5f5f5')
        e2=Entry(Form3,fg='grey', bg='#f5f5f5')
        e3=Entry(Form3,fg='grey', bg='#f5f5f5')
        e4=Entry(Form3,fg='grey', bg='#f5f5f5')
        e5=Entry(Form3,fg='grey', bg='#f5f5f5')
        e1.config(width='35',bd=2)
        e2.config(width='35',bd=2)
        e3.config(width='35',bd=2)
        e4.config(width='35',bd=2)
        e5.config(width='35',bd=2)
        e1.grid(row=1,column=0,padx=15+20,pady=20-6,ipady=6)
        e2.grid(row=2,column=0,padx=15+20,pady=20-6,ipady=6)
        e3.grid(row=3,column=0,padx=15+20,pady=20-6,ipady=6)
        e4.grid(row=4,column=0,padx=15+20,pady=20-6,ipady=6)
        e5.grid(row=5,column=0,padx=15+20,pady=20-6,ipady=6)
        e1.insert(0,'NAME')
        e2.insert(0,'MOBILE')
        e3.insert(0,'EMAILID')
        e4.insert(0,'PASSWORD')
        e5.insert(0,'CONFIRM PASSWORD')
        e1.bind('<FocusIn>',lambda event, ag=e1:click(event, ag))
        e1.bind('<FocusOut>',lambda event, ag=e1:out(event, ag," NAME"))
        e2.bind('<FocusIn>',lambda event, ag=e2:click(event, ag))
        e2.bind('<FocusOut>',lambda event, ag=e2:out(event, ag," MOBILE"))
        e3.bind('<FocusIn>',lambda event, ag=e3:click(event, ag))
        e3.bind('<FocusOut>',lambda event, ag=e3:out(event, ag,'EMAILID'))
        e4.bind('<FocusIn>',lambda event, ag=e4:clickpwd(event, ag))
        e4.bind('<FocusOut>',lambda event, ag=e4:out(event, ag,'PASSWORD'))
        e5.bind('<FocusIn>',lambda event, ag=e5:clickpwd(event, ag))
        e5.bind('<FocusOut>',lambda event, ag=e5:out(event, ag,'CONFIRM PASSWORD'))
        def signupbutn():
                r,u=0,0
                if(match(r'[A-Za-z0-9!@#$%&*_]',e5.get())):
                        r=1
                c.execute('select email from user')
                l=[]
                for i in c.fetchall():
                        for j in i:
                                l.append(j)
                for i in l:
                    if(e3.get()!=str(i)):
                       u=1
                                        
                if (e1.get()).isalpha():     
                        if(len(e2.get())==10 and (e2.get()).isdigit()==True):
                                if(6<len(e4.get())<12  and e4.get()==e5.get() and r==1):
                                        c.execute('INSERT into user VALUES(?,?,?,?)',(e1.get(),e2.get(),e3.get(),e4.get()))
                                        conn.commit()
                                        messagebox.showinfo('Submit','USER CREATED SUCCESSFULLY\n PLEASE LOG IN TO CONTINUE')
                                        Form3.destroy()
                                        logpage()
                                else:
                                        messagebox.showerror('error','PLease check the Password ')
                                        e4.delete(0,END);e5.delete(0,END);e4.focus()                        
                        else:
                                messagebox.showerror('error','Please check your Mobile No.')
                                e2.delete(0,END);e2.focus()
                else:
                        messagebox.showerror('error','Please check your name ')
                        e1.delete(0,END);e1.focus()
                return
        ac = IntVar()
        def check():
                if ac.get() == 0:
                        b.configure(text='Sign Up',state='disabled')
                else:
                        b.configure(text='Sign Up',state='normal')       
        ck1 = Checkbutton(Form3,background='#fff',font='Algerian 11', text='I Agree to the Terms & Conditions',variable=ac, command=check)
        ck1.grid(row=6, column=0, sticky="w",padx=35)
        b = Button(Form3,text="Sign Up", width = 20,justify=CENTER,bg='black',fg='#efe6e6',bd=8,font='Algerian 25 bold',command=signupbutn,state = DISABLED)       
        b.grid(row=7,columnspan=2,padx=1,pady=10)
def forg():
        Form1 = Frame(t,relief=RIDGE)
        Form1.place(x=450,y=200)
        Form1.configure(bg='white',bd=1)
        Label(Form1,text='forgot your password',bg='black',fg='#efe6e6',bd=8,width='20').grid(row=0,column=0,ipady=6,sticky='new')
        l3=Label(Form1,text='PLEASE ENTER YOUR RECOVERY\n MOBILE NUMBER',bg='#f5f5f5',bd=8,width='20')
        l3.grid(row=1,column=0,ipady=6,sticky='new')
        rpwd=Entry(Form1,cursor='"xterm"',fg='grey', bg='#f5f5f5')
        rpwd.grid(row=2,column=0,padx=15+20,pady=20-6,ipady=6)
        rpwd.config(width='35',bd=2)
        rpwd.insert(0,'Enter your Number Here')
        rpwd.bind('<FocusIn>',lambda event, ag=rpwd:click(event, ag))
        rpwd.bind('<FocusOut>',lambda event, ag=rpwd:out(event, ag,"Enter your Number Here"))
        def fpwd():
                if (len(rpwd.get())==10 and (rpwd.get()).isdigit()==True):
                        c.execute('select mobile from user where mobile=?',(rpwd.get(),))
                        s=c.fetchall()
                        if len(s)!=0:
                            for i in s:
                                    print(i)
                                    if str(rpwd.get()) in i:
                                            print('hi')
                                            messagebox.showerror('Hello','Sorry we r unable to find you!')
                                    else:    
                                            rpw=''
                                            c.execute('select Name from user where mobile=?',(rpwd.get(),))
                                            for i in c.fetchall():
                                                    for j in i:
                                                            rpw=j
                                            Form1.destroy()
                                            modpwd(rpw)    
                        else:
                            messagebox.showerror('Error','INVALID MOBILE NUMBER')    
                else:
                        messagebox.showerror('Error','PLease enter your correct 10 digit mobile number')
        Button(Form1,text='VALIDATE',command=fpwd,bg='black',fg='#efe6e6').grid(row=3,columnspan=1,pady=14)
def logpage():
        Form = Frame(t,relief=RIDGE)
        Form.place(x=450,y=170)
        Form.configure(bg='#fff',bd=1)
        Label(Form,text='LOGIN',bg='black',fg='#efe6e6',bd=8,font='Algerian 25 bold',width='20').grid(row=0,column=0,ipady=6,sticky='new')
        e1=Entry(Form,cursor='"xterm"',fg='grey', bg='#f5f5f5')
        e2=Entry(Form,fg='grey',cursor='"xterm"', bg='#f5f5f5')
        e1.config(width='35',bd=2)
        e2.config(width='35',bd=2)
        e1.grid(row=2,column=0,padx=15+20,pady=20-6,ipady=6)
        e2.grid(row=3,column=0,padx=15+20,pady=20-6,ipady=6)
        l1=Label(Form,text='FORGOT YOUR PASSWORD !',bg='#fff',fg='#0c0656',font='Algerian 12 underline')
        l1.grid(row=6,column=0,padx=35,sticky='w')
        l1.bind('<Enter>',lambda event,  e=l1:ente(event,e))
        def sdf(Event):
                Form.destroy()
                forg()
        l1.bind('<Button-1>',sdf)
        l1.bind('<Leave>',lambda event,  e=l1,t='#fff':leav(event,e,t))
        l2=Label(Form,text='SIGN UP !',bg='#fff',fg='#0c0656',font='Algerian 12 underline')
        l2.grid(row=6,column=0,padx=35,pady=8,sticky='e')
        l2.bind('<Enter>',lambda event,  e=l2:ente(event,e))
        l2.bind('<Leave>',lambda event,  e=l2,t='#fff':leav(event,e,t))
        def sdff(Event):
                Form.destroy()
                signup()
        l2.bind('<Button-1>',sdff)
        e1.insert(0,' Enter Your Email')
        e2.insert(0,' Password')
        e1.bind('<FocusIn>',lambda event, ag=e1:click(event, ag))
        e1.bind('<FocusOut>',lambda event, ag=e1:out(event, ag," Enter Your Email Address"))
        e2.bind('<FocusIn>',lambda event, ag=e2:clickpwd(event, ag))
        e2.bind('<FocusOut>',lambda event, ag=e2:out(event, ag," Password"))
        def dem():
                r=0
                if(match(r'[A-Za-z0-9!@#$%&*_]',e2.get())):
                        r=1
                if(6<len(e2.get())<12 and r==1):  
                                c.execute('select password from user where email=?',(e1.get(),))
                                s=c.fetchone()
                                #print(s)
                                for i in s:
                                        if i==(e2.get()):
                                                os.system('py pp1.py')    
                                                t.destroy()           
                                        else:
                                                messagebox.showerror('Error','INVALID CREDENTIALS')
                else:
                                messagebox.showerror('error','PASSWORD MUST CONTAINS UPPERCASE, LOWERCASE,\n DIGIT ,SPECIAL CHARACTER , AND HAVING LENGTH OF 6-12 CHARACTERS ')
                                e2.delete(0,END);e2.focus()
        
        ac = IntVar()
        def check():
                if ac.get() == 0:
                        b.configure(text='Sign In',state='disabled')
                else:
                        b.configure(text='Sign In',state='normal')       
        ck1 = Checkbutton(Form,background='#fff',highlightthickness=1,font='Algerian 11', text='I Agree to the Terms & Conditions',
                            variable=ac, command=check)
        ck1.grid(row=4, column=0, sticky="w",padx=35)
        b = Button(Form,text="Sign In", width = 20,justify=CENTER, background = 'black',fg='white',command=dem,state = DISABLED)       
        b.grid(row=5,column=0,padx=1,pady=8)
def modpwd(o):
        Form2 = Frame(t,relief=RIDGE)
        Form2.place(x=450,y=200)
        Form2.configure(bg='white',bd=1)
        Label(Form2,text='Enter your Password',bg='black',fg='#efe6e6',bd=8,font='Algerian 25 bold',width='20').grid(row=0,column=0,ipady=6,sticky='new')
        Label(Form2,text='Hello '+o+'!',bg='white',bd=8,width='20').grid(row=1,column=0,ipady=6,sticky='new')
        e7=Entry(Form2,cursor='"xterm"',fg='grey', bg='#f5f5f5')
        e8=Entry(Form2,fg='grey',cursor='"xterm"', bg='#f5f5f5')
        e7.config(width='35',bd=2)
        e8.config(width='35',bd=2)
        e7.grid(row=2,column=0,padx=15+20,pady=20-6,ipady=6)
        e8.grid(row=3,column=0,padx=15+20,pady=20-6,ipady=6)
        e7.insert(0,'Enter your password')
        e8.insert(0,'Confirm Password')
        e7.bind('<FocusIn>',lambda event, ag=e7:clickpwd(event, ag))
        e7.bind('<FocusOut>',lambda event, ag=e7:out(event, ag,"Enter your password"))
        e8.bind('<FocusIn>',lambda event, ag=e8:clickpwd(event, ag))
        e8.bind('<FocusOut>',lambda event, ag=e8:out(event, ag," Confirm Password"))
        def rpp():
                r=0
                if(match(r'[A-Za-z0-9!@#$%&*_]',e7.get())):
                        r=1
                if(6<len(e7.get())<12  and e7.get()==e8.get() and r==1):
                        c.execute('update user set password=? where name=?',(e7.get(),o))
                        conn.commit()
                        messagebox.showinfo("STATUS","PASSWORD CHANGED SUCCESSFULLY\nPLEASE LOGIN TO CONTINUE")
                        Form2.destroy()
                        logpage()
                else:
                        messagebox.showerror('error','PLease check the Password ')
                        e7.delete(0,END);e8.delete(0,END);e7.focus()
        Button(Form2,text='CONTINUE',command=rpp,bg='black',fg='#efe6e6').grid(row=4,columnspan=1,pady=14)
#==========================================================================================================================

def startpage():
        form5=Frame(t)
        bb=Button(form5,text='TEST NOW!',font=("Times",35),width=20,bg="black",fg="white",relief="raised",bd=40,
                activebackground="black",command=logpage,activeforeground="black")
        def sdff(Event):
                form5.destroy()
                s.destroy()
                logpage()
        bb.bind('<Button-1>',sdff)
        bb.grid(row=0,column=0)
        form5.place(x=700,y=180)
        form5.configure(bg='white')
        
        
#==========================================================================================================================
startpage()
#================================================EXIT_BUTTON================================================================
t.mainloop()
conn.commit()
conn.close()
#================================================Login_page_ends============================================================
