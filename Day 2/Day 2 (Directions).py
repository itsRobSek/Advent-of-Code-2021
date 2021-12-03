# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:45:50 2021

@author: Rob
"""

import pandas as pd
import os

pwd = os.getcwd()

rawdata = pd.read_csv(pwd + '\\input.txt', sep = ' ', header = None, names = ['Depth Reading', 'Direction'])
rawdata.to_excel('output.xlsx', 'Sheet 1')

x_pos, y_pos = {'Horizontal Position':[]}, {'Depth':[]}
x, y = 0, 0

for i in range(len(rawdata)):
    if rawdata.iloc[i][0] == 'forward':
        x += rawdata.iloc[i][1]
        x_pos['Horizontal Position'].append(x)
        if i == 0:
            y_pos['Depth'].append(0)
        else:
            y_pos['Depth'].append(y_pos['Depth'][i-1])
    elif rawdata.iloc[i][0] == 'up':
        y -= rawdata.iloc[i][1]
        y_pos['Depth'].append(y)
        x_pos['Horizontal Position'].append(x_pos['Horizontal Position'][i-1])
    elif rawdata.iloc[i][0] == 'down':
        y += rawdata.iloc[i][1]
        y_pos['Depth'].append(y)
        x_pos['Horizontal Position'].append(x_pos['Horizontal Position'][i-1])
    else:
        None

df = pd.read_excel(pwd + '\\output.xlsx')
df['Horizontal Position'] = pd.DataFrame(x_pos)
df['Depth'] = pd.DataFrame(y_pos)
df.to_excel(pwd + '\\output.xlsx')

print(f'The answer is:', x*y)

###################################
# Part 2
###################################

x_pos['Horizontal Position'].clear()
y_pos['Depth'].clear()

aimdict = {'Aim':[]}
aim = 0

x, y = 0, 0

for i in range(len(rawdata)):
    if rawdata.iloc[i][0] == 'forward':
        x += rawdata.iloc[i][1]
        x_pos['Horizontal Position'].append(x)
        y += (aim * rawdata.iloc[i][1])
        y_pos['Depth'].append(y)
        aimdict['Aim'].append(aim)
    elif rawdata.iloc[i][0] == 'up':
        aim -= rawdata.iloc[i][1]
        aimdict['Aim'].append(aim)
        x_pos['Horizontal Position'].append(x_pos['Horizontal Position'][i-1])
    elif rawdata.iloc[i][0] == 'down':
        aim += rawdata.iloc[i][1]
        aimdict['Aim'].append(aim)
        x_pos['Horizontal Position'].append(x_pos['Horizontal Position'][i-1])
    else:
        None

df = pd.read_excel(pwd + '\\output.xlsx')
df['Horizontal Position'] = pd.DataFrame(x_pos)
df['Depth'] = pd.DataFrame(y_pos)
df['Aim'] = pd.DataFrame(aimdict)
df.to_excel(pwd + '\\output.xlsx')

print(f'The answer is:', x*y)