# do not question the variables!
import random
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from tkinter import *
from PIL import ImageTk, Image
import time
global repeat
repeat = 1
lastclick = 1
click = 0
global roundsplayed
global strround
rat = 1
with open('rrsave.txt') as inrr:
    rrstr = inrr.read()
rr = int(rrstr)
print(rr)
with open('rpsave.txt') as inrp:
    rpstr = inrp.read()
rp = int(rpstr)
print(rp)
with open('rssave.txt') as inrs:
    rsstr = inrs.read()
rs = int(rsstr)
print(rs)
with open('prsave.txt') as inpr:
    prstr = inpr.read()
pr = int(prstr)
print(pr)
with open('ppsave.txt') as inpp:
    ppstr = inpp.read()
pp = int(ppstr)
print(pp)
with open('pssave.txt') as inps:
    psstr = inps.read()
ps = int(psstr)
print(ps)
with open('srsave.txt') as insr:
    srstr = insr.read()
sr = int(srstr)
print(sr)
with open('spsave.txt') as insp:
    spstr = insp.read()
sp = int(spstr)
print(sp)
with open('sssave.txt') as inss:
    ssstr = inss.read()
ss = int(ssstr)
print(ss)
with open('roundsplayed.txt') as round:
    strround = round.read()
roundsplayed = int(strround)
print(roundsplayed)

global int1
stupid = 0
root = tk.Tk()
rockimage = Image.open('rockeeeeeee.jpg')
rockimage = rockimage.resize((113, 64), Image.ANTIALIAS)
roc = ImageTk.PhotoImage(rockimage)
Questionimage = Image.open('Questionmark.jpeg')
Questionimage = Questionimage.resize((113, 103), Image.ANTIALIAS)
question = ImageTk.PhotoImage(Questionimage)
paperimage = Image.open('paper.jpg')
paperimage = paperimage.resize((113, 64), Image.ANTIALIAS)
paperr = ImageTk.PhotoImage(paperimage)
sizorimage = Image.open('sizor.jpg')
sizorimage = sizorimage.resize((113, 64), Image.ANTIALIAS)
sizorr = ImageTk.PhotoImage(sizorimage)
won = 0
lost = 0
root.geometry("540x600")

root.title('sentient toster program')


def clear():
    stupid = 1
    list = root.grid_slaves()
    for l in list:
        l.destroy()


def rat1():
    global rat
    while (rat != 1):
        rat = 1
        rat = 1
        rat = 1
        rat = 1
        rat = 1
        rat = 1
        rat = 1


def rat2():
    global rat
    while (rat != 2):
        rat = 2


def ok():
    lib = tk.Label(root, text="", font="times 36")
    lib.grid(row=0, column=1)
    leeb = tk.Label(root, text="", font="times 36")
    leeb.grid(row=1, column=2)
    leebe = tk.Label(root, text="Rock!", font="times 36")
    leebe.grid(row=1, column=3)
    leab = tk.Label(root, text="", font="times 36")
    leab.grid(row=1, column=4)
    my_ = Label(image=roc)
    my_.label = roc
    my_.grid(row=2, column=9)
    my_im = Label(image=roc)
    my_im.label = roc
    my_im.grid(row=2, column=0)
    root.after(500, my_.destroy)
    root.after(500, my_im.destroy)
    root.after(500, leebe.destroy)
    root.after(500, please)
    root.after(1000, itworks)


def please():
    lib = tk.Label(root, text="", font="times 36")
    lib.grid(row=0, column=1)
    leeb = tk.Label(root, text="", font="times 36")
    leeb.grid(row=1, column=2)
    leebe = tk.Label(root, text="Paper!", font="times 36")
    leebe.grid(row=1, column=3)
    leab = tk.Label(root, text="", font="times 36")
    leab.grid(row=1, column=4)
    my_ = Label(image=paperr)
    my_.label = paperr
    my_.grid(row=2, column=8)
    my_i = Label(image=paperr)
    my_i.label = paperr
    my_i.grid(row=2, column=0)
    root.after(500, my_i.destroy)
    root.after(500, my_.destroy)
    root.after(500, leebe.destroy)


def itworks():
    lib = tk.Label(root, text="", font="times 36")
    lib.grid(row=0, column=1)
    leeb = tk.Label(root, text="", font="times 36")
    leeb.grid(row=1, column=2)
    leebe = tk.Label(root, text="Sissors!", font="times 36")
    leebe.grid(row=1, column=3)
    leab = tk.Label(root, text="           ", font="times 36")
    leab.grid(row=2, column=4)
    my_ = Label(image=sizorr)
    my_.label = sizorr
    my_.grid(row=2, column=0)
    my_i = Label(image=sizorr)
    my_i.label = sizorr
    root.after(500, leebe.destroy)
    my_i.grid(row=2, column=4)
    root.after(500, my_i.destroy)
    root.after(500, my_.destroy)
    root.after(500, start)


