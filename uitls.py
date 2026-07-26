import os


filePath= r"D:\Storeage-1\MlNewBorn\RRAG\res\data.txt"

def read_fileTxt(filepath:str):
    with open(filepath,'r') as f:
        return f.readlines()

def preProcess(data:list):
    final_txt= ""
    for line in data:
        final_txt += line[:-2]
    return final_txt

if __name__=='__main__':
    content = read_fileTxt(filePath)
    txt = preProcess(content)
    print(txt)