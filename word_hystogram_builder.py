# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 00:17:24 2017

@author: VedMedk0
"""

def WordHystogramBuilder(*args):
    
    text=''
    Hyst=dict()
    for file in args: #для всех файлов - в этом цикле составляем словарь
        with open(file) as fin: #контекстный менедджер для безопасного открытия файла
            text = fin.read() #читаем текст из файла
        text=text.split(' ') # превращаем текст в список слов
        for word in text: # добавляем слова в словарь
            if word in Hyst: #Если есть слово увеличиваем счетчик словарь
                Hyst[word] += 1
            else: #если нет - заводим новую пару
                Hyst[word]=1
    Hyst=Invert_Dict(Hyst) #Инвертируем словарь для удобного вывода
    with open('WordHyst.txt', 'tw', encoding='utf-8') as f: #завести в открытой папке ненужный файл
        for i in sorted(Hyst.keys(),reverse=True): #i проходит по всем значениям в порядке убывания
            f.write(str(i)) #пишем в файл кол-во слов
            f.write(':')
            f.write(str(Hyst.get(i)))
            f.write('\n')
            
def Invert_Dict(d): #функция инверсии словаря
    inv = dict()
    for key in d: #для всех ключей в d
        val = d[key] # значение по ключу в val в d - будущий ключ
        if val not in inv:inv[val] = [key] # если ключа val нет в inv - завести и 
        else:inv[val].append(key) #если есть - добавить значение к текущим
    return inv

WordHystogramBuilder('test.txt', 'test1.txt','test2.txt')