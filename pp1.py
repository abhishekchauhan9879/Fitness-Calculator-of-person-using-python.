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
t.configure(bg='white')
fullscreen(t)
im=Image.open('illustration-step22.jpg')
photo=ImageTk.PhotoImage(im)
l=Label(t,fg='white',image=photo,bd=0,background='black')
l.place(x=0,y=515)
def des():
        for i in t.winfo_children():
                i.destroy()
def click(event,ag):
    if ag.get() != '':
       ag.delete(0, "end")
       ag.insert(0, '')
       ag.config(fg = 'black')
def out(event,ag,txt):
    if ag.get() == '':
        ag.insert(0,txt)
        ag.config(fg = 'grey',show='')
def calc():
        Form3 = Frame(t,relief=RIDGE)
        Form3.place(x=260,y=20)
        Form3.configure(bg='white')
        Label(Form3,text='HELP US TO KNOW YOU BETTER',bg='white',fg='black',bd=8,font='Algerian 25 bold',width='20').grid(row=0,columnspan=2,ipady=6,sticky='new')
        l={"MALE","FEMALE"}
        c=StringVar()
        droplist=OptionMenu(Form3,c,*l)
        droplist.config(width=30,height=1,bg='white')
        c.set("I AM ")
        droplist.grid(row=1,columnspan=2)       
        e1=Entry(Form3,fg='grey', bg='white')
        e2=Entry(Form3,fg='grey', bg='white')
        e3=Entry(Form3,fg='grey', bg='white')
        e4=Entry(Form3,fg='grey', bg='white')
        e5=Entry(Form3,fg='grey', bg='white')
        e6=Entry(Form3,fg='grey', bg='white')
        e7=Entry(Form3,fg='grey', bg='white')
        e8=Entry(Form3,fg='grey', bg='white')
        e9=Entry(Form3,fg='grey', bg='white')
        e10=Entry(Form3,fg='grey', bg='white')
        e11=Entry(Form3,fg='grey', bg='white')
        e1.config(width='35',bd=2)
        e2.config(width='35',bd=2)
        e3.config(width='35',bd=2)
        e4.config(width='35',bd=2)
        e5.config(width='35',bd=2)
        e6.config(width='35',bd=2)
        e7.config(width='35',bd=2)
        e8.config(width='35',bd=2)
        e9.config(width='35',bd=2)
        e10.config(width='35',bd=2)
        e11.config(width='35',bd=2)
        e1.grid(row=1+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e2.grid(row=2+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e3.grid(row=3+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e4.grid(row=4+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e5.grid(row=5+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e6.grid(row=6+1,column=0,padx=15+20,pady=20-6,ipady=6)
        e7.grid(row=1+1,column=1,padx=15+20,pady=20-6,ipady=6)
        e8.grid(row=2+1,column=1,padx=15+20,pady=20-6,ipady=6)
        e9.grid(row=3+1,column=1,padx=15+20,pady=20-6,ipady=6)
        e10.grid(row=4+1,column=1,padx=15,pady=20-6,ipady=6)
        e11.grid(row=5+1,column=1,padx=15,pady=20-6,ipady=6)
        e1.bind('<FocusIn>',lambda event, ag=e1:click(event, ag))
        e1.bind('<FocusOut>',lambda event, ag=e1:out(event, ag," "))
        e2.bind('<FocusIn>',lambda event, ag=e2:click(event, ag))
        e2.bind('<FocusOut>',lambda event, ag=e2:out(event, ag," "))
        e3.bind('<FocusIn>',lambda event, ag=e3:click(event, ag))
        e3.bind('<FocusOut>',lambda event, ag=e3:out(event, ag,''))
        e4.bind('<FocusIn>',lambda event, ag=e4:click(event, ag))
        e4.bind('<FocusOut>',lambda event, ag=e4:out(event, ag," "))
        e5.bind('<FocusIn>',lambda event, ag=e5:click(event, ag))
        e5.bind('<FocusOut>',lambda event, ag=e5:out(event, ag," "))
        e6.bind('<FocusIn>',lambda event, ag=e6:click(event, ag))
        e6.bind('<FocusOut>',lambda event, ag=e6:out(event, ag,''))
        e7.bind('<FocusIn>',lambda event, ag=e7:click(event, ag))
        e7.bind('<FocusOut>',lambda event, ag=e7:out(event, ag," "))
        e8.bind('<FocusIn>',lambda event, ag=e8:click(event, ag))
        e8.bind('<FocusOut>',lambda event, ag=e8:out(event, ag," "))
        e9.bind('<FocusIn>',lambda event, ag=e9:click(event, ag))
        e9.bind('<FocusOut>',lambda event, ag=e9:out(event, ag,''))
        e10.bind('<FocusIn>',lambda event, ag=e10:click(event, ag))
        e10.bind('<FocusOut>',lambda event, ag=e10:out(event, ag," "))
        e11.bind('<FocusIn>',lambda event, ag=e11:click(event, ag))
        e11.bind('<FocusOut>',lambda event, ag=e11:out(event, ag," "))
        
        LK=Label(t,text='MORE OPTIONS',bg='white',fg='black',bd=2,font='Algerian 15 bold')
        L=Label(t,text='Signout',bg='white',fg='white',font='Algerian 15 bold')
        l1=Label(t,text='Exit',bg='white',fg='white',font='Algerian 15 bold')
        L.place(x=1350,y=20)
        l1.place(x=1470,y=20)
        def opensign(event):
                os.system('py p5.py')
                t.destroy()
        def fin(event):
                    LK.configure(fg='white')
                    L.configure(fg='black')
                    l1.configure(fg='black')
        def de(event):
                t.destroy()
        l1.bind('<Button-1>',de)
        L.bind('<Button-1>',opensign)
        LK.place(x=1380,y=0)
        LK.bind('<Enter>',fin)
        def repo(a,b,c,d,e,f,g,h,i):
                #des()
                Form3.destroy()
                Form31 = Frame(t,relief=RIDGE)
                Form31.place(x=260,y=10)
                Form31.configure(bg='white')
                Label(Form31,text='YOUR MEDICAL STATUS',bg='white',fg='black',bd=8,font='Algerian 25 bold',width='20').grid(row=0,column=1,columnspan=2,ipady=6,sticky='new')
                l1=Label(Form31,text='BMI:',fg='black', bg='white')
                l2=Label(Form31,text='BP:',fg='black', bg='white')
                l3=Label(Form31,text='PULSE RATE:',fg='black', bg='white')
                l4=Label(Form31,text='RBC COUNT:',fg='black', bg='white')
                l5=Label(Form31,text='WBC COUNT:',fg='black', bg='white')
                l6=Label(Form31,text='PLATELETS:',fg='black', bg='white')
                l7=Label(Form31,text='HB:',fg='black', bg='white')
                l8=Label(Form31,text='URIC ACID:',fg='black', bg='white')
                l9=Label(Form31,text='CHROLESTROL:',fg='black', bg='white')       
                e1=Entry(Form31,fg='black', bg='white')
                e2=Entry(Form31,fg='black', bg='white')
                e3=Entry(Form31,fg='black', bg='white')
                e4=Entry(Form31,fg='black', bg='white')
                e5=Entry(Form31,fg='black', bg='white')
                e6=Entry(Form31,fg='black', bg='white')
                e7=Entry(Form31,fg='black', bg='white')
                e8=Entry(Form31,fg='black', bg='white')
                e9=Entry(Form31,fg='black', bg='white')
                e1.config(width='15',bd=2)
                e2.config(width='15',bd=2)
                e3.config(width='15',bd=2)
                e4.config(width='15',bd=2)
                e5.config(width='15',bd=2)
                e6.config(width='15',bd=2)
                e7.config(width='15',bd=2)
                e8.config(width='15',bd=2)
                e9.config(width='15',bd=2)
                e1.insert(0,str(a))
                e2.insert(0,str(b))
                e3.insert(0,str(c))
                e4.insert(0,str(d))
                e5.insert(0,str(e))
                e6.insert(0,str(f))
                e7.insert(0,str(g))
                e8.insert(0,str(h))
                e9.insert(0,str(i))
                l1.grid(row=1,column=0,padx=15,pady=20-6,ipady=6)
                l2.grid(row=2,column=0,padx=15,pady=20-6,ipady=6)
                l3.grid(row=3,column=0,padx=15,pady=20-6,ipady=6)
                l4.grid(row=4,column=0,padx=15,pady=20-6,ipady=6)
                l5.grid(row=5,column=0,padx=15,pady=20-6,ipady=6)
                l6.grid(row=1,column=2,padx=15,pady=20-6,ipady=6)
                l7.grid(row=2,column=2,padx=15,pady=20-6,ipady=6)
                l8.grid(row=3,column=2,padx=15,pady=20-6,ipady=6)
                l9.grid(row=4,column=2,padx=15,pady=20-6,ipady=6)
                e1.grid(row=1,column=1,padx=15+20,pady=20-6,ipady=6)
                e2.grid(row=2,column=1,padx=15+20,pady=20-6,ipady=6)
                e3.grid(row=3,column=1,padx=15+20,pady=20-6,ipady=6)
                e4.grid(row=4,column=1,padx=15+20,pady=20-6,ipady=6)
                e5.grid(row=5,column=1,padx=15+20,pady=20-6,ipady=6)
                e6.grid(row=1,column=3,padx=15+20,pady=20-6,ipady=6)
                e7.grid(row=2,column=3,padx=15+20,pady=20-6,ipady=6)
                e8.grid(row=3,column=3,padx=15+20,pady=20-6,ipady=6)
                e9.grid(row=4,column=3,padx=15+20,pady=20-6,ipady=6)  
                Button(t,text='CHECK ANOTHER\nMEDICAL STATUS',command=calc,bg='white',fg='black',bd=2,font='Algerian 15 bold').place(x=650,y=450)
                LK=Label(t,text='MORE OPTIONS',bg='white',fg='black',bd=2,font='Algerian 15 bold')
                def opensign(event):
                        os.system('py p4.py')
                L=Label(t,text='Signout',bg='white',command=opensign,fg='white',font='Algerian 15 bold')
                    
                l1=Label(t,text='Exit',bg='white',fg='white',font='Algerian 15 bold')
                    
                L.place(x=1350,y=20)
                l1.place(x=1470,y=20)
                def opensign(event):
                        os.system('py p5.py')
                        t.destroy()

                def fin(event):
                    LK.configure(fg='white')
                    L.configure(fg='black')
                    l1.configure(fg='black')
                    
                def de(event):
                        t.destroy()
                l1.bind('<Button-1>',de)
                L.bind('<Button-1>',opensign)
                LK.place(x=1380,y=0)
                LK.bind('<Enter>',fin)
        def male():
                bmi,bp,rbc,wbc,plate,hp,uric,chol,pul=0,'','','','','','','',''
                bmi=float(e1.get())/pow((float(e2.get())),2)
                print(bmi)

                if 0<int(e3.get())<=60 or 0<int(e4.get())<=80:
                        bp='low'
                elif 60<int(e3.get())<=80 or 80<int(e4.get())<=120:
                        bp='normal'
                elif 80<int(e3.get())<=200 or 120<int(e4.get())<=190:
                        bp='high'
                print(bp)

                if 4.5<=float(e6.get())<=5.5:
                        rbc='normal'
                elif(0<float(e6.get())<4.5):
                        rbc='low'
                elif(5.5<float(e6.get())):
                        rbc='High'
                print(rbc)

                if 5000<=float(e7.get())<=10000:
                        wbc='normal'
                elif(0<float(e7.get())<5000):
                        wbc='low'
                elif(10000<float(e7.get())):
                        wbc='High'
                print(wbc)

                if 1.4<=float(e8.get())<=4.0:
                        plate='normal'
                elif(0<float(e8.get())<1.4):
                        plate='low'
                elif(4.0<float(e8.get())):
                        plate='High'
                print(plate)

                
                if 13.5<=float(e9.get())<=17.5:
                        hb='normal'
                elif(0<float(e9.get())<13.5):
                        hb='low'
                elif(17.5<float(e9.get())):
                        hb='High'
                print(hb)

                if 3.4<=float(e10.get())<=7.0:
                        uric='normal'
                elif(0<float(e10.get())<3.4):
                        uric='low'
                elif(7.0<float(e10.get())):
                        uric='High'
                print(uric)

                if 0<=float(e11.get())<=100:
                        chol='low'
                elif(100<float(e11.get())<=139):
                        chol='normal'
                elif(139<float(e11.get())):
                        chol='High'
                print(chol)

                if 0<=float(e5.get())<60:
                        pul='low'
                elif(60<=float(e5.get())<=100):
                        pul='normal'
                elif(100<float(e5.get())):
                        pul='High'
                print(pul)
                repo(bmi,bp,pul,rbc,wbc,plate,hb,uric,chol)

        def female():
                bmi,bp,rbc,wbc,plate,hp,uric,chol,pul=0,'','','','','','','',''
                bmi=float(e1.get())/pow((float(e2.get())),2)
                print(bmi)

                if 0<int(e3.get())<=60 or 0<int(e4.get())<=80:
                        bp='low'
                elif 60<int(e3.get())<=80 or 80<int(e4.get())<=120:
                        bp='normal'
                elif 80<int(e3.get())<=200 or 120<int(e4.get())<=190:
                        bp='high'
                print(bp)

                if 4.0<=float(e6.get())<=5.0:
                        rbc='normal'
                elif(0<float(e6.get())<4.0):
                        rbc='low'
                elif(5.0<float(e6.get())):
                        rbc='High'
                print(rbc)

                if 5000<=float(e7.get())<=10000:
                        wbc='normal'
                elif(0<float(e7.get())<5000):
                        wbc='low'
                elif(10000<float(e7.get())):
                        wbc='High'
                print(wbc)

                if 1.4<=float(e8.get())<=4.0:
                        plate='normal'
                elif(0<float(e8.get())<1.4):
                        plate='low'
                elif(4.0<float(e8.get())):
                        plate='High'
                print(plate)

                
                if 12.0<=float(e9.get())<=15.5:
                        hb='normal'
                elif(0<float(e9.get())<12.0):
                        hb='low'
                elif(15.5<float(e9.get())):
                        hb='High'
                print(hb)

                if 2.4<=float(e10.get())<=6.0:
                        uric='normal'
                elif(0<float(e10.get())<2.4):
                        uric='low'
                elif(6.0<float(e10.get())):
                        uric='High'
                print(uric)

                if 0<=float(e11.get())<=100:
                        chol='low'
                elif(100<float(e11.get())<=139):
                        chol='normal'
                elif(139<float(e11.get())):
                        chol='High'
                print(chol)

                if 0<=float(e5.get())<60:
                        pul='low'
                elif(60<=float(e5.get())<=100):
                        pul='normal'
                elif(100<float(e5.get())):
                        pul='High'
                print(pul)
                repo(bmi,bp,pul,rbc,wbc,plate,hb,uric,chol)
        def fgt():
                c1=c.get()
                if c1=='MALE':
                        male()
                if c1=='FEMALE':
                        female()
        Button(Form3,text='GENERATE REPORT',bg='white',fg='black',command=fgt,bd=2,font='Algerian 25 bold').grid(row=7,column=1)
        e1.insert(0,'WEIGHT (IN KG)')
        e2.insert(0,'HEIGHT (in METRES)')
        e3.insert(0,'BP LOW ')
        e4.insert(0,'BP HIGH')
        e5.insert(0,'PULSE RATE PER MINUTE')
        e6.insert(0,'RBC COUNT (IN 10^6/ml)')
        e7.insert(0,'WBC COUNT(in /ml)')
        e8.insert(0,'PLATELETS(in 10^5/ml)')
        e9.insert(0,'HB (gram per deciliter)')
        e10.insert(0,'URIC ACID(mg/dl)')
        e11.insert(0,'CHOLESTROL(in md/dl)')
        
calc()     
t.mainloop()

