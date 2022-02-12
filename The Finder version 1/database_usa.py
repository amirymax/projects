#The finder

#helps you to find

#everything

#you wanna search

#from your local drivers

#Made by AMIRY CORPORATION

#Copyright © 2019

#All rights reserved


from tkinter import *

from tkinter import messagebox

import os

from os.path import *




s=''' The Finder

The Finder program helps you find
any type of file that you want.
Program is made by a programmer
Zikrullo Amiri in 2019 year.

Version:     2.0


e-mail:      amirymax@gmail.com
                   amirymax@mail.com
                   amirymax@mail.ru
                  
                  
web-pages:     facebook.com\\amirymax
                         instagram.com\\amirymax

                         
'''
#music

m1=open('m.txt','r',encoding='utf-8')

m=[]

for i in m1:m.append(i[:-1])

#video

v1=open('v.txt','r',encoding='utf-8')
v=[]
for i in v1:v.append(i[:-1])

#photo

a1=open('a.txt','r',encoding='utf-8')
a=[]
for i in a1:a.append(i[:-1])

#doc

d1=open('d.txt','r',encoding='utf-8')
d=[]
for i in d1:d.append(i[:-1])

#ppt

p1=open('p.txt','r',encoding='utf-8')

p=[]

for i in p1:p.append(i[:-1])

#pdf

pd1=open('pd.txt','r',encoding='utf-8')
pd=[]
for i in pd1:pd.append(i[:-1])

#folder

f1=open('f.txt','r',encoding='utf-8')
f=[]
for i in f1:f.append(i[:-1])

#general

g1=open('g.txt','r',encoding='utf-8')

g=[]

for i in g1:g.append(i[:-1])

#Functions

#The length of a list
def leng(a):
   
   b=['1']
   
   for i in a:
      if field1.get().lower() \
         not in i[0].lower():
         b.append(len(i[1]))
      else:
         break
      
   s=len(b[0])
   
            
   return max(s)+20


#Opening files from list function

def openl():
   
   os.startfile(l.get(l.curselection()))
   la.destroy()
   Label(w3,text=l.get(l.curselection()),
         font='courier -20 bold',
         fg='red',bg='sky blue').grid(
            row=5,column=1,columnspan=7)   

#Clearing Function
   
def cls():
   
   l.delete(0,END)

#Check file from list
   
      
def cleanup():
    l=w3.grid_slaves()
    l=l[::-1]
    for i in l[6:]:
        i.destroy()

#Musics function

