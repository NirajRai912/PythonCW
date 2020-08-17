from tkinter import *
import math, random
from tkinter import messagebox 

class online:
    def __init__(self,gui):
        self.gui=gui
        self.gui.geometry("1920x1080+0+0")
        self.gui.title("Menu and billing")
        bg_color="#C67CFF"
        title = Label(self.gui,text="RESTRO",bd=10,bg="#C67CFF",font=("Arial",30,"bold"),relief=GROOVE,fg="white",pady=2).pack(fill=X) 
        ##############---Variables---##############
        #Hot drinks
        self.coffee = IntVar()
        self.milktea = IntVar()
        self.hotchoco = IntVar()
        self.black_tea = IntVar()
        self.green_tea = IntVar()

        #Cold drinks
        self.pepsi = IntVar()
        self.coke = IntVar()
        self.choco_shakes = IntVar()
        self.lassi = IntVar()
        self.lemonade = IntVar()

        #Hard drinks
        self.JD = IntVar()
        self.OD = IntVar()
        self.BL = IntVar()
        self.mt8848 = IntVar()
        self.vodka = IntVar()

        #total
        self.gtot=StringVar()
        self.tot=StringVar()
        self.tax=StringVar()
        self.dis=StringVar()
        self.bill=StringVar()
        a=random.randint(100,9999)
        self.bill.set(str(a))

        #############---bottom---############
        bot=LabelFrame(self.gui,bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#C67CFF")
        bot.place(x=0,y=710,relwidth=1,height=75)
       
        tot=Label(bot,text="Total Price",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=12)
        tot_box=Entry(bot,width=16,textvariable=self.tot,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        tot_box.place(x=150,y=9)

        tax=Label(bot,text="Total Tax",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=120,pady=1)
        tax_box=Entry(bot,width=16,textvariable=self.tax,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        tax_box.place(x=400,y=9)

        dis=Label(bot,text="Total discount",bg="#C67CFF",fg="white",font=("times new roman",18,"bold")).grid(row=0,column=3,padx=30,pady=1)
        dis_box=Entry(bot,width=16,textvariable=self.dis,font=("arial",10,"bold"),bd=5,relief=SUNKEN)
        dis_box.place(x=700,y=9)

        about_box=Button(bot,width=16,text="about us",font=("arial",10,"bold"),bd=5,relief=GROOVE,command=self.about_us)
        about_box.place(x=850,y=9)

    def about_us(self):
        f = open("app.txt", "w")
        f.write("This app is in first phase.\n Final phase is yet to come")
        f.close()

        #############---Menu---##############

        B1=LabelFrame(self.gui,text="Hot Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#86b9f0")
        B1.place(x=0,y=80,width=900,height=200)

        coffee=PhotoImage(file="cofee.png")
        bla_=Button(B1,image=coffee)
        bla_.pack()
        bla_.place(height=100,width=120,x=50,y=5)

        tea=PhotoImage(file='tea.png')
        bla_=Button(B1,image=tea)
        bla_.pack()
        bla_.place(height=100,width=120,x=215,y=5)

        black=PhotoImage(file='black.png')
        gre_=Button(B1,image=black)
        gre_.pack()
        gre_.place(height=100,width=120,x=380,y=5)

        green = PhotoImage(file='green.png')
        hot_=Button(B1,image=green)
        hot_.pack()
        hot_.place(height=100,width=120,x=545,y=5)

        hot=PhotoImage(file='hot chocolate.png')
        tea_=Button(B1,image=hot)
        tea_.pack()
        tea_.place(height=100,width=120,x=705,y=5)

        coffee=Entry(B1,width=5,textvariable=self.coffee,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        coffee.place(x=80,y=120)

        milktea=Entry(B1,width=5,textvariable=self.milktea,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        milktea.place(x=240,y=120)

        hotchoco=Entry(B1,width=5,textvariable=self.hotchoco,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        hotchoco.place(x=400,y=120)

        black_tea=Entry(B1,width=5,textvariable=self.black_tea,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        black_tea.place(x=560,y=120)

        green_tea=Entry(B1,width=5,textvariable=self.green_tea,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        green_tea.place(x=720,y=120)

        m2=LabelFrame(self.gui,text="Cold Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#fc7cf6")
        m2.place(x=0,y=290,width=900,height=200)

        pepsi=PhotoImage(file='pepsi.png')
        pep_=Button(m2,image=pepsi)
        pep_.pack()
        pep_.place(height=100,width=120,x=50,y=5)

        coke=PhotoImage(file='coke.png')
        cok_=Button(m2,image=coke)
        cok_.pack()
        cok_.place(height=100,width=120,x=215,y=5)

        choco=PhotoImage(file='choco shakes.png')
        cho_=Button(m2,image=choco)
        cho_.pack()
        cho_.place(height=100,width=120,x=380,y=5)

        lassi=PhotoImage(file='lassi.png')
        las_=Button(m2,image=lassi)
        las_.pack()
        las_.place(height=100,width=120,x=545,y=5)

        lemonade=PhotoImage(file='lemonade.png')
        lem_=Button(m2,image=lemonade)
        lem_.pack()
        lem_.place(height=100,width=120,x=705,y=5)

        pepsi=Entry(m2,width=5,textvariable=self.pepsi,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        pepsi.place(x=80,y=120)

        coke=Entry(m2,width=5,textvariable=self.coke,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        coke.place(x=240,y=120)

        lassi=Entry(m2,width=5,textvariable=self.lassi,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        lassi.place(x=400,y=120)

        choco_shakes=Entry(m2,width=5,textvariable=self.choco_shakes,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        choco_shakes.place(x=560,y=120)

        lemonade=Entry(m2,width=5,textvariable=self.lemonade,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        lemonade.place(x=720,y=120)
        
        d3=LabelFrame(self.gui,text="Hard Drinks",bd=10,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#fc7c7c")
        d3.place(x=0,y=500,width=900,height=200)

        JD=PhotoImage(file='JD.png')
        JD_=Button(d3,image=JD)
        JD_.pack()
        JD_.place(height=100,width=120,x=50,y=5)

        OD=PhotoImage(file='OD.png')
        OD_=Button(d3,image=OD)
        OD_.pack()
        OD_.place(height=100,width=120,x=215,y=5)

        mt=PhotoImage(file='mt8848.png')
        mt_=Button(d3,image=mt)
        mt_.pack()
        mt_.place(height=100,width=120,x=380,y=5)

        BL=PhotoImage(file='BL.png')
        BL_=Button(d3,image=BL)
        BL_.pack()
        BL_.place(height=100,width=120,x=545,y=5)

        vod=PhotoImage(file='vodka.png')
        vod_=Button(d3,image=vod)
        vod_.pack()
        vod_.place(height=100,width=120,x=705,y=5)

        JD=Entry(d3,width=5,textvariable=self.JD,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        JD.place(x=80,y=120)

        OD=Entry(d3,width=5,textvariable=self.OD,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        OD.place(x=240,y=120)

        BL=Entry(d3,width=5,textvariable=self.BL,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        BL.place(x=400,y=120)

        mt8848=Entry(d3,width=5,textvariable=self.mt8848,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        mt8848.place(x=560,y=120)

        vodka=Entry(d3,width=5,textvariable=self.vodka,font=("Arial",14,"bold"),bd=5,relief=SUNKEN)
        vodka.place(x=720,y=120)
        
        
        ##############---Calculation---############
        cal=LabelFrame(self.gui,bd=10,relief=GROOVE,bg="gold")
        cal.place(x=915,y=500,width=600,height=200)

        cal_btn=Frame(cal,bd=10,relief=GROOVE)
        cal_btn.place(x=7,width=567,height=180)
        
        gen_bill1=Button(cal_btn,command=lambda:[self.gtotal(),self.bill_area()],text="Generate Bill",bg="#299AF4",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10)
        gen_bill2=Button(cal_btn,command=self.reset,text="Reset",bg="#80ED70",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=10,pady=12)
        gen_bill3=Button(cal_btn,command=self.Exit,text="Exit",bg="#F44329",bd=5,fg="white",pady=20,width=12,height=3,font=("times new roman",16,"bold")).grid(row=0,column=2,padx=10,pady=12)
        self.gtotal()
        ##############---Billing---#############
        bill=Frame(self.gui,bd=10,relief=GROOVE)
        bill.place(x=915,y=80,width=600,height=410)
        bill_title=Label(bill,text="Billing",font=("times new roman",12,"bold"),bd=6,relief=GROOVE).pack(fill=X)
        scroll=Scrollbar(bill,orient=VERTICAL)
        self.textarea=Text(bill,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        scroll.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        self.welcome_area()
    def gtotal(self):
        self.a_p=self.coffee.get()*40
        self.l_p=self.milktea.get()*40
        self.cap_p=self.hotchoco.get()*40
        self.b_p=self.black_tea.get()*40
        self.g_p=self.green_tea.get()*40
        self.p_p=self.pepsi.get()*40
        self.co_p=self.coke.get()*40
        self.ch_p=self.choco_shakes.get()*40
        self.le_p=self.lemonade.get()*40
        self.la_p=self.lassi.get()*40
        self.J_p=self.JD.get()*40
        self.O_p=self.OD.get()*40
        self.BL_p=self.BL.get()*40
        self.m_p=self.mt8848.get()*40
        self.v_p=self.vodka.get()*40
        self.grand_total=float(
                             self.a_p+
                             self.l_p+
                             self.cap_p+
                             self.b_p+
                             self.g_p+
                             self.p_p+
                             self.co_p+
                             self.ch_p+
                             self.le_p+
                             self.la_p+
                             self.J_p+                                 
                             self.O_p+
                             self.BL_p+
                             self.m_p+
                             self.v_p
                             )
        try:
            self.tot.set("Rs."+str(self.grand_total))
        except:
            self.tot.set("Rs." + 0)

        self.t_tax=round((self.grand_total*0.08),2)
        self.tax.set("Rs."+str(self.t_tax))
        self.d_dis=round((self.grand_total*0.01),2)
        self.dis.set("Rs."+str(self.d_dis))
        self.gtot=round(float(self.grand_total + self.t_tax - self.d_dis),2)
    
    def welcome_area(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t                   Welcome to Restro")
        self.textarea.insert(END,f"\n\n\tBill number: {self.bill.get()}")
        self.textarea.insert(END,f"\n\n*********************************************************************")
        self.textarea.insert(END,f"\n Drinks\t\t\t\tQuantity\t\t\t      Price")
        self.textarea.insert(END,"\n*********************************************************************")

    def bill_area(self):
        self.welcome_area()
        if self.coffee.get()!=0:
            self.textarea.insert(END,f"\n Coffee\t\t\t\t{self.coffee.get()}\t\t\t      {self.a_p}")
        if self.milktea.get()!=0:
            self.textarea.insert(END,f"\n Milk Tea\t\t\t\t{self.milktea.get()}\t\t\t      {self.l_p}")
        if self.hotchoco.get()!=0:
            self.textarea.insert(END,f"\n Hot Chocolate\t\t\t\t{self.hotchoco.get()}\t\t\t      {self.cap_p}")
        if self.black_tea.get()!=0:
            self.textarea.insert(END,f"\n Black Tea\t\t\t\t{self.black_tea.get()}\t\t\t      {self.b_p}")    
        if self.green_tea.get()!=0:
            self.textarea.insert(END,f"\n Green Tea\t\t\t\t{self.green_tea.get()}\t\t\t      {self.g_p}")
        if self.pepsi.get()!=0:
            self.textarea.insert(END,f"\n Pepsi\t\t\t\t{self.pepsi.get()}\t\t\t      {self.p_p}")
        if self.coke.get()!=0:
            self.textarea.insert(END,f"\n Coke\t\t\t\t{self.coke.get()}\t\t\t      {self.co_p}")
        if self.choco_shakes.get()!=0:
            self.textarea.insert(END,f"\n Choco Shakes\t\t\t\t{self.choco_shakes.get()}\t\t\t      {self.ch_p}")
        if self.lemonade.get()!=0:
            self.textarea.insert(END,f"\n Lemonade\t\t\t\t{self.lemonade.get()}\t\t\t      {self.le_p}")
        if self.lassi.get()!=0:
            self.textarea.insert(END,f"\n Lassi\t\t\t\t{self.lassi.get()}\t\t\t      {self.la_p}")
        if self.JD.get()!=0:
            self.textarea.insert(END,f"\n Jack Daniels\t\t\t\t{self.JD.get()}\t\t\t      {self.J_p}")
        if self.OD.get()!=0:
            self.textarea.insert(END,f"\n Old Durbar\t\t\t\t{self.OD.get()}\t\t\t      {self.O_p}")
        if self.mt8848.get()!=0:
            self.textarea.insert(END,f"\n Mt 8848\t\t\t\t{self.mt8848.get()}\t\t\t      {self.m_p}")
        if self.BL.get()!=0:
            self.textarea.insert(END,f"\n Black Label\t\t\t\t{self.BL.get()}\t\t\t      {self.BL_p}")
        if self.vodka.get()!=0:
            self.textarea.insert(END,f"\n Vodka\t\t\t\t{self.vodka.get()}\t\t\t      {self.v_p}")
        self.textarea.insert(END,f"\n\n---------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Total Tax\t\t\t\t\t\t\t     {self.tax.get()}")
        self.textarea.insert(END,f"\n Total Discount\t\t\t\t\t\t\t     {self.dis.get()}")
        self.textarea.insert(END,"\n---------------------------------------------------------------------")
        self.textarea.insert(END,f"\n Grand Total\t\t\t\t\t\t\t    Rs. {self.gtot}")
    def reset(self):
         #Hot drinks
        self.coffee.set(0)
        self.milktea.set(0)
        self.hotchoco.set(0)
        self.black_tea.set(0) 
        self.green_tea.set(0) 

        #Cold drinks
        self.pepsi.set(0)
        self.coke.set(0) 
        self.choco_shakes.set(0) 
        self.lassi.set(0) 
        self.lemonade.set(0) 

        #Hard drinks
        self.JD.set(0) 
        self.OD.set(0) 
        self.BL.set(0) 
        self.mt8848.set(0) 
        self.vodka.set(0)

        #total
        self.tot.set("")
        self.tax.set("")
        self.dis.set("")
        self.bill.set("")
        a=random.randint(100,9999)
        self.bill.set(str(a))
        self.welcome_area()
               
    def Exit(self):
        ex=messagebox.askyesno("Exit","Do you want to exit?")
        if ex>0:
            self.gui.destroy()
gui = Tk()
obj = online(gui)
gui.mainloop() 