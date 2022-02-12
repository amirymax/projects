import download_local_files
from tkinter import *
from tkinter import ttk
import os


######Functions###

def english_version():
    window.destroy()
    os.startfile('database_usa.py')

def tajik_version():
    window.destroy()
    os.startfile('database_taj.py')

text1='''Забонро интихоб кунед:
Select the language please:'''

window=Tk()

window.config(bg='sky blue')
window.resizable(False,False)

x=window.winfo_screenwidth()
y=window.winfo_screenheight()

x1=x/2
y1=y/2


window.geometry('+%d+%d'%(x1-(x*11/100),y1-(y*13/100)))
window.title('Интихоби Забон - Language choosing')

taj=PhotoImage(file='photos/tajikistan.png')
uks=PhotoImage(file='photos/uks.png')

Label(window,text=text1,
      bg='sky blue', fg='red',
      font='courier -17 bold').grid(
          row=0,column=0,columnspan=5,padx=10)

Label(window,bg='sky blue').grid(
    row=1,column=0)

Button(window,text=taj,
       image=taj, width=90,height=90,
           bg='sky blue',border=0,command=tajik_version).grid(
    row=1,column=1,padx=5,pady=10)

Label(window,text='Тоҷикӣ',font='courier -18 bold underline',
      fg='red',bg='sky blue').grid(
    row=2,column=1,padx=5)

Button(window,text='English',
       image=uks, width=90,height=90,
           bg='sky blue',border=0,
       command=english_version).grid(
    row=1,column=2,padx=5,pady=10)

Label(window,text='English',font='courier -18 bold underline',fg='red',bg='sky blue').grid(
    row=2,column=2,padx=5)
