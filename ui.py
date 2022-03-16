#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import send
import configparser

def click_func():
    send.send()

inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

# ウィンドウ
root = tkinter.Tk()
root.title("メール送信")
root.geometry("400x300")

# 送信ボタン
button = tkinter.Button(
    root,
    text="送信",
    command=click_func
)
button.pack(side="bottom",ipadx="20",ipady="10")

# テキストボックス
txt = tkinter.Entry(
    width=30
)
txt.insert(tkinter.END,inifile.get('template', 'subject'))
txt.place(x=40, y=20)

root.mainloop()
