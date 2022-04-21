# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 13:53:55 2020

@author: Marco
"""

import os
import pandas as pd
from pandas import Series
from pandas import DataFrame
from matplotlib import pyplot as plot
from matplotlib import figure
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime 
import xlsxwriter
import subprocess
import sys
import scipy
import os
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
from datetime import datetime, timedelta
import xlsxwriter
from scipy import stats
from sklearn import preprocessing
from scipy.stats import pearsonr
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import *
import tkinter.font
from tkinter.ttk import *
from PIL import *
import pyglet
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import asksaveasfile 
import calendar
#%%

def add_dates(dates): #it must be the column of datetime dates of a Dataframe
    df = pd.DataFrame()
    tt = pd.Series(str)
    h = 0
    ref = dates.dt.date[0]
    nn = ref.strftime("20%y-%m-%d")
    tt[h] = nn
    for i in range(len(dates)):
        if dates[i] != ref:
            h = h + 1
            ref = dates.dt.date[i]
            nn = ref.strftime("20%y-%m-%d")
            tt[h] = nn
    df.insert(0, 'Days', tt)
    return df

def add_dates_2(dates): #it must be the column of datetime dates of a Dataframe
    df = pd.DataFrame()
    tt = pd.Series(str)
    h = 0
    ref = dates.dt.date.iloc[0]
    nn = ref.strftime("20%y-%m-%d")
    tt[h] = nn
    for i in range(len(dates)):
        if dates.dt.date.iloc[i] != ref:
            h = h + 1
            ref = dates.dt.date.iloc[i]
            nn = ref.strftime("20%y-%m-%d")
            tt[h] = nn
    df.insert(0, 'Days', tt)
    return df

def add_months(dates): #column time of a dataset
    days = add_dates_2(dates)
    days = days.Days.to_list()
    months = []
    first = days[0]
    mon = datetime.strptime(first, "20%y-%m-%d")
    mon = mon.month
    months.append(mon)
    for i in range(len(days)):
        ref = days[i]
        mon = datetime.strptime(ref, "20%y-%m-%d")
        mon = mon.month
        if mon != months[-1]:
            months.append(mon)
    
    months_2 = []
    for i in range(len(months)):
        month_str = calendar.month_name[months[i]]
        months_2.append(month_str)

    return months_2

    


def add_hours(DDD):
    DDD_time = DDD.time.tolist()
    tt = list()
    h = 1
    KK = DDD_time[0]
    ref = int(KK.hour)
    tt.append(ref)
    for i in range(len(DDD_time)):
        KKu = DDD_time[i]
        KK = KKu.hour
        if KK != ref:
            h = h + 1
            ref = KK
            tt.append(ref)
    return tt

def sub_List(lista, value_1, value_2):
    ix = iy = 0
    for i in range(len(lista)):
        if lista[i] == value_1:
            ix = i
        if lista[i] == value_2:
            iy = i
    sublist = lista[ix:iy]
    return sublist


#FUNCTION USED TO DISPLAY ALL CHARACTERISTICS OF THE COLUMNS OF THE DATASET


def Descr(dataset):
    dd = pd.DataFrame()
    LL = list(dataset.columns)
    K = ['mean','standard deviation', 'count', 'minimum value', 'maximum value']
    dd.insert(0, 'Parameters', K)
    h = 1 
    for i in range(len(LL)):
        j = dataset["%s" %(LL[i])]
        hh = desc_col(j)
        dd.insert(loc = h, column = "%s" %(LL[i]), value =  hh)
        h = h + 1
    return dd


#FIRST COLUMN INSERT

def desc_col(col_umn):
    GG = pd.Series(float)
    mean = col_umn.mean()
    std = col_umn.std()
    count = col_umn.count()
    m_min = col_umn.min()
    m_max = col_umn.max()
    
    mean = round(mean, 2)
    std = round(std, 2)
    count = round(count, 2)    
    
    GG[0] = mean
    GG[1] = std
    GG[2] = count
    GG[3] = m_min
    GG[4] = m_max
    return GG

def Clear_data(tv):
    tv.delete(*tv.get_children())
    return None

def dataset_cleaning(data, n_rows, tv):
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
    
    Clear_data(tv)
    tv["column"] = list(data.columns)
    tv["show"] = "headings"
    
    for column in tv["columns"]:
        tv.heading(column, text=column)
    
    df_rows = data.to_numpy().tolist()
    for row in df_rows:
        tv.insert("", "end", values = row)
    
    return None

def second_vector(time_s):
    LIST = []
    ref = time_s.iloc[0]
    for i in range(len(time_s)):
        time_seq =  time_s.iloc[i]
        diff = (time_seq - ref).total_seconds()
        LIST.append(diff)
        
    return LIST 

def add_dates_index(dates): #it must be the column of datetime dates of a Dataframe
    tt = []
    ref = dates.date[0]
    nn = ref.strftime("20%y-%m-%d")
    tt.append(nn)
    for i in range(len(dates)):
        if dates.date[i] != ref:
            ref = dates.date[i]
            nn = ref.strftime("20%y-%m-%d")
            tt.append(nn)
    return tt

def convert_to_periodtimeindex(data):
    col_list = data.columns.to_list()
    if 'time' in col_list:
        x_time = data.time.to_list()
    
    x_mod = pd.DataFrame(index=pd.to_datetime(x_time, unit='ns'))
    col_list.remove('time')
    h = 0 
    for i in range(len(col_list)):
        ref = col_list[i]
        value = data['%s' %(ref)].to_list()
        x_mod.insert(h, ref, value)
        h = h + 1
        
    return x_mod

def covariance_mat(databases, titles):
    total_df = pd.DataFrame()
    for i in range(len(databases)):
        col_list = databases[i].columns.to_list()
        num = str(i)
        for j in range(len(col_list)):
            val = col_list[j]
            total_df[''+ val + " " + titles[i]] = databases[i]["%s" %(val)]
    
    return total_df

def string_slicing(string):
    length = len(string)
    value = "/"
    sub = ''
    ind = 0
    for i in range(len(string)):
        if string[i] == value:
            ind = i
    
    ind = ind + 1
    sub = string[ind:]
    
    return sub
            
def add_dates_index(dates): #it must be the column of datetime dates of a Dataframe
    tt = []
    ref = dates.date[0]
    nn = ref.strftime("20%y-%m-%d")
    tt.append(nn)
    for i in range(len(dates)):
        if dates.date[i] != ref:
            ref = dates.date[i]
            nn = ref.strftime("20%y-%m-%d")
            tt.append(nn)
    return tt         

def start_end_selection(df1, df2): 
    #df1 and df2 are dataset
    
    #extract the time column from the datasets
    df1_time = df1.time
    df2_time = df2.time
    
    df1_time_list = df1_time.to_list()
    df2_time_list = df2_time.to_list()
    
    if df1_time_list[0] >= df2_time_list[0]:
        start = df1_time_list[0]
    else:
        start = df2_time_list[0]
        
    if df1_time_list[-1] >= df2_time_list[-1]:
        end = df2_time_list[-1]
    else:
        end = df1_time_list[-1]
    
    return start, end #these parameters are Timestamps, important to set 2 values in the main program

def rows_selection(df1, df2):
    start, end = start_end_selection(df1, df2)
    df1 = df1.loc[(df1['time'] >= start) & (df1['time'] <= end)]
    df2 = df2.loc[(df2['time'] >= start) & (df2['time'] <= end)]
    return df1, df2 #return 2 datasets
    
def check_crosstab(tab):
    value = False
    rows, columns = tab.shape
    for i in range(rows):
        for j in range(columns):
            val = tab.iloc[i, j]
            if val < 5:
                value = True
    
    return value

def crosstable_periods(df1, df2):
    i = 2
    j = 2
    interv1 = pd.qcut(df1, q = i, duplicates='drop')
    interv2 = pd.qcut(df2, q = j, duplicates='drop')
    cross = pd.crosstab(interv1, interv2)
    if check_crosstab(cross) == True:
        return cross
    for k in range(20):
        ii = i + k
        interval_1 = pd.qcut(df1, q = ii, duplicates='drop')
        jj = j + k
        interval_2 = pd.qcut(df2, q = jj, duplicates='drop')
        cross1 = pd.crosstab(interval_1, interv2)
        cross2 = pd.crosstab(interv1, interval_2)
        if (check_crosstab(cross1) == True):
            return cross
        if (check_crosstab(cross2) == True):
            return cross1
        else:
            i = ii
            j = jj
            interval_1 = pd.qcut(df1, q = i, duplicates='drop')
            interval_2 = pd.qcut(df2, q = j, duplicates='drop')
            cross3 = pd.crosstab(interval_1, interval_2)
            if (check_crosstab(cross) == True):
                return cross2
        
    return cross

def remove_duplicates_from_list(x):
    return list(dict.fromkeys(x))

def sort_dates(timestamps):
    
    dates = [datetime.strptime(ts, "%Y-%m-%d") for ts in timestamps]
    dates.sort()
    sorteddates = [datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
    
    return sorteddates

def commonelements(list1):
    intersection = []
    for i in range(len(list1)):
        ref = list1[i]
        if list1.count(ref):
            intersection.append(ref)
    
    return intersection

def cut_extension(string):
    value = '.'
    ind = 0
    for i in range(len(string)):
        if string[i] == value:
            ind = i
    sub = string[:ind]
    
    return sub

def cut_value(string):
    length = len(string)
    value = "_"
    sub = ''
    ind = 0
    for i in range(len(string)):
        if string[i] == value:
            ind = i
    
    ind = ind + 1
    sub = string[ind:]
    
    return sub

def cut_space_value(string):
    length = len(string)
    value = " "
    sub = ''
    ind = 0
    for i in range(len(string)):
        if string[i] == value:
            ind = i
    
    ind = ind + 1
    sub = string[ind:]
    
    return sub

def cut_first_space_value(string):
    length = len(string)
    value = " "
    sub = ''
    ind = 0
    for i in range(len(string)):
        if string[i] == value:
            ind = i
    
    ind = ind - 1
    sub = string[:ind]
    
    return sub

def sort_dates2(timestamps):
    
    dates = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f") for ts in timestamps]
    dates.sort()
    sorteddates = [datetime.strftime(ts, "%Y-%m-%d %H:%M:%S.%f") for ts in dates]
    
    return sorteddates


def table_features(df, cols):
    dates = add_dates_2(df.time)
    dates = dates.Days.to_list()
    last_item = dates[-1]
    last_item = datetime.strptime(last_item, "20%y-%m-%d")
    last_item = last_item + timedelta(days=1)
    last_item = last_item.date()
    last_item = last_item.strftime("20%y-%m-%d")
    dates.append(last_item)
    
    col_list = df.columns.to_list()
    new_df = pd.DataFrame()
    std_cols = []
    NNDD =  []
    dataf = pd.DataFrame()
    h = 0
    for i in range(len(cols)):
        if cols[i] in col_list:
            name = "mean_" + cols[i]
            new_df.insert(h, name, df[cols[i]])
        h = h + 1
    regrouped_mean = new_df.groupby(by=df['time'].dt.date).mean()
    regrouped_mean = regrouped_mean.round(decimals = 3)
    colsss = regrouped_mean.columns.to_list()
    for i in range(len(colsss)):
        ref = "standard.dev_" + cut_value(colsss[i])
        NNDD.append(ref)
    regrouped_std = new_df.groupby(by=df['time'].dt.date).std()
    regrouped_std.columns = NNDD
    regrouped_std = regrouped_std.round(decimals =3)
    new_new_df = pd.DataFrame()
    col_list = regrouped_mean.columns.to_list()
    col_list1 = regrouped_mean.columns.to_list()
    col_list2 = regrouped_std.columns.to_list()
    regrouped_mean.reset_index(drop=True, inplace=True)
    regrouped_std.reset_index(drop=True, inplace=True)
    del dates[-1]
    new_new_df.insert(0, "time", dates)
    h =  1
    for i in range(len(col_list1)):
        for j in range(len(col_list2)):
            ref1 = cut_value(col_list1[i])
            ref2 = cut_value(col_list2[j])
            if ref1 == ref2:
                r1 = regrouped_mean[col_list1[i]]
                r2 = regrouped_std[col_list2[j]]
                new_new_df.insert(h, col_list1[i], r1)
                h = h + 1
                new_new_df.insert(h, col_list2[j], r2)
                h = h + 1
    
    return new_new_df

def index_constr(a,b):
    lulist = []
    lulist.append(a)
    for i in range(b):
        j = i + 1
        res = lulist[-1] + 1
        if res <= b:
            lulist.append(j)
    
    return lulist
