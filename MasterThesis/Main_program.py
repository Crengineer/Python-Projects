# -*- coding: utf-8 -*-
"""

@author: Marco

"""
#%%
#########################################################################################################################################################################################################################################

import sys

def control_packages():
    packages = ["numpy",
                "seaborn",
                "scipy",
                "os",
                "pandas",
                "matplotlib",
                "seaborn",
                "datetime",
                "xlsxwriter",
                "sklearn",
                "tkinter",
                "PIL",
                "sys",
                "subprocess",
                "pyautogui",
                "pythermalcomfort",
                "json",
                "requests",
                "PIL",
                "pyowm",
                "glob",
                "sysidentpy",
                "statsmodels",
                "xlrd",
                "openpyxl",
                "calendar",
                "tkscrolledframe",
                "math"]
    for f in packages:
        if f in sys.modules:
            print()
        else:
            #subprocess.check_call([sys.executable, "-m", "pip", "install", f])
            import importlib
            try:
                importlib.import_module(f)
            except ImportError:
                import pip
                pip.main(['install', f])
            finally:
                globals()[f] = importlib.import_module(f)
    return None

control_packages() #Function used to check if in the computer are present some modules that are not installed yet, 
                   #and then install them after the checking

#########################################################################################################################################################################################################################################
#%%
import subprocess
import scipy
import os
import glob
import pandas as pd
from pandas import Series
from pandas import DataFrame
from matplotlib import pyplot as plot
from matplotlib import figure
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta, timezone, date
import xlsxwriter
from scipy import stats
from sklearn import preprocessing
from scipy.stats import pearsonr
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *
from tkinter import colorchooser
import tkinter.font
from tkinter.ttk import *
from PIL import *
from PIL import ImageTk, Image 
import pyglet
import pyautogui
import json
import requests
from pyowm.owm import OWM
from pyowm.utils import timestamps, formatting
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import asksaveasfile 
from Support_functions import *
import pythermalcomfort
import sysidentpy
import statsmodels
import xlrd
import openpyxl
from sklearn.metrics import r2_score
import calendar
from scipy.stats import chi2_contingency
from tkscrolledframe import ScrolledFrame
import math

#%%

# FIRST WINDOW 

def main(root, FFont):
    
    #FRAMES
    
    frame0 = tk.LabelFrame(root, text = "Graphical User Interface", bg = '#1a8cff', font = FFont)
    frame0.place(x = 0, y = 0, height = 100, width = 1300) 
    
    txt = tk.Text(frame0, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "Hello! Here is the Graphical User Interface for Data Visualization. You can load datasets and display them.\n In this panel, you can choose which operation to perform among: Data Visualisation, in the first upper left panel, the Weather Forecasting in the lower left panel and Data Analysis in the lower right panel.\n In the right part, the chosen dataset will be displayed with its own statistics, column by column")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 100, width = 1300)   
    frame = tk.LabelFrame(root, text = "Data representation window", bg = '#1a8cff', font = FFont)
    frame.place(x = 700, y = 100, height = 300, width = 600)
    frame2 = tk.LabelFrame(root, text = "Data selector", bg='#1a8cff', font = FFont)
    frame2.place(height = 300, width = 700, x = 0, y = 100)
    frame3 = tk.LabelFrame(root, text = "Statistics", bg='#1a8cff', font = FFont)
    frame3.place(height = 300, width = 600, x =700, y = 400)
    frame4 = tk.LabelFrame(root, text = "Data Analysis", bg='#1a8cff', font = FFont)
    frame4.place(height = 300, width = 400, x =300, y = 400)
    frame5 = tk.LabelFrame(root, text = "Weather Forecast", bg='#1a8cff', font = FFont)
    frame5.place(height = 300, width = 300, x =0, y = 400)
    
    label_file = tk.Label(frame2, text = "No file selected", bg = '#b3d9ff', font = FFont, relief="groove")
    label_file.place(x = 25, y = 75)

    # TREEVIEW

    tv1 = ttk.Treeview(frame)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame, orient = "vertical", command = tv1.yview)
    treescrollx = tk.Scrollbar(frame, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")

    tv2 = ttk.Treeview(frame3)
    tv2.place(relheight=1, relwidth=1)

    treescrolly2 = tk.Scrollbar(frame3, orient = "vertical", command = tv2.yview)
    treescrollx2 = tk.Scrollbar(frame3, orient = "horizontal", command= tv2.xview)
    tv2.configure(xscrollcommand = treescrollx2.set, yscrollcommand = treescrolly2.set)
    treescrollx2.pack(side="bottom", fill = "x")
    treescrolly2.pack(side="right", fill = "y")
    
    #BUTTONS
    
    button1 = tk.Button(frame2, text = "Browse a file", bg = '#b3d9ff', font = FFont, command =lambda: File_dialog(label_file)) #Open the window directory
    button1.place(x = 25, y = 25)

    button2 = tk.Button(frame2, text = "Load a file", bg = '#b3d9ff', font = FFont, command = lambda: Load_excel_data(label_file, tv1, tv2, frame, frame2, frame3))
    button2.place(x = 125, y = 25)
    
    button5 = tk.Button(frame5, text = "Weather Prediction Part", bg = '#b3d9ff', font = FFont, command = lambda: Weather_Forecast(label_file))
    button5.place(x = 0, y = 25)
    
    label_title = tk.Label(frame4, text = "Options", bg = '#b3d9ff', font = FFont, relief="groove")
    label_title.place(x = 25, y = 25)
    
    LD = ["Thermal sensation analysis frame", 
          "Testing frame", 
          "Correlation analysis frame",
          "Preprocessing analysis frame"]
    
    Combo0 = ttk.Combobox(frame4, values = LD, width = 50)
    Combo0.place( x = 25, y =  100)
    
    buttonopt = tk.Button(frame4, text = "Select option", bg = '#b3d9ff', font = FFont, command = lambda: Analysis_menus(label_file, Combo0))
    buttonopt.place(x = 25, y = 150)
    
    
    return None

def Analysis_menus(label_file, Combo0):
    sel = Combo0.get()
    if sel == "Thermal sensation analysis frame":
        Diagnostic_part(label_file)
    if sel == "Testing frame":
        Analysis_part(label_file)
    if sel == "Correlation analysis frame":
        Correlation_part(label_file)
    if sel == "Preprocessing analysis frame":
        Preprocessing_part(label_file)
    
    return None

def Weather_Forecast(label_file):
    owm = OWM(api_key)
    mgr = owm.weather_manager()

    window1 = tk.Toplevel(root)
    window1.geometry("1400x700")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame = tk.LabelFrame(window1, text = "Weather Forecast window", bg = '#1a8cff', font = FFont)
    frame.place(x = 0, y = 0, height = 700, width = 1400)
    frame1 = tk.LabelFrame(frame, text = "Future days prediction", bg = '#1a8cff', font = FFont)
    frame1.place(x = 600, y = 0, height = 350, width = 800)
    frame2 = tk.LabelFrame(frame, text = "Next hours prediction", bg = '#1a8cff', font = FFont)
    frame2.place(x = 0, y = 300, height = 350, width = 600)
    frame3 = tk.LabelFrame(frame, text = "Weather forecasting", bg = '#1a8cff', font = FFont)
    frame3.place(x = 600, y = 350, height = 325, width = 800)
    
    #WEATHER PART
    
    title =  tk.Label(frame, text = 'Type the city you desire (first letter must be capital)\n and continue with analysis',  bg = '#b3d9ff', font = FFont, relief="groove")
    title.place(x = 0, y = 0)

    cit=StringVar()

    today = datetime.now() 
    date = tk.Label(frame, text=today.strftime('%A--'), bg='#b3d9ff', font = FFont) 
    date.place(x=0, y=50) 
    month = tk.Label(frame, text=today.strftime('%m %B'), bg='#b3d9ff', font = FFont) 
    month.place(x=100, y=50) 

    # Time 
    hour = tk.Label(frame, text=today.strftime('%I : %M %p'), 
             bg='#b3d9ff', font = FFont) 
    hour.place(x=0, y=75) 
    # City Search 
    hour = tk.Label(frame, text='Select the city:', bg='#b3d9ff', font = FFont) 
    hour.place(x=0, y=100)
    city_name = StringVar() 
    city_entry = Entry(frame, textvariable=city_name, width=25, font = FFont) 
    city_entry.place(x=0, y=125)
    
    city_nameButton = tk.Button(frame, text="Search", command=lambda: city_name(frame1, frame2, frame3), font = FFont, bg='#b3d9ff') 
    city_nameButton.place(x=350, y=125)
    
    # Country  Names and Coordinates 
    lable_citi = tk.Label(frame, text="...", width=0,  
                   bg='#b3d9ff', font = FFont) 
    lable_citi.place(x=200, y=50) 
  
    lable_country = tk.Label(frame, text="...", width=0,  
                      bg='#b3d9ff', font = FFont) 
    lable_country.place(x=300, y=50) 
    
    lable_lat_long = tk.Label(frame, text="Long-Lat: ", width=0, 
                  bg='#b3d9ff', font = FFont) 
    lable_lat_long.place(x=150, y=100) 
    
    lable_lon = tk.Label(frame, text="...", width=0, 
                  bg='#b3d9ff', font = FFont) 
    lable_lon.place(x=250, y=100) 
    
    lable_lat = tk.Label(frame, text="...", width=0, 
                  bg='#b3d9ff', font = FFont) 
    lable_lat.place(x=300, y=100) 
  
# Current Temperature 
    lable_temp_L = tk.Label(frame, text="Actual temperature", width=0, bg='#b3d9ff', 
                   font = FFont, fg='black') 
    lable_temp_L.place(x=0, y=175)
    
    lable_temp = tk.Label(frame, text="...", width=0, bg='#b3d9ff', 
                   font = FFont, fg='black') 
    lable_temp.place(x=175, y=175) 
  
# Other temperature details 
  
    humi = tk.Label(frame, text="Humidity: ", width=0,  
             bg='#b3d9ff', font = FFont) 
    humi.place(x=0, y=200) 
  
    lable_humidity = tk.Label(frame, text="...", width=0, 
                       bg='#b3d9ff', font = FFont) 
    lable_humidity.place(x=100, y=200) 
  
  
    maxi = tk.Label(frame, text="Max. Temp.: ", width=0,  
             bg='#b3d9ff', font = FFont) 
    maxi.place(x=0, y=225) 
  
    max_temp = tk.Label(frame, text="...", width=0,  
                 bg='#b3d9ff', font = FFont) 
    max_temp.place(x=100, y=225) 
  
  
    mini = tk.Label(frame, text="Min. Temp.: ", width=0,  
             bg='#b3d9ff', font = FFont) 
    mini.place(x=150, y=225) 
  
    min_temp = tk.Label(frame, text="...", width=0,  
                 bg='#b3d9ff', font = FFont) 
    min_temp.place(x=250, y=225) 
    
    #RIGHT SIDE
    
    mgr = owm.weather_manager()
    
    def proceed(cit, frame5):
        city=cit.get()
        if city=='':
            return messagebox.showerror('Error','Enter City Name')
        elif api_key=='your api key':
            return messagebox.showerror('Error','Enter your api key')
    
        else:
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            cityname = city
            complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
            response = requests.get(complete_url) 
            x = response.json()  
            if x["cod"] != "404": 
      
                y = x["main"] 
                currenttemp = y["temp"] 
                currentpressure = y["pressure"] 
                currenthumidiy = y["humidity"]
                z = x["weather"] 
                weather_description = z[0]["description"]  
                temperature_label =  tk.Label(frame5, text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius',  bg = '#b3d9ff', font = FFont, relief="groove")
                temperature_label.place(x = 0, y = 100)
                atmospheric_label =  tk.Label(frame5, text='Atmospheric Pressure: '+str(currentpressure)+' hPa',  bg = '#b3d9ff', font = FFont, relief="groove")
                atmospheric_label.place(x = 0, y = 125)
                humidity_label =  tk.Label(frame5, text='Humidity: '+str(currenthumidiy),  bg = '#b3d9ff', font = FFont, relief="groove")
                humidity_label.place(x = 0, y = 150)
                descr_label =  tk.Label(frame5, text='Description: '+str(weather_description),  bg = '#b3d9ff', font = FFont, relief="groove")
                descr_label.place(x = 0, y = 175)
                
            else: 
                return messagebox.showerror('Error','No City Found')
        
    def city_name(frame1, frame2, frame3): 
        frame1.destroy()
        frame2.destroy()
        frame3.destroy()
        frame2 = tk.LabelFrame(frame, text = "Next hours prediction", bg = '#1a8cff', font = FFont)
        frame2.place(x = 0, y = 300, height = 350, width = 600)
        frame1 = tk.LabelFrame(frame, text = "Future days prediction", bg = '#1a8cff', font = FFont)
        frame1.place(x = 600, y = 0, height = 350, width = 800)
        frame3 = tk.LabelFrame(frame, text = "Weather forecasting", bg = '#1a8cff', font = FFont)
        frame3.place(x = 600, y = 350, height = 325, width = 800)
        # API Call 
        api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                               + city_entry.get() + "&units=metric&appid="+api_key) 
  
        api = json.loads(api_request.content) 
        
    # Temperatures 
        y = api['main'] 
        current_temprature = y['temp'] 
        humidity = y['humidity'] 
        tempmin = y['temp_min'] 
        tempmax = y['temp_max'] 
  
    # Coordinates 
        x = api['coord'] 
        longitude = x['lon'] 
        latitude = x['lat'] 
  
    # Country 
        z = api['sys'] 
        country = z['country'] 
        citi = api['name'] 
  
    # Adding the received info into the screen 
        lable_temp.configure(text=current_temprature) 
        lable_humidity.configure(text=humidity) 
        max_temp.configure(text=tempmax) 
        min_temp.configure(text=tempmin) 
        lable_lon.configure(text=longitude) 
        lable_lat.configure(text=latitude) 
        lable_country.configure(text=country) 
        lable_citi.configure(text=citi) 
        
        #Graph Plot
        str_insert = "" + citi + "," + country
        
        mgr = owm.weather_manager()
        
        dt = datetime.today()
        today = datetime.combine(dt, datetime.min.time())
        
        one_day_ahead = today + timedelta(days=1)
        two_day_ahead = today + timedelta(days=2)
        three_day_ahead = today + timedelta(days=3)
        four_day_ahead = today + timedelta(days=4)
        five_day_ahead = today + timedelta(days=5)
        six_day_ahead = today + timedelta(days=6)
        seven_day_ahead = today + timedelta(days=7)
        
        one_call_call = mgr.one_call(lat=latitude, lon=longitude)
        one_day_vect = []
        date_vect = []
        hum_vect = []
        
        placestring = "" + citi + "," + country
        one_call_call_2 = mgr.one_call(lat=latitude, lon=longitude).forecast_hourly
        refe_time = []
        weder = []
        today_ref = datetime.now()
        today_ref = today_ref.strftime('%y-%m-%d %H:%M')
        today_ref = datetime.strptime(today_ref, '%y-%m-%d %H:%M')
        today_ref = today_ref - timedelta(hours=2)
        timeapp = []

        for elem in one_call_call_2:
            today_ref = today_ref + timedelta(hours=1)
            RR = today_ref.strftime('%y-%m-%d %H:%M')
            refe_time.append(RR)
            weder.append(elem.detailed_status)
        
        del refe_time[0]
        del weder[0]
        
        new_string = ""
        ultim_list = []
        
        for i in range(len(refe_time)):
            new_string = "" + refe_time[i] + " Weather: " + weder[i] + ""
            ultim_list.append(new_string)
    
        Combofor = ttk.Combobox(frame3, values = ultim_list, width=40)
        Combofor.place( x = 375, y =  50)
        
        frame4_label = tk.Label(frame3, text="Weather forecasting in two days", width=0,  
             bg='#b3d9ff', font = FFont) 
        frame4_label.place( x = 375, y =  0)
        
        
        #TEMPERATURE
        for i in range(6):
            
            one_day_ahead_temp_night = one_call_call.forecast_daily[i].temperature('celsius').get('feels_like_night')
            one_day_ahead_temp_morn = one_call_call.forecast_daily[i].temperature('celsius').get('feels_like_morn')
            one_day_ahead_temp_day = one_call_call.forecast_daily[i].temperature('celsius').get('feels_like_day')
            one_day_ahead_temp_eve = one_call_call.forecast_daily[i].temperature('celsius').get('feels_like_eve')
            one_day_vect.append(one_day_ahead_temp_night)
            one_day_vect.append(one_day_ahead_temp_morn)
            one_day_vect.append(one_day_ahead_temp_day)
            one_day_vect.append(one_day_ahead_temp_eve)
            
            if i == 0:
                date_vect.append(one_day_ahead)
                one_day_ahead = one_day_ahead + timedelta(hours=6)
                date_vect.append(one_day_ahead)
                one_day_ahead = one_day_ahead + timedelta(hours=6)
                date_vect.append(one_day_ahead)
                one_day_ahead = one_day_ahead + timedelta(hours=6)
                date_vect.append(one_day_ahead)
            if i == 1:
                date_vect.append(two_day_ahead)
                two_day_ahead = two_day_ahead + timedelta(hours=6)
                date_vect.append(two_day_ahead)
                two_day_ahead = two_day_ahead + timedelta(hours=6)
                date_vect.append(two_day_ahead)
                two_day_ahead = two_day_ahead + timedelta(hours=6)
                date_vect.append(two_day_ahead)
            if i == 2:
                date_vect.append(three_day_ahead)
                three_day_ahead = three_day_ahead + timedelta(hours=6)
                date_vect.append(three_day_ahead)
                three_day_ahead = three_day_ahead + timedelta(hours=6)
                date_vect.append(three_day_ahead)
                three_day_ahead = three_day_ahead + timedelta(hours=6)
                date_vect.append(three_day_ahead)
            if i == 3:
                date_vect.append(four_day_ahead)
                four_day_ahead = four_day_ahead + timedelta(hours=6)
                date_vect.append(four_day_ahead)
                four_day_ahead = four_day_ahead + timedelta(hours=6)
                date_vect.append(four_day_ahead)
                four_day_ahead = four_day_ahead + timedelta(hours=6)
                date_vect.append(four_day_ahead)
            if i == 4:
                date_vect.append(five_day_ahead)
                five_day_ahead = five_day_ahead + timedelta(hours=6)
                date_vect.append(five_day_ahead)
                five_day_ahead = five_day_ahead + timedelta(hours=6)
                date_vect.append(five_day_ahead)
                five_day_ahead = five_day_ahead + timedelta(hours=6)
                date_vect.append(five_day_ahead)
            if i == 5:
                date_vect.append(six_day_ahead)
                six_day_ahead = six_day_ahead + timedelta(hours=6)
                date_vect.append(six_day_ahead)
                six_day_ahead = six_day_ahead + timedelta(hours=6)
                date_vect.append(six_day_ahead)
                six_day_ahead = six_day_ahead + timedelta(hours=6)
                date_vect.append(six_day_ahead)
            if i == 6:
                date_vect.append(seven_day_ahead)
                seven_day_ahead = seven_day_ahead + timedelta(hours=6)
                date_vect.append(seven_day_ahead)
                seven_day_ahead = seven_day_ahead + timedelta(hours=6)
                date_vect.append(seven_day_ahead)
                seven_day_ahead = seven_day_ahead + timedelta(hours=6)
                date_vect.append(seven_day_ahead)
        
        #HUMIDITY 
        
        for i in range(6):
            one_day_ahead_hum = one_call_call.forecast_daily[i].humidity
            
            hum_vect.append(one_day_ahead_hum)
            hum_vect.append(one_day_ahead_hum)
            hum_vect.append(one_day_ahead_hum)
            hum_vect.append(one_day_ahead_hum)
        
        cloth_vect = []
        for i in range(6):
            temp_morn = one_call_call.forecast_daily[i].temperature('celsius').get('morn')
            cloth_day = pythermalcomfort.models.clo_tout(tout=temp_morn, units='SI')
            cloth_vect.append(cloth_day)
        
        #FRAME 3
        
        total_clo_vect = []
        
        # in this case, for not exact values of clo, we use intermediate values to decide the clothing
        
        for i in range(6):
            value = cloth_vect[i]
            
            if (value <= 0.43):
                clo = 'Walking shorts, short-sleeve shirt'
                total_clo_vect.append(clo)
            if (value >= 0.43) & (value < 0.52):
                clo = 'Typical summer indoor clothing '
                total_clo_vect.append(clo)
            if (value >= 0.52) & (value < 0.555):
                clo = 'Knee-length skirt, short-sleeve shirt, sandals, underwear'
                total_clo_vect.append(clo)
            if (value >= 0.555) & (value < 0.59):
                clo = 'Trousers, short-sleeve shirt, socks, shoes, underwear'
                total_clo_vect.append(clo)
            if (value >= 0.59) & (value < 0.64):
                clo = 'Trousers, long-sleeve shirt'
                total_clo_vect.append(clo)
            if (value >= 0.64) & (value < 0.705):
                clo = 'Knee-length skirt, long-sleeve shirt, full slip'
                total_clo_vect.append(clo)
            if (value >= 0.705) & (value < 0.85):
                clo = 'Sweat pants, long-sleeve sweatshirt'
                total_clo_vect.append(clo)
            if (value >= 0.85) & (value < 0.98):
                clo = 'Jacket, Trousers, long-sleeve shirt'
                total_clo_vect.append(clo)
            if (value >= 0.98) & (value <= 1.0):
                clo = 'Typical winter indoor clothing'
                total_clo_vect.append(clo)
                
        one_day_ahead_2 = one_day_ahead.strftime("20%y-%m-%d ")
        two_day_ahead_2 = two_day_ahead.strftime("20%y-%m-%d ")
        three_day_ahead_2 = three_day_ahead.strftime("20%y-%m-%d ")
        four_day_ahead_2 = four_day_ahead.strftime("20%y-%m-%d ")
        five_day_ahead_2 = five_day_ahead.strftime("20%y-%m-%d ")
        six_day_ahead_2 = six_day_ahead.strftime("20%y-%m-%d ")
        seven_day_ahead_2 = seven_day_ahead.strftime("20%y-%m-%d ")
        
        date_vect_2 = []
        
        date_vect_2.append(one_day_ahead_2)
        date_vect_2.append(two_day_ahead_2)
        date_vect_2.append(three_day_ahead_2)
        date_vect_2.append(four_day_ahead_2)
        date_vect_2.append(five_day_ahead_2)
        date_vect_2.append(six_day_ahead_2)
        date_vect_2.append(seven_day_ahead_2)
        
        tot_vect_2 = []
        
        for i in range(6):
            t = date_vect_2[i] + total_clo_vect[i]
            tot_vect_2.append(t)
            
        frame3_label = tk.Label(frame3, text="Clothing prediction in the next 6 days", width=0,  
             bg='#b3d9ff', font = FFont) 
        frame3_label.place( x = 50, y =  0)
        
        Combo = ttk.Combobox(frame3, values = tot_vect_2, width=50)
        Combo.place( x = 50, y =  50)
        
        #FRAME 2 (under daily results)
        today = datetime.now()
        
        one_hour_ahead = today + timedelta(hours=1)
        two_hour_ahead = today + timedelta(hours=2)
        three_hour_ahead = today + timedelta(hours=3)
        four_hour_ahead = today + timedelta(hours=4)
        five_hour_ahead = today + timedelta(hours=5)
        six_hour_ahead = today + timedelta(hours=6)
    
        one_hour_vect = []
        date_hour_vect = []
        hum_hour_vect = []
        
        #TEMPERATURE
        for i in range(5):
            one_hour_ahead_temp = one_call_call.forecast_hourly[i].temperature('celsius').get('feels_like')
            one_hour_vect.append(one_hour_ahead_temp)
            if i == 0:
                date_hour_vect.append(one_hour_ahead)    
            if i == 1:
                date_hour_vect.append(two_hour_ahead)    
            if i == 2:
                date_hour_vect.append(three_hour_ahead)    
            if i == 3:
                date_hour_vect.append(four_hour_ahead)    
            if i == 4:
                date_hour_vect.append(five_hour_ahead)    
            if i == 5:
                date_hour_vect.append(six_hour_ahead)    
        
        #HUMIDITY 
        
        for i in range(5):
            one_hour_ahead_hum = one_call_call.forecast_daily[i].humidity
            
            hum_hour_vect.append(one_hour_ahead_hum)
        
        # FIGURE PART
        total_data = {'Dates': date_vect, 'Temperature': one_day_vect, 'Humidity': hum_vect}
        dataf = pd.DataFrame(data=total_data)
        
        total_data_2 = {'Dates': date_hour_vect, 'Temperature': one_hour_vect, 'Humidity': hum_hour_vect}
        dataf2 = pd.DataFrame(data=total_data_2)
        
        fig, axes = plt.subplots(nrows=2, ncols=1,figsize=(8,3))
        canvas = FigureCanvasTkAgg(fig, master=frame1)

        # canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        # canvas.draw()
        
        
        axes[0].set_ylabel(r'°C')
        axes[0].grid()
        axes[0].plot(total_data['Dates'], total_data['Temperature'], 'o-', color = 'red', label = 'Dates', alpha=.9)
        axes[0].set_title('6 days outdoor temperature, perceived due to humidity and wind', fontsize=12)
        axes[0].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        axes[1].set_ylabel(r'%')
        axes[1].grid()
        axes[1].plot(total_data['Dates'], total_data['Humidity'], 'o-', color = 'blue', label = 'Dates', alpha=.9)
        axes[1].set_title('6 days relative daily mean humidity', fontsize=12)
        axes[1].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=frame1)
        toolbar = NavigationToolbar2Tk(canvas, frame1)
        toolbar.update()
        
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        canvas.draw()
        canvas.blit()
        
        fig2, axes2 = plt.subplots(nrows=2, ncols=1,figsize=(8,3))
        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)

        # canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        # canvas2.draw()
        # canvas2.blit()
        
        axes2[0].set_ylabel(r'°C')
        axes2[0].grid()
        axes2[0].plot(dataf2['Dates'], dataf2['Temperature'], 'o-', color = 'red', label = 'Dates', alpha=.9)
        axes2[0].set_title('6 hours outdoor temperature, perceived due to humidity and wind', fontsize=12)
        axes2[0].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        axes2[1].set_ylabel(r'%')
        axes2[1].grid()
        axes2[1].plot(dataf2['Dates'], dataf2['Humidity'], 'o-', color = 'blue', label = 'Dates', alpha=.9)
        axes2[1].set_title('6 hours relative daily mean humidity', fontsize=12)
        axes2[1].grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        
        fig2.tight_layout()
        canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
        toolbar2 = NavigationToolbar2Tk(canvas2, frame2)
        toolbar2.update()
        canvas2.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        canvas2.draw()
        canvas2.blit()
    
        return None
    
    return None
    
#########################################################################################################################################################################################################################################

#FUNCTIONS

