# -*- coding: utf-8 -*-
"""
Determine optimal number of clusters with dendogram 
Program by Ammar AHmed Siddiqui
#"""

# Importing general libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing cluster specific library [dendrogram]
import scipy.cluster.hierarchy as sch

from sklearn.cluster import AgglomerativeClustering


# Load customers Mall Daataset
dataset = pd.read_csv("D:\IMPORTANT\MASTERS\BAHRIA UNIV\Spring2023 Semester\CourseMaterial\Tools in DS\Mall_customers.csv")

# Print dataset top 20 lines only
print(dataset.head())


# Extract 3rd and 4th columns only for analysis
# 3rd Column = Annual Income
# 4th Column = Spending Score

newdata = dataset.iloc[:,[3,4]].values
indexdata = dataset.iloc[:,[0]].values

col3 = dataset.iloc[:,[3]].values
col4 = dataset.iloc[:,[4]].values

for m in ['ward','average','complete','single']:

    for j in range(4,8): #Actual rnge from 4 to 7
    
        mTitle = "Agglomerative Clustering, #Clusters = " + str(j)+ " Linkage = "+ m
        print(mTitle)

        Agg_hc = AgglomerativeClustering(n_clusters = j, affinity = 'euclidean', linkage = m)
        y_hc = Agg_hc.fit_predict(newdata) # model fitting on the dataset

        plt.scatter(indexdata, y_hc, 1,y_hc)
        plt.title('Values Plot ' + mTitle)
        plt.xlabel('Index')
        plt.ylabel('Cluster #')
        plt.show()

        plt.scatter(col3, col4,10,y_hc)
        plt.title('Scatter Plot ' + mTitle)
        plt.xlabel('Customers - Annual Income')
        plt.ylabel('Customers - Spending Score')
        plt.show()