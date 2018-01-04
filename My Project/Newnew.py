import tkinter as tk


buttonState = 0
bg0 = "white smoke"
bg1 = "light salmon"
bg2 = "spring green"

#####SHIT############
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


##########################




"""def input_update1(inputVar, outputVar):
    def closure(*args):
        var1 = inputVar.get()
        outputVar.set(var1)
    return closure"""

def buttonPress():
    global buttonState
    global bg1
    global bg2
    
    if buttonState == 0: 

        var1 = val_part1.get().replace(',', '.')
        var2 = val_part2.get().replace(',', '.')
        var3 = val_part3.get().replace(',', '.')
        var4 = val_cont1.get().replace(',', '.')
        var5 = val_cont2.get().replace(',', '.')
        var6 = val_cont3.get().replace(',', '.')
        
        if var1== "":
            try:
                a1 = (float(var3)*float(var6)-float(var2)*float(var5))/float(var4)
                val_part1.set(round(a1,4))#("{0:.4f}".format(a1))
                particles1.config(bg=bg2)
            except:
                try:
                    a1 = (float(var3)*(float(var4)+float(var5))-float(var2)*float(var5))/float(var4)
                    val_part1.set(round(a1,4))#("{0:.4f}".format(a1))
                    particles1.config(bg=bg2)
                except:
                    val_part1.set("WRONG")
                    particles1.config(bg=bg1)

        if var2== "":
            try:
                a2 = (float(var3)*float(var6)-float(var1)*float(var4))/float(var5)
                val_part2.set(round(a2,4))#("{0:.4f}".format(a2))
                particles2.config(bg=bg2)
            except:
                try:
                    a2 = (float(var3)*(float(var4)+float(var5))-float(var1)*float(var4))/float(var5)
                    val_part2.set(round(a2,4))#("{0:.4f}".format(a2))
                    particles2.config(bg=bg2)
                except:
                    val_part2.set("WRONG")
                    particles2.config(bg=bg1)

        if var3== "":
            try:
                a3 = (float(var1)*float(var4)+float(var2)*float(var5))/float(var6)
                val_part3.set(round(a3,4))#("{0:.4f}".format(a3))
                particles3.config(bg=bg2)
            except:
                try:
                    a3 = (float(var1)*float(var4)+float(var2)*float(var5))/(float(var4)+float(var5))
                    val_part3.set(round(a3,4))#("{0:.4f}".format(a3))
                    particles3.config(bg=bg2)
                except:
                    val_part3.set("WRONG")
                    particles3.config(bg=bg1)

        if var4== "":
            try:
                a4 = float(var6)-float(var5)
                val_cont1.set(round(a4,4))#("{0:.4f}".format(a4))
                container1.config(bg=bg2)
            except:
                try:
                    a4 = ((float(var2)-float(var3))*float(var5))/(float(var3)-float(var1))
                    val_cont1.set(round(a4,4))#("{0:.4f}".format(a4))
                    container1.config(bg=bg2)
                except:
                    val_cont1.set("WRONG")
                    container1.config(bg=bg1)

        if var5== "":
            try:
                a5 = float(var6)-float(var4)
                val_cont2.set(round(a5,4))#("{0:.4f}".format(a5))
                container2.config(bg=bg2)
            except:
                try:
                    a5 = ((float(var3)-float(var1))*float(var4))/(float(var2)-float(var3))
                    val_cont2.set(round(a5,4))#("{0:.4f}".format(a5))
                    container2.config(bg=bg2)
                except:
                    val_cont2.set("WRONG")
                    container2.config(bg=bg1)

        if var6== "":
            try:
                a6 = float(var4)+float(var5)
                val_cont3.set(round(a6,4))#("{0:.4f}".format(a6))
                container3.config(bg=bg2)
            except:
                try:
                    a6 = (float(var1)*(((float(var2)-float(var3))*float(var5))/(float(var3)-float(var1)))+float(var2)*float(var5))/float(var3)
                    val_cont3.set(round(a6,4))#("{0:.4f}".format(a6))
                    container3.config(bg=bg2)
                except:
                    try:
                        a6 = (float(var1)*float(var4)+float(var2)*(((float(var3)-float(var1))*float(var4))/(float(var2)-float(var3))))/float(var3)
                        val_cont3.set(round(a6,4))#("{0:.4f}".format(a6))
                        container3.config(bg=bg2)
                    except:
                        val_cont3.set("WRONG")
                        container3.config(bg=bg1)
                    
                
        btntxt.set("RESET")
        buttonState = 1
        button.config(bg=bg1)

    else:
        val_part1.set("")
        val_cont1.set("")
        val_part2.set(0)
        val_cont2.set("")
        val_part3.set("")
        val_cont3.set("")
        btntxt.set("GO")
        buttonState = 0
        button.config(bg=bg2)

        particles1.config(bg=bg0)
        particles2.config(bg=bg0)
        particles3.config(bg=bg0)
        container1.config(bg=bg0)
        container2.config(bg=bg0)
        container3.config(bg=bg0)
        
    

#refferences the main window
root = tk.Tk()
root.geometry('700x450')
root.resizable(width=False, height=False)


#changes the left icon
root.iconbitmap(resource_path("my_icon.ico"))

#changes the window Title
root.title("Dilution Calculator")


#background
background_image = tk.PhotoImage(file=resource_path("bcgr.png"))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


##############################