def File_dialog(label_file):
    filename = filedialog.askopenfilename(initialdir = "C:/Users/New/Desktop", title="Select a file", filetype=(("xlsx files", "*.xlsx"),("csv files","*.csv"),("All files","*.*")))
    label_file["text"] = filename
    return None

#########################################################################################################################################################################################################################################
def change_file(frame2):
    llist = frame2.place_slaves()
    
    for l in llist:
        l.destroy()
    
    main(root, FFont)
    return None

#########################################################################################################################################################################################################################################
# FUNCTION USED TO SELECT AND DISPLAY ALL ROWS OF A XLSX FILE/ CSV FILE

def Load_excel_data(label_file, tv1, tv2, frame, frame2, frame3):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename)
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')

    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    strt = string_slicing(file_path)
    
    Label = tk.Label(frame2, text ='%s' %(strt), bg = '#b3d9ff', font = FFont, relief="groove")
    Label.place(x = 25, y = 150)
    
    Clear_data(tv1)
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
    
    
    df = df.round(3)
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values = row)
    
    Clear_data(tv2)
    col_names = list(df.columns)
    for c in col_names:
        if c == 'Unnamed: 0':
            df = df.drop(columns=['Unnamed: 0'], axis = 1)
        if c == 'time':
            df = df.drop(columns=['time'], axis = 1)
        if c == 'name':
            df = df.drop(columns=['name'], axis = 1)
    DD = Descr(df)
    tv2["column"] = list(DD.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column)
        
    DD = DD.round(3)
    df_rows = DD.to_numpy().tolist()
    for row in df_rows:
        tv2.insert("", "end", values = row)
    
    LD = ["Show data parameters of the entire dataset", 
          "Show data parameters between two dates", 
          "Show data parameters between two hours in a day",
          "Show data parameters between two hours in two days",
          "Show data parameters from multiple dataset"
          ]
    
    Combo0 = ttk.Combobox(frame2, values = LD, width = 50)
    Combo0.place( x = 25, y =  125)
    
    First_Label = tk.Label(frame2, text ='No options selected', bg = '#b3d9ff', font = FFont, relief="groove")
    First_Label.place(x = 25, y = 150)
    First_Label.place_forget()
    
    button3 = tk.Button(frame2, bg = '#b3d9ff', text = 'No option selected', font = FFont)
    button3.place(x = 300, y = 200)
    
    btn = tk.Button(frame2, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo_initial_combo(df, label_file, Combo0, First_Label, frame2, button3))
    btn.place( x = 25, y =  200)
    
    buttonchange = tk.Button(frame2, text = "Change file", bg = '#b3d9ff', font = FFont, command = lambda: change_file(frame2))
    buttonchange.place(x = 225, y = 25)
    return None

#########################################################################################################################################################################################################################################

# FUNCTION USED TO CLEAN THE ROWS OF THE TREEVIEW

def Clear_data(tv):
    tv.delete(*tv.get_children())
    return None

#########################################################################################################################################################################################################################################

# FUNCTION USED TO CLEAN THE ROWS OF THE TREEVIEW

def Show_data():
    file_path = label_file["text"]
    excel_filename = r"{}".format(file_path)
    df = pd.read_excel(excel_filename, engine='openpyxl')
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    return None

#########################################################################################################################################################################################################################################

#GRAPH FUNCTIONS

def Graph_of_entire_dataset(field, dataset):
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    #LEFT PART OF THE WINDOW
    
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    default_marker = 'o'
    default_line_style = '-'
    total_def_style = '' + default_marker + default_line_style
    
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 150)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 250)
    
    global Combo
    Combo = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo.place( x = 0, y =  200)
    
    global Combo2
    Combo2 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo2.place( x = 0, y =  300)
    
    choice1 = Combo.get()
    choice2 = Combo2.get()
    
    global Third_Label
    Third_Label = tk.Label(frame1, text ='Default colour \n plot: Blue', font = FFont,  bg = '#b3d9ff', relief="groove")
    Third_Label.place(x = 0, y = 0)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Modified_plot(Third_Label, axes, dataset, field, window1, Combo, Combo2))
    btn5.place( x = 0, y =  50)
    

    plot_colour = str(Third_Label['text'])
    
    if plot_colour != 'Default colour \n plot: Blue':
        default = plot_colour
    else:
        default = '#0000ff'
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
        
    axes.grid()
    axes.plot(dataset.time, dataset['%s' %(field)], total_def_style, color = default, label = field, alpha=.9)
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    return None


#########################################################################################################################################################################################################################################


def Graph_of_multiple_datasets(field, dataset):
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    #LEFT PART OF THE WINDOW

    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    default_marker = 'o'
    default_line_style = ' '
    total_def_style = '' + default_marker + default_line_style
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 150)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 250)
    
    global Combo2
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  200)
    
    global Combo3
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  300)
    
    choice1 = Combo2.get()
    choice2 = Combo3.get()
    
    global Third_Label
    Third_Label = tk.Label(frame1, text ='Default colour \n plot: Blue', font = FFont,  bg = '#b3d9ff', relief="groove")
    Third_Label.place(x = 0, y = 0)

    plot_colour = str(Third_Label['text'])
    
    if plot_colour != 'Default colour \n plot: Blue':
        default = plot_colour
    else:
        default = '#0000ff'
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
    
    basec = ['blue', 'lime', 'red', 'orange', 'yellow', 'purple']
    col_list = dataset.columns.to_list()
    
    finaldf = pd.DataFrame()
    supportdf = pd.DataFrame()
    
    finaldf['time'] = dataset.iloc[:, 0]
    finaldf[col_list[1]] = dataset.iloc[:, 1]
    for i in range(len(col_list)):
        j = i + 1
        supportdf = pd.DataFrame()
        if (cut_value(col_list[i]) == 'time'):
            supportdf['time'] = dataset.iloc[:, i]
            supportdf[col_list[j]] = dataset.iloc[:, j]
            finaldf = pd.concat([finaldf, supportdf])
            finaldf["time"] = pd.to_datetime(finaldf["time"])
            finaldf = finaldf.sort_values(by='time')

    axes.grid()
    time_set = finaldf.time
    finaldf = finaldf.drop(columns = 'time')    
    col_list = finaldf.columns.to_list()    
    axes.plot(time_set, finaldf, total_def_style, alpha=.7)
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best', labels=col_list)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    clors = []
    styles = []
    marks = []
    
    for i in range(len(col_list)):
        ccc = axes.properties()['children'][i].get_color()
        st = axes.properties()['children'][i].get_linestyle()
        mk = axes.properties()['children'][i].get_marker()
        clors.append(ccc)
        styles.append(st)
        marks.append(mk)

    Combo = ttk.Combobox(frame1, values=col_list)
    Combo.place( x = 0, y =  100)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Modified_multiplot(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors, styles, marks))
    btn5.place( x = 0, y =  50)
    
    return None

#########################################################################################################################################################################################################################################

def Graphic_with_aggregators(field, dataset, List_aggr, sublist):
    
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 300)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 400)
    
    global Combo2
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  350)
    
    global Combo3
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  450)

    List_op = List_aggr
    if 'plot' not in List_aggr:
        List_op.append('plot')
    
    #LEFT PART OF THE WINDOW

    Combo = ttk.Combobox(frame1, values=List_op)
    Combo.place( x = 0, y =  100)
    
    chosen_agg = str(Combo.get())
    
    #COLOUR OF AGGREGATORS AND STYLES
    
    default_marker = 'o'
    default_line_style = '-'
    total_def_style = '' + default_marker + default_line_style
    
    default = '#0000ff'
    plot_style = total_def_style
    
    mean_colour = '#ff0000'
    mean_style = ',-'
    
    standev_colour = '#00ff00'
    standev_style = ',-'
    
    standev_colour_2 = '#008000'
    standev2_style = ',-'
    
    standev_colour_3 = '#008000'
    standev3_style = ',-'
    
    median_colour = '#ff00ff'
    median_style = ',-'
    
    Third_Label = tk.Label(frame1, text = default, font = FFont,  bg = default, relief="groove")
    Third_Label.place(x = 0, y = 0)
    
    aggrbutton = tk.Button(frame1, text="Change colour \n of the aggregator", bg = '#b3d9ff', font = FFont, command=lambda: Added_aggregators(Third_Label, axes, dataset, field, window1, List_aggr, sublist, Combo, default, mean_colour, standev_colour, standev_colour_2, standev_colour_3, median_colour, Combo2, Combo3, plot_style, mean_style, standev_style, standev2_style, standev3_style, median_style))
    aggrbutton.place( x = 0, y =  150)
    
    data_t = dataset.time
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
    
    axes.grid()
    axes.plot(dataset.time, dataset['%s' %(field)], plot_style, color = default, label = field, alpha=.9)

    if "mean" in List_aggr:
        mean_by_date = []
        
        for i in range(len(sublist)):
            d = sublist[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)
        axes.plot(dataset.time, mean_by_date, mean_style, c= mean_colour, label = "daily mean", alpha=.5)
        
    if "standard deviation" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
                
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        axes.plot(dataset.time, mean_dev, standev_style, c= standev_colour, label = "standard deviation: + \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev, standev_style, c= standev_colour, label = "standard deviation: - \u03C3", alpha=.3)
        axes.fill_between(dataset.time, mean_less_dev, mean_dev, color=standev_colour, alpha=0.2)
    if "standard deviation 2" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        axes.plot(dataset.time, mean_dev, standev2_style,c= standev_colour_2, label = "standard deviation: + \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev, standev2_style, c= standev_colour_2, label = "standard deviation: - \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_dev_2, standev2_style, c=standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev_2, standev2_style, c=standev_colour_2, label = "standard deviation 2: -2 \u03C3", alpha=.3)
        axes.fill_between(dataset.time, mean_dev, mean_dev_2, color=standev_colour_2, alpha=0.2)
        axes.fill_between(dataset.time, mean_less_dev_2, mean_less_dev, color=standev_colour_2, alpha=0.2)
    
    if "standard deviation 3" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        axes.plot(dataset.time, mean_dev_2, standev3_style, c=standev_colour_3, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev_2, standev3_style, c=standev_colour_3, label = "standard deviation 2: -2 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_dev_3, standev3_style, c=standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev_3, standev3_style, c=standev_colour_3, label = "standard deviation: -3 \u03C3", alpha=.3)
        axes.fill_between(dataset.time, mean_dev_2, mean_dev_3, color=standev_colour_3, alpha=0.2)
        axes.fill_between(dataset.time, mean_less_dev_3, mean_less_dev_2, color=standev_colour_3, alpha=0.2)
        
    if "median" in List_aggr:
        median = []
        
        for i in range(len(sublist)):
            d = sublist[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_median = float(DDD_field.median())
            for j in range(len(DDD)):
                median.append(DDD_median)
        axes.plot(dataset.time, median, median_style, c= median_colour, label = "daily median", alpha=.5)
    
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    return None

def Graphic_with_multi_aggregators(field, dataset, List_aggr):
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 300)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 400)
    
    global Combo2
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  350)
    
    global Combo3
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  450)

    List_op = List_aggr
    if 'plot' not in List_aggr:
        List_op.append('plot')
    
    #LEFT PART OF THE WINDOW

    Combo = ttk.Combobox(frame1, values=List_op)
    Combo.place( x = 0, y =  100)
    
    chosen_agg = str(Combo.get())
    
    #COLOUR OF AGGREGATORS AND STYLES
    
    default_marker = 'o'
    default_line_style = '-'
    total_def_style = '' + default_marker + default_line_style
    
    default = '#0000ff'
    plot_style = total_def_style
    
    mean_colour = '#ff0000'
    mean_style = ',-'
    
    standev_colour = '#00ff00'
    standev_style = ',-'
    
    standev_colour_2 = '#008000'
    standev2_style = ',-'
    
    standev_colour_3 = '#008000'
    standev3_style = ',-'
    
    median_colour = '#ff00ff'
    median_style = ',-'
    
    Third_Label = tk.Label(frame1, text = default, font = FFont,  bg = default, relief="groove")
    Third_Label.place(x = 0, y = 0)
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
    
    basec = ['blue', 'lime', 'red', 'orange', 'yellow', 'purple']
    col_list = dataset.columns.to_list()
    
    finaldf = pd.DataFrame()
    supportdf = pd.DataFrame()
    
    finaldf['time'] = dataset.iloc[:, 0]
    finaldf[col_list[1]] = dataset.iloc[:, 1]
    for i in range(len(col_list)):
        j = i + 1
        supportdf = pd.DataFrame()
        if (cut_value(col_list[i]) == 'time'):
            supportdf['time'] = dataset.iloc[:, i]
            supportdf[col_list[j]] = dataset.iloc[:, j]
            finaldf = pd.concat([finaldf, supportdf])
            finaldf["time"] = pd.to_datetime(finaldf["time"])
            finaldf = finaldf.sort_values(by='time')
        
    dfs = pd.DataFrame()
    finaldf = finaldf.dropna(subset=['time'])
    dfs = finaldf
    axes.grid()
    time_set = finaldf.time

    dat = add_dates_2(time_set)
    dates = dat['Days'].tolist()
    sublist = dates
    col_list = finaldf.columns.to_list()
    dfs = dfs.drop(columns = 'time')    
    col_list = finaldf.columns.to_list()    
    axes.plot(time_set, dfs, total_def_style, alpha=.7)
    
    clors = []
    styles = []
    marks = []
    
    #finaldf.drop(columns='time')
    col_list = dfs.columns.to_list()
    for i in range(len(col_list)):
        ccc = axes.properties()['children'][i].get_color()
        st = axes.properties()['children'][i].get_linestyle()
        mk = axes.properties()['children'][i].get_marker()
        clors.append(ccc)
        styles.append(st)
        marks.append(mk)
    
    col_list = finaldf.columns.to_list()    
    
    if "mean" in List_aggr:
        meandf = pd.DataFrame()
        meandf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                meandf[namedf] = mean_by_date
                
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        axes.plot(tiset, meandf, mean_style, c= mean_colour, label = "daily mean", alpha=.5)
        
    if "standard deviation" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        #mean_less_dev = meandf.sum(stdevdf)
        # mul2 = stdevdf.mul(2)
        # mean_dev_2 = meandf.add(mul2)
        # mean_less_dev_2 = meandf.sub(mul2)
        # mul3 = stdevdf.mul(3)
        # mean_dev_3 = meandf.add(mul3)
        # mean_less_dev_3 = meandf.sub(mul3)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour, label = "standard deviation: + \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour, label = "standard deviation: - \u03C3", alpha=.3)
        # for l in range(len(mean_dev)):
        #     axes.fill_between(tiset, mean_less_dev[i], mean_dev[i], color=standev_colour, alpha=0.2)
    
    
    if "standard deviation 2" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    DDD_dev = DDD_dev*2
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        #mean_less_dev = meandf.sum(stdevdf)
        # mul2 = stdevdf.mul(2)
        # mean_dev_2 = meandf.add(mul2)
        # mean_less_dev_2 = meandf.sub(mul2)
        # mul3 = stdevdf.mul(3)
        # mean_dev_3 = meandf.add(mul3)
        # mean_less_dev_3 = meandf.sub(mul3)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_dev, standev2_style,c= standev_colour_2, label = "standard deviation: + \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_less_dev, standev2_style, c= standev_colour_2, label = "standard deviation: - \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_dev_2, standev2_style, c=standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_less_dev_2, standev2_style, c=standev_colour_2, label = "standard deviation 2: -2 \u03C3", alpha=.3)
        # axes.fill_between(dataset.time, mean_dev, mean_dev_2, color=standev_colour_2, alpha=0.2)
        # axes.fill_between(dataset.time, mean_less_dev_2, mean_less_dev, color=standev_colour_2, alpha=0.2)
    
    if "standard deviation 3" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    DDD_dev = DDD_dev*3
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_dev_2, standev3_style, c=standev_colour_3, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_less_dev_2, standev3_style, c=standev_colour_3, label = "standard deviation 2: -2 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_dev_3, standev3_style, c=standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)
        # axes.plot(dataset.time, mean_less_dev_3, standev3_style, c=standev_colour_3, label = "standard deviation: -3 \u03C3", alpha=.3)
        # axes.fill_between(dataset.time, mean_dev_2, mean_dev_3, color=standev_colour_3, alpha=0.2)
        # axes.fill_between(dataset.time, mean_less_dev_3, mean_less_dev_2, color=standev_colour_3, alpha=0.2)
        
    if "median" in List_aggr:
        meandf = pd.DataFrame()
        meandf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.median(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                meandf[namedf] = mean_by_date
                
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        
        axes.plot(tiset, meandf, mean_style, c= mean_colour, label = "daily median", alpha=.5)
        # axes.plot(dataset.time, median, median_style, c= median_colour, label = "daily median", alpha=.5)
    
    
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    finaldf = finaldf.drop(columns = 'time')
    col_list = finaldf.columns.to_list()    
    Combo = ttk.Combobox(frame1, values=col_list)
    Combo.place( x = 0, y =  100)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Added_multi_aggregators(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors, styles, marks))
    btn5.place( x = 0, y =  50)
    
    return None

#########################################################################################################################################################################################################################################

def Range_panel_print(df, sublist):
    
    window1 = tk.Toplevel(root)
    window1.geometry("1000x500")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
    frame0.place( height = 500, width = 1000) 

    # COMBOBOX
    
    col_list = df.columns.to_list()
    col_list.remove('time')
    
    option_vector = []
    
    for i in range(len(col_list)):
        ref = "Show " + col_list[i]
        option_vector.append(ref)
    
    aggregations = ["mean",
                    "standard deviation",
                    "standard deviation 2",
                    "standard deviation 3",
                    "median"
                    ]
    
    global List_aggr
    List_aggr = []
    
    Combo1 = ttk.Combobox(frame0, values = option_vector)
    Combo1.place( x = 50, y =  50)
    
    First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    First_Label.place(x = 250, y = 50)
    
    Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    Second_Label.place(x = 450, y = 100)
    
    btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn.place( x = 200, y =  100)
    
    btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn2.place( x = 50, y =  100)
    
    Combo2 = ttk.Combobox(frame0, values = aggregations)
    Combo2.place( x = 50, y =  250)

    Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
    Aggr_List.place(x = 450, y =  150)
    
    btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn3.place( x = 50, y =  300)
    
    btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn4.place( x = 50, y =  150)
    
    return None

#########################################################################################################################################################################################################################################

def date_hour_panel_print(df, sublist):
    window1 = tk.Toplevel(root)
    window1.geometry("1000x500")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
    frame0.place( height = 500, width = 1000) 

    # COMBOBOX
    
    col_list = df.columns.to_list()
    col_list.remove('time')
    
    option_vector = []
    
    for i in range(len(col_list)):
        ref = "Show " + col_list[i]
        option_vector.append(ref)
    
    aggregations = ["mean",
                    "standard deviation",
                    "standard deviation 2",
                    "standard deviation 3",
                    "median"
                    ]
    
    global List_aggr
    List_aggr = []
        
    Combo1 = ttk.Combobox(frame0, values = option_vector)
    Combo1.place( x = 50, y =  50)
    
    First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    First_Label.place(x = 250, y = 50)
    
    Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    Second_Label.place(x = 450, y = 100)
    
    btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn.place( x = 200, y =  100)
    
    btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn2.place( x = 50, y =  100)
    
    Combo2 = ttk.Combobox(frame0, values = aggregations)
    Combo2.place( x = 50, y =  250)

    Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
    Aggr_List.place(x = 450, y =  150)
    
    btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn3.place( x = 50, y =  300)
    
    btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn4.place( x = 50, y =  150)
    
    return None

#########################################################################################################################################################################################################################################

def Modified_plot(Third_Label, axes, dataset, field, window1, Combo, Combo2):
    my_color = colorchooser.askcolor()[1]
    
    marker_choice = str(Combo.get()).split(' ')[0]
    lsc = str(Combo2.get())
    line_style_choice = str(Combo2.get()).split(' ')[0]

    if marker_choice == '':
        default_marker = 'o'
    if line_style_choice == '':
        default_line_style = '-' 

    default_marker = marker_choice
    if lsc == 'None line style':
        default_line_style = ''
    else:    
        default_line_style = line_style_choice
    total_def_style = '' + default_marker + default_line_style
    
    window1.destroy()

    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    

    Fourth_Label = tk.Label(frame1, text ='Select the marker', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 150)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 250)
    
    Combo = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo.place( x = 0, y =  200)
    
    Combo2 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo2.place( x = 0, y =  300)
    
    #LEFT PART OF THE WINDOW
    Third_Label = tk.Label(frame1, text = my_color, font = FFont,  bg = my_color, relief="groove")
    Third_Label.place(x = 0, y = 0)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Modified_plot(Third_Label, axes, dataset, field, window1, Combo, Combo2))
    btn5.place( x = 0, y =  50)

    plot_colour = str(Third_Label['text'])
    
    
    if plot_colour != 'Default colour \n plot: Blue':
        default = plot_colour
    else:
        default = '#0000ff'
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel(r'Movement detection up-to 12 m')
    
    axes.grid()
    axes.plot(dataset.time, dataset['%s' %(field)], marker = default_marker, linestyle=default_line_style, color = plot_colour, label = field, alpha=.9)
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    return None

def Modified_multiplot(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors, styles, marks):
    my_color = colorchooser.askcolor()[1]
    
    marker_choice = str(Combo2.get()).split(' ')[0]
    lsc = str(Combo3.get())
    line_style_choice = str(Combo3.get()).split(' ')[0]

    if marker_choice == '':
        default_marker = 'o'
    if line_style_choice == '':
        default_line_style = '-'
        
    default_marker = marker_choice
    if lsc == 'None line style':
        default_line_style = ' '
    else:    
        default_line_style = line_style_choice
    total_def_style = '' + default_marker + default_line_style
    
    chosen_agg = str(Combo.get())
    index_of_colist = col_list.index(chosen_agg)
    
    window1.destroy()

    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    #LEFT PART OF THE WINDOW

    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    default_marker = 'o'
    default_line_style = ' '
    total_def_style = '' + default_marker + default_line_style
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 150)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 250)
    
    #global Combo
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  200)
    
    #global Combo2
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  300)
    
    choice1 = Combo2.get()
    choice2 = Combo3.get()
    
    #global Third_Label
    Third_Label = tk.Label(frame1, text ='Default colour \n plot: Blue', font = FFont,  bg = '#b3d9ff', relief="groove")
    Third_Label.place(x = 0, y = 0)
    
    plot_colour = str(Third_Label['text'])
    
    if plot_colour != 'Default colour \n plot: Blue':
        default = plot_colour
    else:
        default = '#0000ff'
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
    
    basec = ['blue', 'lime', 'red', 'orange', 'yellow', 'purple']
    col_list = dataset.columns.to_list()
    
    finaldf = pd.DataFrame()
    supportdf = pd.DataFrame()
    
    finaldf['time'] = dataset.iloc[:, 0]
    finaldf[col_list[1]] = dataset.iloc[:, 1]
    for i in range(len(col_list)):
        j = i + 1
        supportdf = pd.DataFrame()
        if (cut_value(col_list[i]) == 'time'):
            supportdf['time'] = dataset.iloc[:, i]
            supportdf[col_list[j]] = dataset.iloc[:, j]
            finaldf = pd.concat([finaldf, supportdf])
            finaldf["time"] = pd.to_datetime(finaldf["time"])
            finaldf = finaldf.sort_values(by='time')


    axes.grid()
    time_set = finaldf.time
    finaldf = finaldf.drop(columns = 'time')    
    col_list = finaldf.columns.to_list()    
    axes.plot(time_set, finaldf, total_def_style, alpha=.7)
    for i in range(len(col_list)):
        axes.properties()['children'][i].set_color(clors[i])
        axes.properties()['children'][i].set_linestyle(styles[i])
        axes.properties()['children'][i].set_marker(marks[i])
    axes.properties()['children'][index_of_colist].set_color(my_color)
    axes.properties()['children'][index_of_colist].set_marker(marker_choice)
    axes.properties()['children'][index_of_colist].set_linestyle(line_style_choice)
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best', labels=col_list)
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    clors = []
    styles = []
    marks = []
    
    for i in range(len(col_list)):
        ccc = axes.properties()['children'][i].get_color()
        st = axes.properties()['children'][i].get_linestyle()
        mk = axes.properties()['children'][i].get_marker()
        clors.append(ccc)
        styles.append(st)
        marks.append(mk)
        
    Combo = ttk.Combobox(frame1, values=col_list)
    Combo.place( x = 0, y =  100)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Modified_multiplot(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors,  styles, marks))
    btn5.place( x = 0, y =  50)
    return None

#########################################################################################################################################################################################################################################

def color_of_aggregators(Third_Label, axes, dataset, field, window1, List_aggr, sublist):
    my_color = colorchooser.askcolor()[1]
    window1.destroy()
    
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
        
    List_op = List_aggr
    if 'plot' not in List_aggr:
        List_op.append('plot')
    
    #LEFT PART OF THE WINDOW
    Third_Label = tk.Label(frame1, text = my_color, font = FFont,  bg = my_color, relief="groove")
    Third_Label.place(x = 0, y = 0)
        
    btn5 = tk.Button(frame1, text="Change colour plot", bg = '#b3d9ff', font = FFont, command=lambda: Modified_plot(Third_Label, axes, dataset, field, window1))
    btn5.place( x = 0, y =  50)
    
    Combo = ttk.Combobox(frame1, values=List_op)
    Combo.place( x = 0, y =  100)
    
    aggrbutton = tk.Button(frame1, text="Change colour \n of the aggregator", bg = '#b3d9ff', font = FFont, command=lambda: color_of_aggregators(Third_Label, axes, dataset, field, window1, List_aggr, sublist))
    aggrbutton.place( x = 0, y =  200)
    
    global mean_colour
    mean_colour = '#ff0000'
    
    global standev_colour
    standev_colour = '#00ff00'

    plot_colour = str(Third_Label['text'])
    
    if plot_colour != 'Default colour \n plot: Blue':
        default = plot_colour
    else:
        default = '#0000ff'
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel(r'Movement detection up-to 12 m')
    
    axes.grid()
    axes.plot(dataset.time, dataset['%s' %(field)], 'o-', color = default, label = field, alpha=.9)
    
    if "mean" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)
        axes.plot(dataset.time, mean_by_date, c= mean_colour,marker=",", ls='-', label = "daily mean", alpha=.3)
        
    if "standard deviation" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)
            
        col = dataset['%s' %(field)]
        dev = float(col.std())
        dev_col = []
        for i in range(len(col)):
            dev_col.append(dev)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        axes.plot(dataset.time, mean_dev, c= standev_colour,marker=",", ls='-', label = "standard deviation: + \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev, c=standev_colour,marker=",", ls='-', label = "standard deviation: - \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_dev_2, c='#008000',marker=",", ls='-', label = "standard deviation 2: +2 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev_2, c='#008000',marker=",", ls='-', label = "standard deviation 2: -2 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_dev_3, c='#008000',marker=",", ls='-', label = "standard deviation: +3 \u03C3", alpha=.3)
        axes.plot(dataset.time, mean_less_dev_3, c='#008000',marker=",", ls='-', label = "standard deviation: -3 \u03C3", alpha=.3)
        axes.fill_between(dataset.time, mean_less_dev, mean_dev, color='#00b300', alpha=0.2)
        axes.fill_between(dataset.time, mean_dev, mean_dev_2, color='#00ff00', alpha=0.2)
        axes.fill_between(dataset.time, mean_dev, mean_dev_3, color='#4dff4d', alpha=0.2)
        axes.fill_between(dataset.time, mean_less_dev_2, mean_less_dev, color='#00ff00', alpha=0.2)
        axes.fill_between(dataset.time, mean_less_dev_3, mean_less_dev_2, color='#4dff4d', alpha=0.2)
    
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    return None

