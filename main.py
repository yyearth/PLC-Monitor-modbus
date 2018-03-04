from tkinter import * 
from weather import *
from Modbus170409 import *
from tkinter import simpledialog
from tkinter import messagebox
import time
import sys   

class App(object):
    

    city=' '
    PLCflg = False

    def __init__(self,master):
        #super(Application, self).__init__()
        
        self.master = master

        self.frame1 = Frame(master,height=580,width=450) # green----------
        
        self.label = Label(self.frame1,text='当前地理位置：',font=('黑体', '12'))
        self.label.grid(row=0,column=0,columnspan=2,padx=10,pady=10,sticky=W)

        self.locstr = StringVar()
        self.locstr.set('xxx市')
        self.loclabel = Label(self.frame1,width=16,textvariable=self.locstr,font=('Helvetica', '22'))
        self.loclabel.grid(row=1,column=0,columnspan=3,padx=10,pady=10,sticky=E+W)

        self.changebutton = Button(self.frame1,text='更改',width=4,font=('黑体', '12'),command=self.changeCity)
        self.changebutton.grid(row=0,column=2,padx=10,pady=10,sticky=E+W)

        self.changebutton = Button(self.frame1,text='自动',width=9,font=('黑体', '12'),command=self.weatherInit)
        self.changebutton.grid(row=0,column=1,padx=10,pady=10,sticky=E)


        # self.weathertext = Text(self.frame1,height=2,width=3)
        # self.weathertext.insert(INSERT,'asd;flkskjdkfksldflsakdflkas')
        # self.weathertext.grid(row=1)

        self.weatherframe = LabelFrame(self.frame1,labelanchor='n',text='今日天气',font=('Helvetica', '16'))
                                                #,width=300,height=300
        self.weastr1 = StringVar()
        self.weastr1.set('--')
        self.weastr2 = StringVar()
        self.weastr2.set('-- --℃')
        self.weastr3 = StringVar()
        self.weastr3.set('-- --℃')
        self.weastr4 = StringVar()
        self.weastr4.set('--风')
        self.weastr5 = StringVar()
        self.weastr5.set('--级')
        self.weastr6 = StringVar()
        self.weastr6.set('--℃')

        self.wealabel1 = Label(self.weatherframe,textvariable=self.weastr1,font=('Helvetica', '16'))
        self.wealabel1.grid(row=0,column=0,padx=10,pady=10,sticky=E+W)
        self.wealabel2 = Label(self.weatherframe,textvariable=self.weastr2,font=('Helvetica', '16'))
        self.wealabel2.grid(row=1,column=0,padx=10,pady=10,sticky=E+W)
        self.wealabel3 = Label(self.weatherframe,textvariable=self.weastr3,font=('Helvetica', '16'))
        self.wealabel3.grid(row=2,column=0,padx=10,pady=10,sticky=E+W)
        self.wealabel4 = Label(self.weatherframe,textvariable=self.weastr4,font=('Helvetica', '16'))
        self.wealabel4.grid(row=3,column=0,padx=10,pady=10,sticky=E+W)
        self.wealabel5 = Label(self.weatherframe,textvariable=self.weastr5,font=('Helvetica', '16'))
        self.wealabel5.grid(row=4,column=0,padx=10,pady=10,sticky=E+W)
        self.wealabel6 = Label(self.weatherframe,width=9,textvariable=self.weastr6,font=('Helvetica', '40'))
        self.wealabel6.grid(row=0,column=1,rowspan=5,padx=5,pady=5,sticky=N+S+E+W)
        
        self.weatherframe.grid(row=3,column=0,columnspan=3,rowspan=5,padx=10,sticky=E+W)
        # self.weatherframe.grid_propagate(0)

        self.tomorrowframe = LabelFrame(self.frame1,labelanchor='n',text='明日天气',font=('Helvetica', '16'))
                                                #,width=300,height=300
        self.tomweastr1 = StringVar()
        self.tomweastr1.set('--')
        self.tomweastr2 = StringVar()
        self.tomweastr2.set('-- --℃')
        self.tomweastr3 = StringVar()
        self.tomweastr3.set('-- --℃')
        self.tomweastr4 = StringVar()
        self.tomweastr4.set('--风')
        self.tomweastr5 = StringVar()
        self.tomweastr5.set('---')
        # self.tomweastr6 = StringVar()
        # self.tomweastr6.set('16℃')

        self.wealabel1 = Label(self.tomorrowframe,width=4,textvariable=self.tomweastr1,font=('Helvetica', '16'))
        self.wealabel1.grid(row=0,column=0,padx=2,pady=10)
        self.wealabel2 = Label(self.tomorrowframe,width=8,textvariable=self.tomweastr2,font=('Helvetica', '16'))
        self.wealabel2.grid(row=0,column=1,padx=0,pady=10)
        self.wealabel3 = Label(self.tomorrowframe,width=8,textvariable=self.tomweastr3,font=('Helvetica', '16'))
        self.wealabel3.grid(row=0,column=2,padx=0,pady=10)
        self.wealabel4 = Label(self.tomorrowframe,width=6,textvariable=self.tomweastr4,font=('Helvetica', '16'))
        self.wealabel4.grid(row=0,column=3,padx=0,pady=10)
        self.wealabel5 = Label(self.tomorrowframe,width=6,textvariable=self.tomweastr5,font=('Helvetica', '16'))
        self.wealabel5.grid(row=0,column=4,padx=0,pady=10)
        # self.wealabel6 = Label(self.tomorrowframe,width=9,textvariable=self.tomweastr6,font=('Helvetica', '40'))
        # self.wealabel6.grid(row=0,column=1,rowspan=5,padx=5,pady=5,sticky=N+S+E+W)
        
        self.tomorrowframe.grid(row=8,column=0,columnspan=3,padx=10,sticky=E+W)


        self.weadata = StringVar()
        self.weadata.set('更新于: '+'今天'+'--:--')
        self.weadatalabel = Label(self.frame1,textvariable=self.weadata,font=('Helvetica', '12'))
        self.weadatalabel.grid(row=9,column=0,padx=10,pady=20,sticky=W)

        self.weaupdatabutton = Button(self.frame1,text='更新',font=('Helvetica', '12'),command=self.updateWeather)
        self.weaupdatabutton.grid(row=9,column=2,padx=10,pady=20,sticky=E+W)

        self.internetstate = StringVar()
        self.internetstate.set('已连接到互联网')
        self.internetstatelabel = Label(self.frame1,textvariable=self.internetstate,font=('Helvetica', '12'))
        self.internetstatelabel.grid(row=10,column=0,padx=10,sticky=W)

        self.frame1.grid(row=0,column=0,padx=10,pady=10,sticky=E)
        self.frame1.grid_propagate(0)
        #-----------------------------------------------------------------------------------------
        
        self.frame2 = Frame(master,height=580,width=430)

        self.PLCstatestr = StringVar()
        self.PLCstatestr.set('PLC未连接')
        self.timestr = StringVar()
        self.timestr.set(time.strftime('%H:%M:%S'))

        self.PLCstatelabel = Label(self.frame2,textvariable=self.PLCstatestr,font=('Helvetica', '12'))
        self.PLCstatelabel.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        self.PLCstatelabel = Label(self.frame2,textvariable=self.timestr,font=('Helvetica', '18'))
        self.PLCstatelabel.grid(row=1,column=0,columnspan=3,padx=10,pady=10,sticky=W+E)

        self.PLCstatelabel.after(800,self.tick)

        self.PLCbutton = Button(self.frame2,text='连接到PLC',font=('Helvetica', '12'),command=self.connect)
        self.PLCbutton.grid(row=0,column=2,padx=10,pady=10,sticky=E)

        self.soilframe = LabelFrame(self.frame2,text='土壤信息',labelanchor='n',font=('黑体', '16'))

        self.temstr = StringVar()
        self.temstr.set('xx.xx℃')

        self.wetstr = StringVar()
        self.wetstr.set('xx.xx %')

        Label(self.soilframe,text='温度：',font=('黑体', '16')).grid(row=0,column=0,padx=10,pady=0,sticky=N+W)
        Label(self.soilframe,textvariable=self.temstr,width=9,height=2,font=('Helvetica', '40')).grid(row=0,column=1,padx=10,pady=0)

        Label(self.soilframe,text='湿度：',font=('黑体', '16')).grid(row=1,column=0,padx=10,pady=10,sticky=N+W)
        Label(self.soilframe,textvariable=self.wetstr,width=9,height=2,font=('Helvetica', '40')).grid(row=1,column=1,padx=10,pady=10)

        self.soilframe.grid(row=2,column=0,columnspan=3,padx=10,pady=10,sticky=E+W)


        self.waterframe = LabelFrame(self.frame2,text='智能浇水！',labelanchor='n',font=('黑体', '16'))


        Label(self.waterframe,text='设定湿度:',font=('黑体', '16')).grid(row=0,column=0,padx=10,pady=10)

        waterentry = Entry(self.waterframe,justify=CENTER,width=5,font=('黑体', '20'),validate='focusout',validatecommand=self.validateText,invalidcommand=self.deleteText)
        waterentry.grid(row=0,column=1,padx=0,pady=10)

        Label(self.waterframe,text='%       ',font=('Helvetica', '16')).grid(row=0,column=2,padx=10,pady=10)

        Button(self.waterframe,text='极速浇水',width=10,font=('黑体', '12')).grid(row=0,column=3,sticky=E+W,padx=10,pady=5)

        Button(self.waterframe,text='常规浇水',width=10,font=('黑体', '12')).grid(row=1,column=3,sticky=E+W,padx=10,pady=5)

        Button(self.waterframe,text='慢速浇水',width=10,font=('黑体', '12')).grid(row=2,column=3,sticky=E+W,padx=10,pady=5)

        self.waterframe.grid(row=3,column=0,columnspan=3,padx=10,pady=0,sticky=E+W)

        self.frame2.grid(row=0,column=1,sticky=W)
        self.frame2.grid_propagate(0)

        self.weatherInit()
        self.updateWeather(1)


        #self.tick()

        #self.label = Label(master,text='test')
        #self.label.grid()
    def validateText(self):
        val = self.waterentry.get()
        return True

    def deleteText(self):
        
        return True
    
    def weatherInit(self):
        self.city = getLocation()
        self.locstr.set(self.city+'市')

    def changeCity(self):
        self.city = simpledialog.askstring('更改地点', '输入中文地点', initialvalue = self.city)
        self.locstr.set(self.city+'市')
        self.updateWeather()
        # messagebox.showinfo('更新提示', '天气已更新')
    def connect(self):
        data = (-1,-2)
        # data = getMb()
        self.temstr.set(str(data[0])+'℃')
        self.wetstr.set(str(data[1])+' %')

        messagebox.showinfo('更新提示', '土壤信息已更新')
        self.PLCstatestr.set('PLC已连接')
        self.PLCbutton.config(text='更新',width=10)
        self.PLCflg = True


    def updateWeather(self,mode=0):
        json = getWeather(self.city)  
        self.weastr1.set(json['data']['forecast'][0]['type'])
        self.weastr2.set(json['data']['forecast'][0]['high'])
        self.weastr3.set(json['data']['forecast'][0]['low'])
        self.weastr4.set(json['data']['forecast'][0]['fengxiang'])
        self.weastr5.set(json['data']['forecast'][0]['fengli'])
        self.weastr6.set(json['data']['wendu']+'℃')

        self.tomweastr1.set(json['data']['forecast'][1]['type'])
        self.tomweastr2.set(json['data']['forecast'][1]['high'])
        self.tomweastr3.set(json['data']['forecast'][1]['low'])
        self.tomweastr4.set(json['data']['forecast'][1]['fengxiang'])
        self.tomweastr5.set(json['data']['forecast'][1]['fengli'])

        self.weadata.set('更新于: '+'今天'+time.strftime('%H:%M:%S'))
        if mode==0:
            messagebox.showinfo('更新提示', '天气已更新')

    def tick(self):
        self.timestr.set(time.strftime('%H:%M:%S'))
        if self.PLCflg:
            data = (-2,-3)
            # data = getMb()
            self.temstr.set(str(data[0])+'℃')
            self.wetstr.set(str(data[1])+' %')
        self.PLCstatelabel.after(1000,self.tick)
        


if __name__ == '__main__':
    root = Tk()
    root.title('PLC灌溉系统  Beta 1.2')
    root.geometry('920x600+220+20')

    App(root)



    mainloop()
