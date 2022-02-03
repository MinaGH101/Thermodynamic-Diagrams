# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 13:51:27 2022

@author: Mahdiyar
"""

import numpy as np
import pandas as pd
import sympy as sp
from sympy import *
import os
import matplotlib.pyplot as plt
from tkinter import filedialog

import tkinter as tk
from tkinter import *

class Draw(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('ΔG_M Diagram')
    self.geometry("800x500")
     
    self.v1 = tk.IntVar()
    self.v2 = tk.IntVar()
    self.v3 = tk.IntVar()
    self.v4 = tk.IntVar()
    self.v5 = tk.IntVar()
    self.v6 = tk.IntVar()
    self.v7 = tk.IntVar()
    self.v8 = tk.IntVar()
    self.v9 = tk.StringVar()
    self.v10 = tk.IntVar()
     
    # self.v1.trace_add("write", self.draw_dGM)
    # self.v2.trace_add("write", self.draw_dGM)
    # self.v3.trace_add("write", self.draw_dGM)
    # self.v4.trace_add("write", self.draw_dGM)
    # self.v5.trace_add("write", self.draw_dGM)
    # self.v6.trace_add("write", self.draw_dGM)
    # self.v7.trace_add("write", self.draw_dGM)
    # self.v8.trace_add("write", self.draw_dGM)
    # self.v9.trace_add("write", self.draw_dGM)
    # self.v10.trace_add("write", self.draw_dGM)
    
    self.create_widgets()
    self.myButton()
    self.path()
    
  def create_widgets(self):
    self.v1_label = tk.Label(self, text="Component A melting Temp (K)")
    self.v2_label = tk.Label(self, text="Component B melting Temp (K)")
    self.v3_label = tk.Label(self, text="Component A ΔH (J)")
    self.v4_label = tk.Label(self, text="Component A ΔS (J)")
    self.v5_label = tk.Label(self, text="Component B ΔH (J)")
    self.v6_label = tk.Label(self, text="Component B ΔS (J)")
    self.v7_label = tk.Label(self, text="Ω_A (J)")
    self.v8_label = tk.Label(self, text="Ω_B (J)")
    self.v9_label = tk.Label(self, text="path to save diagrams (example: C:/Users/User/Desktop/diagrams)")
    self.v10_label = tk.Label(self, text="number of diagrams to draw")

       
    self.v1_entry = tk.Entry(self, textvariable=self.v1)
    self.v2_entry = tk.Entry(self, textvariable=self.v2)
    self.v3_entry = tk.Entry(self, textvariable=self.v3)
    self.v4_entry = tk.Entry(self, textvariable=self.v4)
    self.v5_entry = tk.Entry(self, textvariable=self.v5)
    self.v6_entry = tk.Entry(self, textvariable=self.v6)
    self.v7_entry = tk.Entry(self, textvariable=self.v7)
    self.v8_entry = tk.Entry(self, textvariable=self.v8)
    self.v9_entry = tk.Entry(self, textvariable=self.v9, width=40)
    self.v10_entry = tk.Entry(self, textvariable=self.v10)
       

    self.v1_label.grid(row=0, column=0, padx=5, pady=5)
    self.v1_entry.grid(row=0, column=1, padx=5, pady=5)
    self.v2_label.grid(row=1, column=0, padx=5, pady=5)
    self.v2_entry.grid(row=1, column=1, padx=5, pady=5)
    self.v3_label.grid(row=2, column=0, padx=5, pady=5)
    self.v3_entry.grid(row=2, column=1, padx=5, pady=5)
    self.v4_label.grid(row=3, column=0, padx=5, pady=5)
    self.v4_entry.grid(row=3, column=1, padx=5, pady=5)
    self.v5_label.grid(row=4, column=0, padx=5, pady=5)
    self.v5_entry.grid(row=4, column=1, padx=5, pady=5)
    self.v6_label.grid(row=5, column=0, padx=5, pady=5)
    self.v6_entry.grid(row=5, column=1, padx=5, pady=5)
    self.v7_label.grid(row=6, column=0, padx=5, pady=5)
    self.v7_entry.grid(row=6, column=1, padx=5, pady=5)
    self.v8_label.grid(row=7, column=0, padx=5, pady=5)
    self.v8_entry.grid(row=7, column=1, padx=5, pady=5)
    self.v9_label.grid(row=8, column=0, padx=5, pady=5)
    # self.v9_entry.grid(row=8, column=1, padx=5, pady=5)
    self.v10_label.grid(row=9, column=0, padx=5, pady=5)
    self.v10_entry.grid(row=9, column=1, padx=5, pady=5)
      
      
  def browse_button(self):
    self.filename = filedialog.askdirectory()
    # folderPath.set(self.filename)
    # self.la = Label(self, text=self.filename, textvariable=StringVar()).grid(row=8,column=2)
    
  def path(self):
    self.button2 = Button(self, text="Browse", command=self.browse_button)
    self.button2.grid(row=8, column=1)

  def draw_dGM(self, *args):
    TmA=self.v1.get()
    TmB=self.v2.get()
    HA=self.v3.get()
    SA=self.v4.get()
    HB=self.v5.get()
    SB=self.v6.get()
    Ol=self.v7.get()
    Os=self.v8.get()
    path=self.filename
    n_diagrams=self.v10.get()
    X = list(np.arange(0,1,0.01))
    T = list(np.arange(TmA,TmB, (TmB-TmA)/(n_diagrams)))
    def dGmA(T):
        dGm1 = HA-SA*T
        return dGm1
    def dGmB(T):
        dGm2 = HB-SB*T
        return dGm2
    def dGMl(XA, T , Ol):
        dGM = ((1-XA)*(dGmB(T))) + (8.3*T*((XA*ln(XA))+((1-XA)*ln(1-XA)))) + (Ol*XA*(1-XA))
        return dGM
    def dGMs(XA, T , Os):
        dGM = (-1)*(XA*(dGmA(T))) + (8.3*T*((XA*ln(XA))+((1-XA)*ln(1-XA)))) + (Os*XA*(1-XA))
        return dGM
    for j in range(len(T)):
        dGl = []
        dGs = []
        for i in range(len(X)):
            dGl.append(dGMl(1-X[i], T[j],Ol))
            dGs.append(dGMs(1-X[i], T[j],Os))
        plt.figure(figsize=(4,7))
        plt.plot(X , dGl, linewidth=2.0 , color='m')
        plt.plot(X, dGs,linewidth=2.0 , color= 'c')
        #plt.ylim(0, 3)
        plt.xlim(0, 1)
        a = 'T = '
        b = str(int(T[j]))
        c = 'K'
        plt.title(a+b+c)
        plt.ylabel('dGM(J)')
        plt.xlabel('XB')
        plt.legend(['liquid', 'solid'], loc='upper left')
        path1 = path
        name = str(int(T[j]))
        file = plt.savefig(fname=os.path.join(path1, name))
        # plt.show()
            
  def myButton(self):
    self.butt = Button(self, text='Draw Diagrams!' , command = self.draw_dGM)
    self.butt.grid(row=11, column=1)
      
      
if __name__ == "__main__":
  app = Draw()
  app.mainloop()     
      
      
      
      
      

      
      
      
      
      
      
      
      
      
      
      
      
      
