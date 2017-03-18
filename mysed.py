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
#print("Welcome to SED! If you want open file, print '/o %filename%', if you want write text manually, print '/m': ")
while True: # стартовое меню закроется тогда, когда будет сделан выбор
    
    command = input("Welcome to SED! If you want open file, print '/o %filename%', if you want write text manually, print '/m %text%': ")
    if command[0:2] == '/o': #хотим открыть файл
        with open(command[3:len(command)]) as fin: #контекстный менедджер для безопасного открытия файла
            text = fin.read() #читаем текст из файла
            break #выходим из стартового меню
    elif command[0:2] =='/m': #печатаем сами
        if len(command)<= 2:
            print
        text=command[3:len(command)]
        break
    elif command == '/e': #передумали что-то делать и выходим
        sys.exit()
    else:
        print('Whoops! Wrong command.') #нет такой команды

while True:
    print('welcome! \n If you want to replace string1 with string2 enter /r/string1/string2 \n If you want to exit enter /e')
    command = input()
    if command == '/e':
        break
    elif command[0:2 ]== '/r':
        command=command[3:len(command)].split('/')
        text.replace(command[0],command[1])
        print (text)
    else:
        print('Whoops! Wrong command.')
print ('bye')
    
    
    
    
    
    
