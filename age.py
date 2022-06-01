from tkinter import *
from datetime import datetime

bg='black'
fg='cyan'

App=Tk()
App.title('Age Calculator')
App['background']=bg
App.geometry('250x250')


msg=Label(App,text='ENTER YOUR DOB',background=bg,foreground=fg)
msg.grid(row=0,column=2,columnspan=3,padx='20px',pady='5px')

dayL=Label(App,text='Day: ',background=bg,foreground=fg)
dayE=Entry(App,width=3)

monL=Label(App,text='Month: ',background=bg,foreground=fg)
monE=Entry(App,width=3)

yrL=Label(App,text='Year: ',background=bg,foreground=fg)
yrE=Entry(App,width=4)

dayL.grid(row=1,column=0)
dayE.grid(row=1,column=1)
monL.grid(row=1,column=2)
monE.grid(row=1,column=3)
yrL.grid(row=1,column=4)
yrE.grid(row=1,column=5)

def find_days():
    date=int(dayE.get())
    mon=int(monE.get())
    year=int(yrE.get())
    dob=datetime(day=date,month=mon,year=year)

    time_now=datetime.now()
    time_diff=time_now - dob

    dys=Label(App,text='You lived '+str(time_diff.days)+ 'days!',background=bg,foreground=fg)
    dys.grid(row=3,column=0,columnspan=4)


def find_secs():
    date=int(dayE.get())
    mon=int(monE.get())
    year=int(yrE.get())
    dob=datetime(day=date,month=mon,year=year)

    time_now=datetime.now()
    time_diff=time_now - dob

    sec=Label(App,text='You lived '+ str(time_diff.total_seconds())+ 'seconds!',background=bg,foreground=fg)
    sec.grid(row=4,column=0,columnspan=6)

dysB=Button(App,text='Total Days',command=find_days,background=bg,foreground=fg)
secB=Button(App,text='Total Seconds',command=find_secs,background=bg,foreground=fg)
dysB.grid(row=2,column=0,columnspan=3)
secB.grid(row=2,column=3,columnspan=3)


App.mainloop()
