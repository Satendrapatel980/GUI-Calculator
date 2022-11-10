from tkinter import *
import tkinter.ttk
 
first = Tk()
 
first.title("Welcome To Fitness calculator")
 
first.geometry('700x700')

first.config(bg='chartreuse1')


lbl1=Label(first, text="Fitness Calculator ",bg="red",fg="white")
lbl1.place(x=5,y=32)
lbl1.config(font=("Bebas Neue", 50))
lb01=Label(first,text="We Measure Your Fitness!",bg="red",fg="white")
lb01.place(x=5,y=115)
lb01.config(font=("Bebas Neue",25))

tkinter.ttk.Separator(first, orient=VERTICAL).place(x=50,y=1)

lb12=Label(first,text=" \"If we could give every individual the right amount of nourishment and exercise,",bg="chartreuse1",fg="red")
lb12.place(x=640,y=315)
lb12.config(font=("Aileron", 15))
lb13=Label(first,text=" not too little and not too much,",bg="chartreuse1",fg="white")
lb13.place(x=645,y=340)
lb13.config(font=("Aileron", 15))
lb14=Label(first,text=" we would have found the safest way to health.\"",bg="chartreuse1",fg="black")
lb14.place(x=645,y=365)
lb14.config(font=("Aileron",15))
lb1h=Label(first,text="------------------------------------------------------------------------------------------------------------------------------------------------------",bg="red",fg="white")
lb1h.place(x=5,y=620)
lb1h.config(font=("Bebas Neue",20))
           

