# -*- coding: utf-8 -*-

import pandas as pd
import os

pwd = os.getcwd()

rawdata = pd.read_csv(pwd + '\\input.txt', header = None, names = ['Depth Reading'])
rawdata.to_excel('output.xlsx', 'Sheet 1')

diff, ordi = {'Diff btwn Last' : []}, {'Ordinance' : []}
delta = 0
diff['Diff btwn Last'].append(delta)
ordi['Ordinance'].append('Zero')

for i in range(1, len(rawdata)):
    delta = int(rawdata.iloc[i][0]) - int(rawdata.iloc[i-1][0])
    diff['Diff btwn Last'].append(delta)
    if delta > 0:
        ordi['Ordinance'].append('Positive')
    elif delta < 0:
        ordi['Ordinance'].append('Negative')
    else:
        ordi['Ordinance'].append('None')

x = 0
for item in list(ordi.values())[0]:
    if item == 'Positive':
        x +=1
    else:
        None

print(f'There are', x, 'instances in which the depth readings increase from the previous readings.')

df = pd.read_excel(pwd + '\\output.xlsx')
df['Diff btwn Last'] = pd.DataFrame(diff)
df['Ordinance'] = pd.DataFrame(ordi)
df.to_excel(pwd + '\\output.xlsx')

###################################
# Part 2
###################################

move, mordi = {'Moving Average' : []}, {'Moving Average Ordinance' : []}

group = 3
last = 0

for i in range(group):
    mordi['Moving Average Ordinance'].append('Zero')

for i in range(group, len(rawdata)):
    mean = (int(rawdata.iloc[i-2][0]) + int(rawdata.iloc[i-1][0]) + int(rawdata.iloc[i][0]))
    move['Moving Average'].append(mean)
    delta = mean - last
    if delta > 0:
        mordi['Moving Average Ordinance'].append('Positive')
    elif delta < 0:
        mordi['Moving Average Ordinance'].append('Negative')
    else:
        mordi['Moving Average Ordinance'].append('None')
    last = mean
        
x = 0
for item in list(mordi.values())[0]:
    if item == 'Positive':
        x +=1
    else:
        None

print(f'There are', x, 'instances in which the depth readings increase from the three previous readings.')

df = pd.read_excel(pwd + '\\output.xlsx')
df['Moving Average'] = pd.DataFrame(move)
df['Moving Average Ordinance'] = pd.DataFrame(mordi)
df.to_excel(pwd + '\\output.xlsx')

# print(move)