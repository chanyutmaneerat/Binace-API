
import requests
import json
from pprint import pprint
import time

API_HOST = 'https://api.bitkub.com'


def chek_price():
    alltext = ''
    mycoin = ['THB_BTC','THB_XRP','THB_ETH']
    response = requests.get(API_HOST + '/api/market/ticker' )
    result = response.json()
    #print(result)
    for c in mycoin:
        sym = c
        data = result[sym]
        pchange = data['percentChange']
        text = ('{} => {} pchange ({})'.format(sym,data['last'],pchange))
        alltext += text + '\n'
        v_result.set(alltext)
    print(alltext)
    print('----------------')
    R1.after(1000,chek_price) #เป็นการสั่งให้ refret หน่วยเป็น มิลิเซกกั้น(1 วินาที = 1000 มิลิเซกกั้น)
    # .after เป็นการทำให้ R1 refret ทุก 200 ms

#######GUI################
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x600')
GUI.title('โปรแกรมเช็คราคาจาก Bitkub')
Font1 = ('Angsana New',30)
L1 = ttk.Label(GUI,text = 'ราคา Binace ล่าสุด',font = Font1)
L1.pack()

B1 = ttk.Button(GUI,text='Chek!',command=chek_price)
B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
v_result.set('-------result------')
R1 = ttk.Label(textvariable = v_result,font = Font1)
R1.pack()

GUI.mainloop()




