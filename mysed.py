# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 23:37:16 2017

@author: VedMedk0
"""

import sys

class WrongFileCommand(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

#right_input = True
text=''
print("Welcome to SED! If you want open file, print '/o %filename%' \n If you want write text manually, enter '/m %text%' \n If you want to see help enter /h \n if you want to exit enter /e : ")
#print("Welcome to SED! If you want open file, print '/o %filename%', if you want write text manually, print '/m': ")
    
while True:
    command = input()
    if command == '/e': #хотим выйти
        break
    elif command[0:2] == '/o': #хотим открыть файл
        with open(command[3:len(command)]) as fin: #контекстный менедджер для безопасного открытия файла
            text = fin.read() #читаем текст из файла
    elif command[0:2] =='/m': #печатаем сами
        if len(command)<= 2:
            print ('sorry! no text here')
        else:
            text=command[3:len(command)]
    elif command[0:2 ]== '/r': #хотим заменить
        command=command[3:len(command)].split('/')
        if len(command) == 1:   # если второй аргумент пустой
            text=text.replace(command[0],'')
        else:
            text=text.replace(command[0],command[1])
        print (text)
    elif command == '/p': #посмотреть редактируемый текст
        print(text)
    elif command[0:2] == '/s': #coхранить в файл
        with open(command[3:len(command)], 'tw', encoding='utf-8') as f: #завести в открытой папке ненужный файл
            f.write(text)
    elif command[0:2] == '/h': #помощь
        print('Replace string1 with string2(or nothing, if empty) : /r/string1/string2 \n Exit: /e \n Print: /p \n Save: /s %filename%')
    else:
        print('Whoops! Wrong command.')
print ('bye')
    
    
    
    
    
    