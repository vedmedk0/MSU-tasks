# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:49:45 2017

@author: VedMedk0
altcontextmanager
"""

from contextlib import contextmanager
import os

@contextmanager
def SafeChdir(path):
    current_dir = os.getcwd()
    os.chdir(path)
    yield 
    os.chdir(current_dir)
    
    


with SafeChdir('C:\\Users\\VedMedk0\\Music'):
    os.getcwd()
    with open('hellou', 'tw', encoding='utf-8') as f:
        pass
    