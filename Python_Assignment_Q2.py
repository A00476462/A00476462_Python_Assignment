# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:33:39 2023

@author: guoli
"""

import pandas as pd
   
def count_vowels (file_path):
    """    
    Parameters
    ----------
    file_path : input file path
        input file path, sample: r'D:\2023_Study in SMU\Python_Assignment\titles.csv'.

    Returns
    -------
    None.

    """
    df = pd.DataFrame(columns=['Vowels'])
    
    imdb_data = pd.read_csv(file_path)
    title_column = imdb_data['title']
    vowels = 'aeiouAEIOU'
    row = 0
    print("***********Please input correct file path on line 43! For example: ")
    print('D:\\2023_Study in SMU\\Python_Assignment\\titles.csv' + "\n")
    for item in title_column:
        vowel_counts = 0
        row = row +1
        for char in item:
            if char in vowels:
                vowel_counts = vowel_counts + 1
        #print("第" + str(row) + "行" + ": "+ str(vowel_counts) + "——" + item)
        df.loc[len(df)] = vowel_counts  # 在最后一行添加值为 i 的数据
    #print(df)
    imdb_data ['Vowels']= df.iloc[:,0]
    print(imdb_data)
     

file_path = r'D:\2023_Study in SMU\5520_Statistics\5520_Assignments\Python_Assignment\titles.csv'
count_vowels(file_path)