def mp3():
   
   global field1
   
   global w3

   w3=Toplevel()
   
   w3.title('Musics')

   w3.attributes('-topmost')
   
   
   w3.geometry('+530+40')
   
   
   
   w3.iconbitmap("icons\\music.ico")
   w3.config(bg='sky blue')
   
   Label(w3,text='Write name of music',
         font='Batang -24 bold',fg='red',bg='sky blue').grid(
            row=0,column=0,columnspan=6,pady=5)
   
   field1=Entry(w3,font='Courier -22 ',
                fg='cyan',bg='gray')
   
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,height=75,border='0',
          command=playmp3,
          image=pm,bg='sky blue').grid(
             row=2,column=0,padx=30,columnspan=4)
   
   Label(w3,text='Play',font='Batang -24 bold',
         fg='blue',bg='sky blue').grid(
            row=3,column=0,padx=30,columnspan=4)


   
   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue').grid(
             row=2,column=2,pady=5,
             padx=50,columnspan=5)
   
   Label(w3,text='Close',font='Batang -24 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=2,padx=50,columnspan=5)

#Play music function
   
def playmp3():

   global l
   global la
   
   la=Label(w3,text=' ',
               font='courier -20 bold',fg='red',bg='sky blue')                     
   if field1.get().lower() in m[0].lower():

      cleanup()
      
      os.startfile(m[0][1])

      Label(w3,text='Playing',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=m[0][1]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',command=openl,
             image=op,border='0',bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',fg='gray',bg='sky blue').grid(
         row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in m:
         if field1.get().lower() not in i[0].lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() \
              in i.lower():
            
            os.startfile(i[1])
            x=1
            Label(w3,text='Playing',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(m[:m.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)
   
def mp4():
   
   global field1
   global w3
 
   w3=Toplevel()   
   w3.geometry('+530+40')   
   w3.config(bg='sky blue')                
   w3.resizable(False,False)  
   w3.title('Video')
   w3.iconbitmap("icons\\video.ico")
   
   Label(w3,text='Write name of video',
         font='Batang -24 bold',fg='red',bg='sky blue').grid(
            row=0,column=0,columnspan=6,pady=5)
   
   field1=Entry(w3,font='Courier -22',fg='cyan',
                bg='gray')      
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,height=75,border='0',
          command=playmp4,image=pv,bg='sky blue').grid(
             row=2,column=0,padx=30,columnspan=4)
   
   Label(w3,text='Play',font='Batang -24 bold',
         fg='yellow',bg='sky blue').grid(
            row=3,column=0,padx=30,columnspan=4)

   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue').grid(
             row=2,column=2,pady=5,padx=50,
             columnspan=5)
   
   Label(w3,text='Close',font='Batang -24 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=2,padx=50,columnspan=5)
   
def playmp4():
   
   global l
   global la
   la=Label(w3,text=' ',
               font='courier -20 bold',fg='red',bg='sky blue')

   if field1.get().lower() in v[0].lower():

      cleanup()
      
      os.startfile(v[0])

      Label(w3,text='Playing',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=v[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',command=openl,
             image=op,border='0',bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',fg='gray',bg='sky blue').grid(
         row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in v:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)
            x=1
            Label(w3,text='Playing',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(v[:v.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0: 
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)
      
def photo():
   
   global field1
   
   global w3

   w3=Toplevel()
   
   w3.resizable(False,False)
   
   w3.config(bg='sky blue')
   
   w3.attributes('-topmost')
   
   w3.geometry('+530+40')

   w3.title('Photo')
   w3.iconbitmap("icons\\photo.ico")
   
   Label(w3,text='Write name of photo',
         font='batang -24 bold',fg='red',bg='sky blue').grid(
            row=0,column=0,columnspan=6,pady=5)
   
   field1=Entry(w3,font='courier -22',fg='cyan',bg='gray')
   
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,height=75,border='0',
          command=openphoto,image=of,bg='sky blue').grid(
             row=2,column=0,padx=30,columnspan=4)
   
   Label(w3,text='Open',font='Batang -24 bold',
         fg='coral1',bg='sky blue').grid(
            row=3,column=0,padx=30,columnspan=4)


   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue').grid(
             row=2,column=2,pady=5,
             padx=50,columnspan=5)
   
   Label(w3,text='Close',font='Batang -24 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=2,padx=50,columnspan=5)
   
   
def openphoto():
   
   global l
   
   global la
   
   la=Label(w3,text=' ',
               font='courier -20 bold',fg='red',bg='sky blue')                     
   if field1.get().lower() in a[0].lower():

      cleanup()
      
      os.startfile(a[0])

      Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=a[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',command=openl,
             image=op,border='0',bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',fg='gray',bg='sky blue').grid(
         row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in a:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)      
            x=1
            Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(a[:a.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)



def doc():
   
   global field1
   
   global w3

   w3=Toplevel()

   w3.title('Ms Word')
   
   w3.attributes('-topmost')

   
   w3.geometry('+530+40')
   
      
   w3.iconbitmap("icons\\word.ico")
   w3.config(bg='sky blue')
   
   Label(w3,text='Write name of document',
         font='batang -24 bold',fg='red',
         bg='sky blue').grid(
            row=0,column=0,columnspan=6,pady=5)
   
   field1=Entry(w3,font='Courier -20',fg='cyan',
                bg='grey')
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,bg='sky blue',height=75,border='0',
          command=opendoc,image=of).grid(
             row=2,column=0,
             padx=30,columnspan=4)
   
   Label(w3,text='Open',font='batang -22 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=0,padx=30,columnspan=4,)
   
   Button(w3,width=75,bg='sky blue',height=75,border='0',
          command=w3.destroy,image=cl).grid(
             row=2,column=2,
             pady=5,padx=50,columnspan=5)
   
   Label(w3,text='Close',font='batang -22 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=2,padx=50,columnspan=5)


def opendoc():
   
   global l
   
   global la
   
   la=Label(w3,text=' ',
               font='courier -20 bold',fg='red',bg='sky blue')                     
   if field1.get().lower() in d[0].lower():

      cleanup()
      
      os.startfile(d[0])

      Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=d[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',command=openl,
             image=op,border='0',bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',fg='gray',bg='sky blue').grid(
         row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in d:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)
            x=1
            Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(d[:d.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)
      



def ppt():
   
   global field1
   global w3

   w3=Toplevel()
   
  
   
   w3.resizable(False,False)
   
   w3.geometry('+530+50')

   w3.title('Ms PowerPoint')
   w3.iconbitmap("icons\\ppt.ico")

   w3.config(bg='sky blue')
   
   lub=Label(w3,text='Write name of presentation',
         font='batang -24 bold', fg='red',bg='sky blue')

   lub.grid(row=0,column=0,columnspan=6)
   
   field1=Entry(w3,font='Courier -22',
                bg='grey',fg='cyan')
   
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,height=75,border='0',
          command=openppt,image=of,bg='sky blue').grid(
             row=2,column=0,columnspan=4,
             padx=30)
   
   Label(w3,text='Open',font='batang -24 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=0,columnspan=4,padx=30)
   
   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue').grid(
             row=2,column=2,columnspan=5,
             padx=50,pady=5)
   
   Label(w3,text='Close',font='batang -24 bold',
         bg='sky blue',fg='red').grid(
      row=3,column=2,columnspan=5,padx=50)

   
def openppt():
   
   global l
   
   global la
   
   la=Label(w3,text=' ',
               font='courier -20 bold',fg='red',bg='sky blue')                     
   if field1.get().lower() in p[0].lower():

      cleanup()
      
      os.startfile(p[0])

      Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=p[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',
             command=openl,image=op,border='0',
             bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',
            fg='gray',bg='sky blue').grid(
               row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in p:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)
            x=1
            Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(p[:p.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)



def pdf():
   
   global field1
   global w3

   w3=Toplevel()
   w3.title('Portable Document Format')
   
   w3.geometry('+530+50')
   
   w3.attributes('-topmost')
   w3.config(bg='sky blue')
   w3.resizable(False,False)
   
   w3.iconbitmap("icons\\pdf.ico")
   w3.geometry('+530+40')
   
   Label(w3,text='Write name of pdf file',
         font='batang -24 bold',bg='sky blue',
         fg='red').grid(row=0,column=0,
                        columnspan=6,pady=5)
   
   field1=Entry(w3,font='Courier -20',fg='cyan',
                bg='gray')
   
   field1.grid(row=1,column=0,columnspan=6)
   
   Button(w3,width=75,height=75,border='0',
          command=openpdf,image=of,bg='sky blue').grid(
             row=2,column=0,padx=30,columnspan=4)
   
   Label(w3,text='Open',font='Batang -24 bold',
         fg='coral1',bg='sky blue').grid(
            row=3,column=0,padx=30,columnspan=4)


   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue').grid(
             row=2,column=2,pady=5,padx=50,
             columnspan=5)
   
   Label(w3,text='Close',font='Batang -24 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=2,padx=50,columnspan=5)


def openpdf():
   
   global l
   
   global la
   
   la=Label(w3,text=' ',font='courier -20 bold',
            fg='red',bg='sky blue')                     
   if field1.get().lower() in pd[0].lower():

      cleanup()
      
      os.startfile(p[0])

      Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=pd[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0
      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',
             command=openl,image=op,border='0',
             bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',
            fg='gray',bg='sky blue').grid(
               row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in pd:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)
            x=1
            Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(pd[:pd.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)

       

def fold():
   
   global field1
   
   global w3

   w3=Toplevel()
        
   w3.resizable(False,False)
   
   w3.geometry('+530+50')
   w3.config(bg='sky blue')
   
   w3.title('Folder')
   w3.iconbitmap("icons\\folder.ico")
   
   labl=Label(w3,text='Write name of folder',
         font='batang -24 bold',
              bg='sky blue',fg='red')

   labl.grid(row=0,column=0,columnspan=6,pady=5)

   
   field1=Entry(w3,font='Courier -22',fg='cyan',
                bg='grey')
   
   field1.grid(row=1,column=0,columnspan=6)

   
   butt=Button(w3,width=75,height=75,border='0',
          command=openfold,image=of,bg='sky blue')
   
   butt.grid(row=2,column=0,columnspan=4,
             padx=30)

   
   lax=Label(w3,text='Open',font='batang -22 bold',
             fg='red',bg='sky blue')

   lax.grid(row=3,column=0,columnspan=4,padx=30)

   
   btut=Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,bg='sky blue')
   
   btut.grid(row=2,column=2,columnspan=5,
             padx=50,pady=5)

   
   labb=Label(w3,text='Close',font='batang -22 bold',fg='red',bg='sky blue')

   labb.grid(row=3,column=2,columnspan=5,padx=50)


   
def openfold():
   
   global l
   global la
   
   la=Label(w3,text=' ',font='courier -20 bold',
            fg='red',bg='sky blue')                     
   if field1.get().lower() in f[0].lower():

      cleanup()
      
      os.startfile(f[0])

      Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
            bg='sky blue').grid(
               row=4,column=1,columnspan=5)
      
      
      la['text']=f[0]
      la.grid(row=5,column=1,columnspan=7)


      
   else:
      x=0

      cleanup()
      
      y=Scrollbar(w3)
      y.grid(row=6,column=8,sticky='ns')
      
      l=Listbox(w3,yscrollcommand=y.set)
      
      l.grid(row=6,column=0,columnspan=8)
      y.config(command=l.yview)
      
      Button(w3,width=75,height=75,text='Open',
             command=openl,image=op,border='0',
             bg='sky blue').grid(row=7,column=9)
      
      Label(w3,text='Open',font='Batang -22',
            fg='gray',bg='sky blue').grid(
               row=8,column=9,padx=20)
      
      l.delete(0,END)
      
      
      for i in f:
         if field1.get().lower() not in i.lower():
            
            l.insert(END,i)
            
         elif i!='' and field1.get().lower() in i.lower():
            
            os.startfile(i)
            x=1

            Label(w3,text='Opened',
            font='Batang -20 bold',fg='red',
                  bg='sky blue').grid(
               row=4,column=1,columnspan=5)
            
            l.config(width=leng(f[:f.index(i)]))
            
            la.config(text=i)
            
            la.grid(row=5,column=1,columnspan=7)
            
            break
         

      
      if x==0:
         cleanup()
         la['text']='Not Found... :-('
         la.grid(row=5,column=1,columnspan=7)

      
def general():
   
   global field1
   
   global w3
   
   w3=Toplevel()
   
   w3.geometry('+530+50')
   w3.title('General')
   
   w3.iconbitmap("icons\\general.ico")
   w3.config(bg='sky blue')
   
   Label(w3,text='What are you looking for?',
         font='batang -24 bold',fg='red',bg='sky blue').grid(
            row=0,column=0,columnspan=6)
   
   field1=Entry(w3,font='Courier -20',
                bg='grey',fg='cyan')
   
   field1.grid(row=1,column=0,columnspan=6)

   
   Button(w3,width=75,height=75,border='0',
          command=generallist,
          image=op,bg='sky blue').grid(
             row=2,column=0,columnspan=4,padx=30)
   
   Label(w3,text='Find',font='batang -22 bold',
         fg='red',bg='sky blue').grid(
      row=3,column=0,columnspan=4,padx=30)
   
   Button(w3,width=75,height=75,border='0',
          command=w3.destroy,image=cl,
          bg='sky blue').grid(row=2,column=2,
            columnspan=5,padx=50,pady=5)
   
   Label(w3,text='Close',font='batang -22 bold',
         fg='red',bg='sky blue').grid(row=3,
            column=2,columnspan=5,padx=50)

def maxgen(a):
   x=[]
   for i in a:
      x.append(len(i))
   return max(x)

def generallist():
   
   global l
   
   a=[]
   
   
   for i in g:
      if field1.get().lower() in i[:-1].lower():
         a.append(i)
      

   y=Scrollbar(w3)
   
   y.grid(row=6,column=8,sticky='ns')
   
   
   l=Listbox(w3,yscrollcommand=y.set)
   
   l.grid(row=6,column=0,columnspan=8)
   
   y.config(command=l.yview)
  
   
   openb=Button(w3,width=75,height=75,
                text='Open',command=openl,
          image=op,border='0')
   
   openb.grid(row=7,column=9)

   
   openli=Label(w3,text='Open',
                font='batang -22 bold',
                fg='red',bg='sky blue')
   
   openli.grid(row=8,column=9,padx=20)
   
   l.delete(0,END)
   
   
   for i in a:
      if field1.get().lower() in i.lower():
         l.insert(END,i)
         
   l.config(width=maxgen(a))
   
   
def ex():
   
    m=messagebox.askquestion('Exit','Are you sure you wanna exit?')

    if m=='yes':
        w2.destroy()
        m1.close()
        os.remove('m.txt')
        v1.close()
        os.remove('v.txt')
        a1.close()
        os.remove('a.txt')
        d1.close()
        os.remove('d.txt')
        p1.close()
        os.remove('p.txt')
        pd1.close()
        os.remove('pd.txt')
        f1.close()
        os.remove('f.txt')
        g1.close()
        os.remove('g.txt')
        
             
def info():
   
   messagebox.showinfo('Info',s)


   
w2=Tk()
w2.title('The Finder')


w2.resizable(False,False)
w2.iconbitmap('icons\\main_icon.ico')

x=w2.winfo_screenwidth()

back=PhotoImage(file='photos\\background.gif')

w=back.width()
h=back.height()

pi=x/2-w/2

w2.geometry('%dx%d+%d+1'%(w,h,pi))


mi=PhotoImage(file="photos\\music.png")

vi=PhotoImage(file="photos\\video.png")

pi=PhotoImage(file="photos\\pdf.png")

wi=PhotoImage(file="photos\\word.png")

ppi=PhotoImage(file="photos\\ppt.png")

fi=PhotoImage(file="photos\\folder.png")

ei=PhotoImage(file="photos\\exit.png")

pm=PhotoImage(file="photos\\playmusic.png")

pv=PhotoImage(file="photos\\playvideo.png")

op=PhotoImage(file="photos\\open.png")


cl=PhotoImage(file="photos\\close.png")

of=PhotoImage(file="photos\\openfile.png")

ph=PhotoImage(file='photos\\photo.png')

gi=PhotoImage(file='photos\\general.png')

infoi=PhotoImage(file='photos\\info.png')


lab=Label(w2,image=back,width=w,
          height=h,bg='white')

lab.grid(row=0,column=0,columnspan=w,
         rowspan=h)


lab1=Label(w2,text='',bg='gray')

lab1.grid(row=0,column=0)


lab2=Label(w2,text='',bg='gray',)

lab2.grid(row=0,column=1,padx=55)


lab3=Label(w2,text='',bg='gray')

lab3.grid(row=0,column=2,padx=80)






lab5=Label(w2,text='',bg='gray')

lab5.grid(row=1,column=0,pady=55)


lab6=Label(w2,text='',bg='gray')

lab6.grid(row=2,column=0,pady=35)




musb=Button(w2,text='Music',width=95,height=95,
            command=mp3,border='0',image=mi)

musb.grid(row=2,column=7)


vidb=Button(w2,text='Video',width=93,height=95,command=mp4,
             border='0',image=vi)

vidb.grid(row=2,column=12,padx=140)


phb=Button(w2,text='Photo',width=95,height=95,command=photo,
             border='0',image=ph)

phb.grid(row=2,column=17)


wordb=Button(w2,text='Word',width=95,height=95,command=doc,
             border='0',image=wi)

wordb.grid(row=4,column=7)


pptb=Button(w2,text='PPt',width=95,height=95,command=ppt,
             border='0',image=ppi)

pptb.grid(row=4,column=12,pady=70,padx=140)


pdfb=Button(w2,text='Pdf',width=95,height=95,command=pdf,
             border='0',image=pi)

pdfb.grid(row=4,column=17)


folb=Button(w2,text='Folder',width=95,height=95,command=fold,
             border='0',image=fi)

folb.grid(row=6,column=7)

genb=Button(w2,text='General',width=95,height=95,border='0',
             image=gi,command=general)

genb.grid(row=6,column=12)


exb=Button(w2,text='Exit',width=95,height=95,command=ex,
             border='0',image=ei)
Label(w2,text='',bg='burlywood2').grid(row=6,column=18,padx=82)

exb.grid(row=6,column=17)

infob=Button(w2,text='Info',width=95,height=95,command=info,
             border='0',image=infoi)

infob.grid(row=6,column=19)

w2.mainloop()
