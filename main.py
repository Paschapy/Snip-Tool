
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:21:40 2020

@author: akifcal
"""
from opencv import Opencv
from PIL import ImageGrab
import pyautogui,sys

ss=int(pyautogui.prompt(text="SS=1 ||| SS alır",title="SS",default=""))
i=906

if ss==1:
    img=ImageGrab.grab()
    img.save("image.jpg","JPEG")  
    enver=Opencv(i)
    i+=1
    durum=int(pyautogui.prompt(text="Devam edelim mi?",title="Durum",default=""))
    if durum==0:
        pyautogui.alert(text='Kapanıyor', title='ALERT!', button='OK')
        sys.exit()
    tekrar=pyautogui.prompt(text="Tekrar sayısı giriniz.",title="Tekrar",default="")
    tekrar=int(tekrar)
    if tekrar==0:
        pyautogui.alert(text='Kapanıyor', title='ALERT!', button='OK')
        sys.exit()        
    for e in range(tekrar):
        e=i
        i+=1
        img=ImageGrab.grab()
        img.save("image.jpg","JPEG") 
        cv=Opencv(e) 
        step=int(pyautogui.prompt(text="ADIM:{} İleri ||1=>Devam eder /0=>Program kapanır".format(i),title="step",default=""))
        if step > tekrar or step>tekrar-i:
            pyautogui.alert(text='Sidirigit', title='ALERT!', button='OK')
            break
else:
    pyautogui.alert(text='Sidirigit', title='ALERT!', button='OK')
    
        