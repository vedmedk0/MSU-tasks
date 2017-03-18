# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:33:48 2017

@author: VedMedk0
"""
import os
    
class SafeChdir():
    
    def __init__(self, newPath):
        self.newPath = newPath #запоминаем новый путь
        print('im gonna change directory!')

    def __enter__(self):
        self.savedPath = os.getcwd() # cохраняем старый путь. self.savedPath - новая переменная в объекте self
        os.chdir(self.newPath) # меняем папку
        print('im changed directory!')

    def __exit__(self, *args):
        os.chdir(self.savedPath) #возвращаемся
        print('im back!')
        
        
        
#test


with SafeChdir('C:\\Users\\VedMedk0\\Music'):
    os.getcwd()
    with open('hello', 'tw', encoding='utf-8') as f: #завести в открытой папке ненужный файл
        pass
    
