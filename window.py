from tkinter import *
from pymysql import *
from pygame import mixer
from threading import Thread
root = Tk()
def again():
    mixer.init(44100, -16,2,2048)
    e=0
    db = connect("localhost","root","ayush2002","melody")
    cur = db.cursor()
    root = Tk()
    root.title("Melody : Free Music")
    d = StringVar()
    root.config(bg="#000000")
    root.geometry("2010x700+0+0")
    x = []
    def search():
        global root
        e = 0
        data = str(d.get())
        cur.execute(f'select * from list where Song_Name like "%{data}%" or Artist like "%{data}%"')
        x = cur.fetchall()
        def add(i,c):
            global root
            def player():
                global root
                def wind():
                    global root
                    lyricsfile = open(i[3], 'r')
                    lyrics = lyricsfile.readlines()
                    root.destroy()
                    pwind = Tk()
                    pwind.config(bg = "#ed4040")
                    pwind.geometry("1600x500+200+300")
                    pwind.title("Melody Player")
                    def unpause():
                        mixer.music.unpause()
                    def pause():
                        mixer.music.pause()
                    def stop():
                        mixer.music.stop()
                        pwind.destroy()
                    pbut = Button(pwind, width = 10,font =("Consolos",12),fg = "#ed4040",bg = "#ffffff",text = "Play",command = unpause)
                    ppbut = Button(pwind,width = 10,font =("Consolos",12),fg = "#ed4040",bg = "#ffffff",text = "Pause", command = pause)
                    sbut = Button(pwind, width = 10,font =("Consolos",12),fg = "#ed4040",bg = "#ffffff",text = "Stop", command = stop)
                    semp1 = Label(pwind, font =("Consolos",15),fg = "#ffffff",bg = "#ed4040" , text ="")
                    semp2 = Label(pwind, font =("Consolos",15),fg = "#ffffff",bg = "#ed4040" , text ="")
                    sname = Label(pwind, font =("Consolos",15),fg = "#ffffff",bg = "#ed4040",text = i[0] )
                    sbar = Scrollbar(pwind)
                    lylist = Listbox(pwind,width = 100,fg = "#000000",bg = "#f0f0f0",font = ("Consolos",12), yscrollcommand = sbar.set )
                    for line in lyrics:
                        lylist.insert(END, line)
                    sbar.config(command = lylist.yview)
                    lylist.pack(side = LEFT, fill = BOTH)
                    sbar.pack( side = RIGHT, fill = Y)
                    semp1.pack()
                    sname.pack()
                    semp2.pack()
                    pbut.pack()
                    ppbut.pack()
                    sbut.pack()
                    pwind.mainloop()
                def song():
                    mixer.music.load(i[2])
                    mixer.music.play()
                pro1=Thread(target = wind)
                pro2 = Thread(target = song)
                pro1.start()
                pro2.start()
            if c%2==0:
                result = Button(cont,width = 40 ,text = i[0],  font = ("Consolos",12), fg = "#ffffff",bg = "#ed4040",command = player)
                result.pack()
                result.update()
                root.update()
            else:
                result = Button(cont,width = 40 ,text = i[0],  font = ("Consolos",12), fg = "#ed4040",bg = "#ffffff",command = player)
                result.pack()
                result.update()
                root.update()           
        for i in x:
            add(i,e)
            e = e + 1
        again()

    lab = Label(root, text = "Melody : Free Music", font = ("Consolos",20) ,  fg = "#ed4040",bg = "#000000")
    cont = Listbox(root,width = 1000,bg = "#000000")
    emplab1 = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    emplab2 = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    emplab3 = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    emplab4 = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    emplab5 = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    result = Label(root, text="", font = ("Consolos",8),bg = "#000000")
    but = Button(root,text = "Search",bg = "#ed4040",fg = "#ffffff",font = ("Consolos",12), command = search)
    ent = Entry(root, font = ("Consolos",14),width = 60,textvariable = d)
    re = Button(root, text = "Reset",bg = "#ed4040",fg = "#ffffff",font = ("Consolos",12),command = again)
    info = Label (root, bg = "#000000",fg = "#ed4040",font = ("Consolos",12), text = "Click Reset after every search")
    emplab1.pack()
    lab.pack()
    emplab2.pack()
    ent.pack()
    emplab3.pack()
    but.pack()
    emplab4.pack()
    info.pack()
    emplab5.pack()
    re.pack()
    result.pack()
    cont.pack(fill = BOTH)

    root.mainloop()

again()