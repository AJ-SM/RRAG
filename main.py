import os
from uitls import read_fileTxt
from uitls import preProcess


# Getting the file
file_path = r"D:\Storeage-1\MlNewBorn\RRAG\res\data.txt"
# Reading the whole file
data = read_fileTxt(file_path)
# Creating a single string NOT recommended for very big txt Python usually have the limit of  63 GB
txt = preProcess(data)



