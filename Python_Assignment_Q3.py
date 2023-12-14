# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 00:16:08 2023

@author: guoli
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('CSV File Upload and Display')
    
    # create model to upload a csv file
    uploaded_file = st.file_uploader("Please upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # read uploaded CSV file
        df = pd.read_csv(uploaded_file)

        # display uploaded CSV file
        st.write("The content of the CSV file is as below：")
        st.write(df)
        
        #plot a histgram for age
        st.subheader("Histgram for Age")
        plt.figure(figsize=(8, 6))
        hist, bins, _ = plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='grey', alpha = 0.7)  # 假设年龄这一列的列名为'年龄'
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.grid(axis='y', linestyle='--', alpha=0.7)  # 添加网格线
        
        # 在每个柱子的顶部显示数值
        # for i in range(len(hist)):
        #     plt.text(bins[i] + 0.5, hist[i] + 0.5, str(int(hist[i])), ha='center', va='bottom', fontsize=8)
        
        for i in range(len(hist)):
            plt.text((bins[i] + bins[i+1]) / 2, hist[i], str(int(hist[i])), ha='center', va='bottom', fontsize=8)


        st.pyplot(plt)
        
if __name__ == "__main__":
    main()