#########################################################################################################################################################################################################################################

def Added_aggregators(Third_Label, axes, dataset, field, window1, List_aggr, sublist, Combo, plotcol, meancol, stdcol, stdcol2, stdcol3, medicolor, Combo2, Combo3, plot_style, mean_style, standev_style, standev2_style, standev3_style, median_style):
    my_color = colorchooser.askcolor()[1]
    
    marker_choice = str(Combo2.get()).split(' ')[0]
    lsc = str(Combo3.get())
    line_style_choice = str(Combo3.get()).split(' ')[0]

    if marker_choice == '':
        default_marker = 'o'
    if line_style_choice == '':
        default_line_style = '-'
        
    default_marker = marker_choice
    if lsc == 'No line style':
        default_line_style = ''
    else:    
        default_line_style = line_style_choice
    total_def_style = '' + default_marker + default_line_style
    
    chosen_agg = Combo.get()
    window1.destroy()
    
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['No line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']

    Fourth_Label = tk.Label(frame1, text ='Select the marker of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 300)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 400)
    
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  350)
    
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  450)
    
    List_op = List_aggr
    if 'plot' not in List_aggr:
        List_op.append('plot')
    
    #COLOUR PARAMETERS
    
    if chosen_agg == 'plot':
        plotcol = my_color
        plot_style = total_def_style
        
    if chosen_agg == 'mean':
        meancol = my_color
        mean_style = total_def_style
    
    if chosen_agg == 'standard deviation':
        stdcol = my_color
        standev_style = total_def_style
    
    if chosen_agg == 'standard deviation 2':
        stdcol2 = my_color
        standev2_style = total_def_style
        
    if chosen_agg == 'standard deviation 3':
        stdcol3 = my_color
        standev3_style = total_def_style
        
    if chosen_agg == 'median':
        medicolor = my_color
        median_style = total_def_style
    
    #LEFT PART OF THE WINDOW
    
    Third_Label = tk.Label(frame1, text = my_color, font = FFont,  bg = my_color, relief="groove")
    Third_Label.place(x = 0, y = 0)
    
    Combo = ttk.Combobox(frame1, values=List_op)
    Combo.place( x = 0, y =  100)
    
    aggrbutton = tk.Button(frame1, text="Change colour of the aggregator", bg = '#b3d9ff', font = FFont, command=lambda: Added_aggregators(Third_Label, axes, dataset, field, window1, List_aggr, sublist, Combo, plotcol, meancol, stdcol, stdcol2, stdcol3, medicolor, Combo2, Combo3, plot_style, mean_style, standev_style, standev2_style, standev3_style, median_style))
    aggrbutton.place( x = 0, y =  200)
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel(r'Movement detection up-to 12 m')
    
    axes.grid()
    
    axes.plot(dataset.time, dataset['%s' %(field)], plot_style, color = plotcol, label = field, alpha=.9)
    
    if "mean" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)
        if chosen_agg == 'mean':
            axes.plot(dataset.time, mean_by_date, mean_style, c= meancol, label = "daily mean", alpha=.5)
        else:
            axes.plot(dataset.time, mean_by_date, c= meancol,marker=",", ls='-', label = "daily mean", alpha=.5)
        
    if "standard deviation" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        if chosen_agg == 'standard deviation':
            axes.plot(dataset.time, mean_dev, standev_style, c= stdcol, label = "standard deviation: + \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev,  standev_style, c= stdcol, label = "standard deviation: - \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_less_dev, mean_dev, color=stdcol, alpha=0.2)
        else:
            axes.plot(dataset.time, mean_dev, c= stdcol,marker=",", ls='-', label = "standard deviation: + \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev, c= stdcol,marker=",", ls='-', label = "standard deviation: - \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_less_dev, mean_dev, color=stdcol, alpha=0.2)
    if "standard deviation 2" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        if chosen_agg == 'standard deviation 2':
            axes.plot(dataset.time, mean_dev, standev2_style, c= stdcol2, label = "standard deviation: + \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev, standev2_style, c= stdcol2, label = "standard deviation: - \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_dev_2, standev2_style, c=stdcol2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_2, standev2_style, c=stdcol2, label = "standard deviation 2: -2 \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_dev, mean_dev_2, color=stdcol2, alpha=0.2)
            axes.fill_between(dataset.time, mean_less_dev_2, mean_less_dev, color=stdcol2, alpha=0.2)
        else:
            axes.plot(dataset.time, mean_dev, c= stdcol2,marker=",", ls='-', label = "standard deviation: + \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev, c= stdcol2,marker=",", ls='-', label = "standard deviation: - \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_dev_2, c=stdcol2,marker=",", ls='-', label = "standard deviation 2: +2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_2, c=stdcol2,marker=",", ls='-', label = "standard deviation 2: -2 \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_dev, mean_dev_2, color=stdcol2, alpha=0.2)
            axes.fill_between(dataset.time, mean_less_dev_2, mean_less_dev, color=stdcol2, alpha=0.2)
    
    if "standard deviation 3" in List_aggr:
        dates = sublist
        mean_by_date = []
        
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_mean = float(DDD_field.mean())
            for j in range(len(DDD)):
                mean_by_date.append(DDD_mean)

        dates = sublist
        dev_col = []
        for i in range(len(dates)):
            d = dates[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] <= d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_std = float(DDD_field.std())
            for j in range(len(DDD)):
                dev_col.append(DDD_std)
        datas = pd.DataFrame({'Mean': mean_by_date, 'Dev': dev_col})
        mean_d = datas['Mean']
        cov_d = datas['Dev']
        mean_dev = mean_d + cov_d
        mean_less_dev = mean_d - cov_d
        mean_dev_2 = mean_d + cov_d*2
        mean_less_dev_2 = mean_d - cov_d*2
        mean_dev_3 = mean_d + cov_d*3
        mean_less_dev_3 = mean_d - cov_d*3
        if chosen_agg == 'standard deviation 3':
            axes.plot(dataset.time, mean_dev_2, standev3_style, c=stdcol3, label = "standard deviation 2: +2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_2, standev3_style, c=stdcol3, label = "standard deviation 2: -2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_dev_3, standev3_style, c=stdcol3, label = "standard deviation: +3 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_3, standev3_style, c=stdcol3, label = "standard deviation: -3 \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_dev_2, mean_dev_3, color=stdcol3, alpha=0.2)
            axes.fill_between(dataset.time, mean_less_dev_3, mean_less_dev_2, color=stdcol3, alpha=0.2)
        else:
            axes.plot(dataset.time, mean_dev_2, c=stdcol3,marker=",", ls='-', label = "standard deviation 2: +2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_2, c=stdcol3,marker=",", ls='-', label = "standard deviation 2: -2 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_dev_3, c=stdcol3,marker=",", ls='-', label = "standard deviation: +3 \u03C3", alpha=.3)
            axes.plot(dataset.time, mean_less_dev_3, c=stdcol3,marker=",", ls='-', label = "standard deviation: -3 \u03C3", alpha=.3)
            axes.fill_between(dataset.time, mean_dev_2, mean_dev_3, color=stdcol3, alpha=0.2)
            axes.fill_between(dataset.time, mean_less_dev_3, mean_less_dev_2, color=stdcol3, alpha=0.2)
    if "median" in List_aggr:
        median = []
        
        for i in range(len(sublist)):
            #d = dates[i]
            d = sublist[i]
            date = datetime.strptime(d, '%Y-%m-%d')
            date2 = date + timedelta(days=1)
            d2 = date2.strftime("20%y-%m-%d")
            DDD = dataset.loc[(dataset['time'] >= d) & (dataset['time'] < d2)]
            DDD_field = DDD['%s' %(field)]
            DDD_median = float(DDD_field.median())
            for j in range(len(DDD)):
                median.append(DDD_median)
        if chosen_agg == 'median':
            axes.plot(dataset.time, median, median_style, c= medicolor, label = "daily median", alpha=.5)
        else:
            axes.plot(dataset.time, median, c= medicolor,marker=",", ls='-', label = "daily median", alpha=.5)
        
    axes.set_title('%s' %(field), fontsize=12)
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    return None

def Added_multi_aggregators(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors, styles, marks):
    my_color = colorchooser.askcolor()[1]
    
    marker_choice = str(Combo2.get()).split(' ')[0]
    lsc = str(Combo3.get())
    line_style_choice = str(Combo3.get()).split(' ')[0]

    if marker_choice == '':
        default_marker = 'o'
    if line_style_choice == '':
        default_line_style = '-'
        
    default_marker = marker_choice
    if lsc == 'No line style':
        default_line_style = ''
    else:    
        default_line_style = line_style_choice
    total_def_style = '' + default_marker + default_line_style
    
    chosen_agg = str(Combo.get())
    index_of_colist = col_list.index(chosen_agg)
    
    window1.destroy()
    window1 = tk.Toplevel(root)
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    window1.geometry("1300x600")
    frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
    frame0.place(height= 700, width = 1000) 
    frame1 = tk.LabelFrame(window1, text = "Colour choices", bg='#1a8cff', font = FFont)
    frame1.place(height= 700, width = 400, x = 1000, y = 0) 
    
    fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(15,5))
    
    markers_style = ['. point_marker', ', pixel_marker',
                     'o circle_marker',
                     'v triangle_down_marker',
                     '^ triangle_up_marker',
                     '< triangle_left_marker',
                     '> triangle_right_marker',
                     '1 tri_down_marker',
                     '2 tri_up_marker',
                     '3 tri_left_marker',
                     '4 tri_right_marker',
                     's square_marker',
                     'p pentagon_marker',
                     '* star_marker',
                     'h hexagon1_marker',
                     'H hexagon2_marker',
                     '+ plus_marker',
                     'x x_marker',
                     'D diamond_marker',
                     'd thin_diamond_marker',
                     '| vline_marker',
                     '_ hline_marker']
    
    line_style = ['None line style','- solid_line_style','-- dashed_line_style','-. dash-dot_line_style',': dotted_line_style']
    
    Fourth_Label = tk.Label(frame1, text ='Select the marker of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fourth_Label.place(x = 0, y = 300)
    
    Fifth_Label = tk.Label(frame1, text ='Select the line style of the main plot', font = FFont,  bg = '#b3d9ff', relief="groove")
    Fifth_Label.place(x = 0, y = 400)
    
    Combo2 = ttk.Combobox(frame1, values=markers_style, width = 20)
    Combo2.place( x = 0, y =  350)
    
    Combo3 = ttk.Combobox(frame1, values=line_style, width = 20)
    Combo3.place( x = 0, y =  450)

    List_op = List_aggr
    if 'plot' not in List_aggr:
        List_op.append('plot')
    
    #LEFT PART OF THE WINDOW

    Combo = ttk.Combobox(frame1, values=List_op)
    Combo.place( x = 0, y =  100)
    
    chosen_agg = str(Combo.get())
    
    #COLOUR OF AGGREGATORS AND STYLES
    
    default_marker = 'o'
    default_line_style = '-'
    total_def_style = '' + default_marker + default_line_style
    
    default = '#0000ff'
    plot_style = total_def_style
    
    mean_colour = '#ff0000'
    mean_style = ',-'
    
    standev_colour = '#00ff00'
    standev_style = ',-'
    
    standev_colour_2 = '#008000'
    standev2_style = ',-'
    
    standev_colour_3 = '#008000'
    standev3_style = ',-'
    
    median_colour = '#ff00ff'
    median_style = ',-'
    
    Third_Label = tk.Label(frame1, text = default, font = FFont,  bg = default, relief="groove")
    Third_Label.place(x = 0, y = 0)
    
    if field == 'temperature':
        axes.set_ylabel(r'°C ($\pm$ 0,4 °C)')
    if field == 'humidity':
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
    if field == 'luminosity':
        axes.set_ylabel(r'lx')
    if field == 'white':
        axes.set_ylabel(r'lx')
    if field == 'TVOC':
        axes.set_ylabel(r'ppb')
    if field == 'eCO2':
        axes.set_ylabel(r'ppm')
    if field == 'noise':
        axes.set_ylabel(r'dB')
    if field == 'seismic_level':
        axes.set_ylabel(r'250 gal and a period of 0.3s, 0.5s, or 0.7s')
    if field == 'PIR':
        axes.set_ylabel('Movement detection up-to 12 m')
    
    basec = ['blue', 'lime', 'red', 'orange', 'yellow', 'purple']
    col_list = dataset.columns.to_list()
    
    finaldf = pd.DataFrame()
    supportdf = pd.DataFrame()
    
    finaldf['time'] = dataset.iloc[:, 0]
    finaldf[col_list[1]] = dataset.iloc[:, 1]
    for i in range(len(col_list)):
        j = i + 1
        supportdf = pd.DataFrame()
        if (cut_value(col_list[i]) == 'time'):
            supportdf['time'] = dataset.iloc[:, i]
            supportdf[col_list[j]] = dataset.iloc[:, j]
            finaldf = pd.concat([finaldf, supportdf])
            finaldf["time"] = pd.to_datetime(finaldf["time"])
            finaldf = finaldf.sort_values(by='time')

    dfs = pd.DataFrame()
    finaldf = finaldf.dropna(subset=['time'])
    dfs = finaldf
    axes.grid()
    time_set = finaldf.time

    dat = add_dates_2(time_set)
    dates = dat['Days'].tolist()
    sublist = dates
    col_list = finaldf.columns.to_list()
    dfs = dfs.drop(columns = 'time')    
    col_list = finaldf.columns.to_list()    
    axes.plot(time_set, dfs, total_def_style, alpha=.7)
    
    time_set = finaldf.time 
    col_list = dfs.columns.to_list()
    axes.plot(time_set, dfs, total_def_style, alpha=.7)
    for i in range(len(col_list)):
        axes.properties()['children'][i].set_color(clors[i])
        axes.properties()['children'][i].set_linestyle(styles[i])
        axes.properties()['children'][i].set_marker(marks[i])
    axes.properties()['children'][index_of_colist].set_color(my_color)
    axes.properties()['children'][index_of_colist].set_marker(marker_choice)
    axes.properties()['children'][index_of_colist].set_linestyle(line_style_choice)
    
    clors = []
    styles = []
    marks = []
    
    col_list = dfs.columns.to_list()
    for i in range(len(col_list)):
        ccc = axes.properties()['children'][i].get_color()
        st = axes.properties()['children'][i].get_linestyle()
        mk = axes.properties()['children'][i].get_marker()
        clors.append(ccc)
        styles.append(st)
        marks.append(mk)

    
    if "mean" in List_aggr:
        meandf = pd.DataFrame()
        meandf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                meandf[namedf] = mean_by_date
                
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        axes.plot(tiset, meandf, mean_style, c= mean_colour, label = "daily mean", alpha=.5)
        
    if "standard deviation" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour, label = "standard deviation: + \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour, label = "standard deviation: - \u03C3", alpha=.3)
        
    if "standard deviation 2" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    DDD_dev = DDD_dev*2
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour_2, label = "standard deviation 2: +2 \u03C3", alpha=.3)
        
    if "standard deviation 3" in List_aggr:
        col_list = finaldf.columns.to_list()  
        dates = sublist
        mean_by_date = []
        
        meandf = pd.DataFrame()
        stdevdf = pd.DataFrame()
        meandf['time'] = time_set
        stdevdf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            dev_col = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.mean(skipna = True))
                    DDD_dev = float(DDD_field.std(skipna = True))
                    DDD_dev = DDD_dev*3
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    if  not(DDD_dev == nn):
                        DDD_dev = round(DDD_dev, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                        dev_col.append(DDD_dev)
                meandf[namedf] = mean_by_date
                stdevdf[namedf] = dev_col
        
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        stdevdf = stdevdf.drop(columns = 'time')
        clist = meandf.columns.to_list()
        
        mean_dev = pd.DataFrame(meandf.values + stdevdf.values, columns = clist)
        mean_less_dev = pd.DataFrame(meandf.values - stdevdf.values, columns = clist)
        axes.plot(tiset, mean_dev, standev_style, c= standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)
        axes.plot(tiset, mean_less_dev, standev_style, c= standev_colour_3, label = "standard deviation: +3 \u03C3", alpha=.3)

    if "median" in List_aggr:
        meandf = pd.DataFrame()
        meandf['time'] = time_set
        nn = float('NaN')
        for k in range(len(col_list)):
            j = k + 1
            mean_by_date = []
            if (j <= (len(col_list) - 1)):
                namedf = '' + col_list[j] + '_mean'
                for i in range(len(sublist)):
                    d = sublist[i]
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    d2 = date2.strftime("20%y-%m-%d")
                    DDD = finaldf.loc[(finaldf['time'] >= d) & (finaldf['time'] < d2)]
                    DDD_field = DDD[col_list[j]]
                    DDD_mean = float(DDD_field.median(skipna = True))
                    if  not(DDD_mean == nn):
                        DDD_mean = round(DDD_mean, 3)
                    for jj in range(len(DDD)):
                        mean_by_date.append(DDD_mean)
                meandf[namedf] = mean_by_date
                
        tiset = meandf.time
        meandf = meandf.drop(columns = 'time')
        
        axes.plot(tiset, meandf, mean_style, c= mean_colour, label = "daily median", alpha=.5)
        
    axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    axes.legend(loc = 'best')
    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=frame0)
    toolbar = NavigationToolbar2Tk(canvas, frame0)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    canvas.get_tk_widget().pack()
    canvas.draw()
    
    finaldf = finaldf.drop(columns = 'time')
    col_list = finaldf.columns.to_list()
    Combo = ttk.Combobox(frame1, values=col_list)
    Combo.place( x = 0, y =  100)
        
    btn5 = tk.Button(frame1, text="Change settings of plot", bg = '#b3d9ff', font = FFont, command=lambda: Added_multi_aggregators(Third_Label, axes, dataset, field, window1, Combo, Combo2, Combo3, col_list, clors, styles, marks))
    btn5.place( x = 0, y =  50)
    
    return None

#########################################################################################################################################################################################################################################

# COMBOBOXES

#FUNCTIONS USED TO SELECT AND DISPLAY DATE

def checkcombo_initial_combo(df, label_file, Combo0, First_Label, frame2, button3):
    
    value = Combo0.get()
    First_Label.config(text= value)
    
    LD = ["Show data parameters of the entire dataset", 
          "Show data parameters between two dates", 
          "Show data parameters between two hours in a day",
          "Show data parameters between two hours in two days",
          "Show data parameters from multiple dataset"]
    
    sel = str(button3['text'])
    
    if value == "Show data parameters of the entire dataset" :
        button3['text'] = "Show data parameters\n of the entire dataset"
        button3['command'] = lambda: Entire_Dataset_Parameter(label_file)
    if value == "Show data parameters between two dates" :
        button3['text'] = "Show data parameters between\n two dates"
        button3['command'] = lambda: Two_dates_Parameter(df, label_file)
    if value == "Show data parameters between two hours in a day" :
        button3['text'] = "Show data parameters between\n two hours in a day"
        button3['command'] = lambda: Two_hours_Parameter(df, label_file)
    if value == "Show data parameters between two hours in two days" :
        button3['text'] = "Show data parameters between two hours in two days"
        button3['command'] = lambda: Two_hours_two_dates_Parameter(df, label_file)
    if value == "Show data parameters from multiple dataset" :
        button3['text'] = "Show data parameters from multiple dataset"
        button3['command'] = lambda: Multiple_Dataset_Parameter(label_file)
         
    return None

#########################################################################################################################################################################################################################################
        
def check_graphs(frame0, Combo1, First_Label, btn, df):
    value = Combo1.get()
    First_Label.config(text= value)
    gg = cut_space_value(value)
    btn['text'] = "Show " + gg
    btn['command'] = lambda: Graph_of_entire_dataset(gg, df)
    
def check_graphs_multiple(frame0, Combo1, First_Label, btn, filePaths):
    value = str(Combo1.get())
    First_Label.config(text= value)
    gg = cut_space_value(value)
    
    df = pd.DataFrame()
    h = 0 
    if filePaths[0].endswith(".xlsx"):
        ref_dataset = pd.read_excel(filePaths[0], engine="openpyxl")
        ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
        colcol = ref_dataset.columns.to_list()
        ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
        name = string_slicing(filePaths[0])
        timename = '' + name + '_time'
        filename = '' + name + '_' + str(gg)
        df.insert(h, timename, ref_dataset['time'])
        h = h + 1
        df.insert(h, filename, ref_dataset[gg])
        h = h + 1
        for i in range(len(filePaths) - 1):
            j = i + 1
            dataset = pd.read_excel(filePaths[j], engine="openpyxl")
            dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
            dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
            name = string_slicing(filePaths[j])
            timename = '' + name + '_time'
            filename = '' + name + '_' + str(gg)
            df.insert(h, timename, dataset['time'])
            h = h + 1
            df.insert(h, filename, dataset[gg])
            h = h + 1
            
        
    if filePaths[0].endswith(".csv"):
        ref_dataset = pd.read_csv(filePaths[0])
        ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
        colcol = ref_dataset.columns.to_list()
        ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
        name = string_slicing(filePaths[0])
        timename = '' + name + '_time'
        filename = '' + name + '_' + str(gg)
        df.insert(h, timename, ref_dataset['time'])
        h = h + 1
        df.insert(h, filename, ref_dataset[gg])
        h = h + 1
        for i in range(len(filePaths) - 1):
            j = i + 1
            dataset = pd.read_csv(filePaths[j])
            dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
            dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce') 
            name = string_slicing(filePaths[j])
            timename = '' + name + '_time'
            filename = '' + name + '_' + str(gg)
            df.insert(h, timename, dataset['time'])
            h = h + 1
            df.insert(h, filename, dataset[gg])
            h = h + 1

    btn['text'] = "Show " + gg
    btn['command'] = lambda: Graph_of_multiple_datasets(gg, df)
    

#########################################################################################################################################################################################################################################

