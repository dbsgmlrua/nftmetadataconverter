import json
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.constants import LEFT
from tkinter.filedialog import askopenfilename

import os

def makeExcel(data):
    result = []
    for d in data:
        dic = {}
        dic['name'] = d['name']
        attribute = d['attributes']
        
        for a in attribute:
            dic[a['trait_type']] = a['value']
        result.append(dic)
    
    return result
    
if __name__ == "__main__":
    f = open('_metadata.json')
    jsondata = json.load(f)
    result = makeExcel(jsondata)
    df = pd.DataFrame(result)
    print(df)

    df.to_csv('result.csv', index = False, header=True)

