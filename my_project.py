from tkinter import *
from PIL import ImageTk, Image



win=Tk()
win.title(" CGPA CALCULATOR")
win.geometry("1000x600")
win.resizable(0, 0)
win.configure(bg='black')
Label(win, text= "LPU CGPA CALCULATOR",font=('Comic Sans MS',20,'bold'),bg="black", fg= "green").pack()

        #background image
#bg_frame = Image.open('C:\\Users\\lenovo\\Downloads\\pytho.jpeg')
#photo = ImageTk.PhotoImage(bg_frame)
#bg_panel = Label(win, image=photo)
#bg_panel.image = photo
#bg_panel.pack(fill='both', expand='yes')



#name
Label1=Label(win,text="NAME",bg='#808080')
Label1.place(x=62,y=63)

name=StringVar()
textbox1=Entry(win,textvariable=name,width=25,bd=5)
textbox1.place(x=120,y=60)


#reg num
Label2=Label(win,text="REG NUM",bg='#808080')
Label2.place(x=50,y=103)

reg=IntVar()
textbox2=Entry(win,textvariable=reg,width=25,bd=5)
textbox2.place(x=120,y=100)



#semester
Label3=Label(win,text="1st SEMESTER",font=("Helvetica",16),bg='#808080')
Label3.place(x=450,y=60)

Label4=Label(win,text="2nd SEMESTER",font=("Helvetica",16),bg='#808080')
Label4.place(x=750,y=60)

#header

information=Label(win,text="To Know Grade Points:",bg='#FFFFFF')
information.place(x=50,y=150)

def click():
    ck=Text(win,relief=GROOVE,state=NORMAL,bd=3,width=30,height=20)
    ck.insert(END,"\n O  :Grade Point-10\n\n A+ :Grade Point-9\n\n A  :Grade Point-8\n\n B+ :Grade Point-7\n\n B  :Grade Point-6\n\n C+ :Grade Point-5\n\n C  :Grade Point-4\n\n E  :Reappear- Grade Point-0\n\n F  :Fail- Grade Point-0")
    ck.place(x=50,y=200)
    ck.configure(state=DISABLED) #user wont be able to modify content
    


ck=Button(win,text="Click Me",relief=RIDGE,bd=5,state=ACTIVE,command=click,bg='#FFA500',fg='white',activebackground='#ADD8E6')
ck.place(x=200,y=150)

#footer

def reset():
    rt=Text(win,relief=GROOVE,state=NORMAL,bd=3,width=30,height=20)
    rt.insert(END,"\n All Values are back to\n default values.")
    rt.place(x=50,y=200)

#SEM1

    #grades
    s1s1grade1.set('')
    s1s2grade2.set('')
    s1s3grade3.set('')
    s1s4grade4.set('')
    s1s5grade5.set('')
    s1s6grade6.set('')
    #credits
    s1s1credit1.set(0)
    s1s2credit2.set(0)
    s1s3credit3.set(0)
    s1s4credit4.set(0)
    s1s5credit5.set(0)
    s1s6credit6.set(0)
    tgpamark1=0

#SEM2

    #grades
    s2s1grade1.set('')
    s2s2grade2.set('')
    s2s3grade3.set('')
    s2s4grade4.set('')
    s2s5grade5.set('')
    s2s6grade6.set('')

    #credits
    s2s1credit1.set(0)
    s2s2credit2.set(0)
    s2s3credit3.set(0)
    s2s4credit4.set(0)
    s2s5credit5.set(0)
    s2s6credit6.set(0)

#------------------------------------------------------

    tgpamark2=0
    cgpamark=0
    
    

reset=Button(win,text="Reset",relief=RIDGE,bd=5,command=reset)
reset.place(x=120,y=550)

#sem1 TGPA


tgpa1=Label(win,text=0,bg="white",relief=GROOVE,bd=3,width=15)
tgpa1.place(x=480,y=450)



def caltgpa1():
    g1=list()
    g1=[s1s1grade1,s1s2grade2,s1s3grade3,s1s4grade4,s1s5grade5,s1s6grade6]
    

    for i in range(6):
        if  (g1[i].get()=='O' ) : g1[i]=10
        elif(g1[i].get()=='A+') : g1[i]=9
        elif(g1[i].get()=='A' ) : g1[i]=8
        elif(g1[i].get()=='B+') : g1[i]=7
        elif(g1[i].get()=='B' ) : g1[i]=6
        elif(g1[i].get()=='C+') : g1[i]=5
        elif(g1[i].get()=='C' ) : g1[i]=4
        elif(g1[i].get()=='E' ) : g1[i]=0
        elif(g1[i].get()=='F' ) : g1[i]=0
        elif(g1[i].get()==''  ) : g1[i]=0

    
            
            
            
    
    sum1=0
    c1=list()
    c1=[s1s1credit1,s1s2credit2,s1s3credit3,s1s4credit4,s1s5credit5,s1s6credit6]
    
    for i in range(6):
        sum1=sum1+int(c1[i].get())
        c1[i]=int(c1[i].get())

    if(sum1==0): sum1=1
    r1=list()
    for i in range(6): r1.insert(i,g1[i]*c1[i])
    


    sumresult1=sum(r1)
    
    global tgpamark1
    tgpamark1=round(float(sumresult1/sum1),2)
    
    tgpa1.config(text=round(float(sumresult1/sum1),2))



