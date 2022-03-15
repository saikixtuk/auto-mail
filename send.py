#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:36:51 2022

@author: hikaru
"""

import smtplib
import configparser
from email.mime.text import MIMEText
from email.header import Header

# 設定ファイル読み込み
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')

# ユーザネーム、パスワード、送信元メールアドレス、宛先メールアドレス
password = inifile.get('setting', 'user_password')
from_address = inifile.get('setting', 'from_address')
to_address = inifile.get('template', 'to_address')


# メール件名、本文
subject = inifile.get('template', 'subject')
text = inifile.get('template', 'text')

# MIMETextオブジェクトの生成
charset = 'utf-8'
msg = MIMEText(text, 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address

# SMTPサーバへの接続、暗号化、ログイン、送信、切断
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(inifile.get('setting', 'user_name'), password)
server.send_message(msg)
server.quit()