Name=StringVar()
Age=IntVar()
Weight=IntVar()
Height=IntVar()
BPL=StringVar()
BPH=StringVar()
PsRate=StringVar()
RBC=StringVar()
WBC=StringVar()
Plate=StringVar()
HB=StringVar()
UA=StringVar()
Chol=StringVar()
#second interface
def proceed():
    window=Tk()
    window.title("Home | Fitness Calculator")

    window.geometry('700x700')


    """background_image=window.PhotoImage("fit.jpg")
    background_label = window.Label(parent, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)"""






    frame=Frame(window,)                     #windows,frame
    frame.grid(row=0, column=10,sticky="N")
    #label
    #label.grid
    #image=Image.open("fit.jpg")
    #tkpi=ImageTk.PhotoImage("fit.jpg")
    window.configure(background="yellow")  #Window theme
    """mb =  Menubutton ( window, text = "GF") 
    mb.grid() 
    mb.menu  =  Menu ( mb, tearoff = 0 ) 
    mb["menu"]  =  mb.menu 
    cVar  = IntVar() 
    aVar = IntVar() 
    mb.menu.add_command ( label ='Contact', variable = cVar ) 
    mb.menu.add_command( label = 'About', variable = aVar ) 
    mb.grid() """

    menu = Menu(window) 
    window.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='New') 
    filemenu.add_command(label='Open...') 
    filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=window.destroy) 
    helpmenu = Menu(menu) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About')

   # lb1h=Label(window,text="-------------------------------------------------------------------",bg="red",fg="white")
    #lb1h.grid(row=3)
    #lb1h.config(font=("Bebas Neue",20))



    lname=Label(window, text="Name", font="Helvetica" "16",bg="yellow")  #Name
    lname.grid(row=4,column=1)
    ename=Entry(window,cursor="arrow",textvariable=Name, bd=2)
    ename.grid(row=4, column=2)

    """wage=Label(window,text="Age",font="Helvetica" "16",bg="yellow")
    wage.grid(row=1,column=7)
    w = Scale(window, from_=0, to=100,orient=HORIZONTAL) 
    w.grid(row=1,column=9) """
     

    lage=Label(window, text="Age", font="Helvetica" "16",bg="yellow") #Age
    lage.grid(row=4,column=5)
    eage=Entry(window, cursor="arrow",textvariable=Age, bd=2)
    eage.grid(row=4, column=6)

    Gender=Label(window,text="Gender",font="Helvetica" "16",bg="yellow") #gender
    Gender.grid(row=5,column=1)
    G1=Radiobutton(window,text="Male", cursor="dotbox", font="16",bg="yellow",value=1)
    G2=Radiobutton(window,text="Female",cursor="dotbox",font="16",bg="yellow",value=2)
    G1.grid(row=5,column=2)
    G2.grid(row=5, column=6)

    lweight=Label(window,text="Weight (kg)",font="Helvetica" "16",bg="yellow")   #weight
    lweight.grid(row=6,column=1)
    eweight=Entry(window,cursor="arrow",textvariable=Weight,bd=1.5)
    eweight.grid(row=6,column=2)

    lheight=Label(window,text="Height (cm)",font="Helvetica" "16",bg="yellow")  #height
    lheight.grid(row=7,column=1)
    eheight=Entry(window,cursor="arrow",textvariable=Height,bd=1.5)
    eheight.grid(row=7,column=2)

    lbpl=Label(window,text="BP Low (mm)",font="Helvetica" "16",bg="yellow") #Low_BloodPressure
    lbpl.grid(row=8,column=1)
    ebpl=Entry(window,cursor="arrow",textvariable=BPL,bd=1.5)
    ebpl.grid(row=8,column=2)

    lbph=Label(window,text="BP High (mm)",font="Helvetica" "16",bg="yellow") #High_BloodPressure
    lbph.grid(row=9,column=1)
    ebph=Entry(window,cursor="arrow",textvariable=BPH,bd=1.5)
    ebph.grid(row=9,column=2)

    lpulse=Label(window,text="Pulse Rate (bpm)",font="Helvetica" "16",bg="yellow") #PulseRate
    lpulse.grid(row=10,column=1)
    epulse=Entry(window,cursor="arrow",textvariable=PsRate,bd=1.5)
    epulse.grid(row=10,column=2)

    lrbc=Label(window,text="RBC Count (cells/lit",font="Helvetica" "16",bg="yellow") #RBC_COUNT
    lrbc.grid(row=11,column=1)
    erbc=Entry(window,cursor="arrow",textvariable=RBC,bd=1.5)
    erbc.grid(row=11,column=2)

    lwbc=Label(window,text="WBC Count (cells/lit)",font="Helvetica" "16",bg="yellow") #WBC_Count
    lwbc.grid(row=12,column=1)
    ewbc=Entry(window,cursor="arrow",textvariable=WBC,bd=1.5)
    ewbc.grid(row=12,column=2)

    lplt=Label(window,text="Platelets",font="Helvetica" "16",bg="yellow") #platelets
    lplt.grid(row=13,column=1)
    eplt=Entry(window,cursor="arrow",textvariable=Plate,bd=1.5)
    eplt.grid(row=13,column=2)


    lHB=Label(window,text="Hemoglobin (g/dl)",font="Helvetica" "16",bg="yellow") #HB
    lHB.grid(row=14,column=1)
    eHB=Entry(window,cursor="arrow",textvariable=HB,bd=1.5)
    eHB.grid(row=14,column=2)


    luric=Label(window,text="Uric Acid (mg/l)",font="Helvetica" "16",bg="yellow") #uric_acid
    luric.grid(row=15,column=1)   
    euric=Entry(window,cursor="arrow",textvariable=UA,bd=1.5)
    euric.grid(row=15,column=2)

    lcol=Label(window,text="Cholesterol (mg/dl)",font="Helvetica" "16",bg="yellow") #Cholesterol
    lcol.grid(row=16,column=1)
    ecol=Entry(window,cursor="arrow",textvariable=Chol,bd=1.5)
    ecol.grid(row=16,column=2)
   # def multiply(*args):
        
    #    try:
            
        
     #       product.set(round(float(num1.get())*float(num2.get()),2))
      #      newvariable.set(round(product.get()*2),2)
      #except ValueError:
            
       #     pass"""

    def GetDetails():
        window2=Tk()
        menu = Menu(window2) 
        window2.config(menu=menu) 
        filemenu = Menu(menu) 
        menu.add_cascade(label='File', menu=filemenu) 
       # filemenu.add_command(label='New') 
       # filemenu.add_command(label='Open...') 
        filemenu.add_separator() 
        filemenu.add_command(label='Exit', command=window2.destroy) 
        helpmenu = Menu(menu) 
        menu.add_cascade(label='Help', menu=helpmenu) 
        helpmenu.add_command(label='About') 
        
        window2.title("User Fitness Report")
        window2.configure(background="blanchedalmond")
        
        l1=Label(window2,fg="black",bg="blanchedalmond",text="Name                    : " +Name.get())
        l1.grid(row=20,column=18)
        l2=Label(window2,fg="black",bg="blanchedalmond",text="Age                     : " +str(Age.get()))
        l2.grid(row=21,column=18)
        
        l3=Label(window2,fg="black",bg="blanchedalmond",text="Weight(kg)            : " +str(Weight.get()))   #output commands
        l3.grid(row=23,column=18)
        l4=Label(window2,fg="black",bg="blanchedalmond",text="Height(cm)           : " +str(Height.get()))
        l4.grid(row=24,column=18)
        l5=Label(window2,fg="black",bg="blanchedalmond",text="BP Low(mm)          : " +BPL.get())
        l5.grid(row=25,column=18)
        l6=Label(window2,fg="black",bg="blanchedalmond",text="BP High(mm)         : " +BPH.get())
        l6.grid(row=26,column=18)
        l7=Label(window2,fg="black",bg="blanchedalmond",text="Pulse Rate(bpm)   : " +PsRate.get())
        l7.grid(row=27,column=18)
        l8=Label(window2,fg="black",bg="blanchedalmond",text="RBC Count(cells/lit) : " +RBC.get())
        l8.grid(row=28,column=18)
        l9=Label(window2,fg="black",bg="blanchedalmond",text="WBC Count(cells/lit) : " +WBC.get())
        l9.grid(row=29,column=18)
        l10=Label(window2,fg="black",bg="blanchedalmond",text="Platelets           : " +Plate.get())
        l10.grid(row=30,column=18)
        l11=Label(window2,fg="black",bg="blanchedalmond",text="Hemoglobin(g/dl)   : " +HB.get())
        l11.grid(row=31,column=18)
        l12=Label(window2,fg="black",bg="blanchedalmond",text="Uric Acid(mg/l)     : " +UA.get())
        l12.grid(row=32,column=18)
        l13=Label(window2,fg="black",bg="blanchedalmond",text="Cholesterol(mg/dl) : " +Chol.get())
        l13.grid(row=33,column=18)
        bm1=Label(window2,fg="black",bg="blanchedalmond",text="Body Mass Index (B.M.I)       : " + str( (Weight.get())/(Height.get())**2))
        bm1.grid(row=35,column=18)
                  
       # Exit=Button(window2,text="Exit",command=window2.destroy)
        #Exit.grid(row=40,column=30)
        Print=Button(window2,text="Print Report")
        Print.grid(row=40,column=35)
        
            
    generate=Button(window,text="Generate Report",fg="White",bg="black",borderwidth=3,command=GetDetails)
    generate.grid(row=20,column=20)                                                                              #initialize generate button
    window.mainloop()
    
 
btn = Button(first, text="Measure health",height='1',command=proceed,borderwidth=2)
 
btn.place(x=999, y=500)
btn.config(font=(" Baufra",15), fg='gold',bg="purple")
 
first.mainloop()