def check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist):
    value1 = Combo1.get()
    First_Label.config(text= value1)
    value1 = str(value1)
    value = Combo2.get()
    
    LL = []
    Combo3 = ttk.Combobox(frame0, values = LL)
    Combo3.place(  x = 250, y =  250)
    
    btn5 = tk.Button(frame0, text="Eliminate aggregator from\n the menu below", bg = '#b3d9ff', font = FFont, command=lambda: el_aggregator(frame0, Combo3, List_aggr, Aggr_List))
    btn5.place( x = 250, y =  150)
    
    DD = pd.DataFrame()
    
    if (value == "mean"):
        if ("mean" not in List_aggr):
            List_aggr.append("mean")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "mean" not in LIST:
                Aggr_List.insert(0, "mean")
        if ("mean" in List_aggr) :
            pass

        btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
        
    if value == "standard deviation" :
       if ("standard deviation" not in List_aggr):
            List_aggr.append("standard deviation")
            Aggr_List.insert(1, "standard deviation")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation" not in LIST:
                Aggr_List.insert(0, "standard deviation")
       if ("standard deviation" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
    
    if value == "standard deviation 2" :
       if ("standard deviation 2" not in List_aggr):
            List_aggr.append("standard deviation 2")
            Aggr_List.insert(1, "standard deviation 2")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation 2" not in LIST:
                Aggr_List.insert(0, "standard deviation 2")
       if ("standard deviation 2" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
     
    if value == "standard deviation 3" :
       if ("standard deviation 3" not in List_aggr):
            List_aggr.append("standard deviation 3")
            Aggr_List.insert(1, "standard deviation 3")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation 3" not in LIST:
                Aggr_List.insert(0, "standard deviation 3")
       if ("standard deviation 3" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
    
    if value == "median" :
       if ("median" not in List_aggr):
            List_aggr.append("median")
            Aggr_List.insert(1, "median")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "median" not in LIST:
                Aggr_List.insert(0, "median")
       if ("median" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
       
    Add_aggregators(df, List_aggr, value1, btn3, sublist)

    return None

def check_multi_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, btn, filePaths):
    value1 = Combo1.get()
    First_Label.config(text= value1)
    value1 = str(value1)
    value = Combo2.get()
    gg = cut_space_value(value1)
    
    df = pd.DataFrame()
    h = 0 
    if filePaths[0].endswith(".xlsx"):
        ref_dataset = pd.read_excel(filePaths[0], engine="openpyxl")
        ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
        colcol = ref_dataset.columns.to_list()
        ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
        name = string_slicing(filePaths[0])
        timename = '' + name + '_time'
        filename = '' + name + '_' + str(gg)
        df.insert(h, timename, ref_dataset['time'])
        h = h + 1
        df.insert(h, filename, ref_dataset[gg])
        h = h + 1
        for i in range(len(filePaths) - 1):
            j = i + 1
            dataset = pd.read_excel(filePaths[j], engine="openpyxl")
            dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
            dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
            name = string_slicing(filePaths[j])
            timename = '' + name + '_time'
            filename = '' + name + '_' + str(gg)
            df.insert(h, timename, dataset['time'])
            h = h + 1
            df.insert(h, filename, dataset[gg])
            h = h + 1
            
        
    if filePaths[0].endswith(".csv"):
        ref_dataset = pd.read_csv(filePaths[0])
        ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
        colcol = ref_dataset.columns.to_list()
        ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
        name = string_slicing(filePaths[0])
        timename = '' + name + '_time'
        filename = '' + name + '_' + str(gg)
        df.insert(h, timename, ref_dataset['time'])
        h = h + 1
        df.insert(h, filename, ref_dataset[gg])
        h = h + 1
        for i in range(len(filePaths) - 1):
            j = i + 1
            dataset = pd.read_csv(filePaths[j])
            dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
            dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce') 
            name = string_slicing(filePaths[j])
            timename = '' + name + '_time'
            filename = '' + name + '_' + str(gg)
            df.insert(h, timename, dataset['time'])
            h = h + 1
            df.insert(h, filename, dataset[gg])
            h = h + 1
    
    LL = []
    Combo3 = ttk.Combobox(frame0, values = LL)
    Combo3.place(  x = 250, y =  250)
    
    btn5 = tk.Button(frame0, text="Eliminate aggregator from\n the menu below", bg = '#b3d9ff', font = FFont, command=lambda: el_aggregator(frame0, Combo3, List_aggr, Aggr_List))
    btn5.place( x = 250, y =  150)
    
    DD = pd.DataFrame()
    
    if (value == "mean"):
        if ("mean" not in List_aggr):
            List_aggr.append("mean")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "mean" not in LIST:
                Aggr_List.insert(0, "mean")
        if ("mean" in List_aggr) :
            pass

        btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
        
    if value == "standard deviation" :
       if ("standard deviation" not in List_aggr):
            List_aggr.append("standard deviation")
            Aggr_List.insert(1, "standard deviation")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation" not in LIST:
                Aggr_List.insert(0, "standard deviation")
       if ("standard deviation" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
    
    if value == "standard deviation 2" :
       if ("standard deviation 2" not in List_aggr):
            List_aggr.append("standard deviation 2")
            Aggr_List.insert(1, "standard deviation 2")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation 2" not in LIST:
                Aggr_List.insert(0, "standard deviation 2")
       if ("standard deviation 2" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
     
    if value == "standard deviation 3" :
       if ("standard deviation 3" not in List_aggr):
            List_aggr.append("standard deviation 3")
            Aggr_List.insert(1, "standard deviation 3")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "standard deviation 3" not in LIST:
                Aggr_List.insert(0, "standard deviation 3")
       if ("standard deviation 3" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
    
    if value == "median" :
       if ("median" not in List_aggr):
            List_aggr.append("median")
            Aggr_List.insert(1, "median")
            Combo3['values'] = List_aggr
            LIST = Aggr_List.get(0, END)
            if "median" not in LIST:
                Aggr_List.insert(0, "median")
       if ("median" in List_aggr) :
            pass
       btn3['text'] = "Plot graph with aggregators\n selected in the menu above"
       
    Add_multi_aggregators(df, List_aggr, value1, btn3)

    return None

#########################################################################################################################################################################################################################################

def Add_aggregators(df, List_aggr, value1, btn3, sublist):
    jj = cut_space_value(value1)
    btn3['command'] = lambda: Graphic_with_aggregators(jj, df, List_aggr, sublist)
    
    return None

def Add_multi_aggregators(df, List_aggr, value1, btn3):
    jj = cut_space_value(value1)
    btn3['command'] = lambda: Graphic_with_multi_aggregators(jj, df, List_aggr)
    
    return None

def button3_values_for_two_date_and_hour_displacement(df, List_aggr, value1, btn3):
    jj = cut_space_value(value1)
    btn3['command'] = lambda: graph_4(jj, df, List_aggr)
    
    return None

#########################################################################################################################################################################################################################################

def el_aggregator(frame0, Combo3, List_aggr, Aggr_List):
    value = str(Combo3.get())
    if len(List_aggr) != 0:
        List_aggr.remove(value)
    Combo3['values'] = List_aggr
    LIST = Aggr_List.get(0, END)
    LLIST = list(LIST)
    
    if (value == "mean") & (value in LLIST):
        LLIST.remove("mean")
        Aggr_List.delete(0, END)
        for i in LLIST:
            Aggr_List.insert(END, i)
    if (value == "mean") & (value not in LLIST):
        pass
    if (value == "standard deviation") & (value in LIST):
        LLIST.remove("standard deviation")
        Aggr_List.delete(0, END)
        for i in LLIST:
            Aggr_List.insert(END, i)
    if (value == "standard deviation") & (value not in LLIST):
        pass
    if (value == "standard deviation 2") & (value in LIST):
        LLIST.remove("standard deviation 2")
        Aggr_List.delete(0, END)
        for i in LLIST:
            Aggr_List.insert(END, i)
    if (value == "standard deviation 2") & (value not in LLIST):
        pass
    if (value == "standard deviation 3") & (value in LIST):
        LLIST.remove("standard deviation 3")
        Aggr_List.delete(0, END)
        for i in LLIST:
            Aggr_List.insert(END, i)
    if (value == "standard deviation 3") & (value not in LLIST):
        pass
    if (value == "median") & (value in LIST):
        LLIST.remove("median")
        Aggr_List.delete(0, END)
        for i in LLIST:
            Aggr_List.insert(END, i)
    if (value == "median") & (value not in LLIST):
        pass
    
    return None

#########################################################################################################################################################################################################################################

def checkcombo_0(Combo0, Zero_Label, frame_1, dataset):
    value = Combo0.get()
    Zero_Label.config(text= value)   

#########################################################################################################################################################################################################################################

def checkcombo_01(Combo0, Combo1, Zero_Label, First_Label, frame_1, df):
    value = Combo0.get()
    Zero_Label.config(text= value)   
    value1 = Combo1.get()
    First_Label.config(text= value1)

#########################################################################################################################################################################################################################################

def checkcombo1(Combo1, First_Label):
    value = Combo1.get()
    First_Label.config(text= value)

#########################################################################################################################################################################################################################################
    
def checkcombo2(Combo2, Second_Label):
    value = Combo2.get()
    Second_Label.config(text= value)
    
#########################################################################################################################################################################################################################################
    
def combo_date(date1, date2, dataset):
    dd = pd.DataFrame()
    df = dataset[(dataset["time"] >= date1) & (dataset["time"] <= date2)]
    return df


#########################################################################################################################################################################################################################################

# FUNCTION USED TO SELECT ALL DATA BETWEEN TWO DATES

def select_range(df, Combo1, Combo2, tv0, tv1, tv2, frame_1, LD):
    DDD = pd.DataFrame()
    value_1 = Combo1.get() #string
    value_2 = Combo2.get() #string
    date1 = datetime.strptime(value_1, '%Y-%m-%d') #date
    date2 = datetime.strptime(value_2, '%Y-%m-%d') #date
    
    if date1 > date2:
        
        date1 = date1 + timedelta(days=1)
        value_1 = date1.strftime("%y-%m-%d")
        value_2 = date2.strftime("%y-%m-%d")
        DDD = df.loc[(df['time'] >= value_2) & (df['time'] <= value_1), :]
        DO = DDD
    
        Clear_data(tv0)
        tv0["column"] = list(DDD.columns)
        tv0["show"] = "headings"
    
        for column in tv0["columns"]:
            tv0.heading(column, text=column)
            
        DDD = DDD.round(3)
        df_rows = DDD.to_numpy().tolist()
        for row in df_rows:
            tv0.insert("", "end", values = row)
        
        Clear_data(tv2)
    
        col_names = list(df.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               df = df.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               df = df.drop(columns=['time'], axis = 1)
            if c == 'name':
               df = df.drop(columns=['name'], axis = 1)
        DD = Descr(df)
        tv2["column"] = list(DD.columns)
        tv2["show"] = "headings"
        for column in tv2["columns"]:
            tv2.heading(column, text=column)
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv2.insert("", "end", values = row)
    
        Clear_data(tv1)
    
        col_names = list(DDD.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               DDD = DDD.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               DDD = DDD.drop(columns=['time'], axis = 1)
            if c == 'name':
               DDD = DDD.drop(columns=['name'], axis = 1)
        DD = Descr(DDD)
        tv1["column"] = list(DD.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)
        
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values = row)
        sublist= sub_List(LD, value_1, value_2)

    if date1 == date2:
        
        date2 = date2 + timedelta(days=1)
        value_1 = date1.strftime("%y-%m-%d")
        value_2 = date2.strftime("%y-%m-%d")
        DDD = df.loc[(df['time'] >= value_1) & (df['time'] < value_2), :]
        DO = DDD
        
        Clear_data(tv0)
        tv0["column"] = list(DDD.columns)
        tv0["show"] = "headings"
    
        for column in tv0["columns"]:
            tv0.heading(column, text=column)
        
        DDD = DDD.round(3)
        df_rows = DDD.to_numpy().tolist()
        for row in df_rows:
            tv0.insert("", "end", values = row)
        
        Clear_data(tv2)
    
        col_names = list(df.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               df = df.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               df = df.drop(columns=['time'], axis = 1)
            if c == 'name':
               df = df.drop(columns=['name'], axis = 1)
        DD = Descr(df)
        tv2["column"] = list(DD.columns)
        tv2["show"] = "headings"
        for column in tv2["columns"]:
            tv2.heading(column, text=column)
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv2.insert("", "end", values = row)
    
        Clear_data(tv1)
    
        col_names = list(DDD.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               DDD = DDD.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               DDD = DDD.drop(columns=['time'], axis = 1)
            if c == 'name':
               DDD = DDD.drop(columns=['name'], axis = 1)
        DD = Descr(DDD)
        tv1["column"] = list(DD.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values = row)
        sublist= sub_List(LD, value_1, value_2)

    if date2 > date1:
        date2 = date2 + timedelta(days=1)
        value_1 = date1.strftime("20%y-%m-%d")
        value_2 = date2.strftime("20%y-%m-%d")
        DDD = df.loc[(df['time'] >= value_1) & (df['time'] < value_2), :]
        DO = DDD
        Clear_data(tv0)
        tv0["column"] = list(DDD.columns)
        tv0["show"] = "headings"
    
        for column in tv0["columns"]:
            tv0.heading(column, text=column)
        
        DDD = DDD.round(3)
        df_rows = DDD.to_numpy().tolist()
        for row in df_rows:
            tv0.insert("", "end", values = row)
        
        Clear_data(tv2)
    
        col_names = list(df.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               df = df.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               df = df.drop(columns=['time'], axis = 1)
            if c == 'name':
               df = df.drop(columns=['name'], axis = 1)
        DD = Descr(df)
        tv2["column"] = list(DD.columns)
        tv2["show"] = "headings"
        for column in tv2["columns"]:
            tv2.heading(column, text=column)
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv2.insert("", "end", values = row)
    
        Clear_data(tv1)
    
        col_names = list(DDD.columns)
        for c in col_names:
            if c == 'Unnamed: 0':
               DDD = DDD.drop(columns=['Unnamed: 0'], axis = 1)
            if c == 'time':
               DDD = DDD.drop(columns=['time'], axis = 1)
            if c == 'name':
               DDD = DDD.drop(columns=['name'], axis = 1)
        DD = Descr(DDD)
        tv1["column"] = list(DD.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)
        
        DD = DD.round(3)
        df_rows = DD.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values = row)
        sublist= sub_List(LD, value_1, value_2)
    
    savefile = DO
    
    btn_save = tk.Button(frame_1, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
    btn_save.place( x = 150, y =  450)
    
    btn_save_csv = tk.Button(frame_1, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
    btn_save_csv.place( x = 300, y =  450)
        
    button0 = tk.Button(frame_1, text = "Plot Data", font = FFont, bg = '#b3d9ff', command =lambda: Range_panel_print(DO, sublist)) #Open the window directory
    button0.place(x = 25, y = 450)
    
    def save_path(df):
        ttt = False
        ins = ''
        popup(ins, df)
        return None
    
    def popup(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_excel(r'' + dir_name + '/' + ins +'.xlsx', index = False, engine = 'openpyxl')
            return None
    
    def save_path_csv(df):
        ttt = False
        ins = ''
        popup_csv(ins, df)
        return None
    
    def popup_csv(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value_csv(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value_csv(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_csv(r'' + dir_name + '/' + ins +'.csv', index = False)
            return None
    return None

#########################################################################################################################################################################################################################################

def select_hour_range(df, Combo0, tv0, tv1, tv2, frame_1, LD_0):
    DDD = pd.DataFrame()
    value_0 = Combo0.get()
    date = datetime.strptime(value_0, '%Y-%m-%d')
    date2 = date + timedelta(days=1)
    value0 = date2.strftime("20%y-%m-%d")
    DDD = df.loc[(df['time'] >= value_0) & (df['time'] < value0)]
    
    tt = add_hours(DDD)
    sublist= sub_List(LD_0, value_0, value0)
    
    Combo1 = ttk.Combobox(frame_1, values = tt)
    Combo1.place( x = 0, y =  250)
    
    First_Label = tk.Label(frame_1, text ='No hour selected', bg = '#b3d9ff', font = FFont, relief="groove")
    First_Label.place(x = 0, y = 300)
    
    Combo2 = ttk.Combobox(frame_1, values = tt)
    Combo2.place( x = 300, y =  250)
    
    Second_Label = tk.Label(frame_1, text ='No hour selected', bg = '#b3d9ff', font = FFont, relief="groove")
    Second_Label.place(x = 300, y = 300)
    
    btn = tk.Button(frame_1, text="Select first hour to start the period", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo1(Combo1, First_Label))
    btn.place( x = 0, y =  200)
    
    btn2 = tk.Button(frame_1, text="Select second hour to end the period", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo2(Combo2, Second_Label))
    btn2.place( x = 300, y =  200)
    
    btn3 = tk.Button(frame_1, text="Selected hours", bg = '#b3d9ff', font = FFont, command=lambda: divided_by_hours(df, DDD, Combo1, Combo2, tv0, tv1, tv2, frame_1, sublist))
    btn3.place( x = 0, y =  400)
    return None

#########################################################################################################################################################################################################################################

def divided_by_hours(df, DDD, Combo1, Combo2, tv0, tv1, tv2, frame_1, sublist):
    value_1 = int(Combo1.get())
    value_2 = int(Combo2.get())
    
    if value_2 < value_1:
        ff = value_1
        value_1 = value_2
        value_2 = ff
    if value_1 == value_2:
        value_2 = value_2 + 1
        
    DDDF = DDD.loc[(DDD.time.dt.hour >= value_1) & (DDD.time.dt.hour < value_2), :]
    DDDF_time = DDDF['time']
    DO = pd.DataFrame(data=DDDF)
    
    Clear_data(tv0)
    tv0["column"] = list(DDDF.columns)
    tv0["show"] = "headings"
    
    for column in tv0["columns"]:
        tv0.heading(column, text=column)
    DDDF = DDDF.round(3)
    df_rows = DDDF.to_numpy().tolist()
    for row in df_rows:
        tv0.insert("", "end", values = row)
        
    Clear_data(tv2)
    
    col_names = list(df.columns)
    for c in col_names:
        if c == 'Unnamed: 0':
            df = df.drop(columns=['Unnamed: 0'], axis = 1)
        if c == 'time':
            df = df.drop(columns=['time'], axis = 1)
        if c == 'name':
            df = df.drop(columns=['name'], axis = 1)
    DD = Descr(df)
    tv2["column"] = list(DD.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column)
    DD = DD.round(3)
    df_rows = DD.to_numpy().tolist()
    for row in df_rows:
        tv2.insert("", "end", values = row)
    
    Clear_data(tv1)
    
    col_names = list(DDDF.columns)
    for c in col_names:
        if c == 'Unnamed: 0':
            DDDF = DDDF.drop(columns=['Unnamed: 0'], axis = 1)
        if c == 'time':
            DDDF = DDDF.drop(columns=['time'], axis = 1)
        if c == 'name':
            DDDF = DDDF.drop(columns=['name'], axis = 1)
    DD = Descr(DDDF)
    tv1["column"] = list(DD.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
    DD = DD.round(3)
    df_rows = DD.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values = row)

    button0 = tk.Button(frame_1, text = "Plot Data", bg = '#b3d9ff', font = FFont, command =lambda: date_hour_panel_print(DO, sublist)) #Open the window directory
    button0.place(x = 25, y = 450)
    
    savefile = DO
    
    btn_save = tk.Button(frame_1, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
    btn_save.place( x = 200, y =  450)
    
    btn_save_csv = tk.Button(frame_1, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
    btn_save_csv.place( x = 350, y =  450)
    
    def save_path(df):
        ttt = False
        ins = ''
        popup(ins, df)
        return None
    
    def popup(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_excel(r'' + dir_name + '/' + ins +'.xlsx', index = False, engine = 'openpyxl')
            return None
        
    def save_path_csv(df):
        ttt = False
        ins = ''
        popup_csv(ins, df)
        return None
    
    def popup_csv(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value_csv(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value_csv(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_csv(r'' + dir_name + '/' + ins +'.csv', index = False)
            return None
    
    return None

#########################################################################################################################################################################################################################################

def select_hour_range_and_dates(df, Combo0, Combo1, tv0, tv1, tv2, frame_1, LD_0):
    DDD = pd.DataFrame()
    value_0 = str(Combo0.get())
    value_1 = Combo1.get()
    date = datetime.strptime(value_1, '%Y-%m-%d')
    date2 = date + timedelta(days=1)
    value_1 = date2.strftime("20%y-%m-%d")
    DDD = df.loc[(df['time'] >= value_0) & (df['time'] <= value_1), :]

    sublist = sub_List(LD_0, value_0, value_1)
    
    DDD_time = DDD.time.tolist()
    dff = pd.DataFrame()
    hour_list = list()
    h = 1
    indx = DDD_time[0]
    ref = int(indx.hour)
    hour_list.append(ref)
    for i in range(len(DDD_time)):
        indxu = DDD_time[i]
        indx = indxu.hour
        if indx != ref:
            h = h + 1
            ref = indx
            hour_list.append(ref)
    
    Combo2 = ttk.Combobox(frame_1, values = hour_list)
    Combo2.place( x = 0, y =  250)
    
    First_Label = tk.Label(frame_1, text ='No hour selected', bg = '#b3d9ff', font = FFont, relief="groove")
    First_Label.place(x = 0, y = 350)
    
    Combo3 = ttk.Combobox(frame_1, values = hour_list)
    Combo3.place( x = 300, y =  250)
    
    Second_Label = tk.Label(frame_1, text ='No hour selected', bg = '#b3d9ff', font = FFont, relief="groove")
    Second_Label.place(x = 300, y = 350)
    
    btn = tk.Button(frame_1, text="Select first hour to start period", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo1(Combo2, First_Label))
    btn.place( x = 0, y =  300)
    
    btn2 = tk.Button(frame_1, text="Select second hour to end the period", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo2(Combo3, Second_Label))
    btn2.place( x = 300, y =  300)
    
    btn3 = tk.Button(frame_1, text="Selected hours", bg = '#b3d9ff', font = FFont, command=lambda: divided_by_hours_everyday(df, DDD, Combo2, Combo3, tv0, tv1, tv2, frame_1, sublist))
    btn3.place( x = 0, y =  400)
        
    return None

def divided_by_hours_everyday(df, DDD, Combo2, Combo3, tv0, tv1, tv2, frame_1, sublist):
    value_1 = int(Combo2.get())
    value_2 = int(Combo3.get())
    
    if value_2 < value_1:
        ff = value_1
        value_1 = value_2
        value_2 = ff
    if value_1 == value_2:
        value_2 = value_2 + 1

    DDDF = DDD.loc[(DDD.time.dt.hour >= value_1) & (DDD.time.dt.hour < value_2), :]
    DDDF_time = DDDF['time']
    DO = pd.DataFrame(data=DDDF)
    
    Clear_data(tv0)
    tv0["column"] = list(DDDF.columns)
    tv0["show"] = "headings"
    
    for column in tv0["columns"]:
        tv0.heading(column, text=column)
    DDDF = DDDF.round(3)
    df_rows = DDDF.to_numpy().tolist()
    for row in df_rows:
        tv0.insert("", "end", values = row)
        
    Clear_data(tv2)
    
    col_names = list(df.columns)
    for c in col_names:
        if c == 'Unnamed: 0':
            df = df.drop(columns=['Unnamed: 0'], axis = 1)
        if c == 'time':
            df = df.drop(columns=['time'], axis = 1)
        if c == 'name':
            df = df.drop(columns=['name'], axis = 1)
    DD = Descr(df)
    tv2["column"] = list(DD.columns)
    tv2["show"] = "headings"
    for column in tv2["columns"]:
        tv2.heading(column, text=column)
    DD = DD.round(3)
    df_rows = DD.to_numpy().tolist()
    for row in df_rows:
        tv2.insert("", "end", values = row)
    
    Clear_data(tv1)
    
    col_names = list(DDDF.columns)
    for c in col_names:
        if c == 'Unnamed: 0':
            DDDF = DDDF.drop(columns=['Unnamed: 0'], axis = 1)
        if c == 'time':
            DDDF = DDDF.drop(columns=['time'], axis = 1)
        if c == 'name':
            DDDF = DDDF.drop(columns=['name'], axis = 1)
    DD = Descr(DDDF)
    tv1["column"] = list(DD.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
    DD = DD.round(3)
    df_rows = DD.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values = row)
        
    DDDF.insert(loc = 1, column = "time", value =  DDDF_time)
    
    savefile = DO
       
    button0 = tk.Button(frame_1, text = "Plot Data", bg = '#b3d9ff', font = FFont, command =lambda: Range_panel_print(DO, sublist)) #Open the window directory
    button0.place(x = 25, y = 450)
    
    btn_save = tk.Button(frame_1, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
    btn_save.place( x = 200, y =  450)
    
    btn_save_csv = tk.Button(frame_1, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
    btn_save_csv.place( x = 350, y =  450)
    
    def save_path(df):
        ttt = False
        ins = ''
        popup(ins, df)
        return None
    
    def popup(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_excel(r'' + dir_name + '/' + ins +'.xlsx', index = False, engine = 'openpyxl')
            return None
        
    def save_path_csv(df):
        ttt = False
        ins = ''
        popup_csv(ins, df)
        return None
    
    def popup_csv(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value_csv(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value_csv(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_csv(r'' + dir_name + '/' + ins +'.csv', index = False)
            return None
    
    return None

    return None
#########################################################################################################################################################################################################################################

        
def Entire_Dataset_Parameter(label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    window1 = tk.Toplevel(root)
    window1.geometry("1000x500")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
    frame0.place( height = 500, width = 1000) 
    
    # COMBOBOX
    
    col_list = df.columns.to_list()
    col_list.remove('time')
    
    option_vector = []
    
    for i in range(len(col_list)):
        ref = "Show " + col_list[i]
        option_vector.append(ref)
    
    aggregations = ["mean",
                    "standard deviation",
                    "standard deviation 2",
                    "standard deviation 3",
                    "median"
                    ]
    
    global List_aggr
    List_aggr = []
    
    try:
        dat = add_dates(df.time)
    except:
        dat = add_dates_2(df.time)
            
    dates = dat['Days'].tolist()
    sublist = dates
    
    Combo1 = ttk.Combobox(frame0, values = option_vector)
    Combo1.place( x = 50, y =  50)
    
    First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    First_Label.place(x = 250, y = 50)
    
    Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
    Second_Label.place(x = 450, y = 100)

    btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn.place( x = 200, y =  100)
    
    btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
    btn2.place( x = 50, y =  100)
    
    Combo2 = ttk.Combobox(frame0, values = aggregations)
    Combo2.place( x = 50, y =  250)

    Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
    Aggr_List.place(x = 450, y =  150)
    
    btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn3.place( x = 50, y =  300)
    
    btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
    btn4.place( x = 50, y =  150)
    
    return None

#########################################################################################################################################################################################################################################

def Two_dates_Parameter(df, label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename)
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1100x600")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    # FRAMES 
    
    frame_1 = tk.LabelFrame(window1, text = "Data selection",  bg='#1a8cff', font = FFont)
    frame_1.place( height = 600, width = 400, x = 0, y = 0)
    frame_2 = tk.LabelFrame(window1, text = "Chosen file", bg='#1a8cff', font = FFont)
    frame_2.place( height = 200, width = 700, x = 400, y = 0)
    frame_3 = tk.LabelFrame(window1, text = "Statistics",  bg='#1a8cff', font = FFont)
    frame_3.place( height = 200, width = 700, x = 400, y = 200)
    frame_4 = tk.LabelFrame(window1, text = "Statistics of the original dataset",  bg='#1a8cff', font = FFont)
    frame_4.place( height = 200, width = 700, x = 400, y = 400)
    
    #List of dates representation
    
    lab = tk.Label(frame_1, text='List of dates', bg = '#b3d9ff', font = FFont, relief="groove")
    lab.place(x=0, y = 50)
    
    LD_1 = add_dates(df.time) # it returns an array of dates present in the chosen file
    LD = LD_1['Days'].values.tolist()
        
    First_Label = tk.Label(frame_1, text ='No date selected', bg = '#b3d9ff', font = FFont, relief="groove")
    First_Label.place(x = 0, y = 150)
    
    Second_Label = tk.Label(frame_1, text ='No date selected',  bg = '#b3d9ff', font = FFont, relief="groove")
    Second_Label.place(x = 200, y = 150)
    
    Combo1 = ttk.Combobox(frame_1, values = LD)
    Combo1.place( x = 0, y =  250)
    
    Combo2 = ttk.Combobox(frame_1, values = LD)
    Combo2.place( x = 200, y =  250)
    
    btn = tk.Button(frame_1, text="Select first date to search", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo1(Combo1, First_Label))
    btn.place( x = 0, y =  100)
    
    btn2 = tk.Button(frame_1, text="Select second date to search", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo2(Combo2, Second_Label))
    btn2.place( x = 200, y =  100)
    
    # TREESCROLL
    
    tv0 = ttk.Treeview(frame_2)
    tv0.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame_2, orient = "vertical", command = tv0.yview)
    treescrollx = tk.Scrollbar(frame_2, orient = "horizontal", command= tv0.xview)
    tv0.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")
    
    tv1 = ttk.Treeview(frame_3)
    tv1.place(relheight=1, relwidth=1)

    treescrolly1 = tk.Scrollbar(frame_3, orient = "vertical", command = tv1.yview)
    treescrollx1 = tk.Scrollbar(frame_3, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx1.set, yscrollcommand = treescrolly1.set)
    treescrollx1.pack(side="bottom", fill = "x")
    treescrolly1.pack(side="right", fill = "y")
    
    tv2 = ttk.Treeview(frame_4)
    tv2.place(relheight=1, relwidth=1)

    treescrolly2 = tk.Scrollbar(frame_4, orient = "vertical", command = tv2.yview)
    treescrollx2 = tk.Scrollbar(frame_4, orient = "horizontal", command= tv2.xview)
    tv2.configure(xscrollcommand = treescrollx2.set, yscrollcommand = treescrolly2.set)
    treescrollx2.pack(side="bottom", fill = "x")
    treescrolly2.pack(side="right", fill = "y")
    
    #BUTTONS
    
    button_0 = tk.Button(frame_1, text = "Select Range", bg = '#b3d9ff', font = FFont, command =lambda: select_range(df, Combo1, Combo2, tv0, tv1, tv2, frame_1, LD)) #Open the window directory
    button_0.place(x = 25, y = 400)
    
    return None

#########################################################################################################################################################################################################################################

def Two_hours_Parameter(df, label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1200x600")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    # FRAMES 
  
    frame_1 = tk.LabelFrame(window1, text = "Data selection",  bg='#1a8cff', font = FFont)
    frame_1.place( height = 600, width = 600, x = 0, y = 0)
    frame_2 = tk.LabelFrame(window1, text = "Chosen file",  bg='#1a8cff', font = FFont)
    frame_2.place( height = 200, width = 700, x = 600, y = 0)
    frame_3 = tk.LabelFrame(window1, text = "Statistics",  bg='#1a8cff', font = FFont)
    frame_3.place( height = 200, width = 700, x = 600, y = 200)
    frame_4 = tk.LabelFrame(window1, text = "Statistics of the original dataset",  bg='#1a8cff', font = FFont)
    frame_4.place( height = 200, width = 700, x = 600, y = 400)
    #List of dates representation
    
    lab = tk.Label(frame_1,  bg='#1a8cff', text='List of dates')
    lab.place(x=0, y = 50)    
    
    LD0 = add_dates(df.time)
    LD_0 = LD0['Days'].values.tolist()

    Zero_Label = tk.Label(frame_1, text ='No date selected', bg = '#b3d9ff', font = FFont, relief="groove")
    Zero_Label.place(x = 200, y = 150)

    Combo0 = ttk.Combobox(frame_1, values = LD_0)
    Combo0.place( x = 0, y =  150)
    
    btn0 = tk.Button(frame_1, text="Select the date to search", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo_0(Combo0, Zero_Label, frame_1, df))
    btn0.place( x = 0, y =  100)

    # TREESCROLL
    
    tv0 = ttk.Treeview(frame_2)
    tv0.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame_2, orient = "vertical", command = tv0.yview)
    treescrollx = tk.Scrollbar(frame_2, orient = "horizontal", command= tv0.xview)
    tv0.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")
    
    tv1 = ttk.Treeview(frame_3)
    tv1.place(relheight=1, relwidth=1)

    treescrolly1 = tk.Scrollbar(frame_3, orient = "vertical", command = tv1.yview)
    treescrollx1 = tk.Scrollbar(frame_3, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx1.set, yscrollcommand = treescrolly1.set)
    treescrollx1.pack(side="bottom", fill = "x")
    treescrolly1.pack(side="right", fill = "y")
    
    tv2 = ttk.Treeview(frame_4)
    tv2.place(relheight=1, relwidth=1)

    treescrolly2 = tk.Scrollbar(frame_4, orient = "vertical", command = tv2.yview)
    treescrollx2 = tk.Scrollbar(frame_4, orient = "horizontal", command= tv2.xview)
    tv2.configure(xscrollcommand = treescrollx2.set, yscrollcommand = treescrolly2.set)
    treescrollx2.pack(side="bottom", fill = "x")
    treescrolly2.pack(side="right", fill = "y")

    #BUTTONS
    
    button_0 = tk.Button(frame_1, text = "Display hours selector", bg = '#b3d9ff', font = FFont, command =lambda: select_hour_range(df, Combo0, tv0, tv1, tv2, frame_1, LD_0)) #Open the window directory
    button_0.place(x = 350, y = 150)

    return None

#########################################################################################################################################################################################################################################

def Two_hours_two_dates_Parameter(df, label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1200x600")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    # FRAMES 
  
    frame_1 = tk.LabelFrame(window1, text = "Data selection",  bg='#1a8cff', font = FFont)
    frame_1.place( height = 600, width = 600, x = 0, y = 0)
    frame_2 = tk.LabelFrame(window1, text = "Chosen file",  bg='#1a8cff', font = FFont)
    frame_2.place( height = 200, width = 700, x = 600, y = 0)
    frame_3 = tk.LabelFrame(window1, text = "Statistics",  bg='#1a8cff', font = FFont)
    frame_3.place( height = 200, width = 700, x = 600, y = 200)
    frame_4 = tk.LabelFrame(window1, text = "Statistics of the original dataset",  bg='#1a8cff', font = FFont)
    frame_4.place( height = 200, width = 700, x = 600, y = 400)
    #List of dates representation
    
    lab = tk.Label(frame_1, text='List of dates', relief="groove")
    lab.place(x=0, y = 50)
    
    LD0 = add_dates(df.time)
    LD_0 = LD0['Days'].values.tolist()

    Zero_Label = tk.Label(frame_1, text ='No date selected',  bg = '#b3d9ff', font = FFont, relief="groove")
    Zero_Label.place(x = 0, y = 200)

    Combo0 = ttk.Combobox(frame_1, values = LD_0)
    Combo0.place( x = 0, y =  150)
    
    First_Label = tk.Label(frame_1, text ='No date selected', bg = '#b3d9ff', font = FFont, relief="groove")
    First_Label.place(x = 200, y = 200)

    Combo1 = ttk.Combobox(frame_1, values = LD_0)
    Combo1.place( x = 200, y =  150)
    
    btn0 = tk.Button(frame_1, text="Select the dates to search", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo_01(Combo0, Combo1, Zero_Label, First_Label, frame_1, df))
    btn0.place( x = 0, y =  100)

    # TREESCROLL
    
    tv0 = ttk.Treeview(frame_2)
    tv0.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame_2, orient = "vertical", command = tv0.yview)
    treescrollx = tk.Scrollbar(frame_2, orient = "horizontal", command= tv0.xview)
    tv0.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")
    
    tv1 = ttk.Treeview(frame_3)
    tv1.place(relheight=1, relwidth=1)

    treescrolly1 = tk.Scrollbar(frame_3, orient = "vertical", command = tv1.yview)
    treescrollx1 = tk.Scrollbar(frame_3, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx1.set, yscrollcommand = treescrolly1.set)
    treescrollx1.pack(side="bottom", fill = "x")
    treescrolly1.pack(side="right", fill = "y")
    
    tv2 = ttk.Treeview(frame_4)
    tv2.place(relheight=1, relwidth=1)

    treescrolly2 = tk.Scrollbar(frame_4, orient = "vertical", command = tv2.yview)
    treescrollx2 = tk.Scrollbar(frame_4, orient = "horizontal", command= tv2.xview)
    tv2.configure(xscrollcommand = treescrollx2.set, yscrollcommand = treescrolly2.set)
    treescrollx2.pack(side="bottom", fill = "x")
    treescrolly2.pack(side="right", fill = "y")

    #BUTTONS
    
    button_0 = tk.Button(frame_1, text = "Display hours selector", bg = '#b3d9ff', font = FFont, command =lambda: select_hour_range_and_dates(df, Combo0, Combo1, tv0, tv1, tv2, frame_1, LD_0)) #Open the window directory
    button_0.place(x = 350, y = 150)
    
    return None

#########################################################################################################################################################################################################################################

def Multiple_Dataset_Parameter(label_file):
    file_path = label_file["text"]
    
    window1 = tk.Toplevel(root)
    window1.geometry("1000x700")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
    frame0.place( height = 700, width = 1000) 
    frame1 = tk.LabelFrame(frame0, text = "Data display", bg='#1a8cff', font = FFont)
    frame1.place(x = 0, y = 250, height = 350, width = 1000) 
    
    
    txt = tk.Text(frame0, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "The following panel is dedicated to multiple plots. To select multiple files, keep pressed the Ctrl button.")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 100, width = 1200)  
    
    tv1 = ttk.Treeview(frame1)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame1, orient = "vertical", command = tv1.yview)
    treescrollx = tk.Scrollbar(frame1, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")
    
    label_file = tk.Label(frame0, text = "No file selected", bg = '#b3d9ff', font = FFont, relief="groove")
    label_file.place(x = 25, y = 300)
    label_file.place_forget()
        
    button1 = tk.Button(frame0, text = "Select files\n from folder", bg = '#b3d9ff', font = FFont, command =lambda: File_dialog_2(label_file, tv1, frame0)) #Open the window directory
    button1.place(x = 25, y = 125)

    button2 = tk.Button(frame0, text = "Load files from folder", bg = '#b3d9ff', font = FFont, command = lambda: Load_multiple_dat(label_file, df, frame0))
    button2.place(x = 175, y = 125)
    
    def File_dialog_2(label_file, tv1, frame0):
        files = filedialog.askopenfilename(multiple=True) # asks user to choose a director
        label_file["text"] = files
        
        file_path = label_file["text"]
        var = root.tk.splitlist(file_path)
        filePaths = []
        for f in var:
            filePaths.append(f)
        
        df = pd.DataFrame()
        h = 0
        col_list = []
        if filePaths[0].endswith(".xlsx"):
            ref_dataset = pd.read_excel(filePaths[0], engine="openpyxl")
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            for hh in colcol:
                col_list.append(hh)
            name = str(string_slicing(filePaths[0]))
            for ind in range(len(colcol)):
                ref = '' + name + '_' + str(colcol[ind])
                df.insert(h, ref, ref_dataset[colcol[ind]])
                h = h + 1
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_excel(filePaths[j], engine="openpyxl")
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = dataset.columns.to_list()
                if 'time' in colcol:
                    dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                for hh in colcol:
                    col_list.append(hh)
                name = str(string_slicing(filePaths[j]))
                for ind in range(len(colcol)):
                    ref = '' + name + '_' + str(colcol[ind])
                    df.insert(h, ref, dataset[colcol[ind]])
                    h = h + 1
                
        if filePaths[0].endswith(".csv"):
            ref_dataset = pd.read_csv(filePaths[0])
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            for hh in colcol:
                col_list.append(hh)
            name = str(string_slicing(filePaths[0]))
            for ind in range(len(colcol)):
                ref = '' + name + '_' + str(colcol[ind])
                df.insert(h, ref, ref_dataset[colcol[ind]])
                h = h + 1
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_csv(filePaths[j])
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = dataset.columns.to_list()
                if 'time' in colcol:
                    dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                for hh in colcol:
                    col_list.append(hh)
                name = str(string_slicing(filePaths[j]))
                for ind in range(len(colcol)):
                    ref = '' + name + '_' + str(colcol[ind])
                    df.insert(h, ref, dataset[colcol[ind]])
                    h = h + 1
        
        Clear_data(tv1)
        tv1["column"] = list(df.columns)
        tv1["show"] = "headings"
        
        for column in tv1["columns"]:
            tv1.heading(column, text=column)
        
        
        df = df.round(3)
        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            tv1.insert("", "end", values = row)
        
        savefile = df
    
        btn_save = tk.Button(frame0, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
        btn_save.place( x = 400, y =  125)
        
        btn_save_csv = tk.Button(frame0, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
        btn_save_csv.place( x = 550, y =  125)
        
        def save_path(df):
            ttt = False
            ins = ''
            popup(ins, df)
            return None
        
        def popup(ins, df):
            window1 = tk.Toplevel(root)
            window1.geometry("300x200")
            window1.iconphoto(False, tk.PhotoImage(file=path_ref))
            frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
            frame.place(x = 0, y = 0, height = 300, width = 300)
            
            select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
            select_l.place(x = 25, y = 25)
            
            E1 = tk.Entry(frame, bd =5)
            E1.place(x = 25, y = 50)
            
            btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value(E1, ins, window1, df))
            btn.place( x = 25, y =  75)
            
            def insert_value(E1, ins, window1, df):
                ins = E1.get()
                dir_name = filedialog.askdirectory() # asks user to choose a director
                df.to_excel(r'' + dir_name + '/' + ins +'.xlsx', index = False, engine = 'openpyxl')
                return None
            
        def save_path_csv(df):
            ttt = False
            ins = ''
            popup_csv(ins, df)
            return None
        
        def popup_csv(ins, df):
            window1 = tk.Toplevel(root)
            window1.geometry("300x200")
            window1.iconphoto(False, tk.PhotoImage(file=path_ref))
            frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
            frame.place(x = 0, y = 0, height = 300, width = 300)
            
            select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
            select_l.place(x = 25, y = 25)
            
            E1 = tk.Entry(frame, bd =5)
            E1.place(x = 25, y = 50)
            
            btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value_csv(E1, ins, window1, df))
            btn.place( x = 25, y =  75)
        
        def insert_value_csv(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_csv(r'' + dir_name + '/' + ins +'.csv', index = False)
            return None
            
        return None
    
    def Load_multiple_dat(label_file, df, frame1):
        file_path = label_file["text"]
        try:
            var = root.tk.splitlist(file_path)
            filePaths = []
            for f in var:
                filePaths.append(f)
        except ValueError:
            tk.messagebox.showerror("Information","The file you have chosen is unvalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information",f"No such file as {file_path}")
            return None
        
        window1 = tk.Toplevel(root)
        window1.geometry("1000x500")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
        frame0.place( height = 500, width = 1000) 
        
        col_list = []
        
        if filePaths[0].endswith(".xlsx"):
            ref_dataset = pd.read_excel(filePaths[0], engine="openpyxl")
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            for hh in colcol:
                col_list.append(hh)
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_excel(filePaths[j], engine="openpyxl")
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = ref_dataset.columns.to_list()
                if 'time' in colcol:
                    ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
                for hh in colcol:
                    col_list.append(hh)
                
        if filePaths[0].endswith(".csv"):
            ref_dataset = pd.read_csv(filePaths[0])
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            for hh in colcol:
                col_list.append(hh)
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_csv(filePaths[j])
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = ref_dataset.columns.to_list()
                if 'time' in colcol:
                    ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
                for hh in colcol:
                    col_list.append(hh)
        
        # COMBOBOX
        
        col_list = remove_duplicates_from_list(col_list)
        col_list.remove('time')
        option_vector = []
        
        for i in range(len(col_list)):
            ref = "Show " + col_list[i]
            option_vector.append(ref)
        
        aggregations = ["mean",
                        "standard deviation",
                        "standard deviation 2",
                        "standard deviation 3",
                        "median"
                        ]
        
        global List_aggr
        List_aggr = []
        
        Combo1 = ttk.Combobox(frame0, values = option_vector)
        Combo1.place( x = 50, y =  50)
        
        First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
        First_Label.place(x = 250, y = 50)
        
        Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
        Second_Label.place(x = 450, y = 100)
    
        btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs_multiple(frame0, Combo1, First_Label, btn, filePaths))
        btn.place( x = 200, y =  100)
        
        btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs_multiple(frame0, Combo1, First_Label, btn, filePaths))
        btn2.place( x = 50, y =  100)
        
        Combo2 = ttk.Combobox(frame0, values = aggregations)
        Combo2.place( x = 50, y =  250)
    
        Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
        Aggr_List.place(x = 450, y =  150)
        
        btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_multi_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, btn, filePaths))
        btn3.place( x = 50, y =  300)
        
        btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_multi_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, btn, filePaths))
        btn4.place( x = 50, y =  150)
        
        return None
    
    return None

#########################################################################################################################################################################################################################################

def Diagnostic_part(label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1300x800")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame = tk.LabelFrame(window1, text = "Data analysis window", bg = '#1a8cff', font = FFont)
    frame.place(x = 0, y = 0, height = 800, width = 1300)
    frame1 = tk.LabelFrame(frame, text = "Options to be chosen for analysis", bg = '#1a8cff', font = FFont)
    frame1.place(x = 0, y = 100, height = 600, width = 1300)
    frame2 = tk.LabelFrame(frame, text = "Report frame", bg = '#1a8cff', font = FFont)
    frame2.place(x = 0, y = 475, height = 200, width = 700)
    
    
    txt = tk.Text(frame, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "The following analysis part is aimed to provide the thermal comfort results, based on chosen file.\n The assumption is that we are considering closed ambients and sedentary work, and assumed air velocity is: velocity of the air v = 0.1 m/s.\nThe main assumption on Mean Radiant Temperature is that it's equal to the measured temperature.\nKeep pressed the right button of the mouse to scroll from left to right and viceversa on report frame")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 100, width = 1200)  
    
    # LISTS
    
    dict_act = pythermalcomfort.utilities.met_typical_tasks
    act_list = list(dict_act.keys())
    act_val_list = list(dict_act.values())
    
    dict_clo = pythermalcomfort.utilities.clo_typical_ensembles
    clo_list = list(pythermalcomfort.utilities.clo_typical_ensembles.keys())
    clo_val_list = list(pythermalcomfort.utilities.clo_typical_ensembles.values())
    
    def risk_calculation(frame2, df):
        frame2.destroy()
        frame2 = tk.LabelFrame(frame, text = "Health warnings", bg = '#1a8cff', font = FFont)
        frame2.place(x = 0, y = 475, height = 200, width = 700)

        v = tk.Scrollbar(frame2) 
        v.pack(side = RIGHT, fill = Y) 
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, wrap = NONE,  
                 yscrollcommand = v.set) 
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 200, width = 650)
        v.config(command=txt2.yview) 
        
        txt2.insert(INSERT, "\nWarnings are represented where the values of relative humidity are too high or too low \nthan the safe zone between 40% and 60%\n\n")
        txt2.insert(END, "")
        
        ref_df = pd.DataFrame()
        ref_df['time'] = df['time']
        ref_df['humidity'] = df['humidity']
        hum = ref_df.humidity.to_list()
        u40 = False
        o60 = False
        for i in range(len(hum)):
            if hum[i] < 40:
                diff = 40 - hum[i]
                diff = str(diff)
                under_40 = ref_df.loc[ref_df.humidity < 40, :]
                u40 = True
                txt2.insert(INSERT, "\nDetected values that are low than 40%\n")
                txt2.insert(END, "")
                txt2.insert(INSERT, "\nOptimal environment for Influenza and Ozone irritation effects. \nHumidity needs to be increased of %s\n" %(diff)) 
                txt2.insert(END, "")
                if hum[i] <= 20:
                    txt2.insert(INSERT, "\nOptimal environment for bacteria profileration. \nHumidity needs to be increased of %s\n" %(diff))
                    txt2.insert(END, "")
                if hum[i] <= 30:
                    txt2.insert(INSERT, "\nOptimal environment for viruses profileration.\nOptimal environment for respiratory diseases increase.\nOptimal environment for Allergic Rhinitis and Asthma increase. Humidity needs to be increased of %s\n" %(diff))
                    txt2.insert(END, "")
                break
            if hum[i] > 60:
                diff = hum[i] - 60
                diff = str(diff)
                over_60 = ref_df.loc[ref_df.humidity > 60, :]
                o60 = True
                txt2.insert(INSERT, "\nOptimal environment for Chemical interaction and consequent irritations. \nDetected values that are higher than 60%\n")
                txt2.insert(END, "")
                if hum[i] >= 70:
                    txt2.insert(INSERT, "\nOptimal environment for Mites proliferation, with consequent increment in dust allergies. \nHumidity has to be decreased of %s\n" %(diff))
                    txt2.insert(END, "")
                if hum[i] >= 70:
                    txt2.insert(INSERT, "\nOptimal environment for Adenoviruses and Coxsackie viruses. \nHumidity has to be decreased of %s\n" %(diff))
                    txt2.insert(END, "")
                if hum[i] >= 80:
                    txt2.insert(INSERT, "\nOptimal environment for fungi growth, and consequently for allergies.\nOptimal environment for bacteria spread.\nOptimal environment for virus spread.\nOptimal environment for Allergic Rhinitis and Asthma increase\n Humidity has to be decreased of %s\n" %(diff))
                    txt2.insert(END, "")
                
                break
        stringg = []
        if u40 == True:
            dataref = under_40
            col_list = dataref.columns.to_list()
            stringg = []
            
            for i in range(len(dataref)):
                rr = dataref.iloc[i, :]
                kk = '\n'
                hh = '\n'
                for j in range(len(col_list)):
                    jj = str(rr[col_list[j]])
                    kk = '' + kk + ''+ col_list[j] + '\n' + jj + '\n'
                kk = kk + '\n'
                stringg.append(kk)
                    
            
            for i in range(len(stringg)):
                string_resp = stringg[i]
                txt2.insert(INSERT, string_resp)
                txt2.insert(END, " ")
        if o60 == True:
            dataref = over_60
            col_list = dataref.columns.to_list()
        
            stringg = []
                
            for i in range(len(dataref)):
                rr = dataref.iloc[i, :]
                kk = '\n'
                hh = '\n'
                for j in range(len(col_list)):
                    jj = str(rr[col_list[j]])
                    kk = '' + kk + ''+ col_list[j] + '\n' + jj + '\n'
                kk = kk + '\n'
                stringg.append(kk)
                    
            
        for i in range(len(stringg)):
            string_resp = stringg[i]
            txt2.insert(INSERT, string_resp)
            txt2.insert(END, "")
    

        return None
    
    risk_calculation(frame2, df)
        
    # VARIABLES
    
    global met_value
    met_value = 0
    
    met = '0'
    
    global clo_value
    clo_value = 0
    
    clo = '0'
    
    vr = '0'
    
    global v
    
    v = 0.1
    
    # Last hour calculation of temperature ad relative humidity
    
    df_time = df['time']
    dates_of_df = add_dates(df_time) 
    sel_dates = dates_of_df['Days'].values.tolist()
    if len(sel_dates) >= 2:
        last_d = sel_dates[-1]
        bef_last_d = sel_dates[-2]
        df_last_d = df.loc[(df['time'] >= bef_last_d) & (df['time'] <= last_d)]
        last_d_h = add_hours(df_last_d)
        last_h = int(last_d_h[-1])
        b_last_h = last_h - 1
        last_h_last_day = df_last_d.loc[(df_last_d.time.dt.hour > b_last_h) & (df_last_d.time.dt.hour <= last_h), :]
    else:
        last_d = sel_dates[0]
        df_last_d = df
        last_d_h = add_hours(df_last_d)
        last_h = int(last_d_h[-1])
        b_last_h = last_h - 1
        last_h_last_day = df_last_d.loc[(df_last_d.time.dt.hour > b_last_h) & (df_last_d.time.dt.hour <= last_h), :]
        
    temp_set  = last_h_last_day.temperature
    hum_set = last_h_last_day.humidity
    DD = pd.DataFrame({'temperature': temp_set, 'humidity': hum_set})
    temp_mean = round(DD.temperature.mean(), 2)
    hum_mean = round(DD.humidity.mean(), 2)
    hum_mean_str = str(hum_mean)
    
    # FOR REAL MEASUREMENT
    #if the surface of the window is on the left/right
    #tr = (0.18*(temp_mean + temp_mean) + 0.22*(temp_mean + act_tem) + 0.30*(temp_mean + temp_mean))/(1.4)
    tr = temp_mean
    
    #FOR REGISTERED DATA
    
    #reg_data = pd.read_excel(r'C:\Users\New\Desktop\Python Script\PYTHON PROGRAMS\XLSX FILES ROOM NAMES\Files selected from all data\All data folder\TKINTER\REPORT METEO MILANO\INTERO ANNO 2019\Temperature_2019.xlsx', engine='openpyxl' )
    
    data_ref = last_d
    
    #LABEL
    
    Title_Label = tk.Label(frame1, text ='MET parameter - Metabolic Rate',  bg = '#b3d9ff', font = FFont, relief="groove")
    Title_Label.place(x = 25, y = 0)
    
    Title_Label_clo = tk.Label(frame1, text ='CLO parameter - Clothing Index',  bg = '#b3d9ff', font = FFont, relief="groove")
    Title_Label_clo.place(x = 25, y =  125)
    
    Title2_Label = tk.Label(frame1, text ='Parameters for PMV calculation',  bg = '#b3d9ff', font = FFont, relief="groove")
    Title2_Label.place(x = 300, y = 0)
    
    Zero_Label = tk.Label(frame1, text ='No metabolic rate selected',  bg = '#b3d9ff', font = FFont, relief="groove")
    Zero_Label.place(x = 25, y = 50)
    
    Zero_Label_2 = tk.Label(frame1, text ='No clothing selected',  bg = '#b3d9ff', font = FFont, relief="groove")
    Zero_Label_2.place(x = 25, y =  175)
    
    Met_Label_t = tk.Label(frame1, text ='Met:',  bg = '#b3d9ff', font = FFont, relief="groove")
    Met_Label_t.place(x = 350, y = 25)
    
    Met_Label = tk.Label(frame1, text ='%s' %(met),  bg = '#b3d9ff', font = FFont, relief="groove")
    Met_Label.place(x = 400, y = 25)
    
    Clo_Label_t = tk.Label(frame1, text ='Clo:',  bg = '#b3d9ff', font = FFont, relief="groove")
    Clo_Label_t.place(x = 350, y = 50)
    
    Mrt_Label = tk.Label(frame1, text ='Mrt:',  bg = '#b3d9ff', font = FFont, relief="groove")
    Mrt_Label.place(x = 350, y = 75)
    
    Mrt_Label_t = tk.Label(frame1, text ='%s' %(tr),  bg = '#b3d9ff', font = FFont, relief="groove")
    Mrt_Label_t.place(x = 400, y = 75)
    
    Clo_Label = tk.Label(frame1, text ='%s' %(clo),  bg = '#b3d9ff', font = FFont, relief="groove")
    Clo_Label.place(x = 400, y = 50)
    
    Rel_Vel_Label = tk.Label(frame1, text = 'vr:',  bg = '#b3d9ff', font = FFont, relief="groove")
    Rel_Vel_Label.place(x = 500, y = 25)
    
    Rel_vel_Value_Label = tk.Label(frame1, text = '%s' %(vr),  bg = '#b3d9ff', font = FFont, relief="groove")
    Rel_vel_Value_Label.place(x = 550, y = 25)
    
    Rel_hum_Value_Label = tk.Label(frame1, text = 'Rel. Hum. : %s' %(hum_mean_str),  bg = '#b3d9ff', font = FFont, relief="groove")
    Rel_hum_Value_Label.place(x = 500, y = 50)
    
    # COMBOS
    
    Combo0 = ttk.Combobox(frame1, values = act_list)
    Combo0.place( x = 25, y =  25)
    
    Combo1 = ttk.Combobox(frame1, values = clo_list,  width = 50)
    Combo1.place( x = 25, y =  150)
    
    #BUTTONS
    
    btn0 = tk.Button(frame1, text="Select the activity", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo_met(Combo0, Zero_Label, frame1, df, Met_Label, met_value))
    btn0.place( x = 25, y =  75)
    
    btn1 = tk.Button(frame1, text="Select the clothing", bg = '#b3d9ff', font = FFont, command=lambda: checkcombo_clo(Combo1, Zero_Label_2, frame1, df, Clo_Label, clo_value))
    btn1.place( x = 25, y =  200)
    
    btn2 = tk.Button(frame1, text="Calculate Relative velocity", bg = '#b3d9ff', font = FFont, command=lambda: rel_vel_calc(Rel_vel_Value_Label, frame1, Met_Label))
    btn2.place( x = 25, y =  250)
    
    btn3 = tk.Button(frame1, text="Calculate PMV and PPD", bg = '#b3d9ff', font = FFont, command=lambda: PMV_PPD(frame1, temp_mean, tr, Rel_vel_Value_Label, hum_mean, Met_Label, Clo_Label ))
    btn3.place( x = 25, y =  300)
    
    btn4 = tk.Button(frame1, text="Print data", bg = '#b3d9ff', font = FFont, command=lambda: print_crit(df))
    btn4.place( x = 300, y =  300)
    

    def print_crit(df):
        window1 = tk.Toplevel(root)
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        window1.geometry("1300x600")
        frame0 = tk.LabelFrame(window1, text = "Graph Plot", bg='#1a8cff', font = FFont)
        frame0.place(height= 600, width = 1300) 
        upper = 60
        lower = 40
        fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(20,5))
        axes.set_ylabel(r'% RH ($\pm$ 3 %)')
        
        time = df['time']
        hum = df['humidity']
        
        upper = 60
        lower = 40

        supper = np.ma.masked_where(hum < upper, hum)
        slower = np.ma.masked_where(hum > lower, hum)
        smiddle = np.ma.masked_where((hum < lower) | (hum > upper), hum)

        axes.grid()
        axes.plot(time, smiddle, time, supper, time, slower, label = 'humidity', alpha=.9)
        axes.set_title('Humidity', fontsize=12)
        axes.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=frame0)
        toolbar = NavigationToolbar2Tk(canvas, frame0)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas.get_tk_widget().pack()
        canvas.draw()
    

        return None
    def checkcombo_met(Combo0, Zero_Label, frame1, df, Met_Label, met_value):
        met = '0'
        value = Combo0.get()
        Zero_Label.config(text= value)   
        if value == 'Sleeping':
            met = '0.7'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Reclining':
            met = '0.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Seated, quiet':
            met = '1.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Reading, seated':
            met = '1.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Writing':
            met = '1.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Typing':
            met = '1.1'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Standing, relaxed':
            met = '1.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Filing, seated':
            met = '1.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Flying aircraft, routine':
            met = '1.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Filing, standing':
            met = '1.4'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Driving a car':
            met = '1.5'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Walking about':
            met = '1.7'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Cooking':
            met = '1.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Table sawing':
            met = '1.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Walking 2mph (3.2kmh)':
            met = '2.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Lifting/packing':
            met = '2.1'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Seated, heavy limb movement':
            met = '2.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Light machine work':
            met = '2.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Flying aircraft, combat':
            met = '2.4'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Walking 3mph (4.8kmh)':
            met = '2.6'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'House cleaning':
            met = '2.7'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Driving, heavy vehicle':
            met = '3.2'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Dancing':
            met = '3.4'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Calisthenics':
            met = '3.5'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Walking 4mph (6.4kmh)':
            met = '3.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Tennis':
            met = '3.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Heavy machine work':
            met = '4.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Handling 100lb (45 kg) bags':
            met = '4.0'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Pick and shovel work':
            met = '4.4'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Basketball':
            met = '6.3'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
        if value == 'Wrestling':
            met = '7.8'
            Met_Label.config(text= "%s" %(met))
            met_value = float(met)
    
        return None
    
    def checkcombo_clo(Combo1, Zero_Label_2, frame1, df, Clo_Label, clo_value):
        clo = '0'
        value = Combo1.get()
        Zero_Label_2.config(text= value) 
        
        if value == 'Walking shorts, short-sleeve shirt':
            clo = '0.36'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Typical summer indoor clothing':
            clo = ' 0.5'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Knee-length skirt, short-sleeve shirt, sandals, underwear':
            clo = '0.54'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Trousers, short-sleeve shirt, socks, shoes, underwear':
            clo = '0.57'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Trousers, long-sleeve shirt':
            clo = '0.61'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Knee-length skirt, long-sleeve shirt, full slip':
            clo = '0.67'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Sweat pants, long-sleeve sweatshirt':
            clo = '0.74'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Jacket, Trousers, long-sleeve shirt':
            clo = '0.96'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
        if value == 'Typical winter indoor clothing':
            clo = '1.0'
            Clo_Label.config(text= "%s" %(clo))
            clo_value = float(clo)
            
        return None
    
    def PMV_PPD(frame1, temp_mean, tr, Rel_vel_Value_Label, hum_mean, Met_Label, Clo_Label):
        vr = float(Rel_vel_Value_Label['text'])
        met = float(Met_Label['text'])
        clo = float(Clo_Label['text'])
        RES = pythermalcomfort.models.pmv_ppd(temp_mean, tr, vr, hum_mean, met, clo, wme=0, standard= 'ASHRAE', units='SI')
        PMV = str(RES['pmv'])
        PPD = str(RES['ppd'])
        
        PMV_label =  tk.Label(frame1, text = 'Predictive Mean Vote : %s' %(PMV),  bg = '#b3d9ff', font = FFont, relief="groove")
        PMV_label.place(x = 600, y = 100)
                        
        PPD_label =  tk.Label(frame1, text = 'Predicted Percentage of Dissatisfied : %s' %(PPD),  bg = '#b3d9ff', font = FFont, relief="groove")
        PPD_label.place(x = 600, y = 150)
        
        txt = tk.Text(frame1, bg = '#b3d9ff', font = FFont)
        txt.insert(INSERT, "Description of the PMV - PPD values\n")
        txt.insert(END, "")
        txt.configure(font=FFont)
        txt.place(x = 600, y = 200, height = 100, width = 400)
        
        #ACCORDING TO UNI EN ISO 7730, Tab A.1)
        if (RES['pmv'] <= -2) & (RES['pmv'] > -3):
            txt.insert(INSERT, "Cold climate: need to increase a lot the temperature.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= -1) & (RES['pmv'] > -2):
            txt.insert(INSERT, "Cool climate: need to increase the temperature.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= -0.7) & (RES['pmv'] > -1):
            txt.insert(INSERT, "Slightly cool climate: little increase the temperature.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= 0.7) & (RES['pmv'] > -0.7):
            txt.insert(INSERT, "Acceptable climate: Nothing to do by now.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= 1) & (RES['pmv'] > 0.7):
            txt.insert(INSERT, "Slightly warm climate: little decrease the temperature.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= 2) & (RES['pmv'] > 1):
            txt.insert(INSERT, "Warm climate: need to decrease the temperature.\n")
            txt.insert(END, "")
        if (RES['pmv'] <= 3) & (RES['pmv'] > 2):
            txt.insert(INSERT, "Hot climate: need to decrease a lot the temperature.\n")
            txt.insert(END, "")
        
        return None
    
    def rel_vel_calc(Rel_vel_Value_Label, frame1, Met_Label):
        met_value = float(Met_Label['text'])
        rel_vel_air = pythermalcomfort.psychrometrics.v_relative(v, met_value)
        rl = str(rel_vel_air)
        Rel_vel_Value_Label = tk.Label(frame1, text = '%s' %(rl),  bg = '#b3d9ff', font = FFont, relief="groove")
        Rel_vel_Value_Label.place(x = 550, y = 25)
        
        return None
    
    return None


#########################################################################################################################################################################################################################################

def Analysis_part(label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1300x800")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame = tk.LabelFrame(window1, text = "Prediction analysis window", bg = '#1a8cff', font = FFont)
    frame.place(x = 0, y = 0, height = 800, width = 1300)
    frame1 = tk.LabelFrame(frame, text = "Options to be chosen for analysis", bg = '#1a8cff', font = FFont)
    frame1.place(x = 0, y = 75, height = 575, width = 1300)
    frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
    frame2.place(x = 700, y = 0, height = 600, width = 600)
    frame3 = tk.LabelFrame(frame, text = "Multiple dataset analysis", bg = '#1a8cff', font = FFont)
    frame3.place(x = 0, y = 225, height = 600, width = 700)
    
    txt = tk.Text(frame, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "The following analysis part is aimed to evaluate, through statistical tests, the features of the dataset. First select the alpha test of the statistical test and the column to be examined of the dataframe.\nThe last part is dedicated to multivariate analysis; it's important that all data to be analyzed have to be in the same folder. Select multiple files keeping Ctrl button.\nFor the resampling rate, insert a number, plus : D for days, H for hours, T for minutes, S for seconds. For select the days, you must select also the name of the dataset")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 75, width = 1300)  
    
    txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont)
    txt2.insert(INSERT, "")
    txt2.insert(END, ".")
    txt2.configure(font=FFont)
    txt2.place(x = 0, y = 0, height = 100, width = 550)

    col_list = df.columns.to_list()
    
    sublist = add_dates(df.time)
    sublist = sublist.Days.to_list()
    
    LLIST = tk.Listbox(frame, bg = '#b3d9ff', font = FFont, selectmode = 'multiple', height = 3, width=10)
    LLIST.place(x = 400, y =  100)
    
    h = 0
    for i in range(len(col_list)):
        LLIST.insert(h, col_list[i])
        h = h + 1

    alpha_label =  tk.Label(frame1, text = 'Select the alpha test\nas a percentage number',  bg = '#b3d9ff', font = FFont, relief="groove")
    alpha_label.place(x = 25, y = 25)
    
    E1 = tk.Entry(frame1, bd =2)
    E1.place(x = 200, y = 25)
    
    tests = ["Data features",
            "Shapiro-Wilk Test",
             "Chi square independency test",
             "Linear regression",
             "Pearson R test",
             "Spearman R test"]
    
    Combo1= ttk.Combobox(frame1, values = tests, width = 25)
    Combo1.place( x = 350, y =  75)
    
    btn = tk.Button(frame1, text="Select the alpha percent and then test", bg = '#b3d9ff', font = FFont, command=lambda: menu_test(df, E1, LLIST, Combo1, frame2))
    btn.place( x = 25, y =  75)
    
    btn_graph = tk.Button(frame1, text="Plot original data ", bg = '#b3d9ff', font = FFont, command=lambda: plot_newest_data(df, sublist))
    btn_graph.place( x = 525, y =  25)
    
    label_file = tk.Label(frame3, text = "No file selected", bg = '#b3d9ff', font = FFont, relief="groove")
    label_file.place(x = 25, y = 300)
    label_file.place_forget()
        
    button1 = tk.Button(frame3, text = "Select files\n from folder", bg = '#b3d9ff', font = FFont, command =lambda: File_dialog_2(label_file)) #Open the window directory
    button1.place(x = 25, y = 25)

    button2 = tk.Button(frame3, text = "Load files from folder", bg = '#b3d9ff', font = FFont, command = lambda: Load_excel_datas(label_file, frame3, df, frame2))
    button2.place(x = 175, y = 25)
    
    
    def stat_Data_Feature(df, E1, LLIST, frame2):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Data Features", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        alphatest = float(E1.get()) / 100
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        
        txt2.insert(INSERT, "\nData Features in total and day by day\n")
        txt2.insert(END, "")

        List = []
        choices = LLIST.curselection()
        List.append('time')
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        dataref = table_features(df, List)
        col_list = dataref.columns.to_list()
        stringg = []
        
        for i in range(len(dataref)):
            rr = dataref.iloc[i, :]
            kk = '\n'
            hh = '\n'
            for j in range(len(col_list)):
                jj = str(rr[col_list[j]])
                kk = '' + kk + ''+ col_list[j] + '\n' + jj + '\n'
            kk = kk + '\n'
            stringg.append(kk)
                
        
        for i in range(len(stringg)):
            string_resp = stringg[i]
            txt2.insert(INSERT, string_resp)
            txt2.insert(END, "")
    
        return None 


    def stat_shapiro_testing(df, E1, LLIST, frame2):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        alphatest = float(E1.get()) / 100
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        
        txt2.insert(INSERT, "\nShapiro-Wilk Test\nNull hypothesis: Normally distributed population\nCounter hypothesis: Non Normally distributed hypothesis")
        txt2.insert(END, "")

        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1
        
        col_list = new_df.columns.to_list()
        index = new_df.index
        number_of_rows = len(index)
        if number_of_rows > 5000:
            diff = number_of_rows - 5000
            drop_indices = np.random.choice(new_df.index, diff, replace=False)
            df_subset = new_df.loc[drop_indices, :]
            new_df = new_df.drop(drop_indices)
        
        for i in range(len(col_list)):
            ref = col_list[i]
            colo = new_df["%s" %(ref)]
            shap = stats.shapiro(colo)
            
            if shap[1] > alphatest:
                string_resp = "\nShapiro test for Normal Distribution\nWe cannot refuse the hypothesis that the distribution of " + ref + " comes from a Normal Distribution\nStatistics: " + str((shap[0], 3)) + " P-value:" + str((shap[1])) + ".\n"
            else:
               string_resp = "\nShapiro test for Normal Distribution\nWe cannot refuse the hypothesis that the distribution of " + ref + " doesn't come from a Normal Distribution\nStatistics: " + str((shap[0])) + " P-value:" + str((shap[1])) + ".\n"
            txt2.insert(INSERT, string_resp)
            txt2.insert(END, "")
    
        return None 

    def stat_chisquare_testing(df, E1, LLIST, frame2):
        
        alphatest = float(E1.get()) / 100
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nChi squared Test for independence\nNull hypothesis: Independent Datasets\nCounter hypothesis: Non Independent dataset\n")
        txt2.insert(END, "")
        
        col_list = df.columns.to_list()
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1
        
        col_list2 = new_df.columns.to_list()
        for i in range(len(col_list2)):
            coll = col_list2[i]
            selected = new_df["%s" %(coll)]
            for j in range(len(col_list2)):
                collo = col_list2[j]
                if (coll != collo) & (i >= j):
                    second_sel = new_df["%s" %(collo)]     
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if pval > alphatest:
                        string_resp = "\nChi square test for independence\nWe cannot refuse the hypothesis that " + coll + " and " + collo + " are independent\nStatistics: " + str(round(stat, 3)) + " P-value:" + str(pval) + ".\n"
                    else:
                       string_resp = "\nChi square test for independence\nWe cannot refuse the hypothesis that " + coll + " and " + collo + " aren't independent\nStatistics: " + str(round(stat, 3)) + " P-value:" + str(pval) + ".\n"
                    
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None
    
    def stat_pearsonr_testing(df, E1, LLIST, frame2):
        
        alphatest = float(E1.get()) / 100
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nPearson R Test for correlations\nThe procedure has as results the Pearson Correlation Coefficient and the two-tailed p-value\n")
        txt2.insert(END, "")
        
        col_list = df.columns.to_list()
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1
        
        col_list2 = new_df.columns.to_list()
        for i in range(len(col_list2)):
            coll = col_list2[i]
            selected = new_df["%s" %(coll)]
            for j in range(len(col_list2)):
                collo = col_list2[j]
                if (coll != collo) & (i >= j):
                    second_sel = new_df["%s" %(collo)]     
                    shap = stats.shapiro(selected)
                    shap2 = stats.shapiro(second_sel)
                    
                    if (shap[1] > alphatest) & (shap2[1] > alphatest):
                        pears = stats.pearsonr(selected, second_sel)
                        if pears[1] > alphatest:
                            string_resp = "\nPearson R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(pears[0], 3)) + " and the relative two-tailed p-value is :" + str(round(pears[1], 3)) + "We cannot refuse the hypothesis that two dataset are uncorrelated.\n"
                        else:
                            string_resp = "\nPearson R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(pears[0], 3)) + " and the relative two-tailed p-value is :" + str(round(pears[1], 3)) + "We cannot refuse the hypothesis that two dataset are correlated.\n"
                    else:
                       string_resp = "\nDue to the fact that the two dataset aren't Normal, we cannot apply the Pearson R test.\nA good substitute of this test is Spearman R test\n"
                    
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

    
        return None 
    
    def stat_spearmanr_testing(df, E1, LLIST, frame2):
        
        alphatest = float(E1.get()) / 100
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nSpearman R Test for correlations\nThe procedure has as results the Spearman Correlation Coefficient and the two-tailed p-value.\nNull Hypothesis: the two sets are uncorrelated\nCounter Hypothesiss: the two sets are correlated\n")
        txt2.insert(END, "")
        
        col_list = df.columns.to_list()
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1
        
        col_list2 = new_df.columns.to_list()
        for i in range(len(col_list2)):
            coll = col_list2[i]
            selected = new_df["%s" %(coll)]
            for j in range(len(col_list2)):
                collo = col_list2[j]
                if (coll != collo) & (i >= j):
                    second_sel = new_df["%s" %(collo)]     
                    spear = stats.spearmanr(selected, second_sel)
                    
                    if spear[1] > alphatest:
                        string_resp = "\nSpearman R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(spear[0], 3)) + " and the relative p-value is :" + str(round(spear[1], 3)) + "\nWe cannot refuse the hypothesis that the two dataset are uncorrelated.\n"
                    else:
                        string_resp = "\nSpearman R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(spear[0], 3)) + " and the relative p-value is :" + str(round(spear[1], 3)) + "\nWe cannot refuse the hypothesis that two dataset are correlated.\n"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

    
        return None
    
    def stat_linregr_testing(df, E1, LLIST, frame2):
        
        alphatest = float(E1.get()) / 100
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nLinear regression between datasets\nThe procedure has as results the slope, the intercept of regressionline, the correlation coefficient, the p-value and the standard error\n")
        txt2.insert(END, "")
        
        col_list = df.columns.to_list()
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1
        
        col_list2 = new_df.columns.to_list()
        for i in range(len(col_list2)):
            coll = col_list2[i]
            selected = new_df["%s" %(coll)]
            for j in range(len(col_list2)):
                collo = col_list2[j]
                if (coll != collo) & (i >= j):
                    second_sel = new_df["%s" %(collo)]     
                    lin = stats.linregress(selected, second_sel)
                    if lin[3] > alphatest:
                        string_resp = """\nLinear Regression\nThe slope between """ + coll + """ and """ + collo +""" is equal to: """ + str(round(lin[0], 3)) + """, the intercept of the regression line is: """ +  str(round(lin[1], 3)) + """, the correlation coefficient is: """ +  str(round(lin[2], 3))  + """ and the relative p-value is :""" + str(round(lin[3], 3)) + """.\nThe standard error of the estimated slope (gradient), under the assumption of residual normality is: """ +  str(round(lin[4], 3)) +""".\nWe cannot refuse the hypothesis that the slope is equal to zero.\n"""
                    else:
                        string_resp = """\nLinear Regression\nThe slope between """ + coll + """ and """ + collo +""" is equal to: """ + str(round(lin[0], 3)) + """, the intercept of the regression line is: """ +  str(round(lin[1], 3)) + """, the correlation coefficient is: """ +  str(round(lin[2], 3))  + """ and the relative p-value is :""" + str(round(lin[3], 3)) + """.\nThe standard error of the estimated slope (gradient), under the assumption of residual normality is: """ +  str(round(lin[4], 3)) +""".\nWe cannot refuse the hypothesis that the slope is not equal to zero.\n"""
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

    
        return None 
    
    def File_dialog_2(label_file):
        files = filedialog.askopenfilename(multiple=True) # asks user to choose a director
        label_file["text"] = files
        return None
    
    def Load_excel_datas(label_file, frame3, df, frame2):
        file_path = label_file["text"]
        try:
            var = root.tk.splitlist(file_path)
            filePaths = []
            for f in var:
                filePaths.append(f)
        except ValueError:
            tk.messagebox.showerror("Information","The file you have chosen is unvalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information",f"No such file as {file_path}")
            return None
        
        if filePaths[0].endswith(".xlsx"):
            ref_dataset = pd.read_excel(filePaths[0], engine="openpyxl")
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            col_list = ref_dataset.columns.to_list()
            tot_list = col_list
            dd = add_dates_2(ref_dataset.time)
            dd = dd.Days.to_list()
            dates = []
            dates_2 = []
            dates.append(string_slicing(filePaths[0]))
            for jj in dd:
                dates.append(jj)
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_excel(filePaths[j], engine="openpyxl")
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                dd = add_dates_2(dataset.time)
                dd = dd.Days.to_list()
                dates.append(string_slicing(filePaths[j]))
                for jj in dd:
                    dates.append(jj)
                    dates_2.append(jj)
                col_list_2 = dataset.columns.to_list()
                for k in col_list_2:
                    if k in tot_list:
                        tot_list.append(k)
                        
            tot_list = remove_duplicates_from_list(tot_list)
        
        if filePaths[0].endswith(".csv"):
            ref_dataset = pd.read_csv(filePaths[0])
            ref_dataset = ref_dataset.loc[:, ~ref_dataset.columns.str.match('Unnamed')]
            colcol = ref_dataset.columns.to_list()
            if 'time' in colcol:
                ref_dataset['time'] = pd.to_datetime(ref_dataset['time'], errors='coerce')
            col_list = ref_dataset.columns.to_list()
            tot_list = col_list
            dd = add_dates_2(ref_dataset.time)
            dd = dd.Days.to_list()
            dates = []
            dates_2 = []
            dates.append(string_slicing(filePaths[0]))
            for jj in dd:
                dates.append(jj)
                dates_2.append(jj)
            for i in range(len(filePaths) - 1):
                j = i + 1
                dataset = pd.read_csv(filePaths[j])
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                dd = add_dates_2(dataset.time)
                dd = dd.Days.to_list()
                dates.append(string_slicing(filePaths[j]))
                for jj in dd:
                    dates.append(jj)
                    dates_2.append(jj)
                col_list_2 = dataset.columns.to_list()
                for k in col_list_2:
                    if k in tot_list:
                        tot_list.append(k)
                        
            tot_list = remove_duplicates_from_list(tot_list)
        
        dates_2 = commonelements(dates_2)
            
        commond = tk.Listbox(frame3, bg = '#b3d9ff', font = FFont, height = 6, width=10)
        commond.place(x = 25, y = 200)
        
        title_file_2 = tk.Label(frame3, text = "Common days", bg = '#b3d9ff', font = FFont, relief="groove")
        title_file_2.place(x = 25, y = 175)
        
        h = 0
        for i in range(len(dates_2)):
            commond.insert(h, dates_2[i])
            h = h + 1
            
        title_file = tk.Label(frame3, text = "Select columns to test", bg = '#b3d9ff', font = FFont, relief="groove")
        title_file.place(x = 400, y = 0)

        LLIST = tk.Listbox(frame3, bg = '#b3d9ff', font = FFont, selectmode = 'multiple', height = 3, width=10)
        LLIST.place(x = 400, y =  25)
        
        columns_frame = tk.Label(frame3, text = "", bg = '#b3d9ff', font = FFont, relief="groove")
        columns_frame.place(x = 100, y = 100)
        columns_frame.place_forget()
        
        h = 0
        for i in range(len(tot_list)):
            LLIST.insert(h, tot_list[i])
            h = h + 1
        
        btn_col = tk.Button(frame3, text="Select columns\nto examinate", bg = '#b3d9ff', font = FFont, command=lambda: put_columns(columns_frame, LLIST))
        btn_col.place( x = 500, y =  25)
        
        sampling_file = tk.Label(frame3, text = "Select sampling rate", bg = '#b3d9ff', font = FFont, relief="groove")
        sampling_file.place(x = 25, y = 75)
        
        E1 = tk.Entry(frame3, bd =3)
        E1.place(x = 175, y = 75)
        
        alpha_file = tk.Label(frame3, text = "", bg = '#b3d9ff', font = FFont, relief="groove")
        alpha_file.place(x = 525, y = 525)
        alpha_file.place_forget()
        
        alpha_label =  tk.Label(frame3, text = 'Select the alpha test\nas a percentage number',  bg = '#b3d9ff', font = FFont, relief="groove")
        alpha_label.place(x = 200, y = 350)

        E2 = tk.Entry(frame3, bd =2, width=4)
        E2.place(x = 200, y = 400)
        
        btn_alpha = tk.Button(frame3, text="Insert alpha", bg = '#b3d9ff', font = FFont, command=lambda: put_alpha(alpha_file, E2))
        btn_alpha.place(x = 300, y = 400)
    
        dates_file = tk.Label(frame3, text = "Select the \nstarting and ending date", bg = '#b3d9ff', font = FFont, relief="groove")
        dates_file.place(x = 25, y = 125)

        LLIST2 = tk.Listbox(frame3, bg = '#b3d9ff', font = FFont, selectmode = 'multiple', height = 6, width=25)
        LLIST2.place(x = 200, y =  125)
        
        h = 0
        for i in range(len(dates)):
            LLIST2.insert(h, dates[i])
            h = h + 1
        
        tests = [
                 "Shapiro-Wilk Test",
                 "Chi square independency test",
                 "Linear regression",
                 "Pearson R test",
                 "Spearman R test",
                 "T test for paired samples",
                 "T test for unpaired samples",
                 "Wilcoxon rank test",
                 "Mann-Whitney U test",
                 "ANOVA one way test",
                 "Kruskal-Wallis H test"
                 ]
        
        
        test_label = tk.Label(frame3, text = "Select test", bg = '#b3d9ff', font = FFont, relief="groove")
        test_label.place(x = 500, y = 225)
        
        Combo1= ttk.Combobox(frame3, values = tests, width = 25)
        Combo1.place( x = 500, y =  250)
        
        points_label = tk.Label(frame3, text = "N° of points: ", bg = '#b3d9ff', font = FFont, relief="groove")
        points_label.place(x = 500, y = 175)
        
        btn_resample = tk.Button(frame3, text="Compute test", bg = '#b3d9ff', font = FFont, command=lambda: resample_common(filePaths, LLIST2, frame3, dates, E1, LLIST, columns_frame, Combo1, frame2, alpha_file, points_label))
        btn_resample.place( x = 500, y =  125)
        
        
        return None
    
    def put_columns(columns_frame, LLIST):
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
            
            
        total = ','.join(List)
        
        columns_frame['text'] = total
        return None
    
    def put_alpha(alpha_file, E2):
        
        alphatest = float(E2.get()) / 100
        alphatest = str(alphatest)
        alpha_file['text'] = alphatest
        
        return None
    
    def resample_common(filePaths, LLIST2, frame3, dates, E1, LLIST, columns_frame, Combo1, frame2, alpha_label, points_label):
        
        points_label.place_forget()
        
        test = Combo1.get()
        
        alphatest = alpha_label['text']
        alphatest = float(alphatest)
        
        ref_columns = columns_frame['text']
        ref_columns = ref_columns.split(',')
        
        ins = E1.get()
        
        List = []
        List_col = []
        choices = LLIST2.curselection()
        for i in choices:
            ent = LLIST2.get(i)
            List.append(ent)
        choices2 = LLIST.curselection()
        for i in choices2:
            ent = LLIST.get(i)
            List_col.append(ent)
        total_df = pd.DataFrame()
        DDD = pd.DataFrame()
        final_df = pd.DataFrame()
        
        if filePaths[0].endswith(".xlsx"):
            for i in range(len(filePaths)):

                h = 0
                ddd = []
                dataset = pd.read_excel(filePaths[i], engine="openpyxl")
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = dataset.columns.to_list()
                ind1 = ''
                ind2 = ''
                refind = 0
                if 'time' in colcol:
                    dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                if (i < (len(filePaths) - 1)):
                    ii = i + 1
                    for j in range(len(List)):
                        if  string_slicing(filePaths[i]) == List[j]:
                            ind1 = string_slicing(filePaths[i])
                            refind = j + 1
                        if  string_slicing(filePaths[ii]) == List[j]:
                            ind2 = string_slicing(filePaths[ii])
                    for k in range(len(List)):
                        kk = refind + k
                        if (ind2 == List[kk]):
                            break
                        else:
                            ddd.append(List[kk])
                else:
                    for j in range(len(List)):
                        if (List[j] == string_slicing(filePaths[i])):
                            ddd = List[j:]
                    del ddd[0]
                
                for d in ddd:
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    DDD = dataset.loc[(dataset.time >= date) & (dataset.time < date2), :]
                    total_df = total_df.append(DDD)
                total_df = convert_to_periodtimeindex(total_df)
                total_df = total_df.resample(ins).mean().interpolate('time')
                list_col_dataframe = total_df.columns.to_list()
                title = string_slicing(filePaths[i])
                title = cut_extension(title)
                for col in list_col_dataframe:
                    string = '' + title + '_' + col + ''
                    final_df['%s' %(string)] = total_df['%s' %(col)]

        final_df = final_df.interpolate('time')
        index = final_df.index
        number_of_rows = len(index)
        points_label = tk.Label(frame3, text = "N° of points: "+ str(number_of_rows), bg = '#b3d9ff', font = FFont, relief="groove")
        points_label.place(x = 500, y = 175)
                
        
        if filePaths[0].endswith(".csv"):
            for i in range(len(filePaths)):
                h = 0
                ddd = []
                dataset = pd.read_csv(filePaths[i])
                dataset = dataset.loc[:, ~dataset.columns.str.match('Unnamed')]
                colcol = dataset.columns.to_list()
                ind1 = ''
                ind2 = ''
                if 'time' in colcol:
                    dataset['time'] = pd.to_datetime(dataset['time'], errors='coerce')
                if (i < (len(filePaths) - 1)):
                    ii = i + 1
                    for j in range(len(List)):
                        if List[j] == string_slicing(filePaths[i]):
                            ind1 = string_slicing(filePaths[i])
                        if List[j] == string_slicing(filePaths[ii]):
                            ind2 = string_slicing(filePaths[ii])
                    for k in range(len(List)):
                        if (ind2 == List[k]):
                            break
                        else:
                            ddd.append(List[k])
                    del ddd[0]
                else:
                    for j in range(len(List)):
                        if (List[j] == string_slicing(filePaths[i])):
                            ddd = List[j:]
                    del ddd[0]
                
                for d in ddd:
                    
                    date = datetime.strptime(d, '%Y-%m-%d')
                    date2 = date + timedelta(days=1)
                    DDD = dataset.loc[(dataset.time >= date) & (dataset.time < date2), :]
                    total_df = total_df.append(DDD)
                total_df = convert_to_periodtimeindex(total_df)
                total_df = total_df.resample(ins).mean().interpolate('time')
                list_col_dataframe = total_df.columns.to_list()
                title = string_slicing(filePaths[i])
                title = cut_extension(title)
                for col in list_col_dataframe:
                    string = '' + title + '_' + col + ''
                    final_df['%s' %(string)] = total_df['%s' %(col)]

        final_df = final_df.interpolate('time')
        index = final_df.index
        number_of_rows = len(index)
        points_label = tk.Label(frame3, text = "N° of points: "+ str(number_of_rows), bg = '#b3d9ff', font = FFont, relief="groove")
        points_label.place(x = 500, y = 175)

        menu_test_2(final_df, frame2, alphatest, test, LLIST)

        return None 
    
    
    def plot_newest_data(df, sublist):
        window1 = tk.Toplevel(root)
        window1.geometry("1000x500")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
        frame0.place( height = 500, width = 1000) 
                
        x_time = pd.to_datetime(df.time, unit = 'ns')
            
        # COMBOBOX
        
        col_list = df.columns.to_list()
        col_list.remove('time')
        
        option_vector = []
        
        for i in range(len(col_list)):
            ref = "Show " + col_list[i]
            option_vector.append(ref)
                    
        aggregations = ["mean",
                        "standard deviation",
                        "standard deviation 2",
                        "standard deviation 3",
                        "median"
                        ]
                    
        global List_aggr
        List_aggr = []
                    
        Combo1 = ttk.Combobox(frame0, values = option_vector)
        Combo1.place( x = 50, y =  50)
                    
        First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
        First_Label.place(x = 250, y = 50)
                
        Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
        Second_Label.place(x = 450, y = 100)
            
        btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
        btn.place( x = 200, y =  100)
                    
        btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
        btn2.place( x = 50, y =  100)
                    
        Combo2 = ttk.Combobox(frame0, values = aggregations)
        Combo2.place( x = 50, y =  250)
                
        Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
        Aggr_List.place(x = 450, y =  150)
                    
        btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
        btn3.place( x = 50, y =  300)
                    
        btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
        btn4.place( x = 50, y =  150)
                    
        return None
    
    def menu_test(df, E1, LLIST, Combo1, frame2):
        selection = Combo1.get()
        if selection == "Shapiro-Wilk Test":
            stat_shapiro_testing(df, E1, LLIST, frame2)
        if selection == "Chi square independency test":
            stat_chisquare_testing(df, E1, LLIST, frame2)
        if selection == "Pearson R test":
            stat_pearsonr_testing(df, E1, LLIST, frame2)
        if selection == "Spearman R test":
            stat_spearmanr_testing(df, E1, LLIST, frame2)
        if selection == "Linear regression":
            stat_linregr_testing(df, E1, LLIST, frame2)
        if selection == "Data features":
            stat_Data_Feature(df, E1, LLIST, frame2)
            
   
    def stat_shapiro_testing_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nShapiro-Wilk Test\nNull hypothesis: Normally distributed population\nCounter hypothesis: Non Normally distributed hypothesis\n")
        txt2.insert(END, "")

        col_list = final_df.columns.to_list()
        
        for i in range(len(col_list)):
            ref = col_list[i]
            colo = final_df["%s" %(ref)].dropna()
            shap = stats.shapiro(colo)
            
            if shap[1] > alphatest:
                string_resp = "\nShapiro test for Normal Distribution\nWe cannot refuse the hypothesis that the distribution of " + ref + " comes from a Normal Distribution\nStatistics: " + str((shap[0], 3)) + " P-value:" + str((shap[1])) + ".\n"
            else:
               string_resp = "\nShapiro test for Normal Distribution\nWe cannot refuse the hypothesis that the distribution of " + ref + " doesn't come from a Normal Distribution\nStatistics: " + str((shap[0])) + " P-value:" + str((shap[1])) + ".\n"
            txt2.insert(INSERT, string_resp)
            txt2.insert(END, "")
    
        return None 
    
    def stat_chi_square_testing_2(final_df, frame2, alphatest):

        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nChi squared Test for independence\nNull hypothesis: Independent Datasets\nCounter hypothesis: Non Independent dataset\n")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
        
        for i in range(len(col_list)):
            coll = col_list[i]
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                if (coll != collo):
                    second_sel = final_df["%s" %(collo)].dropna()
                    if (not(selected.empty) and not(second_sel.empty)):
                        cross = crosstable_periods(selected, second_sel)
                        chi2 = chi2_contingency(cross)
                        stat = chi2[0]
                        pval = chi2[1]
                        if pval > alphatest:
                            string_resp = "\nChi square test for independence\nWe cannot refuse the hypothesis that " + coll + " and " + collo + " are independent\nStatistics: " + str(round(stat, 3)) + " P-value:" + str(pval) + ".\n"
                        else:
                           string_resp = "\nChi square test for independence\nWe cannot refuse the hypothesis that " + coll + " and " + collo + " aren't independent\nStatistics: " + str(round(stat, 3)) + " P-value:" + str(pval) + ".\n"
                        
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)
                    
        return None 
    
    def stat_pearsonr_testing_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nPearson R Test for correlations\nThe procedure has as results the Pearson Correlation Coefficient and the two-tailed p-value\n")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
        
        for i in range(len(col_list)):
            coll = col_list[i]
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                if (coll != collo) & (i >= j):
                    second_sel = final_df["%s" %(collo)].dropna()  
                    shap = stats.shapiro(selected)
                    shap2 = stats.shapiro(second_sel)
                    
                    if (shap[1] > alphatest) & (shap2[1] > alphatest):
                        pears = stats.pearsonr(selected, second_sel)
                        if pears[1] > alphatest:
                            string_resp = "\nPearson R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(pears[0], 3)) + " and the relative two-tailed p-value is :" + str(round(pears[1], 3)) + "We cannot refuse the hypothesis that two dataset are uncorrelated.\n"
                        else:
                            string_resp = "\nPearson R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(pears[0], 3)) + " and the relative two-tailed p-value is :" + str(round(pears[1], 3)) + "We cannot refuse the hypothesis that two dataset are correlated.\n"
                    else:
                       string_resp = "\nDue to the fact that the two dataset aren't Normal, we cannot apply the Pearson R test.\nA good substitute of this test is Spearman R test\n"
                    
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_spearmanr_testing_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nSpearman R Test for correlations\nThe procedure has as results the Pearson Correlation Coefficient and the two-tailed p-value\n")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                if (coll != collo) & (i >= j):
                    second_sel = final_df["%s" %(collo)].dropna()     
                    spear = stats.spearmanr(selected, second_sel)
                    
                    if spear[1] > alphatest:
                        string_resp = "\nSpearman R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(spear[0], 3)) + " and the relative two-tailed p-value is :" + str(round(spear[1], 3)) + "\nWe cannot refuse the hypothesis that two dataset are uncorrelated.\n"
                    else:
                        string_resp = "\nSpearman R Test\nThe correlation coefficient between " + coll + " and " + collo +" is equal to: " + str(round(spear[0], 3)) + " and the relative two-tailed p-value is :" + str(round(spear[1], 3)) + "\nWe cannot refuse the hypothesis that two dataset are correlated.\n"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_linregr_testing_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nLinear regression between datasets\nThe procedure has as results the slope, the intercept of regressionline, the correlation coefficient, the p-value and the standard error\n")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                if (coll != collo) & (i >= j):
                    second_sel = final_df["%s" %(collo)].dropna()     
                    lin = stats.linregress(selected, second_sel)
                    if lin[3] > alphatest:
                        string_resp = """\nLinear Regression\nThe slope between """ + coll + """ and """ + collo +""" is equal to: """ + str(round(lin[0], 3)) + """, the intercept of the regression line is: """ +  str(round(lin[1], 3)) + """, the correlation coefficient is: """ +  str(round(lin[2], 3))  + """ and the relative p-value is :""" + str(round(lin[3], 3)) + """.\nThe standard error of the estimated slope (gradient), under the assumption of residual normality is: """ +  str(round(lin[4], 3)) +""".\nWe cannot refuse the hypothesis that the slope is equal to zero.\n"""
                    else:
                        string_resp = """\nLinear Regression\nThe slope between """ + coll + """ and """ + collo +""" is equal to: """ + str(round(lin[0], 3)) + """, the intercept of the regression line is: """ +  str(round(lin[1], 3)) + """, the correlation coefficient is: """ +  str(round(lin[2], 3))  + """ and the relative p-value is :""" + str(round(lin[3], 3)) + """.\nThe standard error of the estimated slope (gradient), under the assumption of residual normality is: """ +  str(round(lin[4], 3)) +""".\nWe cannot refuse the hypothesis that the slope is not equal to zero.\n"""
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_ttest_paired_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, """\nT test for paired samples with Normal Distribution\nThe results are the statistics and the relative p-values.\nTwo-tailed test\nHypothesis Zero: difference in the mean of the population is zero\nCounter hypothesis: difference in the mean of the population is different from zero\nUpper-tailed test\nHypothesis Zero: difference in the mean of the populations is zero\nCounter hypothesis: difference in the mean of the populations is greater than zero\nLower-tailed test\nHypothesis Zero: difference in the mean of the populations is zero\nCounter hypothesis: difference in the mean of the populations is less than zero\n""")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll != collo) & (i >= j):
                    second_sel = final_df["%s" %(collo)].dropna()     
                    shap1 = stats.shapiro(selected)
                    shap2 = stats.shapiro(second_sel)
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval < alphatest):
                        ttest = stats.ttest_rel(selected, second_sel, alternative='two-sided')
                        ttest1 = stats.ttest_rel(selected, second_sel,  alternative='less')
                        ttest2 = stats.ttest_rel(selected, second_sel,  alternative='greater')
                        string_resp = """\nT test for paired samples\n T test for datasets """ + coll + """ and """ + collo +""" is:\nTwo-tailed test statistics is: """ + str(round(ttest[0], 3)) + """ and the relative two-tailed p-value is :""" + str(round(ttest[1], 3)) + """\nUpper-tailed test statistics is :""" + str(round(ttest1[0], 3)) + """and the relative upper-tailed p-value is :""" + str(round(ttest1[1], 3)) + """\nLower-tailed test statistics is :""" + str(round(ttest2[0], 3)) + """and the relative lower-tailed p-value is :""" + str(round(ttest2[1], 3)) + """\n"""
                    elif (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval >= alphatest):
                        string_resp = "\nThe two dataset are Normally distributed but not paired\nIt's preferable to apply T test for unpaired samples"
                    else:
                        string_resp = "\nAt least one of the samples is non Normal\nIt's preferable to apply Wilcoxon signed-rank test"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_ttest_unpaired_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, """\nT test for unpaired samples with Normal Distribution\nThe results are the statistics and the relative p-values.\nTwo-tailed test\nHypothesis Zero: difference in the mean of the population is zero\nCounter hypothesis: difference in the mean of the population is different from zero\n""")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll != collo) & (i >= j) & (name1==name2):
                    second_sel = final_df["%s" %(collo)].dropna()   
                    shap1 = stats.shapiro(selected)
                    shap2 = stats.shapiro(second_sel)
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval > alphatest):
                        ttest = stats.ttest_ind(selected, second_sel)
                        string_resp = """\nT test for unpaired samples\n T test for datasets """ + coll + """ and """ + collo +""" is:\nTwo-tailed test statistics is: """ + str(round(ttest[0], 3)) + """ and the relative two-tailed p-value is :""" + str(round(ttest[1], 3)) + """\n"""
                    elif (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval <= alphatest):
                        string_resp = "\nThe two dataset are Normally distributed but paired\nIt's preferable to apply T test for unpaired samples"
                    else:
                        string_resp = "\nAt least one of the samples is non Normal\nIt's preferable to apply Mann-Whitney U test"    
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_ANOVA_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nANOVA test for Normally distributed and independent samples with same variance\nThe results are the statistics and the p-value\nHypothesis Zero: the two datasets have the same population mean\nCounter hypothesis: difference in the mean of the population is different from zero\n")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll == collo) & (i >= j):
                    second_sel = final_df["%s" %(collo)].dropna()     
                    shap1 = stats.shapiro(selected)
                    shap2 = stats.shapiro(second_sel)
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    bart = stats.bartlett(selected, second_sel)
                    if (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval > alphatest) & (bart[1] > alphatest):
                        ttest = stats.f_oneway(selected, second_sel)
                        string_resp = "\nANOVA test for Normally distributed and independent samples\n ANOVA test for samples statistics " + coll + " and " + collo +" is equal to: " + str(round(ttest[0], 3)) + " and the relative p-value is :" + str(round(ttest[1], 3)) + "\n"
                    elif (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval <= alphatest) & (bart[1] > alphatest):
                        string_resp = "\nThe two dataset are Normally distributed but paired\nThe ANOVA test can't be applied.\nIt's preferable to apply Kruskal-Wallis H test.\n"
                    elif (shap1[1] > alphatest) & (shap2[1] > alphatest) & (pval > alphatest) & (bart[1] <= alphatest):
                        string_resp = "\nThe two dataset are Normally distributed and unpaired but have different standard deviations\nThe homoscedasticity property is not respected and the test cannot be done.\nIt's preferable to apply Kruskal-Wallis H test.\n"    
                    elif (shap1[1] < alphatest) or (shap2[1] < alphatest):
                        string_resp = "\nAt least one of the samples is non Normal\nIt's preferable to apply Kruskal-Wallis H"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_wilcoxon_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, """\nWilcoxon rank test for paired samples, a non parametric version of T test for paired samples\nThe results are the statistics and the relative p-values.\nTwo-tailed test\nHypothesis Zero: median of the differences is zero\nCounter hypothesis: median of the differences is different from zero\nUpper-tailed test\nHypothesis Zero: the median of the differences is negative or equal to zero\nCounter hypothesis: the median of the differences is positive\nLower-tailed test\nHypothesis Zero: the median of the differences is positive or equal to zero\nCounter hypothesis: the median of the differences is negative\n""")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll != collo) & (i >= j) & (name1==name2):
                    second_sel = final_df["%s" %(collo)].dropna()
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if (pval <= alphatest):
                        wilc = stats.wilcoxon(selected, second_sel, alternative='two-sided')
                        wilc1 = stats.wilcoxon(selected, second_sel, alternative='less')
                        wilc2 = stats.wilcoxon(selected, second_sel, alternative='greater')
                        string_resp = """\nWilcoxon rank test for paired samples\nWilcoxon rank test for datasets """ + coll + """ and """ + collo +""" is:\nTwo-tailed test statistics is: """ + str(round(wilc[0], 3)) + """ and the relative two-tailed p-value is :""" + str(round(wilc[1], 3)) + """\nUpper-tailed test statistics is :""" + str(round(wilc1[0], 3)) + """and the relative upper-tailed p-value is :""" + str(round(wilc1[1], 3)) + """\nLower-tailed test statistics is :""" + str(round(wilc2[0], 3)) + """and the relative lower-tailed p-value is :""" + str(round(wilc2[1], 3)) + """\n"""
                    else:
                        string_resp = "\nWilcoxon rank test for paired samples cannot be applied due to independency of the datasets\nPreferable to apply Mann-Whitney U test for independent samples.\n"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_mannwhitneyu_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, """\nMann-Whitney rank test for unpaired samples, a non parametric version of T test for unpaired samples\nThe results are the statistics and the relative p-values.\nTwo-tailed test\nHypothesis Zero: difference in the mean of the population is zero\nCounter hypothesis: difference in the mean of the population is different from zero\nUpper-tailed test\nHypothesis Zero: difference in the mean of the populations is zero\nCounter hypothesis: difference in the mean of the populations is greater than zero\nLower-tailed test\nHypothesis Zero: difference in the mean of the populations is zero\nCounter hypothesis: difference in the mean of the populations is less than zero\n""")
        txt2.insert(END, "")
        
        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)]
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll != collo) & (i >= j) & (name1==name2):
                    second_sel = final_df["%s" %(collo)]     
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if (pval > alphatest):
                        mann = stats.mannwhitneyu(selected, second_sel, alternative='two-sided')
                        mann1 = stats.mannwhitneyu(selected, second_sel, alternative='less')
                        mann2 = stats.mannwhitneyu(selected, second_sel, alternative='greater')
                        string_resp = """\nMann-Whitney U test for independent samples\nMann-Whitney U test for datasets """ + coll + """ and """ + collo +""" is:\nTwo-tailed test statistics is: """ + str(round(mann[0], 3)) + """ and the relative two-tailed p-value is :""" + str(round(mann[1], 3)) + """\nUpper-tailed test statistics is :""" + str(round(mann1[0], 3)) + """and the relative upper-tailed p-value is :""" + str(round(mann1[1], 3)) + """\nLower-tailed test statistics is :""" + str(round(mann2[0], 3)) + """and the relative lower-tailed p-value is :""" + str(round(mann2[1], 3)) + """\n"""
                    else:
                        string_resp = "\nMann-Whitney U test for independent samples cannot be applied due to non independency of the datasets\nPreferable to apply Wilcoxon rank test.\n"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def stat_kruskalwallish_2(final_df, frame2, alphatest):
        
        frame2.destroy()
        frame2 = tk.LabelFrame(frame1, text = "Test results", bg = '#1a8cff', font = FFont)
        frame2.place(x = 700, y = 0, height = 600, width = 600)
        
        treescrolly = tk.Scrollbar(frame2, orient = "vertical")
        treescrollx = tk.Scrollbar(frame2, orient = "horizontal")
        treescrollx.pack(side="bottom", fill = "x")
        treescrolly.pack(side="right", fill = "y")
        txt2 = tk.Text(frame2, bg = '#b3d9ff', font = FFont, xscrollcommand = treescrollx.set,  
                 yscrollcommand = treescrolly.set)
        txt2.configure(font=FFont)
        txt2.place(x = 0, y = 0, height = 500, width = 575)
        
        txt2.insert(INSERT, "\nKruskal-Wallis H test for independent samples, it is a non-parametric version of ANOVA test.\nThe results are the statistics and the relative p-value\nHypothesis Zero: the population median of the datasets are equal\nCounter hypothesis: the population median of the datasets are not equal\n")
        txt2.insert(END, "")

        col_list = final_df.columns.to_list()
    
        for i in range(len(col_list)):
            coll = col_list[i]
            name1 = cut_value(coll)
            selected = final_df["%s" %(coll)].dropna()
            for j in range(len(col_list)):
                collo = col_list[j]
                name2 = cut_value(collo)
                if (coll != collo) & (i >= j) & (name1==name2):
                    second_sel = final_df["%s" %(collo)].dropna()     
                    cross = crosstable_periods(selected, second_sel)
                    chi2 = chi2_contingency(cross)
                    stat = chi2[0]
                    pval = chi2[1]
                    if (pval > alphatest):
                        mann = stats.kruskal(selected, second_sel)
                        string_resp = "\nKruskal-Wallis H test for independent samples\n Kruskal-Wallis H test for samples statistics " + coll + " and " + collo +" is equal to: " + str(round(mann[0], 3)) + " and the relative p-value is :" + str(round(mann[1], 3)) + "\n"
                    else:
                        string_resp = "\nKruskal-Wallis H test for independent samples cannot applied due to non independency of the datasets.\n"
                    txt2.insert(INSERT, string_resp)
                    txt2.insert(END, "")
                    txt2.configure(font=FFont)

        return None 
    
    def menu_test_2(final_df, frame2, alphatest, selection, LLIST):
        if selection == "Shapiro-Wilk Test":
            stat_shapiro_testing_2(final_df, frame2, alphatest)
        if selection == "Chi square independency test":
            stat_chi_square_testing_2(final_df, frame2, alphatest)
        if selection == "Pearson R test":
            stat_pearsonr_testing_2(final_df, frame2, alphatest)
        if selection == "Spearman R test":
            stat_spearmanr_testing_2(final_df, frame2, alphatest)
        if selection == "Linear regression":
            stat_linregr_testing_2(final_df, frame2, alphatest)
        if selection == "T test for paired samples":
            stat_ttest_paired_2(final_df, frame2, alphatest)
        if selection == "T test for unpaired samples":
            stat_ttest_unpaired_2(final_df, frame2, alphatest)
        if selection == "Wilcoxon rank test":
            stat_wilcoxon_2(final_df, frame2, alphatest)
        if selection == "Mann-Whitney U test":
            stat_mannwhitneyu_2(final_df, frame2, alphatest)
        if selection == "ANOVA one way test":
            stat_ANOVA_2(final_df, frame2, alphatest)
        if selection == "Kruskal-Wallis H test":
            stat_kruskalwallish_2(final_df, frame2, alphatest)
        return None

    return None

#########################################################################################################################################################################################################################################

def Correlation_part(label_file):
    global file_path
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            #file_path.endswith(".csv"):
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    
    col_list = df.columns.to_list()
    col_list = df.columns.str.match('Unnamed')

    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    
    window1 = tk.Toplevel(root)
    window1.geometry("1400x800")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame = tk.LabelFrame(window1, text = "Prediction analysis window", bg = '#1a8cff', font = FFont)
    frame.place(x = 0, y = 0, height = 800, width = 1400)
    
    txt = tk.Text(frame, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "This part is dedicated to the correlation between data contained into the DataFrame")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 50, width = 1300)
    
    frame1 = tk.LabelFrame(frame, text = "Correlation map", bg = '#1a8cff', font = FFont)
    frame1.place(x = 500, y = 50, height = 600, width = 800)
    
    option_vector = ["Correlation between variables of the dataframe",
                     "Correlation between variables of two dataframes"]
    
    methods_vector = ["pearson",
                     "kendall",
                     "spearman"]
    
    selection = tk.Label(frame, text="Options",  bg = '#b3d9ff', font = FFont, relief="groove")
    selection.place(x = 50, y = 75)
    
    Combo2 = ttk.Combobox(frame, values = methods_vector, width = 50)
    Combo2.place( x = 50, y =  575)
    
    selection2 = tk.Label(frame, text="Select method for correlation",  bg = '#b3d9ff', font = FFont, relief="groove")
    selection2.place( x = 50, y = 550)
    
    Combo1 = ttk.Combobox(frame, values = option_vector, width = 50)
    Combo1.place( x = 50, y =  125)
    
    btn0 = tk.Button(frame, text="Select option", bg = '#b3d9ff', font = FFont, command=lambda: corr_sel(df, Combo1, Combo2, frame, frame1))
    btn0.place( x = 50, y = 150)
    
    def corr_sel(df, Combo1, Combo2, frame, frame1):
        sel = str(Combo1.get())
        met = str(Combo2.get())
        if sel == "Correlation between variables of the dataframe":
            Dataframe_only(df, frame1, met)
        if sel == "Correlation between variables of two dataframes":
            Dataframes_two(df, frame, frame1, met)
                
        return None
    
    def Dataframes_two(df, frame, frame1, met):
        
        label_file = tk.Label(frame, text = "No file selected", bg = '#b3d9ff', font = FFont, relief="groove")
        label_file.place(x = 25, y = 300)
        label_file.place_forget()
        
        LLIST = tk.Listbox(frame, bg = '#b3d9ff', font = FFont)
        LLIST.place(x = 225, y = 250)
        LLIST.place_forget()
        
        button1 = tk.Button(frame, text = "Browse a file", bg = '#b3d9ff', font = FFont, command =lambda: File_dialog(label_file)) #Open the window directory
        button1.place(x = 25, y = 250)
    
        button2 = tk.Button(frame, text = "Load a file", bg = '#b3d9ff', font = FFont, command = lambda: Load_excel_data_2(label_file, frame, frame1, df, met))
        button2.place(x = 125, y = 250)
        
        return None
    
    def multipsel(dfs, frame, LLIST, met):
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        h = 0 
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, dfs["%s" %(ref)])
            h = h + 1

        Dataframe_only(new_df, frame1, met)
        
        return None
        
    def Load_excel_data_2(label_file, frame, frame1, df, met):
        global file_path_2
        file_path_2 = label_file["text"]
        try:
            if file_path_2.endswith(".xlsx"):
                excel_filename = r"{}".format(file_path_2)
                global df2
                df2 = pd.read_excel(excel_filename, engine='openpyxl')
                df2 = df2.loc[:, ~df2.columns.str.match('Unnamed')]
                colcol = df.columns.to_list()
                if 'time' in colcol:
                    df['time'] = pd.to_datetime(df['time'], errors='coerce')
            else:
                csv_filename = r"{}".format(file_path)
                df2 = pd.read_csv(csv_filename, engine='c')
                df2 = df2.loc[:, ~df2.columns.str.match('Unnamed')]
                colcol = df.columns.to_list()
                if 'time' in colcol:
                    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    
        except ValueError:
            tk.messagebox.showerror("Information","The file you have chosen is unvalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information",f"No such file as {file_path}")
            return None
        
        n1 = string_slicing(file_path)
        n2 = string_slicing(file_path_2)
        
        label_file = tk.Label(frame, text = "Files:" + n1 + " -- " + n2, bg = '#b3d9ff', font = FFont, relief="groove")
        label_file.place(x = 25, y = 500)
        
        both = [n1, n2]
        
        databases = [df, df2]

        dfs = covariance_mat(databases, both)
        
        LLIST = tk.Listbox(frame, bg = '#b3d9ff', font = FFont, selectmode = 'multiple', width=33)
        LLIST.place(x = 225, y = 250)
        
        col_list = dfs.columns.to_list()
        
        h = 0
        for i in range(len(col_list)):
            LLIST.insert(h, col_list[i])
            h = h + 1
        
        button3 = tk.Button(frame, text = "Select columns", bg = '#b3d9ff', font = FFont, command = lambda: multipsel(dfs, frame, LLIST, met))
        button3.place(x = 25, y = 300)
        
        return None
    
    def Dataframe_only(df, frame1, met): 
        frame1.destroy()
        frame1 = tk.LabelFrame(frame, text = "Correlation map", bg = '#1a8cff', font = FFont)
        frame1.place(x = 500, y = 50, height = 600, width = 800)
        fig, axes = plt.subplots(nrows=1, ncols=1,figsize=(10,8))
        corr_matrix = df.corr(method=met)
        axes = sns.heatmap(corr_matrix, annot=True)
        plt.setp(axes.get_xticklabels(), rotation=65, ha="right",
         rotation_mode="anchor")
        plt.setp(axes.get_yticklabels(), rotation=65, ha="right",
         rotation_mode="anchor")
        canvas = FigureCanvasTkAgg(fig, master=frame1)
        toolbar = NavigationToolbar2Tk(canvas, frame1)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.Y, expand=1)
        canvas.draw()
        return None
    
    return None

#########################################################################################################################################################################################################################################

def Preprocessing_part(label_file):
    file_path = label_file["text"]
    try:
        if file_path.endswith(".xlsx"):
            excel_filename = r"{}".format(file_path)
            global df
            df = pd.read_excel(excel_filename, engine='openpyxl')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
        else:
            csv_filename = r"{}".format(file_path)
            df = pd.read_csv(csv_filename, engine='c')
            df = df.loc[:, ~df.columns.str.match('Unnamed')]
            colcol = df.columns.to_list()
            if 'time' in colcol:
                df['time'] = pd.to_datetime(df['time'], errors='coerce')
    except ValueError:
        tk.messagebox.showerror("Information","The file you have chosen is unvalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No such file as {file_path}")
        return None
    
    window1 = tk.Toplevel(root)
    window1.geometry("1300x800")
    window1.iconphoto(False, tk.PhotoImage(file=path_ref))
    frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
    frame.place(x = 0, y = 0, height = 800, width = 1300)
    frame1 = tk.LabelFrame(window1, text = "Data reduction window", bg = '#1a8cff', font = FFont)
    frame1.place(x = 0, y = 100, height = 600, width = 1300)
    frame2 = tk.LabelFrame(frame1, text = "Original data", bg = '#1a8cff', font = FFont)
    frame2.place(x = 700, y = 0, height = 300, width = 600)
    frame3 = tk.LabelFrame(frame1, text = "Refined data", bg = '#1a8cff', font = FFont)
    frame3.place(x = 700, y = 300, height = 250, width = 600)
    frame4 = tk.LabelFrame(window1, text = "Resampling window", bg = '#1a8cff', font = FFont)
    frame4.place(x = 0, y = 325, height = 150, width = 700)
    frame5 = tk.LabelFrame(window1, text = "Interpolation window", bg = '#1a8cff', font = FFont)
    frame5.place(x = 0, y = 475, height = 300, width = 700)
    
    global part_df
    part_df = pd.DataFrame()
    
    datess = add_dates(df.time)
    last_item = df.time.to_list()
    last_item = last_item[-1]
    last_item = last_item + timedelta(days=1)
    last_item = last_item.date()
    last_item = last_item.strftime("20%y-%m-%d")
    datess = datess.Days.to_list()
    datess.append(last_item)
    w = len(datess) - 1
    daylenghts = []
    
    for i in range(w):
        j = i + 1
        ref = datess[i]
        ref_2 = datess[j]
        dataf = df.loc[(df.time >= ref) & (df.time < ref_2)]
        index = dataf.index
        number_of_rows = len(index)
        daylenghts.append(str(len(index)))
    del datess[-1]
    
    dateplus = []
    for i in range(len(datess)):
        string_val = 'Date: ' + datess[i] + ' rows: ' + daylenghts[i]
        dateplus.append(string_val)
    
    datesdays = tk.Label(frame1, text='Days with related rows',  bg = '#b3d9ff', font = FFont, relief="groove")
    datesdays.place(x = 0, y = 125)

    Combo = ttk.Combobox(frame1, values = dateplus, width = 30)
    Combo.place( x = 0, y =  150)
    
    txt = tk.Text(frame, bg = '#b3d9ff', font = FFont)
    txt.insert(INSERT, "This part is dedicated to the preprocessing data part, that can be useful in order to some analysis.\nYou must choose the maximum number of rows to be contained into a day, otherwise the whole day is cutting off.\nFor the sampling part, select the step for the resampling of the data. For the resampling rate, insert a number, plus : D for days, H for hours, T for minutes, S for seconds.\nThe last part is dedicated to interpolation of the dataset")
    txt.insert(END, ".")
    txt.configure(font=FFont)
    txt.place(relx = 0, rely = 0, height = 100, width = 1300)
    
    tv1 = ttk.Treeview(frame2)
    tv1.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(frame2, orient = "vertical", command = tv1.yview)
    treescrollx = tk.Scrollbar(frame2, orient = "horizontal", command= tv1.xview)
    tv1.configure(xscrollcommand = treescrollx.set, yscrollcommand = treescrolly.set)
    treescrollx.pack(side="bottom", fill = "x")
    treescrolly.pack(side="right", fill = "y")
    
    tv2 = ttk.Treeview(frame3)
    tv2.place(relheight=1, relwidth=1)

    treescroll2y = tk.Scrollbar(frame3, orient = "vertical", command = tv2.yview)
    treescroll2x = tk.Scrollbar(frame3, orient = "horizontal", command= tv2.xview)
    tv2.configure(xscrollcommand = treescroll2x.set, yscrollcommand = treescroll2y.set)
    treescroll2x.pack(side="bottom", fill = "x")
    treescroll2y.pack(side="right", fill = "y")
    
    Clear_data(tv1)
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    
    for column in tv1["columns"]:
        tv1.heading(column, text=column)
        
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values = row)
            
    select_l = tk.Label(frame1, text ='Select the number of rows',  bg = '#b3d9ff', font = FFont, relief="groove")
    select_l.place(x = 0, y = 25)
    
    E1 = tk.Entry(frame1, bd =5)
    E1.place(x = 200, y = 25)
    
    selection = tk.Label(frame1,  bg = '#b3d9ff', font = FFont, relief="groove")
    selection.place(x = 0, y = 450)
    selection.place_forget()
    
    rows = tk.Label(frame1, text="n° of rows: %s" %(str(df.time.count())), bg = '#b3d9ff', font = FFont, relief="groove")
    rows.place(x = 200, y = 75)
    
    rows2 = tk.Label(frame1, text="", bg = '#b3d9ff', font = FFont, relief="groove")
    rows2.place(x = 275, y = 100)
    rows2.place_forget()
    
    btn0 = tk.Button(frame1, text="Select value", bg = '#b3d9ff', font = FFont, command=lambda: button_sel(E1, selection))
    btn0.place( x = 0, y =  75)
    
    btn1 = tk.Button(frame1, text="Calculate", bg = '#b3d9ff', font = FFont, command=lambda: dataset_cleaning(df, selection['text'], tv2, frame1, part_df, rows2, btn_save))
    btn1.place( x = 375, y =  50)
    
    btn_graph = tk.Button(frame1, text="Plot original data ", bg = '#b3d9ff', font = FFont, command=lambda: Entire_Dataset_Parameter(label_file))
    btn_graph.place( x = 375, y =  0)
    
    btn_graph2 = tk.Button(frame1, text="Plot newest data ", bg = '#b3d9ff', font = FFont, command=lambda: plot_newest_data(part_df))
    btn_graph2.place( x = 400, y =  100)
    btn_graph2.place_forget()
    
    btn_save = tk.Button(frame1, text="Save new plot ", bg = '#b3d9ff', font = FFont, command=lambda: Entire_Dataset_Parameter(label_file))
    btn_save.place( x = 375, y =  0)
    btn_save.place_forget()
    
    lbratio = tk.Label(frame4, text ='Select sampling ratio',  bg = '#b3d9ff', font = FFont, relief="groove")
    lbratio.place( x = 0, y =  25)
    
    E2 = tk.Entry(frame4, bd =3)
    E2.place(x = 200, y = 25)
    
    timestep = tk.Label(frame4, text="", bg = '#b3d9ff', font = FFont, relief="groove")
    timestep.place(x = 300, y = 25)
    timestep.place_forget()
    
    btnsel2 = tk.Button(frame4, text="Compute resampling", bg = '#b3d9ff', font = FFont, command=lambda: resampling(df, timestep, tv2, frame4))
    btnsel2.place( x = 0, y =  75)
    btnsel2.place_forget()
    
    btnsel = tk.Button(frame4, text="Select step", bg = '#b3d9ff', font = FFont, command=lambda: step_sel(E2, timestep, btnsel2, tv2, frame4))
    btnsel.place( x = 400, y =  25)
    
    lbinterp = tk.Label(frame5, text ='Select interpolation method',  bg = '#b3d9ff', font = FFont, relief="groove")
    lbinterp.place( x = 0, y =  25)
    
    methods = ["linear",
               "time",
               "index",
               "pad",
               "nearest",
               "zero",
               "slinear",
               "quadratic",
               "cubic",
               "spline",
               "barycentric",
               "polynomial",
               "krogh",
               "piecewise_polynomial",
               "pchip",
               "akima",
               "from_derivatives"
        ]
    
    col_list = df.columns.to_list()
    
    LLIST = tk.Listbox(frame5, bg = '#b3d9ff', font = FFont, selectmode = 'multiple', width=10, height=5)
    LLIST.place(x = 200, y = 75)
    
    h = 0
    for i in range(len(col_list)):
        LLIST.insert(h, col_list[i])
        h = h + 1

    Combo3 = ttk.Combobox(frame5, values = methods)
    Combo3.place(x = 200, y = 25)
    
    methodstep = tk.Label(frame5, text="", bg = '#b3d9ff', font = FFont, relief="groove")
    methodstep.place(x = 300, y = 25)
    methodstep.place_forget()
    
    btnsel3 = tk.Button(frame5, text="Compute interpolation", bg = '#b3d9ff', font = FFont, command=lambda: interpolation_pattern(df, methodstep, tv2, frame5, new_df))
    btnsel3.place( x = 0, y =  75)
    btnsel3.place_forget()
    
    btninterp = tk.Button(frame5, text="Select interpolation\nand the columns to be shown", bg = '#b3d9ff', font = FFont, command=lambda: interp_sel(Combo3, LLIST, methodstep, btnsel3, tv2, frame5, df))
    btninterp.place( x = 475, y =  25)
    
    def resampling(df, step, tv2, frame4):
        step = step['text']
        new_df = convert_to_periodtimeindex(df)
        new_df = new_df.resample(step).mean().interpolate('time')
        x_time = new_df.index
        new_df.insert(0, 'time', x_time)
        Clear_data(tv2)
        tv2["column"] = list(new_df.columns)
        tv2["show"] = "headings"
        
        for column in tv2["columns"]:
            tv2.heading(column, text=column)
        new_df = new_df.round(3)
        df_rows = new_df.to_numpy().tolist()
        for row in df_rows:
            tv2.insert("", "end", values = row)
            
        sublist = add_dates_2(new_df.time)
        sublist = sublist.Days.to_list()
        savefile = new_df
            
        btn_graph2 = tk.Button(frame4, text="Plot newest data ", bg = '#b3d9ff', font = FFont, command=lambda: plot_newest_data(new_df, sublist))
        btn_graph2.place( x = 175, y =  75)
            
        btn_save = tk.Button(frame4, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
        btn_save.place( x = 375, y =  75)
        
        btn_save_csv = tk.Button(frame4, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
        btn_save_csv.place( x = 500, y =  75)
        
        def plot_newest_data(df, sublist):
                window1 = tk.Toplevel(root)
                window1.geometry("1000x500")
                window1.iconphoto(False, tk.PhotoImage(file=path_ref))
                frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
                frame0.place( height = 500, width = 1000) 
                
                x_time = pd.to_datetime(df.time, unit = 'ns')
            
                # COMBOBOX
                
                col_list = df.columns.to_list()
                col_list.remove('time')
                
                option_vector = []
                
                for i in range(len(col_list)):
                    ref = "Show " + col_list[i]
                    option_vector.append(ref)
                                
                aggregations = ["mean",
                                "standard deviation",
                                "standard deviation 2",
                                "standard deviation 3",
                                "median"]
                    
                global List_aggr
                List_aggr = []
                    
                Combo1 = ttk.Combobox(frame0, values = option_vector)
                Combo1.place( x = 50, y =  50)
                    
                First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                First_Label.place(x = 250, y = 50)
                
                Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                Second_Label.place(x = 450, y = 100)
            
                btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn.place( x = 200, y =  100)
                    
                btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn2.place( x = 50, y =  100)
                    
                Combo2 = ttk.Combobox(frame0, values = aggregations)
                Combo2.place( x = 50, y =  250)
                
                Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
                Aggr_List.place(x = 450, y =  150)
                    
                btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn3.place( x = 50, y =  300)
                    
                btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn4.place( x = 50, y =  150)
                    
                return None
            
        return None
    
    def interpolation_pattern(DF, step, tv2, frame5):
        step = step['text']

        ddf = pd.DataFrame()
        new_df = pd.DataFrame()
        ddf = convert_to_periodtimeindex(DF)
        col_df = ddf.columns.to_list()
        best_value = 0
        selected_method = ''
        R_2_vec = []
        R22_vec = []
        ind = 0
        R2 = 0
        R2_min = 0
        if (step == "linear") or (step == "spline") or (step == "polynomial"):
            for i in range(4):
                j = i + 1
                R_2_vec = []
                new_df = ddf.interpolate(method = step, order = j)
                col_list = new_df.columns.to_list()
                for i in range(len(col_list)):
                    colo = col_list[i]
                  # print(colo)
                    R_2 = r2_score(DF["%s" %(colo)], new_df["%s" %(colo)])
                    R_2_vec.append(R_2)
                R2 = min(R_2_vec)
                R22_vec.append(R2)
            R2_min = min(R22_vec)
            for i in range(len(R22_vec)):
                if R22_vec[i] == R2_min:
                    ind = i + 1
            new_df = ddf.interpolate(method = step, order = ind)
                
        else:   
            new_df = ddf.interpolate(step)
            R_2_vec = []
            col_list = new_df.columns.to_list()
            for i in range(len(col_list)):
                colo = col_list[i]
                R_2 = r2_score(DF["%s" %(colo)], new_df["%s" %(colo)])
                R_2_vec.append(R_2)
            R2 = min(R_2_vec)
            
        new_df.insert(0, 'time', new_df.index)
        sublist = add_dates_index(new_df.index)
        
        Clear_data(tv2)
        tv2["column"] = list(new_df.columns)
        tv2["show"] = "headings"
            
        for column in tv2["columns"]:
            tv2.heading(column, text=column)
        new_df = new_df.round(3)
        df_rows = new_df.to_numpy().tolist()
        for row in df_rows:
            tv2.insert("", "end", values = row)
                
        savefile = new_df
                
        btn_graph2 = tk.Button(frame5, text="Plot newest data ", bg = '#b3d9ff', font = FFont, command=lambda: plot_newest_data_2(new_df, sublist))
        btn_graph2.place( x = 300, y =  125)
            
        btn_save = tk.Button(frame5, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
        btn_save.place( x = 425, y =  125)
        
        btn_save_csv = tk.Button(frame5, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
        btn_save_csv.place( x = 575, y =  125)
        
        
        
        def plot_newest_data_2(df, sublist):
                window1 = tk.Toplevel(root)
                window1.geometry("1000x500")
                window1.iconphoto(False, tk.PhotoImage(file=path_ref))
                frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
                frame0.place( height = 500, width = 1000) 
                
                x_time = pd.to_datetime(df.index, unit = 'ns')
                df['time'] = df.index
            
                # COMBOBOX
                
                option_vect = df.columns.to_list()
                option_vect.remove('time')
                
                option_vector = []
                for i in range(len(option_vect)):
                    string = "Show " + option_vect[i]
                    option_vector.append(string)
                    
                aggregations = ["mean",
                                "standard deviation",
                                "standard deviation 2",
                                "standard deviation 3",
                                "median"]
                    
                global List_aggr
                List_aggr = []
                    
                Combo1 = ttk.Combobox(frame0, values = option_vector)
                Combo1.place( x = 50, y =  50)
                    
                First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                First_Label.place(x = 250, y = 50)
                
                Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                Second_Label.place(x = 450, y = 100)
            
                btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn.place( x = 200, y =  100)
                    
                btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn2.place( x = 50, y =  100)
                    
                Combo2 = ttk.Combobox(frame0, values = aggregations)
                Combo2.place( x = 50, y =  250)
                
                Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
                Aggr_List.place(x = 450, y =  150)
                    
                btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn3.place( x = 50, y =  300)
                    
                btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn4.place( x = 50, y =  150)
                    
                return None
            
        return None

    def button_sel(bsel, bbut):
        s = bsel.get()
        bbut['text'] = s
        bbut.place(x = 125, y = 75)
        return None
    
    def step_sel(bsel, bbut, btnsel2, tv2, frame4):
        s = bsel.get()
        bbut['text'] = s
        bbut.place(x = 350, y = 25)
        
        btnsel2 = tk.Button(frame4, text="Compute resampling", bg = '#b3d9ff', font = FFont, command=lambda: resampling(df, timestep, tv2, frame4))
        btnsel2.place( x = 0, y =  75)
        
        return None
    
    def interp_sel(Combo, LLIST, bbut, btnsel3, tv2, frame5, df):
        s = Combo.get()
        bbut['text'] = s
        bbut.place(x = 350, y = 25)
        
        List = []
        choices = LLIST.curselection()
        for i in choices:
            ent = LLIST.get(i)
            List.append(ent)
        
        new_df = pd.DataFrame()
        new_df.insert(0, "time", df["time"])
        h = 1
        for i in range(len(List)):
            ref = List[i]
            new_df.insert(h, ref, df["%s" %(ref)])
            h = h + 1

        btnsel3 = tk.Button(frame5, text="Compute interpolation", bg = '#b3d9ff', font = FFont, command=lambda: interpolation_pattern(new_df, bbut, tv2, frame5))
        btnsel3.place( x = 0, y =  75)
        
        return None
    
    def save_path(df):
        ttt = False
        ins = ''
        popup(ins, df)
        return None
        
    def popup(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_excel(r'' + dir_name + '/' + ins +'.xlsx', index = False, engine = 'openpyxl')
            return None
        
        return None
    
    def save_path_csv(df):
        ttt = False
        ins = ''
        popup_csv(ins, df)
        return None
    
    def popup_csv(ins, df):
        window1 = tk.Toplevel(root)
        window1.geometry("300x200")
        window1.iconphoto(False, tk.PhotoImage(file=path_ref))
        frame = tk.LabelFrame(window1, text = "Preprocessing analysis window", bg = '#1a8cff', font = FFont)
        frame.place(x = 0, y = 0, height = 300, width = 300)
        
        select_l = tk.Label(frame, text ='Select the name of the file',  bg = '#b3d9ff', font = FFont, relief="groove")
        select_l.place(x = 25, y = 25)
        
        E1 = tk.Entry(frame, bd =5)
        E1.place(x = 25, y = 50)
        
        btn = tk.Button(frame, text="Insert filename", bg = '#b3d9ff', font = FFont, command=lambda: insert_value_csv(E1, ins, window1, df))
        btn.place( x = 25, y =  75)
        
        def insert_value_csv(E1, ins, window1, df):
            ins = E1.get()
            dir_name = filedialog.askdirectory() # asks user to choose a director
            df.to_csv(r'' + dir_name + '/' + ins +'.csv', index = False)
            return None
        
    def dataset_cleaning(data, n_rows, tv, frame, part_df, rows2, btn_save):
        rows2.place_forget()
        btn_save.place_forget()
        n_rows = float(n_rows)
        col_list = data.columns.to_list()
        if 'time' in col_list:
            datetime = pd.Series(data= data.time)
        else:
            datetime = pd.Series(data= data.index)
        dates = add_dates(datetime)
        last_item = data.time.to_list()
        last_item = last_item[-1]
        last_item = last_item + timedelta(days=1)
        last_item = last_item.date()
        last_item = last_item.strftime("20%y-%m-%d")
        dates = dates.Days.to_list()
        dates.append(last_item)
        w = len(dates) - 1
        for i in range(w):
            j = i + 1
            ref = dates[i]
            ref_2 = dates[j]
            dataf = data.loc[(data.time >= ref) & (data.time < ref_2)]
            time_v = pd.Series(data = dataf.time)
            sec_vector = second_vector(time_v)
            index = dataf.index
            number_of_rows = len(index)
            if number_of_rows <= n_rows:    #N° of rows that can be relevant
                data = data.drop(data[(data.time >= ref) & (data.time < ref_2)].index)

        daylenghts = []
        for i in range(w):
            j = i + 1
            ref = dates[i]
            ref_2 = dates[j]
            dataf = data.loc[(data.time >= ref) & (data.time < ref_2)]
            index = dataf.index
            number_of_rows = len(index)
            daylenghts.append(str(len(index)))
        
        del dates[-1]
        dateplus = []
        for i in range(len(dates)):
            string_val = 'Date: ' + dates[i] + ' rows: ' + daylenghts[i]
            dateplus.append(string_val)
    
        Combo = ttk.Combobox(frame, values = dateplus, width = 30)
        Combo.place( x = 300, y =  150)
    
        rows2 = tk.Label(frame, text="n° of rows of new dataset: %s" %(str(data.time.count())), bg = '#b3d9ff', font = FFont, relief="groove")
        rows2.place(x = 200, y = 100)

        if data.empty:
            Clear_data(tv)
            rows2.place_forget()
            tk.messagebox.showerror("Information",f"\nDataFrame is empty!")
            return None
        else:
            sublist = add_dates_2(data.time)
            sublist = sublist.Days.to_list()
            Clear_data(tv)
            tv["column"] = list(data.columns)
            tv["show"] = "headings"
            
            for column in tv["columns"]:
                tv.heading(column, text=column)
            data = data.round(3)
            df_rows = data.to_numpy().tolist()
            for row in df_rows:
                tv.insert("", "end", values = row)
            
            savefile = data
            
            btn_graph2 = tk.Button(frame1, text="Plot newest data ", bg = '#b3d9ff', font = FFont, command=lambda: plot_newest_data(data, sublist))
            btn_graph2.place( x = 500, y =  0)
            
            btn_save = tk.Button(frame1, text="Save dataset\n in excel format", bg = '#b3d9ff', font = FFont, command=lambda: save_path(savefile))
            btn_save.place( x = 525, y =  50)
            
            btn_save_csv = tk.Button(frame1, text="Save dataset\n in csv format", bg = '#b3d9ff', font = FFont, command=lambda: save_path_csv(savefile))
            btn_save_csv.place( x = 525, y =  125)
            
            
            def plot_newest_data(df, sublist):
                window1 = tk.Toplevel(root)
                window1.geometry("1000x500")
                window1.iconphoto(False, tk.PhotoImage(file=path_ref))
                frame0 = tk.LabelFrame(window1, text = "Options", bg='#1a8cff', font = FFont)
                frame0.place( height = 500, width = 1000) 
                
                x_time = pd.to_datetime(df.time, unit = 'ns')
            
                # COMBOBOX
                
                col_list = df.columns.to_list()
                col_list.remove('time')
                
                option_vector = []
                
                for i in range(len(col_list)):
                    ref = "Show " + col_list[i]
                    option_vector.append(ref)
                    
                aggregations = ["mean",
                                "standard deviation",
                                "standard deviation 2",
                                "standard deviation 3",
                                "median"
                                ]
                    
                global List_aggr
                List_aggr = []
                    
                Combo1 = ttk.Combobox(frame0, values = option_vector)
                Combo1.place( x = 50, y =  50)
                    
                First_Label = tk.Label(frame0, text ='No option selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                First_Label.place(x = 250, y = 50)
                
                Second_Label = tk.Label(frame0, text ='List of aggregators \n actually selected', font = FFont,  bg = '#b3d9ff', relief="groove")
                Second_Label.place(x = 450, y = 100)
            
                btn = tk.Button(frame0, text="Plot Graph", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn.place( x = 200, y =  100)
                    
                btn2 = tk.Button(frame0, text="Confirm the selection", bg = '#b3d9ff', font = FFont, command=lambda: check_graphs(frame0, Combo1, First_Label, btn, df))
                btn2.place( x = 50, y =  100)
                    
                Combo2 = ttk.Combobox(frame0, values = aggregations)
                Combo2.place( x = 50, y =  250)
                
                Aggr_List = tk.Listbox(frame0, font = FFont,  bg = '#b3d9ff')
                Aggr_List.place(x = 450, y =  150)
                    
                btn3 = tk.Button(frame0, text="Aggregators list", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn3.place( x = 50, y =  300)
                    
                btn4 = tk.Button(frame0, text="Add aggregator\n in the menu below", bg = '#b3d9ff', font = FFont, command=lambda: check_aggregators(frame0, Combo1, Combo2, First_Label, Aggr_List, btn3, df, List_aggr, sublist))
                btn4.place( x = 50, y =  150)
                    
                return None
            
        return None
    
    return None

#########################################################################################################################################################################################################################################
def presentation():
    root = tk.Tk()
    root.geometry("800x900")
    root.title("Data Visualization GUI")
    root.iconphoto(False, tk.PhotoImage(file=path_ref))
    canvas = Canvas(root, width = 900, height = 900)      
    canvas.pack()  
    img = PhotoImage(file=path_ref)  
    canvas.create_image(6,6, anchor=NW, image=img)  
    root.after(3000, lambda: root.destroy())
    root.mainloop()

#########################################################################################################################################################################################################################################

# FIRST FUNCTION CALL

main_folder = os.getcwd()
global path_ref
path_ref = ''

for file in os.listdir(main_folder):
    if file.endswith(".png"):
        path_ref = '' + main_folder + '/' + file
        path_ref = r"{}".format(path_ref)

presentation()
global root
root = tk.Tk()
root.geometry("1300x900")
root.title("Graphical User Interface for Data Visualization")
root.iconphoto(False, tk.PhotoImage(file=path_ref))


#
global api_key
api_key = "f07506d04230deee7776eab200f604ca"

global FFont
FFont = tkFont.Font(family="Spyder",size=12,weight="normal")

main(root, FFont)
root.mainloop()