def start():
    shoot = tk.Label(root, text="SHOOT!", font="times 36")
    shoot.grid(row=1, column=2)
    im = Label(image=question)
    im.label = question
    im.grid(row=1, column=4)

    def rock():
        print(rat, "rat")
        global lastclick
        global rr
        global pr
        global sr
        global roundsplayed
        global paper
        if (lastclick == 1):
            rr = rr + 1
            rrstr = str(rr)
            file = open("rrsave.txt", "w")
            file.write(rrstr)
            file.close
            print("rr", rr)
        if (lastclick == 2):
            pr = pr + 1
            prstr = str(pr)
            with open('prsave.txt', 'w') as inpr:
                inpr.write(prstr)
            print(pr, "pr")
        if (lastclick == 3):
            sr = sr + 1
            srstr = str(sr)
            file = open("srsave.txt", "w")
            file.write(srstr)
            file.close
            print(sr, "sr")

        global roundsplayed

        global won
        global hi

        global lost
        if (roundsplayed > 20):
            if (lastclick == 1):
                if (rr > rs and rp):

                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (rs > rp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            elif (lastclick == 2):
                if (pr > pp and ps):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (pp > ps):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            elif (lastclick == 3):
                if (sr > sp and ss):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                    weights=(10, 18, 10),
                    k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (ss > sp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                    weights=(18, 10, 10),
                    k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                    weights=(10, 10, 18),
                    k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
        else:
            hi = random.randint(1, 3)
        lastclick = 1
        print(lastclick, "lastclick check 1")
        roundsplayed = roundsplayed + 1
        print(roundsplayed, "roundsplayed")
        strround = str(roundsplayed)
        file = open("roundsplayed.txt", "w")
        file.write(strround)
        file.close

        if (hi == 3):
            lab["text"] = "You wonn! gg"
            won = won + 1
            if won == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU WON!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(GG)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=roc)
                    mime.label = roc
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=sizorr)
                    my_ime.label = sizorr
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())

        elif hi == 1:
            lab["text"] = "You tie!"
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def afterdestroy():
                LOOL = 0
                liiib = tk.Label(root, text="YOU TIE!", font="times 36")
                liiib.grid(row=1, column=2)
                LOL = tk.Label(root, text="(.-.)!!!", font="times 22")
                LOL.grid(row=2, column=2)
                print("rattatiou!")
                mime = Label(image=roc)
                mime.label = roc
                mime.grid(row=2, column=0)
                my_ime = Label(image=roc)
                my_ime.label = roc
                my_ime.grid(row=2, column=7)

                def e():
                    root.after(530, LOL.destroy)
                    root.after(530, mime.destroy())
                    root.after(530, my_ime.destroy())
                    root.after(530, liiib.destroy())
                    root.after(500, ok)

                root.after(20, e)

            root.after(1, afterdestroy())

        else:
            lost = lost + 1
            if lost == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU lost!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(LOL)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=roc)
                    mime.label = roc
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=paperr)
                    my_ime.label = paperr
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())

        print(won, "won")
        print(lost, "lost")
        if (lost == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()

            buttn = tk.Button(root,
                              text="You lost try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                delete()
                ok()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat2()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1
        if (lost == 1 and rat == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You lost ): try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof3()

            buttn["command"] = stupid
            butn["command"] = stupid1
        if (won == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1

        if (won == 1 and rat == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat1()
                bestof3()

            buttn["command"] = stupid
            butn["command"] = stupid1
            lastclick = 1
            print(lastclick, "lastclick")

    def paper():
        global file
        global roundsplayed
        roundsplayed = roundsplayed + 1
        print(roundsplayed, "roundsplayed")
        strround = str(roundsplayed)
        file = open("roundsplayed.txt", "w")
        file.write(strround)
        file.close
        global lastclick

        global won
        global sstrround
        global lost
        global rp
        global pp
        global hi

        global sp
        if (lastclick == 1):
            rp = rp + 1
            rpstr = str(rp)
            file = open("prsave.txt", "w")
            file.write(rpstr)
            file.close
            print("rp", rp)
        if (lastclick == 2):
            pp = pp + 1
            with open('ppsave.txt', 'w') as inpp:
                ppstr = str(pp)
                inpp.write(ppstr)
            print(pp, "pp")
        if (lastclick == 3):
            sp = sp + 1
            spstr = str(sp)
            file = open("pssave.txt", "w")
            file.write(spstr)
            file.close
            print(sp, "sp")

        if (roundsplayed > 20):
            if (lastclick == 1):
                if (rr > rp and rs):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (rp > rs):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            if (lastclick == 2):
                if (pr > pp and ps):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (ps > pp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            if (lastclick == 3):
                if (sr > sp and ss):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (ss > sp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
        else:
            hi = random.randint(1, 3)

        lastclick = 2
        print(hi)
        if (hi == 1):
            won = won + 1
            if won == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU WON!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(GG)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=paperr)
                    mime.label = paperr
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=roc)
                    my_ime.label = roc
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())

        elif (hi == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def afterdestroy():
                LOOL = 0
                liiib = tk.Label(root, text="YOU TIE!!", font="times 36")
                liiib.grid(row=1, column=2)
                LOL = tk.Label(root, text="(.-.)!!!", font="times 22")
                LOL.grid(row=2, column=2)
                print("rattatiou!")
                mime = Label(image=paperr)
                mime.label = paperr
                mime.grid(row=2, column=0)
                my_ime = Label(image=paperr)
                my_ime.label = paperr
                my_ime.grid(row=2, column=7)

                def e():
                    root.after(530, LOL.destroy)
                    root.after(530, mime.destroy())
                    root.after(530, my_ime.destroy())
                    root.after(530, liiib.destroy())
                    root.after(500, ok)

                root.after(20, e)

            root.after(1, afterdestroy())
        else:
            lost = lost + 1
            if lost == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU lost!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(LOL)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=paperr)
                    mime.label = paperr
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=sizorr)
                    my_ime.label = sizorr
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())

        print(won, "won")
        print(lost, "lost")
        if (lost == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You lost ): try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            lastclick = 2
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat2()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1
        if (lost == 1 and rat == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You lost ): try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof3()

            lastclick = 2
            buttn["command"] = stupid
            butn["command"] = stupid1
        if (won == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1

        if (won == 1 and rat == 2):
            list = root.grid_slaves
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset
            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat1()
                bestof3()

            buttn["command"] = stupid
            butn["command"] = stupid1

    def sizor():
        global file
        global strround
        global roundsplayed

        global lastclick

        global won
        global lost
        global ps
        global rs

        global ss
        global hi

        if (lastclick == 1):
            rs = rs + 1
            rsstr = str(rs)
            file = open("rssave.txt", "w")
            file.write(rsstr)
            file.close
            print("rs", rs)
        if (lastclick == 2):
            ps = ps + 1
            spstr = str(ps)
            file = open("pssave.txt", "w")
            file.write(psstr)
            file.close
            print(ps, "ps")
        if (lastclick == 3):
            ss = ss + 1
            ssstr = str(ss)
            file = open("sssave.txt", "w")
            file.write(ssstr)
            file.close
            print(ss, "ss")
        global won
        global lost
        if (roundsplayed > 20):
            if (lastclick == 1):
                if (rr > rs and rp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                     weights=(18, 10, 10),
                     k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (rs > rp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,weights=(10, 18, 10),k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            if (lastclick == 2):
                if (pr > ps and pp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (pp > ps):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
            if (lastclick == 3):
                if (sr > sp and ss):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 18, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                elif (ss > sp):
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(18, 10, 10),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
                else:
                    sampleList = [1, 2, 3]
                    randomList = random.choices(sampleList,
                                                weights=(10, 10, 18),
                                                k=1)
                    thing = ' '.join(map(str, randomList))
                    hi = int(thing)
        else:
            hi = random.randint(1, 3)
        roundsplayed = roundsplayed + 1
        with open('roundsplayed.txt', 'w') as inrounds:
            stringrounds = str(roundsplayed)
            inrounds.write(stringrounds)

        print(hi, "hi")
        if (hi == 1):
            won = won + 1
            if won == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU WON!!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(GG)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=paperr)
                    mime.label = paperr
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=sizorr)
                    my_ime.label = sizorr
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())

        elif (hi == 3):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def afterdestroy():
                LOOL = 0
                liiib = tk.Label(root, text="YOU TIE!", font="times 36")
                liiib.grid(row=1, column=2)
                LOL = tk.Label(root, text="(.-.)!!", font="times 22")
                LOL.grid(row=2, column=2)
                print("rattatiou!")
                mime = Label(image=paperr)
                mime.label = paperr
                mime.grid(row=2, column=0)
                my_ime = Label(image=sizorr)
                my_ime.label = sizorr
                my_ime.grid(row=2, column=7)

                def e():
                    root.after(530, LOL.destroy)
                    root.after(530, mime.destroy())
                    root.after(530, my_ime.destroy())
                    root.after(530, liiib.destroy())
                    root.after(500, ok)

                root.after(20, e)

            root.after(1, afterdestroy())
        else:
            lost = lost + 1
            if lost == 1 and rat == 1:

                list = root.grid_slaves()
                for l in list:
                    l.destroy()

                def afterdestroy():
                    LOOL = 0
                    liiib = tk.Label(root, text="YOU lost!", font="times 36")
                    liiib.grid(row=1, column=2)
                    LOL = tk.Label(root, text="(LOL)!!!", font="times 22")
                    LOL.grid(row=2, column=2)
                    print("rattatiou!")
                    mime = Label(image=paperr)
                    mime.label = paperr
                    mime.grid(row=2, column=0)
                    my_ime = Label(image=sizorr)
                    my_ime.label = sizorr
                    my_ime.grid(row=2, column=7)

                    def e():
                        root.after(530, LOL.destroy)
                        root.after(530, mime.destroy())
                        root.after(530, my_ime.destroy())
                        root.after(530, liiib.destroy())
                        root.after(500, ok)

                    root.after(20, e)

                root.after(1, afterdestroy())
        print(won, "won")
        print(lost, "lost")

        if (lost == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You lost ): try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset

            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat2()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1
        if (lost == 1 and rat == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You lost ): try again!!",
                              font="times 36")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset

            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof3()

            lastclick = 3
            buttn["command"] = stupid
            butn["command"] = stupid1
        if (won == 2 and rat == 1):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()

            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)

            butn = tk.Button(root,
                             text="Switch to best of 1?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0
            bu = tk.Button(root, text="Reset algorithim?", font="times 36")
            bu.grid(row=2, column=0)
            bu["command"] = reset

            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 1
                print(rat)
                rat1()
                bestof1()

            buttn["command"] = stupid
            butn["command"] = stupid1

        if (won == 1 and rat == 2):
            list = root.grid_slaves()
            for l in list:
                l.destroy()

            def delete():
                buttn.destroy()
                butn.destroy()
                bu.destroy()
            buttn = tk.Button(root,
                              text="You won!! Play again?",
                              font="times 34")
            buttn.grid(row=0, column=0)
            butn = tk.Button(root,
                             text="Switch to best of 3?",
                             font="times 36")
            butn.grid(row=1, column=0)
            lost = 0
            won = 0

            def stupid():
                ok()
                delete()

            def stupid1():
                ok()
                delete()
                rat = 2
                print(rat)
                rat1()
                bestof3()

            buttn["command"] = stupid
            butn["command"] = stupid1

    lab = tk.Label(root, text="", font="times 36")
    lab.grid(row=0, column=1)
    lob = tk.Label(root, text="", font="times 36")

    lob.grid(row=1, column=1)

    bton0 = tk.Button(root,
                      text="rock",
                      font="times 36",
                      command=rock,
                      image=roc)
    bton0.grid(row=0, column=0)

    button = tk.Button(root, text="Paper", font="times 36", image=paperr)
    button.grid(row=1, column=0)
    button["command"] = paper

    button = tk.Button(root, text="Sizor?", font="times 36", image=sizorr)
    button.grid(row=2, column=0)
    button["command"] = sizor


button = tk.Button(root, text="Start!(best of 3)", font="times 36")
button.grid(row=0, column=0)
butt = tk.Button(root, text="Start!(best of 1)", font="times 36")
butt.grid(row=1, column=0)
def reset():
  pp = 0
  file = open("ppsave.txt", "w")
  file.write('0')
  file.close
  pr = 0
  file = open("prsave.txt", "w")
  file.write('0')
  file.close
  ps = 0
  file = open("pssave.txt", "w")
  file.write('0')
  file.close
  roundsplayed = 0
  file = open("roundsplayed.txt", "w")
  file.write('0')
  file.close
  rp = 0
  file = open("rpsave.txt", "w")
  file.write('0')
  file.close
  rs = 0
  file = open("rssave.txt", "w")
  file.write('0')
  file.close
  rr = 0
  file = open("rrsave.txt", "w")
  file.write('0')
  file.close
  sr = 0
  file = open("srsave.txt", "w")
  file.write('0')
  file.close
  ss = 0 
  file = open("sssave.txt", "w")
  file.write('0')
  file.close
  sp = 0
  file = open("sp.txt", "w")
  file.write('0')
  file.close
bu = tk.Button(root, text="Reset algorithim?", font="times 36")
bu.grid(row=2, column=0)
bu["command"] = reset
def bestof3():
    clear()
    ok()
    rat = 1


def bestof1():
    clear()
    ok()
    rat = 2
    rat2()
    print(rat, "rat")


button["command"] = bestof3
butt["command"] = bestof1
root.mainloop()
