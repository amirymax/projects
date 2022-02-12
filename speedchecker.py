from speedtest import Speedtest as s
from tkinter import *
from tkinter import ttk as t

window=Tk()
window.title('SpeedChecker')
window.geometry('270x130')
window.configure(background='black')

def check():
    global label
    label.grid_forget()
    window.geometry('330x130')
    label=Label(window,bg='black',fg='white', font='Arial -20')
    label.grid(row=0,column=0,columnspan=2,rowspan=1,ipady=3,ipadx=15)
    s1='Download speed: %.2f Kbytes/s'%(s().download()/8192)
    s2='Upload speed: %.2f Kbytes/s'%(s().upload()/8192)
    
    label['text']=s1+'\n'+s2
    

label=Label(window,bg='black',fg='white',text='the result will appear here...', font='Arial -20')
label.grid(row=0,column=0,columnspan=2,rowspan=1,ipady=15,ipadx=10)

Button(window,text='Check!',fg='red', font='Arial -20 italic bold underline',border='5', width=10,height=2,command=check).grid(row=1,column=0)
Button(window,text='Exit',font='Arial -20 italic bold underline',border='5', width=10,height=2,command=exit).grid(row=1,column=1)

window.mainloop()
