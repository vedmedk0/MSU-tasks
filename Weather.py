# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 15:44:23 2017

@author: VedMedk0
"""
import requests as rs
import datetime as dt
import pandas as pd

def GetDatafrom(time):#возвращает давление, температуру, влажность по дате
    if time.hour ==0: hour='00' #если час ==0 то страничка выдаст ошибку
    else: hour=str(time.hour)
    sitenamewithdate='http://meteoinfo.ru/archive-pogoda/russia/moscow-area/moscow/' + str(time.year) + '/'+ str(time.month) + '/' + str(time.day) + '/' + hour
    #очень длинная строка для формирования ссылки на страницу
    raws = rs.get(sitenamewithdate).text #запрос возвращает страницу в виде текста
    raws=raws.split('<td class=pogodacell>') #выбор такого параметра разделения
                                             #позволяет легко достать данные
    pressure=int(raws[1][0:3]) #достаем давление
    
#    if raws[2][3]=='-': temperature=float(raws[2][3:7]) #если минус, то достаем 
#    else: temperature=float(raws[2][3:6]) #меньше символов
    temperature=raws[2].split('<',2)[1]
    temperature=float(temperature.split('>',2)[1])
    
    StrangeTime = time.hour==21 or time.hour==9 or time.hour==6 #почему-то в эти часы сайт выдает лишнюю инфу, 
    if StrangeTime: humidity =int(raws[4].split('<',1)[0]) # нужно влажность доставать по-другому
    else: humidity=int(raws[3].split('<',1)[0])
    return (pressure,temperature,humidity)

def PastWeatherData (days_ago):
    DT=dt.timedelta(hours=3) #данные обновляются каждые 3 часа
    now = dt.datetime.now() #настоящее время
    now = now.replace(second=0,minute=0,hour=now.hour-now.hour % 3) #часы должны быть кратны трем
    now=now-2*DT #Погода обновляется через 3 часа
    startdate=now-8*days_ago*DT #с какого дня хотим начать выкачивать
    startdate=startdate.replace(hour=0) # имеет смысл достать данные с начала дня
    dateindex=pd.date_range(start=startdate,  end=now, freq='3H') #индекс датафрейма
    columns = ['Pressure','Temperature', 'Humidity'] #колонки
    Weather_data = pd.DataFrame(index=dateindex,columns=columns)#иниц датафрейма
    for time in dateindex: #для всех дат
        Weather_data.loc[time]=GetDatafrom(time)#каждой строке - по три цифры    
    return Weather_data #возвращаем датафрейм

data=PastWeatherData(15)
#%%
data.to_csv('Weatherdataa.csv', sep=',') #сохраняем как csv
#%matplotlib qt
data.plot(subplots=True, figsize=(6, 6))