btgpa1=Button(win,text="Calculate TGPA",relief=RIDGE,bd=3,command=caltgpa1,state=ACTIVE,font=("Times New Roman",11))
btgpa1.place(x=350,y=448)

#sem2 TGPA



tgpa2=Label(win,text=0,bd=3,bg="white",relief=GROOVE,width=15)
tgpa2.place(x=800,y=450)

def caltgpa2():
    g2=list()
    g2=[s2s1grade1,s2s2grade2,s2s3grade3,s2s4grade4,s2s5grade5,s2s6grade6]
    

    for i in range(6):
        if  (g2[i].get()=='O' ) : g2[i]=10
        elif(g2[i].get()=='A+') : g2[i]=9
        elif(g2[i].get()=='A' ) : g2[i]=8
        elif(g2[i].get()=='B+') : g2[i]=7
        elif(g2[i].get()=='B' ) : g2[i]=6
        elif(g2[i].get()=='C+') : g2[i]=5
        elif(g2[i].get()=='C' ) : g2[i]=4
        elif(g2[i].get()=='E' ) : g2[i]=0
        elif(g2[i].get()=='F' ) : g2[i]=0
        elif(g2[i].get()==''  ) : g2[i]=0


            
    
    sum2=0
    c2=list()
    c2=[s2s1credit1,s2s2credit2,s2s3credit3,s2s4credit4,s2s5credit5,s2s6credit6]
    
    for i in range(6):
        sum2=sum2+int(c2[i].get())
        c2[i]=int(c2[i].get())
    if(sum2==0):
        sum2=1

    r2=list()
    for i in range(6):
        r2.insert(i,g2[i]*c2[i])
    

    sumresult2=sum(r2)

    global tgpamark2
    tgpamark2=round(float(sumresult2/sum2),2)
        
    tgpa2.config(text=round(float(sumresult2/sum2),2))



btgpa2=Button(win,text="Calculate TGPA",relief=RIDGE,bd=3,command=caltgpa2,state=ACTIVE,font=("Times New Roman",11))
btgpa2.place(x=670,y=448)


#CGPA


cgpaall=Label(win,text=0,bg="white",relief=GROOVE,bd=3,width=15)
cgpaall.place(x=620,y=500)

def cgpa():
    global cgpamark
    cgpamark=round(float((tgpamark1+tgpamark2)/2),2)
    cgpaall.config(text=round(float((tgpamark1+tgpamark2)/2),2))

    
cgpa1=Button(win,text="CGPA",relief=RIDGE,bd=5,command=cgpa,state=ACTIVE,font=("Times New Roman",11))
cgpa1.place(x=550,y=496)


#remarks

remarktxt=Label(win,text='',bg="white",relief=GROOVE,width=30,bd=3)
remarktxt.place(x=620,y=550)

def remark():
    if  (cgpamark>=8)              : remarktxt.config(text="VERY GOOD")
    elif(cgpamark>=7 and cgpamark<8): remarktxt.config(text="GOOD")
    elif(cgpamark>=5 and cgpamark<7): remarktxt.config(text="WORK HARDER")
    elif(cgpamark>=0 and cgpamark<5): remarktxt.config(text="VERY POOR")



remarks=Button(win,text="Remarks",relief=RIDGE,command=remark,bd=5,font=("Times New Roman",12))
remarks.place(x=535,y=550)

#DATABASE

import sqlite3