val_part1 = tk.StringVar()
#val_outpart1 = tk.StringVar()
val_cont1 = tk.StringVar()
#val_outcont1 = tk.StringVar()
#val_part1.trace('w', input_update1(val_part1, val_outpart1))
#val_cont1.trace('w', input_update1(val_cont1, val_outcont1))

val_part2 = tk.StringVar(value =0)
#val_outpart2 = tk.StringVar(value=0)
val_cont2 = tk.StringVar()
#val_outcont2 = tk.StringVar()
#val_part2.trace('w', input_update1(val_part2, val_outpart2))
#val_cont2.trace('w', input_update1(val_cont2, val_outcont2))

val_part3 = tk.StringVar()
#val_outpart3 = tk.StringVar()
val_cont3 = tk.StringVar()
#val_outcont3 = tk.StringVar()
#val_part3.trace('w', input_update1(val_part3, val_outpart3))
#val_cont3.trace('w', input_update1(val_cont3, val_outcont3))

####################################
aa = tk.Frame (root)
aa.grid(row=0, column=0, padx= 39, pady = 87)


particles1 = tk.Entry(root, textvariable=val_part1, bg=bg0, justify="center", width=9, font=("Helvetica", 22))
particles1.grid(row=1, column=1, pady=10)
particles1.focus()
#outpart1 = tk.Label(root, textvariable=val_outpart1, justify="center", width=9, font=("Helvetica", 22))
#outpart1.grid(row=3, column=1)
container1 = tk.Entry(root, textvariable=val_cont1, bg=bg0, justify="center", width=9, font=("Helvetica", 22))
container1.grid(row=2, column=1, )
#outcont1 = tk.Label(root, textvariable=val_outcont1, justify="center", width=9, font=("Helvetica", 22))
#outcont1.grid(row=4, column=1)

particles2 = tk.Entry(root, textvariable=val_part2, bg=bg0,justify="center", width=9, font=("Helvetica", 22))
particles2.grid(row=1, column=3, padx = 57)
#outpart2 = tk.Label(root, textvariable=val_outpart2, justify="center", width=9, font=("Helvetica", 22))
#outpart2.grid(row=3, column=3)
container2 = tk.Entry(root, textvariable=val_cont2, bg=bg0,justify="center", width=9, font=("Helvetica", 22))
container2.grid(row=2, column=3)
#outcont2 = tk.Label(root, textvariable=val_outcont2, justify="center", width=9, font=("Helvetica", 22))
#outcont2.grid(row=4, column=3)

particles3 = tk.Entry(root, textvariable=val_part3, bg=bg0,justify="center", width=9, font=("Helvetica", 22))
particles3.grid(row=1, column=5)
#outpart3 = tk.Label(root, textvariable=val_outpart3, justify="center", width=9, font=("Helvetica", 22))
#outpart3.grid(row=3, column=5)
container3 = tk.Entry(root, textvariable=val_cont3, bg=bg0,justify="center", width=9, font=("Helvetica", 22))
container3.grid(row=2, column=5)
#outcont3 = tk.Label(root, textvariable=val_outcont3, justify="center", width=9, font=("Helvetica", 22))
#outcont3.grid(row=4, column=5)

###########################################
#a = tk.Label(root, text="Tekućina1", justify="center", width=8, font=("Helvetica", 22))
#a.grid(row=0, column=1, pady = 60)
#b = tk.Label(root, text="Tekućina2", justify="center", width=8, font=("Helvetica", 22))
#b.grid(row=0, column=3)
#c = tk.Label(root, text="Tekućina3", justify="center", width=8, font=("Helvetica", 22))
#c.grid(row=0, column=5)
#d = tk.Label(root, text="+", justify="center",  font=("Helvetica", 52))
#d.grid(row=1, column=2, rowspan=2, padx = 5)
#e = tk.Label(root, text="=", justify="center",  font=("Helvetica", 52))
#e.grid(row=1, column=4, rowspan=2, padx = 5)

#pt1 = tk.Label(root, text="%", justify="center",  font=("Helvetica", 22))
#pt1.grid(row=1, column=0, pady=10, padx = 25)
#cn1 = tk.Label(root, text="L", justify="center",  font=("Helvetica", 22))
#cn1.grid(row=2, column=0)
"""opt1 = tk.Label(root, text="", justify="center",  font=("Helvetica", 22))
opt1.grid(row=3, column=0)
ocn1 = tk.Label(root, text="", justify="center",  font=("Helvetica", 22))
ocn1.grid(row=4, column=0)"""

###################################
btntxt = tk.StringVar()
btntxt.set("GO")

button = tk.Button(root, textvariable=btntxt, bg= bg2, command = buttonPress, justify="center", width=8, font=("Helvetica", 22))

button.grid(row=3, column=3,  pady = 60)





###################################

"""frame2 = tk.Frame(root)
frame2.place(x=250, y = 100)

output = tk.StringVar(value = 0.00)
out_lbl = tk.Label(root, textvariable=output, bg="DeepSkyBlue4", fg = "white", font=("Helvetica", 92))
out_lbl.place(x=100,y=235)

smil_img0 = tk.PhotoImage(file="smil0.png")
smiley_label = tk.Label(root, image=smil_img0)
smiley_label.place(x=68, y=smiley_y)

input1 = tk.StringVar()
input1.trace('w', input1_update)

entry = tk.Entry(frame2, textvariable=input1, justify="right", bg="black", foreground="white", width = 4, font=("Helvetica", 72))
entry.pack()
entry.focus() #sets focus immediately onto the textbox"""

#makes the program loop
root.mainloop()
