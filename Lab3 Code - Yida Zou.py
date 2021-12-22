"""
Lab 3 Code

Yida Zou
"""
import re, math
import pandas as pd
from os import listdir 
from scipy import stats

data_dir = "F:/Python/data/" #folder of data
kinetic_small_wood = []
kinetic_big_wood = []
kinetic_big_rubber = []

static_small_wood = []
static_big_wood = []
static_big_rubber = []

def getRightRows(csv):
  col = csv['rx-darkorange']
  modes = col.value_counts(sort=True)
  start = []
  end = []
  for i in modes.index:
    if str(i)[0] == '7':
      start.append(i)
    elif str(i)[0] == '3':
      end.append(i)
  top = start[0]
  end = end[0]
  lastOfFirst = col.where(col==top).last_valid_index()
  firstOfSecond = col.where(col==end).first_valid_index()
  return [lastOfFirst,firstOfSecond]

#sort csvs into lists
for folder in listdir(data_dir):
   for csv in listdir(data_dir+folder):
       if re.match("kinetic",csv):
           if re.search("kinetic_small_wood_[0-9]\.csv",csv):
              kinetic_small_wood.append(data_dir+folder+'/'+csv) 
           elif re.search("kinetic_big_wood_[0-9]\.csv",csv):
              kinetic_big_wood.append(data_dir+folder+'/'+csv) 
           elif re.search("kinetic_big_rubber_[0-9]\.csv",csv):
              kinetic_big_rubber.append(data_dir+folder+'/'+csv) 
       elif re.match("static",csv):
           if re.search("static_small_wood_[0-9]\.csv",csv):
              static_small_wood.append(data_dir+folder+'/'+csv) 
           elif re.search("static_big_wood_[0-9]\.csv",csv):
              static_big_wood.append(data_dir+folder+'/'+csv) 
           elif re.search("static_big_rubber_[0-9]\.csv",csv):
              static_big_rubber.append(data_dir+folder+'/'+csv)

for i in kinetic_small_wood:
  with open(i) as csvFile:
    df = pd.read_csv(i,usecols = ['rx-darkorange'])
    getRightRows(i)
    print(df)