#insertDB
def fill():
    f=Text(win,relief=GROOVE,state=NORMAL,bd=3,width=30,height=20)
    
    if(s1s1grade1.get()=='' or s1s2grade2.get()=='' or s1s3grade3.get()=='' or s1s4grade4.get()=='' or s1s5grade5.get()=='' or s1s6grade6.get()=='' or s1s1credit1.get()=='0' or s1s2credit2.get()=='0' or s1s3credit3.get()=='0' or s1s4credit4.get()=='0' or s1s5credit5.get()=='0' or s1s6credit6.get()=='0'):
        f.insert(END,"\n  Please Fill in All details \n\tof Semester 1")
        f.place(x=50,y=200)

    if(s2s1grade1.get()=='' or s2s2grade2.get()=='' or s2s3grade3.get()=='' or s2s4grade4.get()=='' or s2s5grade5.get()=='' or s2s6grade6.get()=='' or s2s1credit1.get()=='0' or s2s2credit2.get()=='0' or s2s3credit3.get()=='0' or s2s4credit4.get()=='0' or s2s5credit5.get()=='0' or s2s6credit6.get()=='0'):
        f.insert(END,"\n  Please Fill in All details \n\tof Semester 2")
        f.place(x=50,y=200)

    if(s1s1grade1.get()!='' and s1s2grade2.get()!='' and s1s3grade3.get()!='' and s1s4grade4.get()!='' and s1s5grade5.get()!='' and s1s6grade6.get()!='' and s2s1grade1.get()!='' and s2s2grade2.get()!='' and s2s3grade3.get()!='' and s2s4grade4.get()!='' and s2s5grade5.get()!='' and s2s6grade6.get()!='' and s1s1credit1.get()!='0' and s1s2credit2.get()!='0' and s1s3credit3.get()!='0' and s1s4credit4.get()!='0' and s1s5credit5.get()!='0' and s1s6credit6.get()!='0' and s2s1credit1.get()!='0' and s2s2credit2.get()!='0' and s2s3credit3.get()!='0' and s2s4credit4.get()!='0' and s2s5credit5.get()!='0' and s2s6credit6.get()!='0'):

        f.insert(END,"\n  Successfully saved")
        f.place(x=50,y=200)
        f1=open("save.txt","a")
        f1.write("\n")
        f1.write("\t" + textbox1.get() + ":" + str(cgpamark))
        f1.close()
    
    
    
save=Button(win,text="Save",relief=RIDGE,bd=5,command=fill)
save.place(x=50,y=550)

#retrieveDB

def load():
    g=Text(win,relief=GROOVE,state=NORMAL,bd=3,width=30,height=20)
    f2=open("save.txt","r")
    g.insert(END,"\n      Already saved data\n")
    g.insert(END,f2.read())
    g.place(x=50,y=200)
    f2.close()
    
load=Button(win,text="Load",relief=RIDGE,bd=5,command=load)
load.place(x=190,y=550)


from tkinter.ttk import *

#sem1
subjects1=Label(win,text="Subjects",font=("Times New Roman",13))
subjects1.place(x=350,y=100)


#sem1 subjects

sem1sub1=Label(win,text="Subject 1",background='#FFFFFF')
sem1sub1.place(x=350,y=150)

sem1sub2=Label(win,text="Subject 2",background='#FFFFFF')
sem1sub2.place(x=350,y=200)

sem1sub3=Label(win,text="Subject 3",background='#FFFFFF')
sem1sub3.place(x=350,y=250)

sem1sub4=Label(win,text="Subject 4",background='#FFFFFF')
sem1sub4.place(x=350,y=300)

sem1sub5=Label(win,text="Subject 5",background='#FFFFFF')
sem1sub5.place(x=350,y=350)

sem1sub6=Label(win,text="Subject 6",background='#FFFFFF')
sem1sub6.place(x=350,y=400)



#sem1 grades

sem1grade=Label(win,text="Grades",font=("Times New Roman",13))
sem1grade.place(x=450,y=100)


