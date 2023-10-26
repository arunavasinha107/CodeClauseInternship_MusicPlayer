import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

root=Tk()
root.title("MUSIC PLAYER")
root.geometry("485x700+290+10")
root.configure(background="#333333")
root.resizable(False,False)
mixer.init()

framecnt=30
frames=[PhotoImage(file="djmusic.gif",format="gif -index %i" %(i)) for i in range(framecnt)]

def update(ind):

    frame=frames[ind]
    ind+=1
    if ind==framecnt:
        ind=0

    label.configure(image=frame)
    root.after(40,update,ind)

label=Label(root)    
label.place(x=0,y=0)
root.after(0,update,0)


def AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for i in songs:
            if i.endswith(".mp3"):
                Playlist.insert(END,i)


def PlayMusic():
    Music_Name=Playlist.get(ACTIVE)
    print(Music_Name,ACTIVE)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


lower_frame=Frame(root,bg="#FFFFFF",width=485,height=180)
lower_frame.place(x=0,y=400)

icon=PhotoImage(file="music.png")
root.iconphoto(False,icon)

menu=PhotoImage(file="menu.png")
Label(root,image=menu).place(x=0,y=580,width=485,height=100)

Frame_Music=Frame(root,bd=2,relief=RIDGE)
Frame_Music.place(x=0,y=585,width=485,height=100)

playbutton=PhotoImage(fi="play.png")
Button(root,image=playbutton,bg="#FFFFFF",bd=0,height=60,width=60,command=PlayMusic).place(x=215,y=487)

stopbutton=PhotoImage(file="stop.png")
Button(root,image=stopbutton,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.stop).place(x=130,y=487)

pausebutton=PhotoImage(file="pause.png")
Button(root,image=pausebutton,bg="#FFFFFF",bd=0,height=60,width=60,command=mixer.music.pause).place(x=300,y=487)

volume1=PhotoImage(file="volume.png")
panel=Label(root,image=volume1).place(x=20,y=487)


Button(root,text="Search Music",width=59,height=1,font=("calibri",12,"bold"),fg="black",bg="#FFFFFF",command=AddMusic).place(x=0,y=550)

Scroll=Scrollbar(Frame_Music)
Playlist=Listbox(Frame_Music,width=100,font=("Times new roman",10),bg="#333333",fg="grey",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=Scroll.set)

Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT,fill=Y)
Playlist.pack(side=RIGHT,fill=BOTH)


root.mainloop()
