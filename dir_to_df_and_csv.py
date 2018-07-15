#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 13:02:03 2018

@author: tatianakurilo
"""
import sys, os, errno, pandas as pd

# SET PATH to the directory with csv files
try:
    dir_path = sys.argv[1] 
except:
    try:
        dir_path = input('Enter path to the data directory: ')
    except:
        raise Exception('No path provided')

if not os.path.exists(dir_path):
    raise FileNotFoundError

# if you need only specific columns, list their names within the brackets: ['column_1', 'column_2', 'etc']
# if you want to keep the order of columns, list all of them in brackets
col_names = [] # empty list equals to False; 


def read_csv_data(data_dir, col_names = False):
    """
    Reads csv files from the provided directory and returns a pandas dataframe of all files
    """
    
    # create an empty list to store dataframes of each file
    df_list = []
    
    def read_csv_to_df(csv_file):
        """
        Reads a csv file into a dataframe using only the columns from 
        the list of column names or all, if no columns list provided
        """
        if col_names: 
            return pd.read_csv(csv_file, usecols=col_names)
        else:
            return pd.read_csv(csv_file)

    # read each csv file to a dataframe and add it to the list
    for item in os.listdir(data_dir):
        if item.endswith(".csv"):
            df_list.append(read_csv_to_df(os.path.join(data_dir, item)))
        
    # return combined dataframe
    return pd.concat(df_list, ignore_index=True)

# read all files from dir_path folder to a dataframe according to col_names
df_from_dir = read_csv_data(dir_path, col_names)

# write the dafaframe to csv file
csv_file = dir_path + '.csv' 
try:
    df_from_dir.to_csv(csv_file, sep=',', encoding='utf-8', index=False)
    print(csv_file)
except:
    print('Failed to create .csv file')

