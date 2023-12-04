from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def s():
    data=json.load(open('data.json'))
    wordd=enterwordentry.get()
    wordd=wordd.lower()
    if wordd in data:
        meaning=data[wordd]
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,item+'\n\n')

    elif len(get_close_matches(wordd,data.keys()))>0:
        close_match=get_close_matches(wordd, data.keys())[0]
        res=messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')
        if res==True:
            enterwordentry.delete(0,END)
            enterwordentry.insert(END,close_match)
            meaning=data[close_match]
            for item in meaning:
                textarea.insert(END, item + '\n\n')
        else:
            messagebox.showinfo('Error','Please check your word')
            enterwordentry.delete(0,END)
            textarea.delete(1.0,END)

    else:
        messagebox.showinfo('information','The word doesnt exist')
        enterwordentry.delete(0,END)
        textarea.delete(1.0,END)
def c():
    enterwordentry.delete(0,END)
    textarea.delete(1.0,END)

def iexit():
    r=messagebox.askyesno('Confirm','Do you want to exit?')
    if r==True:
        root.destroy()
    else:
        pass
def a():
    engine.say(enterwordentry.get())
    engine.runAndWait()

def p():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()





root = Tk()
root.geometry('1296x864+100+30')
root.title('Talking Dictionary')
root.resizable(0,0)
bgimage = PhotoImage(file="bg1.png")
bgLabel =Label(root, image=bgimage)
bgLabel.place(x=0,y=0)

enterwordlabel=Label(root,text='Enter Word', font=('times',30),fg='rosy brown',background='seashell2')
enterwordlabel.place(x=925,y=50)

enterwordentry=Entry(root,font=('times',23,),justify=CENTER,bd=3,relief=GROOVE)
enterwordentry.place(x=845,y=120)

search=PhotoImage(file='search (1).png')
sbutton=Button(root,image=search,command=s)
sbutton.place(x=870,y=190)

micimage=PhotoImage(file='microphone (1).png')
micbutton=Button(root,image=micimage,command=a)
micbutton.place(x=1100,y=190)

enterwordlabel=Label(root,text='Meaning', font=('times',30),fg='rosy brown',background='seashell2')
enterwordlabel.place(x=940,y=300)

textarea=Text(root,width=34,height=14,font=('candara',12),bd=3,relief=GROOVE)
textarea.place(x=860,y=360)


audio=PhotoImage(file='microphone (1).png')
abutton=Button(root,image= audio,command=p)
abutton.place(x=900,y=650)

clear=PhotoImage(file='clear.png')
cbutton=Button(root,image=clear,command=c)
cbutton.place(x=1100,y=650)

exit=PhotoImage(file='exit.png')
ebutton=Button(root,image=exit,command=iexit)
ebutton.place(x=1200,y=700)

def enter_function(event):
    sbutton.invoke()





root.bind('<Return>',enter_function)
root.mainloop()