s1g1=StringVar()
s1s1grade1=Combobox(win, textvariable=s1g1, state='readonly',width=7)
s1s1grade1['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s1grade1.place(x=450,y=150)

s1g2=StringVar()
s1s2grade2=Combobox(win, textvariable=s1g2, state='readonly',width=7)
s1s2grade2['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s2grade2.place(x=450,y=200)

s1g3=StringVar()
s1s3grade3=Combobox(win, textvariable=s1g3, state='readonly',width=7)
s1s3grade3['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s3grade3.place(x=450,y=250)

s1g4=StringVar()
s1s4grade4=Combobox(win, textvariable=s1g4, state='readonly',width=7)
s1s4grade4['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s4grade4.place(x=450,y=300)

s1g5=StringVar()
s1s5grade5=Combobox(win, textvariable=s1g5, state='readonly',width=7)
s1s5grade5['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s5grade5.place(x=450,y=350)

s1g6=StringVar()
s1s6grade6=Combobox(win, textvariable=s1g6, state='readonly',width=7)
s1s6grade6['values']=('O','A+','A','B+','B','C+','C','E','F')
s1s6grade6.place(x=450,y=400)

#sem1 credits

sem1credit=Label(win,text="Credits",font=("Times New Roman",13))
sem1credit.place(x=550,y=100)

s1c1=IntVar()
s1s1credit1=Combobox(win, textvariable=s1c1, state='readonly',width=7)
s1s1credit1['values']=(1,2,3,4)
s1s1credit1.place(x=550,y=150)

s1c2=IntVar()
s1s2credit2=Combobox(win, textvariable=s1c2, state='readonly',width=7)
s1s2credit2['values']=(1,2,3,4)
s1s2credit2.place(x=550,y=200)

s1c3=IntVar()
s1s3credit3=Combobox(win, textvariable=s1c3, state='readonly',width=7)
s1s3credit3['values']=(1,2,3,4)
s1s3credit3.place(x=550,y=250)

s1c4=IntVar()
s1s4credit4=Combobox(win, textvariable=s1c4, state='readonly',width=7)
s1s4credit4['values']=(1,2,3,4)
s1s4credit4.place(x=550,y=300)

s1c5=IntVar()
s1s5credit5=Combobox(win, textvariable=s1c5, state='readonly',width=7)
s1s5credit5['values']=(1,2,3,4)
s1s5credit5.place(x=550,y=350)

s1c6=IntVar()
s1s6credit6=Combobox(win, textvariable=s1c6, state='readonly',width=7)
s1s6credit6['values']=(1,2,3,4)
s1s6credit6.place(x=550,y=400)



#sem2

subjects2=Label(win,text="Subjects",font=("Times New Roman",13))
subjects2.place(x=670,y=100)

#sem2 subjects

sem2sub1=Label(win,text="Subject 1",background='#FFFFFF')
sem2sub1.place(x=670,y=150)

sem2sub2=Label(win,text="Subject 2",background='#FFFFFF')
sem2sub2.place(x=670,y=200)

sem2sub3=Label(win,text="Subject 3",background='#FFFFFF')
sem2sub3.place(x=670,y=250)

sem2sub4=Label(win,text="Subject 4",background='#FFFFFF')
sem2sub4.place(x=670,y=300)

sem2sub5=Label(win,text="Subject 5",background='#FFFFFF')
sem2sub5.place(x=670,y=350)

sem2sub6=Label(win,text="Subject 6",background='#FFFFFF')
sem2sub6.place(x=670,y=400)

#sem2 grades
sem2grade=Label(win,text="Grades",font=("Times New Roman",13))
sem2grade.place(x=770,y=100)

s2g1=StringVar()
s2s1grade1=Combobox(win, textvariable=s2g1, state='readonly',width=7)
s2s1grade1['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s1grade1.place(x=770,y=150)

s2g2=StringVar()
s2s2grade2=Combobox(win, textvariable=s2g2, state='readonly',width=7)
s2s2grade2['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s2grade2.place(x=770,y=200)


s2g3=StringVar()
s2s3grade3=Combobox(win, textvariable=s2g3, state='readonly',width=7)
s2s3grade3['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s3grade3.place(x=770,y=250)


s2g4=StringVar()
s2s4grade4=Combobox(win, textvariable=s2g4, state='readonly',width=7)
s2s4grade4['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s4grade4.place(x=770,y=300)


s2g5=StringVar()
s2s5grade5=Combobox(win, textvariable=s2g5, state='readonly',width=7)
s2s5grade5['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s5grade5.place(x=770,y=350)


s2g6=StringVar()
s2s6grade6=Combobox(win, textvariable=s2g6, state='readonly',width=7)
s2s6grade6['values']=('O','A+','A','B+','B','C+','C','E','F')
s2s6grade6.place(x=770,y=400)


#sem2 credits
sem2credit=Label(win,text="Credits",font=("Times New Roman",13))
sem2credit.place(x=870,y=100)

s2c1=IntVar()
s2s1credit1=Combobox(win, textvariable=s2c1, state='readonly',width=7)
s2s1credit1['values']=(1,2,3,4)
s2s1credit1.place(x=870,y=150)

s2c2=IntVar()
s2s2credit2=Combobox(win, textvariable=s2c2, state='readonly',width=7)
s2s2credit2['values']=(1,2,3,4)
s2s2credit2.place(x=870,y=200)

s2c3=IntVar()
s2s3credit3=Combobox(win, textvariable=s2c3, state='readonly',width=7)
s2s3credit3['values']=(1,2,3,4)
s2s3credit3.place(x=870,y=250)

s2c4=IntVar()
s2s4credit4=Combobox(win, textvariable=s2c4, state='readonly',width=7)
s2s4credit4['values']=(1,2,3,4)
s2s4credit4.place(x=870,y=300)

s2c5=IntVar()
s2s5credit5=Combobox(win, textvariable=s2c5, state='readonly',width=7)
s2s5credit5['values']=(1,2,3,4)
s2s5credit5.place(x=870,y=350)

s2c6=IntVar()
s2s6credit6=Combobox(win, textvariable=s2c6, state='readonly',width=7)
s2s6credit6['values']=(1,2,3,4)
s2s6credit6.place(x=870,y=400)



textbox1.focus()

win.mainloop()
