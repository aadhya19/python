from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox

t=Tk()
t.geometry('900x900')
t.title('Text Editor')
s=''

m=Menu()

#file menu

fm=Menu()

def new_file():
    area.delete(1.0,'end')
fm.add_command(label='New',command=new_file)
fm.add_separator()

def open_file():
    r=Toplevel()
    r.geometry('450x450')
    h=Label(r,text='Enter file name with location')
    h.place(x=135,y=100)
    f_entry=Entry(r,width=55)
    f_entry.place(x=50,y=140)
    def file_opening():
        loc=f_entry.get()
        f=open(loc,'r')
        global s
        s=f.read(10000)
        area.insert(1.0,s)
        f.close()
    bt=Button(r,text='Open',command=file_opening)
    bt.place(x=200,y=200)
fm.add_command(label='Open',command=open_file)
fm.add_separator()

def save_file():
    r=Toplevel()
    r.geometry('450x450')
    h=Label(r,text='Enter file name with location')
    h.place(x=135,y=100)
    f_entry=Entry(r,width=55)
    f_entry.place(x=50,y=140)
    def file_saving():
        loc=f_entry.get()
        f=open(loc,'w')
        global s
        s=area.get(1.0,'end')
        f.write(s)
        f.close()
        messagebox.showinfo('info','Data Saved')
    bt=Button(r,text='Save',command=file_saving)
    bt.place(x=200,y=200)
fm.add_command(label='Save',command=save_file)
fm.add_separator()

m.add_cascade(menu=fm,label='File')

#edit menu

em=Menu()

def cut():
    global s
    s=area.get(1.0,'end')
    f=open('temp.txt','w')
    f.write(s)
    area.delete(1.0,'end')
    f.close()
em.add_command(label='Cut',command=cut)
em.add_separator()

def copy():
    global s
    s=area.get(1.0,'end')
    f=open('temp.txt','w')
    f.write(s)
    f.close()
em.add_command(label='Copy',command=copy)
em.add_separator()

def paste():
    global s
    s=area.get(1.0,'end')
    f=open('temp.txt','r')
    s=f.read(10000)
    area.insert(1.0,s)
    f.close()
em.add_command(label='Paste',command=paste)
em.add_separator()

m.add_cascade(menu=em,label='Edit')

#color menu

cm=Menu()

def bg_color():
    c=colorchooser.askcolor()
    area.config(bg=c[1])
cm.add_command(label='Background',command=bg_color)
cm.add_separator()

def fg_color():
    c=colorchooser.askcolor()
    area.config(fg=c[1])
cm.add_command(label='Foreground',command=fg_color)
cm.add_separator()

m.add_cascade(menu=cm,label='Color')

#size menu

sm=Menu()

def s10():
    area.config(font=('Regular',10))
sm.add_command(label='10',command=s10)
sm.add_separator()

def s20():
    area.config(font=('Regular',20))
sm.add_command(label='20',command=s20)
sm.add_separator()

def s30():
    area.config(font=('Regular',30))
sm.add_command(label='30',command=s30)
sm.add_separator()

def s40():
    area.config(font=('Regular',40))
sm.add_command(label='40',command=s40)
sm.add_separator()

def s50():
    area.config(font=('Regular',50))
sm.add_command(label='50',command=s50)
sm.add_separator()

def s60():
    area.config(font=('Regular',60))
sm.add_command(label='60',command=s60)
sm.add_separator()

def s70():
    area.config(font=('Regular',70))
sm.add_command(label='70',command=s70)
sm.add_separator()

def s80():
    area.config(font=('Regular',80))
sm.add_command(label='80',command=s80)
sm.add_separator()

m.add_cascade(menu=sm,label='Size')

t.config(menu=m)

area=Text(t, height=850, width=850)
area.config(font=('Regular',15))
area.pack()
  
t.mainloop()