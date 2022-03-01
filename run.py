import json
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import LEFT
from tkinter.filedialog import askopenfilename

import os

def makeExcel():
    f = open(root.filename, 'r', encoding="utf-8")
    data = json.load(f)
    result = []
    for d in data:
        dic = {}
        dic['name'] = d['name']
        attribute = d['attributes']
        
        for a in attribute:
            dic[a['trait_type']] = a['value']
        result.append(dic)
        
    df = pd.DataFrame(result)
    print(df)
    setProgressBar(100)
    DonePopup()
    head, tail = os.path.split(root.filename)
    filename, file_extension = os.path.splitext(tail)
    df.to_csv(os.path.basename(filename) + "_result.csv", index = False, header=True)
    
root = Tk()

root.geometry("400x600")
root.resizable(False, False)
root.title("NFT metadata to Excel")

wrapper1 = LabelFrame(root)
wrapper2 = LabelFrame(root)
wrapper3 = LabelFrame(root)

my_label = Label(wrapper1, text="")
my_label.pack(side=LEFT,fill="x", padx=10, pady=5)

active_btn1 = Button(wrapper3, text="Start", command=makeExcel, padx=15)
active_btn1["state"] = "disabled"
active_btn1.pack(side=RIGHT, padx=5, pady=10)

def SetLabel1(text):
    my_label.configure(text=text)
def SelectFile():
    root.filename = askopenfilename(initialdir="./", title="Select A _metadata.json", filetypes=(("json files", "*.json"),("all files","*.*")))
    if root.filename:
        active_btn1["state"] = "normal"
        SetLabel1(root.filename)

browse_btn1 = Button(wrapper1, text="browse", command=SelectFile)
browse_btn1.pack(side=RIGHT, padx=5, pady=5)

mycanvas = Canvas(wrapper2)
mycanvas.pack(side=LEFT, fill=Y, expand="yes")

yscrollbar = ttk.Scrollbar(wrapper2, orient="vertical", command=mycanvas.yview)
yscrollbar.pack(side=RIGHT, fill="y")
mycanvas.configure(yscrollcommand=yscrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))

myFrame = Frame(mycanvas)
mycanvas.create_window((0,0), window=myFrame, anchor="nw")
# myFrame.pack()

my_progress = ttk.Progressbar(wrapper3, orient=HORIZONTAL,length=300, mode='determinate')
my_progress.pack(side=LEFT, pady=10)

def ClosePopup():
    pop.destroy()
    os.startfile('')
    root.destroy()
def DonePopup():
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    win_x = root_x + 130
    win_y = root_y + 100
    global pop
    pop = Toplevel(root)
    pop.title("SUCCESS!")
    # pop.geometry("150x100")
    pop.geometry(f'150x100+{win_x}+{win_y}')  

    pop_label = Label(pop, text="SUCCESS!")
    pop_label.pack(pady=10)

    pop_btn = Button(pop, text="Close", command=ClosePopup)
    pop_btn.pack(pady=10)

def LoggerLogs(text):
    Label(myFrame, text=text).pack()
    mycanvas.yview_moveto('1.0')
    
def setProgressBar(value):
    my_progress['value'] = value


wrapper1.pack(fill='both', expand="yes", padx=10, pady=10)
wrapper2.pack(fill='both', expand="yes", padx=10, pady=10)
wrapper3.pack(fill='both', expand="yes", padx=10, pady=10)
# root.iconbitmap('./icon.ico')
root.mainloop()


